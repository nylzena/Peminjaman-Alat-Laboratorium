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
    body { margin:0; background:var(--bg); color:var(--text); font-family:sans-serif; }
    .container { max-width:960px; margin:24px auto; padding:0 16px; }
    .card { background:var(--card); border:1px solid var(--border); border-radius:12px; padding:20px; margin-bottom:16px; }
    h1,h2 { color:var(--primary); margin:0 0 12px 0; }
    label { display:block; margin-bottom:6px; font-weight:600; }
    input { width:100%; padding:10px; border:1px solid var(--border); border-radius:8px; }
    .grid { display:grid; grid-template-columns:1fr 1fr; gap:12px; }
    .btn { padding:10px 16px; border-radius:10px; cursor:pointer; font-weight:600; }
    .btn-primary { background:var(--primary); color:#fff; }
    .btn-danger { background:var(--danger); color:#fff; }
    .summary-item { margin-bottom:8px; }
    .hero-text { font-size:18px; font-weight:700; text-align:center; margin:16px 0; color:var(--primary); }
  </style>
</head>
<body>
  <div class="container">
    <!-- Step 1: Form identitas -->
    <div id="step1" class="card">
      <h1>Form Peminjaman Alat Laboratorium</h1>
      <div class="grid">
        <div><label>Nama</label><input id="nama" type="text"></div>
        <div><label>Kelompok</label><input id="kelompok" type="text"></div>
        <div><label>Tanggal</label><input id="tanggal" type="date"></div>
        <div><label>Judul Praktik</label><input id="judul" type="text"></div>
        <div><label>Mata Kuliah</label><input id="matkul" type="text"></div>
      </div>
      <div style="margin-top:12px;">
        <button class="btn btn-primary" onclick="goSummary()">Lanjutkan</button>
      </div>
    </div>

    <!-- Step 2: Summary -->
    <div id="summary" class="card" style="display:none;">
      <h2>Ringkasan Peminjaman</h2>
      <div class="summary-item"><b>Nama:</b> <span id="sumNama"></span></div>
      <div class="summary-item"><b>Kelompok:</b> <span id="sumKelompok"></span></div>
      <div class="summary-item"><b>Tanggal:</b> <span id="sumTanggal"></span></div>
      <div class="summary-item"><b>Judul Praktik:</b> <span id="sumJudul"></span></div>
      <div class="summary-item"><b>Mata Kuliah:</b> <span id="sumMatkul"></span></div>

      <h3>Daftar Alat yang Dipilih</h3>
      <ul id="listAlat">
        <li>Pipet tetes</li>
        <li>Gelas beaker 250 mL</li>
        <li>Buret Mikro</li>
        <!-- contoh, nanti bisa diisi dinamis -->
      </ul>

      <div class="hero-text">Jika ingin mengembalikan alat, tekan tombol dibawah ini!</div>
      <div style="text-align:center;">
        <button class="btn btn-danger">LANJUTKAN</button>
      </div>
    </div>
  </div>

  <script>
    function goSummary(){
      document.getElementById("sumNama").textContent = document.getElementById("nama").value;
      document.getElementById("sumKelompok").textContent = document.getElementById("kelompok").value;
      document.getElementById("sumTanggal").textContent = document.getElementById("tanggal").value;
      document.getElementById("sumJudul").textContent = document.getElementById("judul").value;
      document.getElementById("sumMatkul").textContent = document.getElementById("matkul").value;
      document.getElementById("step1").style.display="none";
      document.getElementById("summary").style.display="block";
    }
  </script>
</body>
</html>
