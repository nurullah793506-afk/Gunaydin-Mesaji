import streamlit as st
import json
import random
import os
from datetime import datetime, time
import pytz

# ===================== AYARLAR =====================
TIMEZONE = pytz.timezone("Europe/Istanbul")
ACILIS_SAATI = time(1, 17)   # 08:30
GUNLUK_SORU_SAYISI = 3

QUESTIONS_FILE = "questions.json"
ASKED_FILE = "asked_questions.json"
MESSAGES_FILE = "messages.json"
USED_MESSAGES_FILE = "used_messages.json"
# ==================================================

st.set_page_config(page_title="Günün Sürprizi", page_icon="🌸")
st.title("🌸 Günaydın Güzelim 🌸")

# ===================== ZAMAN KONTROL =====================
now = datetime.now(TIMEZONE).time()
if now < ACILIS_SAATI:
    st.info(f"⏰ Günün sürprizi saat {ACILIS_SAATI.strftime('%H:%M')}'de açılacak 💖")
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

# ===================== VERİLERİ YÜKLE =====================
questions = load_json(QUESTIONS_FILE, [])
asked_questions = load_json(ASKED_FILE, [])
messages = load_json(MESSAGES_FILE, [])
used_messages = load_json(USED_MESSAGES_FILE, [])
# ==========================================================

# ===================== BUGÜNÜN SORULARI =====================
today = datetime.now(TIMEZONE).strftime("%Y-%m-%d")

if "today" not in st.session_state or st.session_state.today != today:
    st.session_state.today = today
    st.session_state.q_index = 0

    remaining_questions = [
        q for q in questions if q["id"] not in asked_questions
    ]

    if len(remaining_questions) < GUNLUK_SORU_SAYISI:
        st.success("🎉 Bugünün tüm sorularını tamamladın!")
        st.stop()

    st.session_state.today_questions = random.sample(
        remaining_questions, GUNLUK_SORU_SAYISI
    )
# ===========================================================

today_questions = st.session_state.today_questions
q_index = st.session_state.q_index

if q_index >= len(today_questions):
    st.success("🎉 Bugünün tüm sorularını tamamladın!")
    st.stop()

# ===================== SORU GÖSTER =====================
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
        st.success("✅ Doğru!")

        # Soruyu kalıcı olarak işaretle
        asked_questions.append(q["id"])
        save_json(ASKED_FILE, asked_questions)

        # Romantik mesaj (tekrar etmeyen)
        available_messages = [
            m for m in messages if m not in used_messages
        ]

        if available_messages:
            romantic_message = random.choice(available_messages)
            used_messages.append(romantic_message)
            save_json(USED_MESSAGES_FILE, used_messages)
            st.success("💖 " + romantic_message)

        st.balloons()
        st.session_state.q_index += 1
        st.rerun()
    else:
        st.warning("❌ hadi bir daha deneyelim aşkım 💭")
# =====================================================
