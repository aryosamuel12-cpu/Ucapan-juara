import streamlit as st
import time

# Konfigurasi tab browser
st.set_page_config(page_title="Selamat Juara 3 Piano! 🎹", page_icon="🎁", layout="centered")

# Mengeluarkan efek balon otomatis saat web pertama dibuka
st.balloons()

# CSS Kustom untuk animasi kotak kado, teks bercahaya, dan kartu ucapan
st.markdown("""
<style>
    /* Teks Judul Glowing */
    .glowing-text {
        font-size: 55px !important;
        font-weight: 900;
        text-align: center;
        background: -webkit-linear-gradient(45deg, #FFD700, #FF8C00, #FF4B4B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: glow 1.5s ease-in-out infinite alternate;
        margin-bottom: 0px;
        padding-bottom: 0px;
    }
    @keyframes glow {
        from { text-shadow: 0 0 10px rgba(255, 215, 0, 0.2), 0 0 20px rgba(255, 140, 0, 0.2); }
        to { text-shadow: 0 0 20px rgba(255, 75, 75, 0.6), 0 0 30px rgba(255, 215, 0, 0.6); }
    }
    
    /* Animasi Kado Melompat */
    .bouncing-gift {
        font-size: 70px;
        text-align: center;
        animation: bounce 2s infinite;
        margin-top: 10px;
        margin-bottom: -10px;
    }
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
        40% {transform: translateY(-25px);}
        60% {transform: translateY(-12px);}
    }
    
    /* Merapikan posisi teks */
    .center-text {
        text-align: center;
        margin-top: 10px;
    }
    
    /* Desain Kartu Ucapan */
    .message-card {
        background-color: rgba(255, 255, 255, 0.05);
        border: 2px solid #FFD700;
        border-radius: 15px;
        padding: 30px 40px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(255, 215, 0, 0.15);
        margin-top: 30px;
        margin-bottom: 40px;
    }
</style>
""", unsafe_allow_html=True)

# 🎁 Bagian Atas: Kado & Judul
st.markdown('<p class="bouncing-gift">🎁🎹🥇</p>', unsafe_allow_html=True)
st.markdown('<p class="glowing-text">SELAMAT!</p>', unsafe_allow_html=True)
st.markdown('<h3 class="center-text">Telah Memenangkan <b>JUARA 3</b> 🥉<br>Lomba Alat Musik Piano! 🎶</h3>', unsafe_allow_html=True)

# 💌 Bagian Tengah: Kartu Ucapan yang Rapi
st.markdown("""
<div class="message-card">
    <h4 style="color: #FFD700; margin-bottom: 20px;">✨ Aku super bangga padamu! ✨</h4>
    <p style="font-size: 16px; line-height: 1.7; margin-bottom: 15px;">
        Semua waktu yang kamu habiskan untuk berlatih, mengulang nada yang sama berkali-kali, 
        dan dedikasimu duduk berjam-jam di depan tuts piano akhirnya terbayar lunas.
    </p>
    <p style="font-size: 16px; line-height: 1.7;">
        Jari-jarimu menari dengan sangat indah. Gelar Juara 3 ini adalah bukti nyata dari bakat, kesabaran, dan kerja kerasmu. 
        Jangan pernah berhenti bermain, teruslah berkarya, dan biarkan dunia mendengar melodi indahmu selanjutnya! 🎵💖
    </p>
</div>
""", unsafe_allow_html=True)

# 🎉 Bagian Bawah: Tombol Kejutan
st.markdown('<p class="center-text" style="color: #FFD700; font-size: 15px;">👇 Buka kado spesialmu di bawah ini 👇</p>', unsafe_allow_html=True)

# Menggunakan kolom agar tombol tidak terlalu lebar dan berada pas di tengah
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🎁 BUKA KADO KEJUTAN! 🎁", use_container_width=True):
        st.balloons()
        st.toast('Kamu Sangat Hebat! 🎹🏆', icon='😍')
        time.sleep(0.5)
        st.snow()
        st.success("Teruslah bersinar dan mainkan melodi terindahmu! ✨")
