/**
 * useWordExport — esporta la formazione in Word A4
 * npm install docx file-saver
 *
 * FIX: il campo viene disegnato direttamente su Canvas 2D
 *      (no SVG serialization — i pattern SVG non sopravvivono a XMLSerializer)
 */
import { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
         ImageRun, AlignmentType, WidthType, ShadingType, BorderStyle,
         VerticalAlign } from 'docx'
import { saveAs } from 'file-saver'
import { ROLE_LABELS, ROLE_COLORS } from '@/composables/useFormations'

function hexToDocx(hex) { return hex.replace('#', '').toUpperCase() }

// ── Disegna il campo + token su Canvas 2D ─────────────────────────────────────
function drawFieldCanvas(positions, players, scale = 4) {
  const VW = 320, VH = 420
  const W = VW * scale, H = VH * scale
  const s = scale  // shorthand

  const canvas = document.createElement('canvas')
  canvas.width = W; canvas.height = H
  const ctx = canvas.getContext('2d')

  // ── Strisce erba ──────────────────────────────
  const stripeH = 24 * s
  for (let y = 0; y < H; y += stripeH * 2) {
    ctx.fillStyle = '#166534'; ctx.fillRect(0, y, W, stripeH)
    ctx.fillStyle = '#15803d'; ctx.fillRect(0, y + stripeH, W, stripeH)
  }

  // ── Linee campo ───────────────────────────────
  ctx.strokeStyle = 'rgba(255,255,255,0.7)'
  ctx.lineWidth = 0.6 * s

  const lx = 9*s, ly = 7*s, lw = 302*s, lh = 406*s

  // Bordo
  ctx.strokeRect(lx, ly, lw, lh)
  // Centrocampo
  ctx.beginPath(); ctx.moveTo(lx, 210*s); ctx.lineTo(lx+lw, 210*s); ctx.stroke()
  // Cerchio centrocampo
  ctx.beginPath(); ctx.arc(160*s, 210*s, 37*s, 0, Math.PI*2); ctx.stroke()
  ctx.fillStyle = 'rgba(255,255,255,0.7)'
  ctx.beginPath(); ctx.arc(160*s, 210*s, 1.5*s, 0, Math.PI*2); ctx.fill()
  // Area rigore alto
  ctx.strokeRect(88*s, 7*s, 144*s, 70*s)
  ctx.strokeRect(123*s, 7*s, 74*s, 25*s)
  // Area rigore basso
  ctx.strokeRect(88*s, 343*s, 144*s, 70*s)
  ctx.strokeRect(123*s, 388*s, 74*s, 25*s)
  // Dischetti
  ctx.beginPath(); ctx.arc(160*s, 50*s,  1.5*s, 0, Math.PI*2); ctx.fill()
  ctx.beginPath(); ctx.arc(160*s, 370*s, 1.5*s, 0, Math.PI*2); ctx.fill()
  // Porte
  ctx.strokeRect(133*s, 413*s, 54*s, 7*s)
  ctx.strokeRect(133*s, 0,     54*s, 7*s)

  // ── Token giocatori ───────────────────────────
  const TW = 52*s, TH = 34*s  // dimensioni token
  const TX = TW/2, TY = TH/2  // metà token

  positions.forEach(pos => {
    const cx = pos.x * s
    const cy = pos.y * s
    const x  = cx - TX
    const y  = cy - TY
    const color = ROLE_COLORS[pos.label] || '#4b5563'

    // Ombra
    ctx.shadowColor = 'rgba(0,0,0,0.6)'
    ctx.shadowBlur = 6*s; ctx.shadowOffsetY = 2*s

    // Rettangolo bianco
    ctx.fillStyle = 'white'
    roundRect(ctx, x, y, TW, TH, 4*s)
    ctx.fill()

    ctx.shadowBlur = 0; ctx.shadowOffsetY = 0

    // Linea separatore colorata
    ctx.strokeStyle = color
    ctx.lineWidth = 1*s
    ctx.beginPath()
    ctx.moveTo(x, cy - 7*s)
    ctx.lineTo(x + TW, cy - 7*s)
    ctx.stroke()

    // Etichetta ruolo
    ctx.fillStyle = color
    ctx.font = `800 ${5.5*s}px Arial`
    ctx.textAlign = 'center'
    ctx.textBaseline = 'middle'
    ctx.fillText(pos.label, cx, cy - 10.5*s)

    // Nomi
    const arr = players[pos.id] || ['', '', '']
    const names = [arr[0]||'', arr[1]||'', arr[2]||'']
    const yOffsets = [-1*s, 5.5*s, 12*s]
    const fontSizes = [4.4*s, 3.8*s, 3.4*s]
    const colors   = ['#111827', '#6b7280', '#9ca3af']

    names.forEach((name, i) => {
      if (!name && i > 0) return
      const surname = name ? name.trim().split(' ').pop() : '—'
      const maxLen = i === 0 ? 10 : 9
      const display = surname.length > maxLen ? surname.slice(0, maxLen) + '.' : surname
      ctx.fillStyle = colors[i]
      ctx.font = `${i === 0 ? '700' : '400'} ${fontSizes[i]}px Arial`
      ctx.fillText(display, cx, cy + yOffsets[i])
    })
  })

  return canvas
}

function roundRect(ctx, x, y, w, h, r) {
  ctx.beginPath()
  ctx.moveTo(x + r, y)
  ctx.lineTo(x + w - r, y)
  ctx.quadraticCurveTo(x + w, y, x + w, y + r)
  ctx.lineTo(x + w, y + h - r)
  ctx.quadraticCurveTo(x + w, y + h, x + w - r, y + h)
  ctx.lineTo(x + r, y + h)
  ctx.quadraticCurveTo(x, y + h, x, y + h - r)
  ctx.lineTo(x, y + r)
  ctx.quadraticCurveTo(x, y, x + r, y)
  ctx.closePath()
}

async function canvasToPngBuffer(canvas) {
  return new Promise((resolve, reject) => {
    canvas.toBlob(blob => blob.arrayBuffer().then(resolve).catch(reject), 'image/png')
  })
}

// ── Export Word ───────────────────────────────────────────────────────────────
export async function exportToWord({ teamName, formation, players, positions, registry }) {
  // Disegna campo su canvas (scala 4x per qualità stampa)
  const canvas    = drawFieldCanvas(positions, players, 4)
  const imgBuffer = await canvasToPngBuffer(canvas)

  // docx.js ImageRun.transformation: valori in PIXEL (non twip/EMU)
  // 120mm a 96 DPI = 120/25.4*96 ≈ 453 pixel → rende ≈ 120mm in Word
  const IMG_W = 453
  const IMG_H = Math.round(IMG_W * 420 / 320)  // ≈ 595px = ~158mm

  // Mappa registry per lookup anno di nascita
  const regMap = {}
  if (registry) registry.forEach(p => { regMap[p.name] = p })
  const getBirthYear = (name) => name ? (regMap[name]?.birthYear ?? null) : null

  const borderThin = { style: BorderStyle.SINGLE, size: 2, color: 'E5E7EB' }
  const borderMed  = { style: BorderStyle.SINGLE, size: 4, color: 'D1D5DB' }
  const borders    = {
    top: borderMed, bottom: borderMed, left: borderMed, right: borderMed,
    insideH: borderThin, insideV: borderThin,
  }

  // Intestazione tabella
  const headerRow = new TableRow({
    tableHeader: true,
    children: [
      mkHdr('Ruolo',    1400),
      mkHdr('Titolare', 2000),
      mkHdr('Anno',      720),
      mkHdr('Riserva 1',2000),
      mkHdr('Anno',      720),
      mkHdr('Riserva 2',2000),
      mkHdr('Anno',      720),
    ],
  })

  const tableRows = positions.map(pos => {
    const arr   = players[pos.id] || ['', '', '']
    const color = hexToDocx(ROLE_COLORS[pos.label] || '#374151')
    const [t, r1, r2] = [arr[0]||'', arr[1]||'', arr[2]||'']

    return new TableRow({
      children: [
        // Ruolo colorato
        new TableCell({
          width: { size: 1400, type: WidthType.DXA },
          shading: { fill: color, type: ShadingType.CLEAR },
          verticalAlign: VerticalAlign.CENTER,
          margins: { top: 60, bottom: 60, left: 80, right: 80 },
          children: [
            new Paragraph({ alignment: AlignmentType.CENTER, children: [
              new TextRun({ text: pos.label, bold: true, color: 'FFFFFF', size: 20, font: 'Arial' }),
            ]}),
            new Paragraph({ alignment: AlignmentType.CENTER, children: [
              new TextRun({ text: ROLE_LABELS[pos.label] || '', color: 'DDDDDD', size: 13, font: 'Arial' }),
            ]}),
          ],
        }),
        mkPlayer(t,  true,  2000),
        mkYear(getBirthYear(t),  720),
        mkPlayer(r1, false, 2000),
        mkYear(getBirthYear(r1), 720),
        mkPlayer(r2, false, 2000),
        mkYear(getBirthYear(r2), 720),
      ],
    })
  })

  const doc = new Document({
    sections: [{
      properties: {
        page: {
          size: { width: 11906, height: 16838 },
          margin: { top: 720, right: 1000, bottom: 720, left: 1000 },
        },
      },
      children: [
        // Titolo
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: 0, after: 140 },
          children: [new TextRun({ text: teamName || 'Formazione', bold: true, size: 42, color: '111827', font: 'Arial' })],
        }),
        // Modulo
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: 0, after: 220 },
          children: [
            new TextRun({ text: 'Modulo: ', size: 22, color: '6B7280', font: 'Arial' }),
            new TextRun({ text: formation, bold: true, size: 22, color: '15803D', font: 'Arial' }),
          ],
        }),
        // Campo centrato
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: 0, after: 260 },
          children: [new ImageRun({ data: imgBuffer, transformation: { width: IMG_W, height: IMG_H }, type: 'png' })],
        }),
        // Titolo tabella
        new Paragraph({
          spacing: { before: 0, after: 100 },
          children: [new TextRun({ text: 'Rosa della squadra', bold: true, size: 24, color: '111827', font: 'Arial' })],
        }),
        // Tabella
        new Table({
          width: { size: 9560, type: WidthType.DXA },
          columnWidths: [1400, 2000, 720, 2000, 720, 2000, 720],
          borders,
          rows: [headerRow, ...tableRows],
        }),
      ],
    }],
  })

  const blob = await Packer.toBlob(doc)
  saveAs(blob, `${(teamName || 'formazione').replace(/[^a-z0-9]/gi, '_')}_${formation}.docx`)
}

// ── Helper celle tabella ──────────────────────────────────────────────────────
function mkHdr(text, width) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: { fill: '1F2937', type: ShadingType.CLEAR },
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 80, bottom: 80, left: 80, right: 80 },
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text, bold: true, color: 'FFFFFF', size: 18, font: 'Arial' })],
    })],
  })
}

function mkPlayer(name, isTitolare, width) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 60, bottom: 60, left: 100, right: 80 },
    children: [new Paragraph({
      children: [new TextRun({
        text: name || '—',
        bold: isTitolare,
        color: name ? (isTitolare ? '111827' : '374151') : 'BBBBBB',
        size: isTitolare ? 20 : 18,
        font: 'Arial',
      })],
    })],
  })
}

function mkYear(year, width) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 60, bottom: 60, left: 50, right: 50 },
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({
        text: year ? String(year) : '—',
        color: year ? '374151' : 'CCCCCC',
        size: 16, font: 'Arial',
      })],
    })],
  })
}