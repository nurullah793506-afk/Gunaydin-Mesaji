import streamlit as st
import datetime
from zoneinfo import ZoneInfo

# ================== SAYFA ==================
st.set_page_config(
    page_title="Günün Sürprizi",
    page_icon="🌸",
    layout="centered"
)

# ================== CSS ==================
st.markdown("""
<style>
.card {
    background: #ffffff;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    margin-top: 20px;
}
.badge {
    background: #4CAF50;
    color: white;
    padding: 6px 14px;
    border-radius: 20px;
    display: inline-block;
    font-size: 14px;
    margin-bottom: 10px;
}
.title {
    text-align: center;
    font-size: 26px;
    font-weight: 600;
}
.subtitle {
    text-align: center;
    color: #666;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🌸 Günaydın Güzelim 🌸</div>", unsafe_allow_html=True)

# ================== SAAT ==================
now = datetime.datetime.now(ZoneInfo("Europe/Istanbul"))
unlock_time = now.replace(hour=5, minute=35, second=0, microsecond=0)

if now < unlock_time:
    st.markdown(f"""
    <div class='card subtitle'>
        ⏰ Günün sürprizi saat <b>{unlock_time.strftime('%H:%M')}</b>'da açılacak 💖
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# ================== GÜN RESET ==================
today = now.date()

if "tarih" not in st.session_state or st.session_state.tarih != today:
    st.session_state.tarih = today
    st.session_state.soru_index = 0
    st.session_state.cozuldu = False

# ================== GÜNAYDIN ==================
gunaydin_mesajlari = [
    "Bugün de kalbim seninle güne başladı 💕",
    "Seninle başlayan yeni bir güne şükürler olsun ✨",
    "Bilgin kadar güzel bir gün olsun 🌷",
    "Yine gülüşünle aydınlanan bir sabah ☀️"
]

st.markdown(f"""
<div class='card subtitle'>
{gunaydin_mesajlari[today.toordinal() % len(gunaydin_mesajlari)]}
</div>
""", unsafe_allow_html=True)

# ================== SORULAR ==================
questions = [
    {
        "soru": "Acil serviste akut koroner sendrom şüphesiyle gelen hastada ilk tetkik nedir?",
        "secenekler": ["EKG", "Akciğer Grafisi", "Kan Gazı"],
        "dogru": "EKG",
        "mesaj": "Kalbim seninle aynı ritimde atıyor ❤️"
    },
    {
        "soru": "Diş Zikzik ve Erkek Zikziğin en sevdiği sebze nedir?",
        "secenekler": ["Elma", "Lahana", "Maydanoz"],
        "dogru": "Maydanoz",
        "mesaj": "Kuşlarımız kadar neşeli bir gün geçir 🐦"
    },
    {
        "soru": "EKG'de testere dişi görünümü hangi ritim bozukluğunu gösterir?",
        "secenekler": ["Atrial Fibrilasyon", "Atrial Flutter", "Ventriküler Taşikardi"],
        "dogru": "Atrial Flutter",
        "mesaj": "Aşk ritmimiz daim olsun 💓"
    },
    {
        "soru": "Yenidoğanda K vitamini hangi kasa uygulanır?",
        "secenekler": ["M. Deltoideus", "M. Gluteus Maximus", "M. Vastus Lateralis"],
        "dogru": "M. Vastus Lateralis",
        "mesaj": "Bilgin de güzelliğin gibi parıl parıl ✨"
    }
]

# ================== TÜM SORULAR BİTTİYSE ==================
if st.session_state.soru_index >= len(questions):
    st.markdown("""
    <div class='card subtitle'>
        🌸 Bugünün tüm sorularını bitirdin 🌸  
        <br><br>
        Hem bilginle hem kalbinle yine harikaydın 💖  
        Yarın yeni bir sürprizde buluşalım 😌
    </div>
    """, unsafe_allow_html=True)
    st.session_state.cozuldu = True
    st.stop()

# ================== AKTİF SORU ==================
soru = questions[st.session_state.soru_index]

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown(f"### 📝 Soru {st.session_state.soru_index + 1}")
st.write(soru["soru"])

secim = st.radio(
    "Cevabını seç:",
    soru["secenekler"],
    key=f"secim_{st.session_state.soru_index}"
)

if st.button("Cevabı Kontrol Et 🎁"):
    if secim == soru["dogru"]:
        st.success(soru["mesaj"])
        st.balloons()
        st.session_state.soru_index += 1
        st.experimental_rerun()
    else:
        st.warning("Bir tık daha düşün 💭 Tekrar dene 😌")

st.markdown("</div>", unsafe_allow_html=True)
