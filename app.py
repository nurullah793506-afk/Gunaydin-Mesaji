import streamlit as st
import datetime
import random

st.set_page_config(page_title="Günaydın Güzelim", layout="centered")

# -----------------------------
# SAAT AYARI
# -----------------------------
ACILIS_SAATI = datetime.time(5, 43)  # burayı istediğin gibi değiştir

simdi = datetime.datetime.now().time()

st.markdown("""
<style>
.card {
    background-color: #fff0f6;
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
.badge {
    background-color: #ff4d6d;
    color: white;
    padding: 6px 14px;
    border-radius: 20px;
    font-weight: bold;
    display: inline-block;
    margin-top: 12px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# KAPALIYSA
# -----------------------------
if simdi < ACILIS_SAATI:
    st.markdown("## 🌸 Günaydın Her Şeyim ❤️")
    st.info(f"⏰ Günün sürprizi saat **{ACILIS_SAATI.strftime('%H:%M')}**'de açılacak 💖")
    st.stop()

# -----------------------------
# SORULAR
# -----------------------------
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

romantik_mesajlar = [
    "Kalbim seninle aynı ritimde atıyor ❤️",
    "Güne seni düşünerek başlamak en güzel alışkanlığım 💕",
    "Bilgin kadar gülüşün de ışık saçıyor ✨",
    "Bugün de seni sevmenin huzuruyla uyandım 🌸",
    "Doğru cevaptan daha güzeli sensin 😌"
]

# -----------------------------
# SESSION STATE
# -----------------------------
if "dogru_sayisi" not in st.session_state:
    st.session_state.dogru_sayisi = 0

if "cozuldu" not in st.session_state:
    st.session_state.cozuldu = False

# -----------------------------
# BAŞLIK
# -----------------------------
st.markdown("## 🌸 Günaydın Güzelim 🌸")
st.markdown("### 📝 Günün Soruları")

# -----------------------------
# İLK 3 SORU
# -----------------------------
for i in range(3):
    soru = questions[i]

    with st.container():
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
                st.session_state.dogru_sayisi += 1
                st.success(random.choice(romantik_mesajlar))
            else:
                st.error("Olmadı aşkım 😌 bir daha dene 💗")

# -----------------------------
# ROZET
# -----------------------------
if st.session_state.dogru_sayisi >= 3 and not st.session_state.cozuldu:
    st.session_state.cozuldu = True
    st.balloons()
    st.markdown('<div class="badge">✅ Bugün Çözüldü</div>', unsafe_allow_html=True)
