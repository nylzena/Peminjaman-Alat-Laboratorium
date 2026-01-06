<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Form Peminjaman Alat Laboratorium</title>
  <style>
    :root {
      --bg: #f4f1e9;
      --card: #fffaf3;
      --text: #3e2f1c;
      --muted: #7a6f5d;
      --primary: #a97155;
      --danger: #b23a48;
      --success: #4a7c59;
      --border: #d9cbb3;
    }
    * { box-sizing: border-box; }
    body { margin:0; background:var(--bg); color:var(--text); font-family:system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial; }
    .container { max-width:960px; margin:24px auto; padding:0 16px; }
    .card { background:var(--card); border:1px solid var(--border); border-radius:12px; padding:20px; margin-bottom:16px; }
    h1,h2,h3 { color:var(--primary); margin:0 0 12px 0; }
    label { display:block; margin-bottom:6px; font-weight:600; color:var(--text); }
    input, select, textarea { width:100%; padding:10px; border:1px solid var(--border); border-radius:8px; background:#fff; color:var(--text); }
    .grid { display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:12px; }
    .btn { padding:10px 16px; border-radius:10px; cursor:pointer; font-weight:600; border:0; }
    .btn-primary { background:var(--primary); color:#fff; }
    .btn-danger { background:var(--danger); color:#fff; }
    .btn-muted { background:transparent; color:var(--muted); border:1px solid var(--border); }
    .summary-item { margin-bottom:8px; }
    .hero-text { font-size:18px; font-weight:700; text-align:center; margin:16px 0; color:var(--primary); }
    .actions { margin-top:12px; display:flex; gap:8px; justify-content:flex-end; flex-wrap:wrap; }
    ul { padding-left:20px; }
    .hidden { display:none; }
    @media (max-width:480px) {
      .hero-text { font-size:16px; }
    }
  </style>
</head>
<body>
  <div class="container">
    <!-- Step 1: Form identitas -->
    <div id="step1" class="card" aria-live="polite">
      <h1>Form Peminjaman Alat Laboratorium</h1>

      <form id="loanForm" onsubmit="return false;" novalidate>
        <div class="grid">
          <div>
            <label for="nama">Nama</label>
            <input id="nama" name="nama" type="text" required aria-required="true" />
          </div>

          <div>
            <label for="kelompok">Kelompok</label>
            <input id="kelompok" name="kelompok" type="text" required aria-required="true" />
          </div>

          <div>
            <label for="tanggal">Tanggal</label>
            <input id="tanggal" name="tanggal" type="date" required aria-required="true" />
          </div>

          <div>
            <label for="judul">Judul Praktik</label>
            <input id="judul" name="judul" type="text" required aria-required="true" />
          </div>

          <div>
            <label for="matkul">Mata Kuliah</label>
            <input id="matkul" name="matkul" type="text" required aria-required="true" />
          </div>
        </div>

        <div class="actions">
          <button type="button" class="btn btn-muted" onclick="resetForm()">Reset</button>
          <button type="button" class="btn btn-primary" onclick="goSummary()">Lanjutkan</button>
        </div>
      </form>
    </div>

    <!-- Step 2: Summary -->
    <div id="summary" class="card hidden" aria-live="polite">
      <h2>Ringkasan Peminjaman</h2>

      <div class="summary-item"><strong>Nama:</strong> <span id="sumNama"></span></div>
      <div class="summary-item"><strong>Kelompok:</strong> <span id="sumKelompok"></span></div>
      <div class="summary-item"><strong>Tanggal:</strong> <span id="sumTanggal"></span></div>
      <div class="summary-item"><strong>Judul Praktik:</strong> <span id="sumJudul"></span></div>
      <div class="summary-item"><strong>Mata Kuliah:</strong> <span id="sumMatkul"></span></div>

      <h3>Daftar Alat yang Dipilih</h3>
      <ul id="listAlat" aria-label="Daftar alat">
        <li>Pipet tetes</li>
        <li>Gelas beaker 250 mL</li>
        <li>Buret Mikro</li>
      </ul>

      <div class="hero-text">Jika ingin mengembalikan alat, tekan tombol di bawah ini</div>

      <div class="actions" style="justify-content:center;">
        <button type="button" class="btn btn-danger" onclick="confirmReturn()">Kembalikan</button>
        <button type="button" class="btn btn-muted" onclick="backToEdit()">Kembali</button>
      </div>
    </div>
  </div>

  <script>
    // Validasi sederhana: pastikan semua field required terisi
    function validateForm() {
      const form = document.getElementById('loanForm');
      const requiredFields = form.querySelectorAll('[required]');
      for (const field of requiredFields) {
        if (!field.value.trim()) {
          field.focus();
          alert('Mohon lengkapi kolom: ' + (field.previousElementSibling ? field.previousElementSibling.textContent : field.name));
          return false;
        }
      }
      return true;
    }

    // Format tanggal ke lokal Indonesia (contoh: 06 Januari 2026)
    function formatDateToID(dateString) {
      if (!dateString) return '';
      try {
        const d = new Date(dateString + 'T00:00:00');
        return d.toLocaleDateString('id-ID', { day: '2-digit', month: 'long', year: 'numeric' });
      } catch (e) {
        return dateString;
      }
    }

    function goSummary() {
      if (!validateForm()) return;

      document.getElementById("sumNama").textContent = document.getElementById("nama").value.trim();
      document.getElementById("sumKelompok").textContent = document.getElementById("kelompok").value.trim();
      document.getElementById("sumTanggal").textContent = formatDateToID(document.getElementById("tanggal").value);
      document.getElementById("sumJudul").textContent = document.getElementById("judul").value.trim();
      document.getElementById("sumMatkul").textContent = document.getElementById("matkul").value.trim();

      document.getElementById("step1").classList.add('hidden');
      document.getElementById("summary").classList.remove('hidden');
      // fokus ke ringkasan untuk aksesibilitas
      document.getElementById("summary").focus();
    }

    function backToEdit() {
      document.getElementById("summary").classList.add('hidden');
      document.getElementById("step1").classList.remove('hidden');
      document.getElementById("nama").focus();
    }

    function resetForm() {
      if (confirm('Reset semua isian?')) {
        document.getElementById('loanForm').reset();
      }
    }

    function confirmReturn() {
      // contoh tindakan: konfirmasi lalu tampilkan pesan
      if (confirm('Konfirmasi pengembalian alat?')) {
        alert('Terima kasih. Pengembalian dicatat.');
        // setelah konfirmasi, kembali ke form kosong
        document.getElementById('loanForm').reset();
        backToEdit();
      }
    }

    // Optional: tekan Enter pada input terakhir akan memicu goSummary
    document.getElementById('matkul').addEventListener('keydown', function(e){
      if (e.key === 'Enter') {
        e.preventDefault();
        goSummary();
      }
    });
  </script>
</body>
</html>
