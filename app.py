import streamlit as st
import json
import random
import os
from datetime import datetime, time
import pytz

# ===================== AYARLAR =====================
TIMEZONE = pytz.timezone("Europe/Istanbul")
ACILIS_SAATI = time(11, 00)
GUNLUK_SORU_SAYISI = 5

QUESTIONS_FILE = "questions.json"
ASKED_FILE = "asked_questions.json"
MESSAGES_FILE = "messages.json"
USED_MESSAGES_FILE = "used_messages.json"
# ==================================================

st.set_page_config(page_title="Günün Seçilmiş Soruları", page_icon="👑")
st.title("💖 Günaydın Güzelliğim 💕")

# ===================== CSS ANİMASYONLAR =====================
st.markdown("""
<style>

/* Yukarı uçan kalpler */
.heart-float {
  position: fixed;
  bottom: -20px;
  font-size: 24px;
  animation: floatUp 3s linear forwards;
  color: #ff4d88;
  z-index: 9999;
}

@keyframes floatUp {
  0% { transform: translateY(0); opacity: 1; }
  100% { transform: translateY(-100vh); opacity: 0; }
}

/* Sallanan büyük kalpler */
.heart-swing {
  font-size: 70px;
  display: inline-block;
  animation: swing 1s ease-in-out infinite;
  margin: 0 10px;
}

@keyframes swing {
  0% { transform: rotate(-12deg); }
  50% { transform: rotate(12deg); }
  100% { transform: rotate(-12deg); }
}

/* Konfeti */
.confetti {
  position: fixed;
  width: 10px;
  height: 10px;
  top: -10px;
  animation: fall 3s linear forwards;
  z-index: 9999;
}

@keyframes fall {
  0% { transform: translateY(0) rotate(0deg); opacity: 1; }
  100% { transform: translateY(100vh) rotate(720deg); opacity: 0; }
}

/* Kraliçe rozeti */
.queen-badge {
  display: inline-block;
  padding: 15px 30px;
  font-size: 28px;
  font-weight: bold;
  color: white;
  background: linear-gradient(45deg, #ff4d88, #ff99cc);
  border-radius: 50px;
  box-shadow: 0 0 20px rgba(255, 77, 136, 0.7);
  animation: glow 1.5s ease-in-out infinite alternate;
  margin-top: 30px;
}

@keyframes glow {
  from { box-shadow: 0 0 10px rgba(255, 77, 136, 0.6); }
  to { box-shadow: 0 0 30px rgba(255, 77, 136, 1); }
}

</style>
""", unsafe_allow_html=True)
# ============================================================

# ===================== ZAMAN KONTROL =====================
now = datetime.now(TIMEZONE).time()
if now < ACILIS_SAATI:
    st.info(f"⏰ Günün seçilmiş soruları saat {ACILIS_SAATI.strftime('%H:%M')}'de açılacak 💖")
    st.stop()
# ========================================================

# ===================== JSON YARDIMCILAR =====================
def load_json(path, default):
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(default, f, ensure_ascii=False, indent=2)
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
# ==========================================================

# ===================== VERİLER =====================
questions = load_json(QUESTIONS_FILE, [])
asked_questions = load_json(ASKED_FILE, [])
messages = load_json(MESSAGES_FILE, [])
used_messages = load_json(USED_MESSAGES_FILE, [])
# ==================================================

# ===================== GÜN KONTROL =====================
today = datetime.now(TIMEZONE).strftime("%Y-%m-%d")

if "today" not in st.session_state or st.session_state.today != today:
    st.session_state.today = today
    st.session_state.q_index = 0
    st.session_state.today_questions = []
    st.session_state.show_message = None
    st.session_state.correct_count = 0

    remaining = [q for q in questions if q["id"] not in asked_questions]

    if len(remaining) < GUNLUK_SORU_SAYISI:
        st.success("🎉 Tüm sorular tamamlandı!")
        st.stop()

    st.session_state.today_questions = random.sample(
        remaining, GUNLUK_SORU_SAYISI
    )
# ==================================================

# ===================== MESAJ =====================
if st.session_state.get("show_message"):
    st.success("💖 " + st.session_state.show_message)
    st.session_state.show_message = None
# ==================================================

today_questions = st.session_state.today_questions
q_index = st.session_state.q_index

# ===================== TEST BİTTİ =====================
if q_index >= len(today_questions):

    if st.session_state.correct_count == GUNLUK_SORU_SAYISI:

        st.success("👑 MÜKEMMELSİN! 5/5 Yaptın! 💖🔥")

        st.markdown("""
        <div style="text-align:center;">
            <div class="queen-badge">
                👑 BUGÜNÜN KRALİÇESİ 👑
            </div>
        </div>
        """, unsafe_allow_html=True)

        colors = ["#ff4d88", "#ffcc00", "#66ff66", "#66ccff", "#ff6666"]
        for i in range(60):
            st.markdown(
                f'<div class="confetti" style="left:{random.randint(0,100)}%; background-color:{random.choice(colors)};"></div>',
                unsafe_allow_html=True
            )

        for i in range(20):
            st.markdown(
                f'<div class="heart-float" style="left:{random.randint(0,100)}%;">💖</div>',
                unsafe_allow_html=True
            )

        st.markdown("""
        <div style="text-align:center; margin-top:40px;">
            <span class="heart-swing">❤️</span>
            <span class="heart-swing">💖</span>
            <span class="heart-swing">💕</span>
            <span class="heart-swing">💗</span>
            <span class="heart-swing">💘</span>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.success("🎉 Bugünün tüm sorularını tamamladın 💖")

        st.markdown("""
        <div style="text-align:center; margin-top:40px;">
            <span class="heart-swing">❤️</span>
            <span class="heart-swing">💖</span>
            <span class="heart-swing">💕</span>
            <span class="heart-swing">💗</span>
            <span class="heart-swing">💘</span>
        </div>
        """, unsafe_allow_html=True)

    st.stop()
# ==================================================

# ===================== SORU =====================
q = today_questions[q_index]

st.subheader(f"📝 Soru {q_index + 1}")
st.write(q["soru"])

choice = st.radio(
    "Cevabını seç:",
    q["secenekler"],
    key=f"choice_{q_index}"
)

if st.button("Cevabı Onayla ✅"):
    if choice == q["dogru"]:

        asked_questions.append(q["id"])
        save_json(ASKED_FILE, asked_questions)

        st.session_state.correct_count += 1

        for i in range(15):
            st.markdown(
                f'<div class="heart-float" style="left:{random.randint(0,100)}%;">❤️</div>',
                unsafe_allow_html=True
            )

        available_messages = [m for m in messages if m not in used_messages]

        if available_messages:
            msg = random.choice(available_messages)
            used_messages.append(msg)
            save_json(USED_MESSAGES_FILE, used_messages)
            st.session_state.show_message = msg

        st.session_state.q_index += 1
        st.rerun()
    else:
        st.warning("❌ Hadi bir daha deneyelim aşkım 💕")
# ==================================================
