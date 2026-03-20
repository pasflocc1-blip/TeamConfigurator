// ViewBox 320x420 — centro X=160, centro Y=210
// Token GRANDE: 52x34, metà=26x17
// Limiti sicuri: x[35..285], y[24..396]
// Spacing minimo: 58 unità X tra centri, 40 unità Y tra righe
//
// Y di riferimento:
//   GK   → 375  (dentro area piccola)
//   DEF  → 320  (davanti area rigore y=343)
//   MID  → 210  (centrocampo)
//   ATT  → 112  (tre quarti)

export const FORMATIONS = {

  '4-3-3': { label: '4-3-3', positions: [
    { id: 'GK',  label: 'POR', x: 160, y: 375 },
    { id: 'RB',  label: 'TD',  x: 38,  y: 320 },
    { id: 'CB1', label: 'DC',  x: 107, y: 322 },
    { id: 'CB2', label: 'DC',  x: 213, y: 322 },
    { id: 'LB',  label: 'TS',  x: 282, y: 320 },
    { id: 'CM1', label: 'CC',  x: 64,  y: 210 },
    { id: 'CM2', label: 'CC',  x: 160, y: 208 },
    { id: 'CM3', label: 'CC',  x: 256, y: 210 },
    { id: 'RW',  label: 'ALD', x: 38,  y: 112 },
    { id: 'ST',  label: 'ATT', x: 160, y: 110 },
    { id: 'LW',  label: 'ALS', x: 282, y: 112 },
  ]},

  '4-4-2': { label: '4-4-2', positions: [
    { id: 'GK',  label: 'POR', x: 160, y: 375 },
    { id: 'RB',  label: 'TD',  x: 38,  y: 320 },
    { id: 'CB1', label: 'DC',  x: 107, y: 322 },
    { id: 'CB2', label: 'DC',  x: 213, y: 322 },
    { id: 'LB',  label: 'TS',  x: 282, y: 320 },
    { id: 'RM',  label: 'CCD', x: 38,  y: 210 },
    { id: 'CM1', label: 'CC',  x: 115, y: 208 },
    { id: 'CM2', label: 'CC',  x: 205, y: 208 },
    { id: 'LM',  label: 'CCS', x: 282, y: 210 },
    { id: 'ST1', label: 'ATT', x: 107, y: 112 },
    { id: 'ST2', label: 'ATT', x: 213, y: 112 },
  ]},

  '3-4-3': { label: '3-4-3', positions: [
    { id: 'GK',  label: 'POR', x: 160, y: 375 },
    { id: 'CB1', label: 'DC',  x: 64,  y: 320 },
    { id: 'CB2', label: 'DC',  x: 160, y: 322 },
    { id: 'CB3', label: 'DC',  x: 256, y: 320 },
    { id: 'RM',  label: 'CCD', x: 38,  y: 210 },
    { id: 'CM1', label: 'CC',  x: 115, y: 208 },
    { id: 'CM2', label: 'CC',  x: 205, y: 208 },
    { id: 'LM',  label: 'CCS', x: 282, y: 210 },
    { id: 'RW',  label: 'ALD', x: 38,  y: 112 },
    { id: 'ST',  label: 'ATT', x: 160, y: 110 },
    { id: 'LW',  label: 'ALS', x: 282, y: 112 },
  ]},

  '3-5-2': { label: '3-5-2', positions: [
    { id: 'GK',  label: 'POR', x: 160, y: 375 },
    { id: 'CB1', label: 'DC',  x: 64,  y: 320 },
    { id: 'CB2', label: 'DC',  x: 160, y: 322 },
    { id: 'CB3', label: 'DC',  x: 256, y: 320 },
    { id: 'RM',  label: 'CCD', x: 36,  y: 210 },
    { id: 'CM1', label: 'CC',  x: 96,  y: 208 },
    { id: 'CM2', label: 'CC',  x: 160, y: 206 },
    { id: 'CM3', label: 'CC',  x: 224, y: 208 },
    { id: 'LM',  label: 'CCS', x: 284, y: 210 },
    { id: 'ST1', label: 'ATT', x: 107, y: 112 },
    { id: 'ST2', label: 'ATT', x: 213, y: 112 },
  ]},

  '4-2-3-1': { label: '4-2-3-1', positions: [
    { id: 'GK',   label: 'POR', x: 160, y: 375 },
    { id: 'RB',   label: 'TD',  x: 38,  y: 322 },
    { id: 'CB1',  label: 'DC',  x: 107, y: 325 },
    { id: 'CB2',  label: 'DC',  x: 213, y: 325 },
    { id: 'LB',   label: 'TS',  x: 282, y: 322 },
    { id: 'CDM1', label: 'CDC', x: 107, y: 264 },
    { id: 'CDM2', label: 'CDC', x: 213, y: 264 },
    { id: 'RW',   label: 'ALD', x: 38,  y: 172 },
    { id: 'AM',   label: 'TRQ', x: 160, y: 170 },
    { id: 'LW',   label: 'ALS', x: 282, y: 172 },
    { id: 'ST',   label: 'ATT', x: 160, y: 90  },
  ]},

  '5-3-2': { label: '5-3-2', positions: [
    { id: 'GK',  label: 'POR', x: 160, y: 375 },
    { id: 'RWB', label: 'TLD', x: 36,  y: 322 },
    { id: 'CB1', label: 'DC',  x: 96,  y: 325 },
    { id: 'CB2', label: 'DC',  x: 160, y: 328 },
    { id: 'CB3', label: 'DC',  x: 224, y: 325 },
    { id: 'LWB', label: 'TLS', x: 284, y: 322 },
    { id: 'CM1', label: 'CC',  x: 64,  y: 210 },
    { id: 'CM2', label: 'CC',  x: 160, y: 208 },
    { id: 'CM3', label: 'CC',  x: 256, y: 210 },
    { id: 'ST1', label: 'ATT', x: 107, y: 112 },
    { id: 'ST2', label: 'ATT', x: 213, y: 112 },
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