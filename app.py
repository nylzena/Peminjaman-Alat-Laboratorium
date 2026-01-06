import streamlit as st
from datetime import date
import time

st.set_page_config(
    page_title="Pengembalian Alat Praktikum",
    layout="centered"
)

# ===== FORCE BACKGROUND =====
st.markdown(
    """
    <style>
    html, body, [class*="css"]  {
        height: 100%;
        background: linear-gradient(135deg, #667eea, #764ba2) !important;
    }

    .block-container {
        background: transparent !important;
    }

    h1, h2, h3 {
        color: #ffffff !important;
        text-align: center;
    }

    label {
        color: #ffffff !important;
        font-weight: 600;
    }

    .stButton > button {
        background-color: #ffffff !important;
        color: #667eea !important;
        border-radius: 12px;
        height: 45px;
        width: 100%;
        font-size: 16px;
        font-weight: bold;
    }

    .card {
        background-color: rgba(255, 255, 255, 0.15);
        padding: 25px;
        border-radius: 16px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===== SESSION =====
if "step" not in st.session_state:
    st.session_state.step = 1
if "data" not in st.session_state:
    st.session_state.data = {}

# ===== ALAT =====
alat_list = [
    "Pipet tetes",
    "Gelas beaker",
    "Gelas ukur",
    "Labu takar",
    "Cawan petri",
    "Buret",
    "Kasa asbes",
    "Bunsen",
    "Tabung reaksi",
    "Corong kaca",
    "Penjepit kayu",
    "Batang pengaduk",
    "Kaki tiga"
]

# ===== STEP 1 =====
if st.session_state.step == 1:
    st.title("Form Peminjaman Alat Praktikum")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    nama = st.text_input("Nama")
    kelompok = st.text_input("Kelompok")
    tanggal = st.date_input("Tanggal", value=date.today())
    judul = st.text_input("Judul Praktik")
    matkul = st.text_input("Mata Kuliah")

    st.subheader("Pilih Alat")
    alat_dipilih = [a for a in alat_list if st.checkbox(a)]

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Lanjutkan"):
        if not nama or not kelompok or not judul or not matkul or not alat_dipilih:
            st.warning("Semua data wajib diisi")
        else:
            st.session_state.data = {
                "nama": nama,
                "kelompok": kelompok,
                "tanggal": tanggal,
                "judul": judul,
                "matkul": matkul,
                "alat": alat_dipilih
            }
            st.session_state.step = 2
            st.rerun()

# ===== STEP 2 =====
elif st.session_state.step == 2:
    st.title("Resume Konfirmasi")

    d = st.session_state.data

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write(f"Nama: {d['nama']}")
    st.write(f"Kelompok: {d['kelompok']}")
    st.write(f"Tanggal: {d['tanggal']}")
    st.write(f"Judul: {d['judul']}")
    st.write(f"Mata Kuliah: {d['matkul']}")

    st.subheader("Alat Dipinjam")
    for a in d["alat"]:
        st.write("- ", a)

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Lanjutkan"):
        st.session_state.step = 3
        st.rerun()

# ===== STEP 3 =====
elif st.session_state.step == 3:
    st.title("Upload Bukti Pengembalian")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    foto = st.file_uploader("Upload foto", type=["jpg", "jpeg", "png"])
    if foto:
        st.image(foto, use_container_width=True)
        if st.button("Konfirmasi"):
            st.session_state.step = 4
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ===== STEP 4 =====
elif st.session_state.step == 4:
    st.title("Status")

    with st.spinner("Memproses..."):
        time.sleep(2)

    st.success("Pengembalian terkonfirmasi!")
    st.balloons()
