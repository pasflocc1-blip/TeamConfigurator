/**
 * useWordExport — esporta la formazione in Word A4
 * Il campo viene ridisegnato su canvas (no SVG DOM)
 * npm install docx file-saver
 */
import {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  ImageRun, AlignmentType, WidthType, ShadingType, BorderStyle,
} from 'docx'
import { saveAs } from 'file-saver'
import { ROLE_LABELS, ROLE_COLORS } from '@/composables/useFormations'

function hexToDocx(hex) { return hex.replace('#', '').toUpperCase() }

// ── Disegna campo su canvas ──────────────────────────────
function drawPitchOnCanvas(positions, players, greenBackground, scale = 4) {
  const VW = 320, VH = 420
  const S  = scale
  const canvas = document.createElement('canvas')
  canvas.width  = VW * S
  canvas.height = VH * S
  const ctx = canvas.getContext('2d')

  if (greenBackground) {
    // Sfondo verde con strisce
    for (let y = 0; y < VH; y += 24) {
      ctx.fillStyle = y % 48 === 0 ? '#166534' : '#15803d'
      ctx.fillRect(0, y * S, VW * S, 24 * S)
    }
    ctx.strokeStyle = 'rgba(255,255,255,0.7)'
    ctx.fillStyle   = 'rgba(255,255,255,0.7)'
  } else {
    // Sfondo bianco — risparmio toner
    ctx.fillStyle = 'white'
    ctx.fillRect(0, 0, VW * S, VH * S)
    ctx.strokeStyle = '#111827'
    ctx.fillStyle   = '#111827'
  }

  ctx.lineWidth = 1.2 * S

  const line   = (x1,y1,x2,y2) => { ctx.beginPath(); ctx.moveTo(x1*S,y1*S); ctx.lineTo(x2*S,y2*S); ctx.stroke() }
  const rect   = (x,y,w,h)     => ctx.strokeRect(x*S, y*S, w*S, h*S)
  const circle = (cx,cy,r)     => { ctx.beginPath(); ctx.arc(cx*S,cy*S,r*S,0,Math.PI*2); ctx.stroke() }
  const dot    = (cx,cy,r)     => { ctx.beginPath(); ctx.arc(cx*S,cy*S,r*S,0,Math.PI*2); ctx.fill() }

  rect(9, 7, 302, 406)
  line(9, 210, 311, 210)
  circle(160, 210, 37)
  dot(160, 210, 1.5)
  rect(88,  7,   144, 70)
  rect(123, 7,   74,  25)
  rect(88,  343, 144, 70)
  rect(123, 388, 74,  25)
  rect(133, 413, 54,  7)
  rect(133, 0,   54,  7)
  dot(160, 50,  1.5)
  dot(160, 370, 1.5)

  // Token giocatori
  const TW = 52 * S
  const TH = 36 * S
  const ROLE_HEX = {
    POR: '#d97706',
    DC: '#1d4ed8', TD: '#1d4ed8', TS: '#1d4ed8', TLD: '#1d4ed8', TLS: '#1d4ed8',
    CC: '#15803d', CCD: '#15803d', CCS: '#15803d', CDC: '#166534',
    TRQ: '#7c3aed',
    ATT: '#b91c1c', ALD: '#b91c1c', ALS: '#b91c1c',
  }

  for (const pos of positions) {
    const px  = pos.x * S
    const py  = pos.y * S
    const arr = players[pos.id] || []
    const col = ROLE_HEX[pos.label] || '#4b5563'

    // Ombra token
    ctx.shadowColor   = 'rgba(0,0,0,0.35)'
    ctx.shadowBlur    = 3 * S
    ctx.shadowOffsetY = 1 * S

    // Rettangolo bianco
    ctx.fillStyle = 'white'
    const rx = px - TW/2, ry = py - TH/2
    const r  = 3.5 * S
    ctx.beginPath()
    ctx.moveTo(rx+r, ry); ctx.lineTo(rx+TW-r, ry)
    ctx.quadraticCurveTo(rx+TW, ry, rx+TW, ry+r)
    ctx.lineTo(rx+TW, ry+TH-r)
    ctx.quadraticCurveTo(rx+TW, ry+TH, rx+TW-r, ry+TH)
    ctx.lineTo(rx+r, ry+TH)
    ctx.quadraticCurveTo(rx, ry+TH, rx, ry+TH-r)
    ctx.lineTo(rx, ry+r)
    ctx.quadraticCurveTo(rx, ry, rx+r, ry)
    ctx.closePath()
    ctx.fill()

    // Bordo token (su bianco mettiamo bordo colorato)
    ctx.shadowColor = 'transparent'; ctx.shadowBlur = 0; ctx.shadowOffsetY = 0
    if (!greenBackground) {
      ctx.strokeStyle = col
      ctx.lineWidth   = 1.2 * S
      ctx.beginPath()
      ctx.moveTo(rx+r, ry); ctx.lineTo(rx+TW-r, ry)
      ctx.quadraticCurveTo(rx+TW, ry, rx+TW, ry+r)
      ctx.lineTo(rx+TW, ry+TH-r)
      ctx.quadraticCurveTo(rx+TW, ry+TH, rx+TW-r, ry+TH)
      ctx.lineTo(rx+r, ry+TH)
      ctx.quadraticCurveTo(rx, ry+TH, rx, ry+TH-r)
      ctx.lineTo(rx, ry+r)
      ctx.quadraticCurveTo(rx, ry, rx+r, ry)
      ctx.closePath()
      ctx.stroke()
    }

    // Separatore colorato
    ctx.strokeStyle = col
    ctx.lineWidth   = 1 * S
    line(pos.x - 26, pos.y - 5, pos.x + 26, pos.y - 5)

    // Etichetta ruolo
    ctx.fillStyle = col
    ctx.font      = `bold ${6.0*S}px Arial`
    ctx.textAlign = 'center'
    ctx.fillText(pos.label, px, py - 8.5*S)

    // Nomi
    const nameColors = greenBackground
      ? ['#111827', '#555555', '#777777']
      : ['#111827', '#555555', '#777777']

    for (let i = 0; i < 3; i++) {
      const name = arr[i] || ''
      if (!name && i > 0) continue
      const surname = name ? name.trim().split(' ').pop() : '—'
      const display = surname.length > 10 ? surname.slice(0, 10) + '.' : surname
      ctx.fillStyle = nameColors[i]
      ctx.font      = `${i===0?'bold':'normal'} ${(i===0?5.2:4.2)*S}px Arial`
      ctx.fillText(display, px, py + (i===0?1.5:i===1?7.5:13.5)*S)
    }

    // Reset stroke per linee campo successive
    ctx.strokeStyle = greenBackground ? 'rgba(255,255,255,0.7)' : '#111827'
    ctx.lineWidth   = 1.2 * S
  }

  return canvas
}

// ── Export Word ──────────────────────────────────────────
export async function exportToWord({ teamName, formation, players, positions, registry, greenBackground = true }) {

  // 1. Disegna campo su canvas
  const canvas = drawPitchOnCanvas(positions, players, greenBackground)
  const imgBuffer = await new Promise((resolve, reject) => {
    canvas.toBlob(blob => {
      if (!blob) { reject(new Error('Canvas toBlob fallito')); return }
      blob.arrayBuffer().then(resolve).catch(reject)
    }, 'image/png')
  })

  // 2. Dimensioni immagine in pixel per docx-js
  // A4 con margini 1cm = ~190mm ≈ 620px
  const IMG_W = 620
  const IMG_H = Math.round(IMG_W * 420 / 320)

  // 3. Mappa anagrafica per anno nascita
  const registryMap = {}
  if (registry) registry.forEach(p => { registryMap[p.name] = p })

  // 4. Tabella formazione
  const SLOT_LABELS = ['Titolare', 'Riserva 1', 'Riserva 2']
  const cellBorder  = { style: BorderStyle.SINGLE, size: 3, color: 'E5E7EB' }
  const cellBorders = { top: cellBorder, bottom: cellBorder, left: cellBorder, right: cellBorder }

  const headerRow = new TableRow({
    tableHeader: true,
    children: [
      makeHeaderCell('Ruolo', 1400),
      ...SLOT_LABELS.flatMap(label => [
        makeHeaderCell(label, 2100),
        makeHeaderCell('Anno', 800),
      ]),
    ],
  })

  const tableRows = positions.map(pos => {
    const arr   = players[pos.id] || ['', '', '']
    const color = hexToDocx(ROLE_COLORS[pos.label] || '#374151')

    return new TableRow({
      children: [
        new TableCell({
          width: { size: 1400, type: WidthType.DXA },
          shading: { fill: color, type: ShadingType.CLEAR },
          margins: { top: 60, bottom: 60, left: 100, right: 100 },
          borders: cellBorders,
          children: [
            new Paragraph({ alignment: AlignmentType.CENTER, children: [
              new TextRun({ text: pos.label, bold: true, color: 'FFFFFF', size: 18, font: 'Arial' }),
            ]}),
            new Paragraph({ alignment: AlignmentType.CENTER, children: [
              new TextRun({ text: ROLE_LABELS[pos.label] || pos.label, color: 'EEEEEE', size: 13, font: 'Arial' }),
            ]}),
          ],
        }),
        ...[0, 1, 2].flatMap(i => {
          const playerName = arr[i] || ''
          // Cerca nell'anagrafica — prova sia nome esatto che cognome
          const regPlayer  = registryMap[playerName] || {}
          // birth_year è il campo del DB (snake_case)
          const year = regPlayer.birth_year
            ? String(regPlayer.birth_year)
            : (regPlayer.birthYear ? String(regPlayer.birthYear) : '')

          return [
            new TableCell({
              width: { size: 2100, type: WidthType.DXA },
              margins: { top: 60, bottom: 60, left: 120, right: 80 },
              borders: cellBorders,
              children: [new Paragraph({ children: [
                new TextRun({
                  text: playerName || '—',
                  bold: i === 0,
                  color: playerName ? (i===0 ? '111827' : '6B7280') : 'CCCCCC',
                  size: i===0 ? 18 : 16,
                  font: 'Arial',
                }),
              ]})],
            }),
            new TableCell({
              width: { size: 800, type: WidthType.DXA },
              margins: { top: 60, bottom: 60, left: 60, right: 60 },
              borders: cellBorders,
              children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
                new TextRun({
                  text: year,
                  color: '6B7280',
                  size: i===0 ? 16 : 14,
                  font: 'Arial',
                }),
              ]})],
            }),
          ]
        }),
      ],
    })
  })

  // 5. Documento Word
  const doc = new Document({
    sections: [{
      properties: {
        page: {
          size: { width: 11906, height: 16838 },
          margin: { top: 720, right: 567, bottom: 720, left: 567 },
        },
      },
      children: [
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: 0, after: 160 },
          children: [new TextRun({ text: teamName || 'Formazione', bold: true, size: 40, color: '111827', font: 'Arial' })],
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: 0, after: 200 },
          children: [
            new TextRun({ text: 'Modulo: ', size: 22, color: '6B7280', font: 'Arial' }),
            new TextRun({ text: formation, bold: true, size: 24, color: '15803D', font: 'Arial' }),
          ],
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: 0, after: 240 },
          children: [
            new ImageRun({
              data: imgBuffer,
              transformation: { width: IMG_W, height: IMG_H },
              type: 'png',
            }),
          ],
        }),
        new Paragraph({
          spacing: { before: 100, after: 100 },
          children: [new TextRun({ text: 'Rosa', bold: true, size: 26, color: '111827', font: 'Arial' })],
        }),
        new Table({
          width: { size: 9527, type: WidthType.DXA },
          columnWidths: [1400, 2100, 800, 2100, 800, 2100, 800],
          rows: [headerRow, ...tableRows],
          borders: {
            top:     { style: BorderStyle.SINGLE, size: 4, color: 'D1D5DB' },
            bottom:  { style: BorderStyle.SINGLE, size: 4, color: 'D1D5DB' },
            left:    { style: BorderStyle.SINGLE, size: 4, color: 'D1D5DB' },
            right:   { style: BorderStyle.SINGLE, size: 4, color: 'D1D5DB' },
            insideH: { style: BorderStyle.SINGLE, size: 2, color: 'E5E7EB' },
            insideV: { style: BorderStyle.SINGLE, size: 2, color: 'E5E7EB' },
          },
        }),
      ],
    }],
  })

  const blob = await Packer.toBlob(doc)
  const filename = `${(teamName || 'formazione').replace(/[^a-z0-9]/gi, '_')}_${formation}.docx`
  saveAs(blob, filename)
}

function makeHeaderCell(text, width) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: { fill: '1F2937', type: ShadingType.CLEAR },
    margins: { top: 80, bottom: 80, left: 100, right: 100 },
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text, bold: true, color: 'FFFFFF', size: 16, font: 'Arial' })],
    })],
  })
}