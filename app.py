import streamlit as st
import time

# Konfigurasi tab browser
st.set_page_config(page_title="Selamat Juara 3 Piano! 🎹", page_icon="🥉", layout="centered")

# Mengeluarkan efek balon otomatis saat web pertama dibuka
st.balloons()

# Menambahkan CSS agar judulnya menyala (glowing) dan meriah
st.markdown("""
<style>
.glowing-text {
    font-size: 55px !important;
    font-weight: 800;
    text-align: center;
    color: #FF4B4B;
    animation: glow 1.5s ease-in-out infinite alternate;
}
@keyframes glow {
    from { text-shadow: 0 0 10px #FF4B4B, 0 0 20px #FF4B4B; }
    to { text-shadow: 0 0 20px #FFD166, 0 0 30px #FFD166; }
}
.sub-text {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Bagian Judul
st.markdown('<p class="glowing-text">🎉 SELAMAT! 🎉</p>', unsafe_allow_html=True)
st.markdown('<h2 class="sub-text">Telah Memenangkan JUARA 3 🥉<br>Lomba Alat Musik Piano! 🎹🎵</h2>', unsafe_allow_html=True)

st.write("---")

# Bagian Kata-kata Ucapan
st.subheader("Aku super bangga padamu! ✨")
st.write("""
Semua waktu yang kamu habiskan untuk berlatih, mengulang nada yang sama berkali-kali, 
dan dedikasimu duduk berjam-jam di depan tuts piano akhirnya terbayar lunas. 

Jari-jarimu menari dengan sangat indah. Gelar Juara 3 ini adalah bukti nyata dari bakat, kesabaran, dan kerja kerasmu. 
Jangan pernah berhenti bermain, teruslah berkarya, dan biarkan dunia mendengar melodi indahmu selanjutnya! 🎶💖
""")

st.write("---")

# Tombol untuk efek meriah tambahan
st.write("Ada kejutan kecil buat kamu, coba klik tombol di bawah:")
if st.button("🌟 KLIK UNTUK MERAYAKAN! 🌟", use_container_width=True):
    # Memunculkan balon lagi
    st.balloons()
    # Memunculkan notifikasi kecil (toast) di pojok bawah
    st.toast('Kamu Luar Biasa! 🎹🏆', icon='😍')
    # Jeda sebentar, lalu munculkan efek salju/konfeti
    time.sleep(0.5)
    st.snow()
