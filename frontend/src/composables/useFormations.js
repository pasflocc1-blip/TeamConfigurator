// ViewBox 320x420 — centro X=160
// Token GRANDI: 52x36, metà=26x18
// Limiti sicuri: x[35..285], y[25..395]
// Spacing minimo: 58 unità X tra centri, 42 unità Y tra righe

export const FORMATIONS = {

  '4-3-3': { label: '4-3-3', positions: [
    { id: 'GK',  label: 'POR', x: 160, y: 375 },
    { id: 'RB',  label: 'TD',  x: 280,  y: 320 },
    { id: 'CB1', label: 'DC',  x: 213, y: 322 },
    { id: 'CB2', label: 'DC',  x: 107, y: 322 },
    { id: 'LB',  label: 'TS',  x: 40, y: 320 },
    { id: 'CM1', label: 'CC',  x: 260,  y: 210 },
    { id: 'CM2', label: 'CC',  x: 160, y: 207 },
    { id: 'CM3', label: 'CC',  x: 60, y: 210 },
    { id: 'RW',  label: 'ALD', x: 280,  y: 112 },
    { id: 'ST',  label: 'ATT', x: 160, y: 108 },
    { id: 'LW',  label: 'ALS', x: 40, y: 112 },
  ]},

  '4-4-2': { label: '4-4-2', positions: [
    { id: 'GK',  label: 'POR', x: 160, y: 375 },
    { id: 'RB',  label: 'TD',  x: 280,  y: 320 },
    { id: 'CB1', label: 'DC',  x: 213, y: 322 },
    { id: 'CB2', label: 'DC',  x: 107, y: 322 },
    { id: 'LB',  label: 'TS',  x: 40, y: 320 },
    { id: 'RM',  label: 'CCD', x: 280,  y: 210 },
    { id: 'CM1', label: 'CC',  x: 203, y: 207 },
    { id: 'CM2', label: 'CC',  x: 117, y: 207 },
    { id: 'LM',  label: 'CCS', x: 40, y: 210 },
    { id: 'ST1', label: 'ATT', x: 213, y: 112 },
    { id: 'ST2', label: 'ATT', x: 107, y: 112 },
  ]},

  '3-4-3': { label: '3-4-3', positions: [
    { id: 'GK',  label: 'POR', x: 160, y: 375 },
    { id: 'CB1', label: 'DC',  x: 255,  y: 320 },
    { id: 'CB2', label: 'DC',  x: 160, y: 323 },
    { id: 'CB3', label: 'DC',  x: 65, y: 320 },
    { id: 'RM',  label: 'CCD', x: 280,  y: 210 },
    { id: 'CM1', label: 'CC',  x: 203, y: 207 },
    { id: 'CM2', label: 'CC',  x: 117, y: 207 },
    { id: 'LM',  label: 'CCS', x: 40, y: 210 },
    { id: 'RW',  label: 'ALD', x: 280,  y: 112 },
    { id: 'ST',  label: 'ATT', x: 160, y: 108 },
    { id: 'LW',  label: 'ALS', x: 40, y: 112 },
  ]},

  '3-5-2': { label: '3-5-2', positions: [
    { id: 'GK',  label: 'POR', x: 160, y: 375 },
    { id: 'CB1', label: 'DC',  x: 255,  y: 320 },
    { id: 'CB2', label: 'DC',  x: 160, y: 323 },
    { id: 'CB3', label: 'DC',  x: 65, y: 320 },
    { id: 'RM',  label: 'CCD', x: 285,  y: 210 },
    { id: 'CM1', label: 'CC',  x: 225,  y: 207 },
    { id: 'CM2', label: 'CC',  x: 160, y: 204 },
    { id: 'CM3', label: 'CC',  x: 95, y: 207 },
    { id: 'LM',  label: 'CCS', x: 35, y: 210 },
    { id: 'ST1', label: 'ATT', x: 213, y: 112 },
    { id: 'ST2', label: 'ATT', x: 107, y: 112 },
  ]},

  '4-2-3-1': { label: '4-2-3-1', positions: [
    { id: 'GK',   label: 'POR', x: 160, y: 375 },
    { id: 'RB',   label: 'TD',  x: 280,  y: 323 },
    { id: 'CB1',  label: 'DC',  x: 213, y: 326 },
    { id: 'CB2',  label: 'DC',  x: 107, y: 326 },
    { id: 'LB',   label: 'TS',  x: 40, y: 323 },
    { id: 'CDM1', label: 'CDC', x: 213, y: 268 },
    { id: 'CDM2', label: 'CDC', x: 107, y: 268 },
    { id: 'RW',   label: 'ALD', x: 280,  y: 180 },
    { id: 'AM',   label: 'TRQ', x: 160, y: 177 },
    { id: 'LW',   label: 'ALS', x: 40, y: 180 },
    { id: 'ST',   label: 'ATT', x: 160, y: 95  },
  ]},

  '5-3-2': { label: '5-3-2', positions: [
    { id: 'GK',  label: 'POR', x: 160, y: 375 },
    { id: 'RWB', label: 'TLD', x: 285,  y: 322 },
    { id: 'CB1', label: 'DC',  x: 225,  y: 325 },
    { id: 'CB2', label: 'DC',  x: 160, y: 328 },
    { id: 'CB3', label: 'DC',  x: 95, y: 325 },
    { id: 'LWB', label: 'TLS', x: 35, y: 322 },
    { id: 'CM1', label: 'CC',  x: 260,  y: 210 },
    { id: 'CM2', label: 'CC',  x: 160, y: 207 },
    { id: 'CM3', label: 'CC',  x: 60, y: 210 },
    { id: 'ST1', label: 'ATT', x: 213, y: 112 },
    { id: 'ST2', label: 'ATT', x: 107, y: 112 },
  ]},
  '3-4-1-2': { label: '3-4-1-2', positions: [
    { id: 'GK',  label: 'POR', x: 160, y: 375 },
    { id: 'CB1', label: 'DC',  x: 255,  y: 320 },
    { id: 'CB2', label: 'DC',  x: 160, y: 323 },
    { id: 'CB3', label: 'DC',  x: 65, y: 320 },
    { id: 'RM',  label: 'CCD', x: 280,  y: 240 },
    { id: 'CM1', label: 'CC',  x: 203, y: 237 },
    { id: 'CM2', label: 'CC',  x: 117, y: 237 },
    { id: 'LM',  label: 'CCS', x: 40, y: 240 },
    { id: 'AM',  label: 'TRQ', x: 160, y: 175 },
    { id: 'ST1', label: 'ATT', x: 213, y: 112 },
    { id: 'ST2', label: 'ATT', x: 107, y: 112 },
  ]},

  '5-4-1': { label: '5-4-1', positions: [
    { id: 'GK',  label: 'POR', x: 160, y: 375 },
    { id: 'RWB', label: 'TLD', x: 285,  y: 320 },
    { id: 'CB1', label: 'DC',  x: 225,  y: 323 },
    { id: 'CB2', label: 'DC',  x: 160, y: 326 },
    { id: 'CB3', label: 'DC',  x: 95, y: 323 },
    { id: 'LWB', label: 'TLS', x: 35, y: 320 },
    { id: 'RM',  label: 'CCD', x: 280,  y: 224 },
    { id: 'CM1', label: 'CC',  x: 203, y: 221 },
    { id: 'CM2', label: 'CC',  x: 117, y: 221 },
    { id: 'LM',  label: 'CCS', x: 40, y: 224 },
    { id: 'ST',  label: 'ATT', x: 160, y: 112 },
  ]},

  '5-2-3': { label: '5-2-3', positions: [
    { id: 'GK',  label: 'POR', x: 160, y: 375 },
    { id: 'RWB', label: 'TLD', x: 285,  y: 320 },
    { id: 'CB1', label: 'DC',  x: 225,  y: 323 },
    { id: 'CB2', label: 'DC',  x: 160, y: 326 },
    { id: 'CB3', label: 'DC',  x: 95, y: 323 },
    { id: 'LWB', label: 'TLS', x: 35, y: 320 },
    { id: 'CM1', label: 'CC',  x: 213, y: 224 },
    { id: 'CM2', label: 'CC',  x: 107, y: 224 },
    { id: 'RW',  label: 'ALD', x: 280,  y: 112 },
    { id: 'ST',  label: 'ATT', x: 160, y: 108 },
    { id: 'LW',  label: 'ALS', x: 40, y: 112 },
  ]},

  '4-1-4-1': { label: '4-1-4-1', positions: [
    { id: 'GK',   label: 'POR', x: 160, y: 375 },
    { id: 'RB',   label: 'TD',  x: 280,  y: 320 },
    { id: 'CB1',  label: 'DC',  x: 213, y: 322 },
    { id: 'CB2',  label: 'DC',  x: 107, y: 322 },
    { id: 'LB',   label: 'TS',  x: 40, y: 320 },
    { id: 'CDM',  label: 'CDC', x: 160, y: 258 },
    { id: 'RM',   label: 'CCD', x: 280,  y: 196 },
    { id: 'CM1',  label: 'CC',  x: 203, y: 193 },
    { id: 'CM2',  label: 'CC',  x: 117, y: 193 },
    { id: 'LM',   label: 'CCS', x: 40, y: 196 },
    { id: 'ST',   label: 'ATT', x: 160, y: 112 },
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