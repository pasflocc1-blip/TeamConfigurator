<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal">
      <div class="modal-header">
        <span>📊 Risultati Query — {{ result.count }} righe</span>
        <button @click="$emit('close')" class="modal-close">×</button>
      </div>
      <div class="sql-preview">{{ sql }}</div>
      <div class="table-wrapper">
        <table class="result-table">
          <thead>
            <tr>
              <th v-for="col in result.columns" :key="col">{{ col }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(row, i) in result.rows" :key="i">
              <td v-for="col in result.columns" :key="col">{{ row[col] ?? '—' }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="modal-footer">
        <span class="row-count">{{ result.count }} righe · {{ result.columns.length }} colonne</span>
        <div style="display:flex; gap:8px">
          <button @click="exportExcel" class="btn-excel">📊 Esporta Excel</button>
          <button @click="$emit('close')" class="btn-close">Chiudi</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import * as XLSX from 'xlsx'

const props = defineProps({ result: Object, sql: String })
defineEmits(['close'])

const exportExcel = () => {
  if (!props.result) return
  const wb = XLSX.utils.book_new()
  const ws = XLSX.utils.json_to_sheet(props.result.rows)
  XLSX.utils.book_append_sheet(wb, ws, 'Risultati')
  const filename = 'export_' + new Date().toISOString().slice(0,10) + '.xlsx'
  XLSX.writeFile(wb, filename)
}
</script>

<style scoped>
.modal-overlay {
  position: fixed; inset: 0; background: rgba(0,0,0,0.8); z-index: 400;
  display: flex; align-items: center; justify-content: center; padding: 12px;
}
.modal {
  background: #0f172a; border: 1px solid #334155; border-radius: 14px;
  width: 100%; max-width: 1100px; height: 90vh;
  display: flex; flex-direction: column; overflow: hidden;
}
.modal-header {
  display: flex; justify-content: space-between; align-items: center;
  padding: 14px 20px; border-bottom: 1px solid #1e293b;
  font-weight: 700; font-size: 15px; color: white; flex-shrink: 0;
}
.modal-close {
  background: none; border: none; color: #64748b; cursor: pointer; font-size: 22px;
}
.sql-preview {
  background: #0a0f1a; padding: 8px 16px; font-family: monospace;
  font-size: 11px; color: #86efac; border-bottom: 1px solid #1e293b;
  white-space: pre; overflow-x: auto; overflow-y: auto;
  max-height: 72px; flex-shrink: 0; line-height: 1.4;
}
.table-wrapper {
  flex: 1; overflow: auto;
}
.result-table {
  width: 100%; border-collapse: collapse; font-size: 13px;
}
.result-table th {
  background: #1e293b; color: #94a3b8; padding: 10px 14px;
  text-align: left; font-weight: 700; text-transform: uppercase;
  font-size: 11px; position: sticky; top: 0; white-space: nowrap;
  border-bottom: 2px solid #334155; z-index: 1;
}
.result-table td {
  color: #e2e8f0; padding: 9px 14px;
  border-bottom: 1px solid #1e293b; white-space: nowrap;
}
.result-table tr:hover td { background: #1e293b; }
.result-table tr:nth-child(even) td { background: rgba(255,255,255,0.02); }
.result-table tr:nth-child(even):hover td { background: #1e293b; }
.modal-footer {
  display: flex; justify-content: space-between; align-items: center;
  padding: 12px 20px; border-top: 1px solid #1e293b; flex-shrink: 0;
}
.row-count { font-size: 12px; color: #64748b; }
.btn-close {
  background: #334155; border: none; border-radius: 8px;
  padding: 9px 20px; color: white; cursor: pointer; font-size: 13px; font-weight: 600;
}
.btn-close:hover { background: #475569; }
.btn-excel {
  background: #166534; border: 1px solid #22c55e; border-radius: 8px;
  padding: 9px 18px; color: #86efac; font-weight: 600; cursor: pointer; font-size: 13px;
}
.btn-excel:hover { background: #15803d; color: white; }
</style>