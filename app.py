import streamlit as st
import datetime
from zoneinfo import ZoneInfo

# ---------------------------------
# AYARLAR
# ---------------------------------
st.set_page_config(page_title="Günaydın Güzelim", layout="centered")

TURKEY_TZ = ZoneInfo("Europe/Istanbul")
ACILIS_SAATI = datetime.time(5, 52)  # SAATİ BURADAN AYARLA

simdi = datetime.datetime.now(TURKEY_TZ).time()

# ---------------------------------
# STİL
# ---------------------------------
st.markdown("""
<style>
.card {
    background-color: #fff0f6;
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 18px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
.badge {
    background-color: #ff4d6d;
    color: white;
    padding: 8px 16px;
    border-radius: 20px;
    font-weight: bold;
    margin-top: 12px;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------
# SAAT KONTROLÜ
# ---------------------------------
if simdi < ACILIS_SAATI:
    st.markdown("## 🌸 Günaydın Her Şeyim❤️🥰😍")
    st.info(f"⏰ Günün sürprizi saat **{ACILIS_SAATI.strftime('%H:%M')}**'de açılacak 💖")
    st.stop()

# ---------------------------------
# SESSION STATE
# ---------------------------------
if "dogru_sayisi" not in st.session_state:
    st.session_state.dogru_sayisi = 0

if "mesaj_index" not in st.session_state:
    st.session_state.mesaj_index = 0

if "cozuldu" not in st.session_state:
    st.session_state.cozuldu = False

# ---------------------------------
# SORULAR
# ---------------------------------
questions = [
    {
        "soru": "Acil serviste akut koroner sendrom şüphesiyle gelen hastada ilk tetkik nedir?",
        "secenekler": ["EKG", "Akciğer Grafisi", "Kan Gazı"],
        "dogru": "EKG"
    },
    {
        "soru": "EKG'de testere dişi görünümü hangi ritim bozukluğunu gösterir?",
        "secenekler": ["Atrial Fibrilasyon", "Atrial Flutter", "Ventriküler Taşikardi"],
        "dogru": "Atrial Flutter"
    },
    {
        "soru": "Yenidoğanda K vitamini hangi kasa uygulanır?",
        "secenekler": ["M. Deltoideus", "M. Gluteus Maximus", "M. Vastus Lateralis"],
        "dogru": "M. Vastus Lateralis"
    },
    {
        "soru": "Diş Zikzik ve Erkek Zikziğin en sevdiği sebze nedir?",
        "secenekler": ["Elma", "Lahana", "Maydanoz"],
        "dogru": "Maydanoz"
    }
]

# ---------------------------------
# ROMANTİK MESAJLAR (TEKRARSIZ)
# ---------------------------------
romantik_mesajlar = [
    "Gün seninle anlamlı, ben seninle tamamım ❤️",
    "Bugünde kalbim seninle güne başladı 💕",
    "Bilgini seviyorum ama seni daha çok ✨",
    "Sabahım sen, motivasyonum sen 🌸",
    "Doğru cevaptan bile daha güzelsin 😌"
    "Seninle başlayan yeni bir güne şükürler olsun🙏❤️"
]

# ---------------------------------
# BAŞLIK
# ---------------------------------
st.markdown("## 🌸 Günaydın Güzelim 🌸")
st.markdown("### 📝 Günün Soruları")

# ---------------------------------
# İLK 3 SORU
# ---------------------------------
for i in range(4):
    soru = questions[i]

    st.markdown(f"""
    <div class="card">
    <b>{i+1}. {soru['soru']}</b>
    </div>
    """, unsafe_allow_html=True)

    cevap = st.radio(
        label="",
        options=soru["secenekler"],
        key=f"soru_{i}"
    )

    if st.button("Cevabı Kontrol Et", key=f"btn_{i}"):

        if cevap == soru["dogru"]:
            if st.session_state.mesaj_index < len(romantik_mesajlar):
                st.success(romantik_mesajlar[st.session_state.mesaj_index])
                st.session_state.mesaj_index += 1

            st.session_state.dogru_sayisi += 1
        else:
            st.error("Olmadı aşkım 😌 bir daha dene 💗")

# ---------------------------------
# ROZET
# ---------------------------------
if st.session_state.dogru_sayisi >= 4 and not st.session_state.cozuldu:
    st.session_state.cozuldu = True
    st.balloons()
    st.markdown('<div class="badge">✅ Bugün Çözüldü</div>', unsafe_allow_html=True)
