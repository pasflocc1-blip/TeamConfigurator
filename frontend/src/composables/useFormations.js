// ViewBox 400x500 — centro X=200
// Token: 64x38, metà=32x19
// Limiti sicuri: x[56..344], y[30..470]
//
// Griglia X per linee:
//   2 giocatori: 150, 250  (gap 100)
//   3 giocatori: 110, 200, 290  (gap 90)
//   4 giocatori: 80, 160, 240, 320  (gap 80)
//   5 giocatori: 56, 124, 200, 276, 344  (gap 68 → margine 4px per lato ✓)
//
// Griglia Y (da fondo verso attacco):
//   POR:   450
//   DEF:   385
//   MID:   255
//   ATT:   130

export const FORMATIONS = {

  '4-3-3': { label: '4-3-3', positions: [
    { id: 'GK',  label: 'POR', x: 200, y: 450 },
    { id: 'RB',  label: 'TD',  x: 320, y: 385 },
    { id: 'CB1', label: 'DC',  x: 240, y: 385 },
    { id: 'CB2', label: 'DC',  x: 160, y: 385 },
    { id: 'LB',  label: 'TS',  x: 80,  y: 385 },
    { id: 'CM1', label: 'CC',  x: 290, y: 255 },
    { id: 'CM2', label: 'CC',  x: 200, y: 255 },
    { id: 'CM3', label: 'CC',  x: 110, y: 255 },
    { id: 'RW',  label: 'ALD', x: 330, y: 130 },
    { id: 'ST',  label: 'ATT', x: 200, y: 130 },
    { id: 'LW',  label: 'ALS', x: 70,  y: 130 },
  ]},

  '4-4-2': { label: '4-4-2', positions: [
    { id: 'GK',  label: 'POR', x: 200, y: 450 },
    { id: 'RB',  label: 'TD',  x: 320, y: 385 },
    { id: 'CB1', label: 'DC',  x: 240, y: 385 },
    { id: 'CB2', label: 'DC',  x: 160, y: 385 },
    { id: 'LB',  label: 'TS',  x: 80,  y: 385 },
    { id: 'RM',  label: 'CCD', x: 320, y: 255 },
    { id: 'CM1', label: 'CC',  x: 240, y: 255 },
    { id: 'CM2', label: 'CC',  x: 160, y: 255 },
    { id: 'LM',  label: 'CCS', x: 80,  y: 255 },
    { id: 'ST1', label: 'ATT', x: 250, y: 130 },
    { id: 'ST2', label: 'ATT', x: 150, y: 130 },
  ]},

  '3-4-3': { label: '3-4-3', positions: [
    { id: 'GK',  label: 'POR', x: 200, y: 450 },
    { id: 'CB1', label: 'DC',  x: 290, y: 385 },
    { id: 'CB2', label: 'DC',  x: 200, y: 385 },
    { id: 'CB3', label: 'DC',  x: 110, y: 385 },
    { id: 'RM',  label: 'CCD', x: 320, y: 255 },
    { id: 'CM1', label: 'CC',  x: 240, y: 255 },
    { id: 'CM2', label: 'CC',  x: 160, y: 255 },
    { id: 'LM',  label: 'CCS', x: 80,  y: 255 },
    { id: 'RW',  label: 'ALD', x: 330, y: 130 },
    { id: 'ST',  label: 'ATT', x: 200, y: 130 },
    { id: 'LW',  label: 'ALS', x: 70,  y: 130 },
  ]},

  // 3-5-2: centrocampisti a 5 → griglia 56,124,200,276,344
  '3-5-2': { label: '3-5-2', positions: [
    { id: 'GK',  label: 'POR', x: 200, y: 450 },
    { id: 'CB1', label: 'DC',  x: 290, y: 385 },
    { id: 'CB2', label: 'DC',  x: 200, y: 385 },
    { id: 'CB3', label: 'DC',  x: 110, y: 385 },
    { id: 'RM',  label: 'CCD', x: 344, y: 255 },
    { id: 'CM1', label: 'CC',  x: 276, y: 255 },
    { id: 'CM2', label: 'CC',  x: 200, y: 255 },
    { id: 'CM3', label: 'CC',  x: 124, y: 255 },
    { id: 'LM',  label: 'CCS', x: 56,  y: 255 },
    { id: 'ST1', label: 'ATT', x: 250, y: 130 },
    { id: 'ST2', label: 'ATT', x: 150, y: 130 },
  ]},

  '4-2-3-1': { label: '4-2-3-1', positions: [
    { id: 'GK',   label: 'POR', x: 200, y: 450 },
    { id: 'RB',   label: 'TD',  x: 320, y: 390 },
    { id: 'CB1',  label: 'DC',  x: 240, y: 390 },
    { id: 'CB2',  label: 'DC',  x: 160, y: 390 },
    { id: 'LB',   label: 'TS',  x: 80,  y: 390 },
    { id: 'CDM1', label: 'CDC', x: 240, y: 320 },
    { id: 'CDM2', label: 'CDC', x: 160, y: 320 },
    { id: 'RW',   label: 'ALD', x: 320, y: 215 },
    { id: 'AM',   label: 'TRQ', x: 200, y: 215 },
    { id: 'LW',   label: 'ALS', x: 80,  y: 215 },
    { id: 'ST',   label: 'ATT', x: 200, y: 115 },
  ]},

  // 5-3-2: difensori a 5 → griglia 56,124,200,276,344
  '5-3-2': { label: '5-3-2', positions: [
    { id: 'GK',  label: 'POR', x: 200, y: 450 },
    { id: 'RWB', label: 'TLD', x: 344, y: 385 },
    { id: 'CB1', label: 'DC',  x: 276, y: 385 },
    { id: 'CB2', label: 'DC',  x: 200, y: 385 },
    { id: 'CB3', label: 'DC',  x: 124, y: 385 },
    { id: 'LWB', label: 'TLS', x: 56,  y: 385 },
    { id: 'CM1', label: 'CC',  x: 290, y: 255 },
    { id: 'CM2', label: 'CC',  x: 200, y: 255 },
    { id: 'CM3', label: 'CC',  x: 110, y: 255 },
    { id: 'ST1', label: 'ATT', x: 250, y: 130 },
    { id: 'ST2', label: 'ATT', x: 150, y: 130 },
  ]},

  '3-4-1-2': { label: '3-4-1-2', positions: [
    { id: 'GK',  label: 'POR', x: 200, y: 450 },
    { id: 'CB1', label: 'DC',  x: 290, y: 385 },
    { id: 'CB2', label: 'DC',  x: 200, y: 385 },
    { id: 'CB3', label: 'DC',  x: 110, y: 385 },
    { id: 'RM',  label: 'CCD', x: 320, y: 285 },
    { id: 'CM1', label: 'CC',  x: 240, y: 285 },
    { id: 'CM2', label: 'CC',  x: 160, y: 285 },
    { id: 'LM',  label: 'CCS', x: 80,  y: 285 },
    { id: 'AM',  label: 'TRQ', x: 200, y: 205 },
    { id: 'ST1', label: 'ATT', x: 250, y: 130 },
    { id: 'ST2', label: 'ATT', x: 150, y: 130 },
  ]},

  // 5-4-1: difensori a 5 → griglia 56,124,200,276,344
  '5-4-1': { label: '5-4-1', positions: [
    { id: 'GK',  label: 'POR', x: 200, y: 450 },
    { id: 'RWB', label: 'TLD', x: 344, y: 385 },
    { id: 'CB1', label: 'DC',  x: 276, y: 385 },
    { id: 'CB2', label: 'DC',  x: 200, y: 385 },
    { id: 'CB3', label: 'DC',  x: 124, y: 385 },
    { id: 'LWB', label: 'TLS', x: 56,  y: 385 },
    { id: 'RM',  label: 'CCD', x: 320, y: 265 },
    { id: 'CM1', label: 'CC',  x: 240, y: 265 },
    { id: 'CM2', label: 'CC',  x: 160, y: 265 },
    { id: 'LM',  label: 'CCS', x: 80,  y: 265 },
    { id: 'ST',  label: 'ATT', x: 200, y: 130 },
  ]},

  // 5-2-3: difensori a 5 → griglia 56,124,200,276,344
  '5-2-3': { label: '5-2-3', positions: [
    { id: 'GK',  label: 'POR', x: 200, y: 450 },
    { id: 'RWB', label: 'TLD', x: 344, y: 385 },
    { id: 'CB1', label: 'DC',  x: 276, y: 385 },
    { id: 'CB2', label: 'DC',  x: 200, y: 385 },
    { id: 'CB3', label: 'DC',  x: 124, y: 385 },
    { id: 'LWB', label: 'TLS', x: 56,  y: 385 },
    { id: 'CM1', label: 'CC',  x: 240, y: 270 },
    { id: 'CM2', label: 'CC',  x: 160, y: 270 },
    { id: 'RW',  label: 'ALD', x: 330, y: 130 },
    { id: 'ST',  label: 'ATT', x: 200, y: 130 },
    { id: 'LW',  label: 'ALS', x: 70,  y: 130 },
  ]},

  '4-1-4-1': { label: '4-1-4-1', positions: [
    { id: 'GK',   label: 'POR', x: 200, y: 450 },
    { id: 'RB',   label: 'TD',  x: 320, y: 385 },
    { id: 'CB1',  label: 'DC',  x: 240, y: 385 },
    { id: 'CB2',  label: 'DC',  x: 160, y: 385 },
    { id: 'LB',   label: 'TS',  x: 80,  y: 385 },
    { id: 'CDM',  label: 'CDC', x: 200, y: 315 },
    { id: 'RM',   label: 'CCD', x: 320, y: 235 },
    { id: 'CM1',  label: 'CC',  x: 240, y: 235 },
    { id: 'CM2',  label: 'CC',  x: 160, y: 235 },
    { id: 'LM',   label: 'CCS', x: 80,  y: 235 },
    { id: 'ST',   label: 'ATT', x: 200, y: 130 },
  ]},
}

export const ROLE_COLORS = {
  POR: '#d97706',
  DC: '#1d4ed8', TD: '#1d4ed8', TS: '#1d4ed8', TLD: '#1d4ed8', TLS: '#1d4ed8',
  CC: '#15803d', CCD: '#15803d', CCS: '#15803d', CDC: '#166534',
  TRQ: '#7c3aed',
  ATT: '#b91c1c', ALD: '#b91c1c', ALS: '#b91c1c',
}

export const ROLE_LABELS = {
  POR: 'Portiere', DC: 'Difensore Centrale',
  TD: 'Terzino Destro', TS: 'Terzino Sinistro',
  TLD: 'Terzino Lat. Dx', TLS: 'Terzino Lat. Sx',
  CC: 'Centrocampista', CCD: 'CC Destro', CCS: 'CC Sinistro', CDC: 'CC Difensivo',
  TRQ: 'Trequartista',
  ATT: 'Attaccante', ALD: 'Ala Destra', ALS: 'Ala Sinistra',
}

export const ALL_ROLES = ['POR','DC','TD','TS','TLD','TLS','CC','CCD','CCS','CDC','TRQ','ATT','ALD','ALS']