import streamlit as st
import json
import random
import datetime
from zoneinfo import ZoneInfo
from pathlib import Path

# -------------------------
# AYARLAR
# -------------------------
st.set_page_config(page_title="Günaydın Güzelim", layout="centered")
TZ = ZoneInfo("Europe/Istanbul")
GUNLUK_SORU_SAYISI = 3

BASE_PATH = Path(__file__).parent
QUESTIONS_FILE = BASE_PATH / "questions.json"
ASKED_FILE = BASE_PATH / "asked_questions.json"

# -------------------------
# DOSYA OKUMA
# -------------------------
def load_json(path):
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

questions = load_json(QUESTIONS_FILE)
asked_ids = load_json(ASKED_FILE)

# -------------------------
# GÜNLÜK SORU SEÇİMİ
# -------------------------
today = datetime.date.today().isoformat()

if "today" not in st.session_state or st.session_state.today != today:
    st.session_state.today = today
    st.session_state.answers = {}
    st.session_state.correct = 0

    kalan_sorular = [q for q in questions if q["id"] not in asked_ids]

    if len(kalan_sorular) < GUNLUK_SORU_SAYISI:
        st.error("Sorulacak yeni soru kalmadı 💔")
        st.stop()

    gunluk_sorular = random.sample(kalan_sorular, GUNLUK_SORU_SAYISI)
    st.session_state.gunluk_sorular = gunluk_sorular

    for q in gunluk_sorular:
        asked_ids.append(q["id"])

    save_json(ASKED_FILE, asked_ids)

# -------------------------
# BAŞLIK
# -------------------------
st.markdown("## 🌸 Günaydın Güzelim 🌸")
st.markdown("### 🧠 Günün TUS Soruları")

# -------------------------
# SORULAR
# -------------------------
for idx, soru in enumerate(st.session_state.gunluk_sorular):
    st.markdown(f"**{idx+1}. {soru['soru']}**")

    cevap = st.radio(
        "",
        soru["secenekler"],
        key=f"soru_{soru['id']}"
    )

    if st.button("Cevabı Kontrol Et", key=f"btn_{soru['id']}"):
        if cevap == soru["dogru"]:
            st.success("Doğru 💖")
            st.session_state.correct += 1
        else:
            st.error(f"Yanlış 😌 Doğru cevap: {soru['dogru']}")

    st.markdown("---")

# -------------------------
# ROZET
# -------------------------
if st.session_state.correct >= GUNLUK_SORU_SAYISI:
    st.balloons()
    st.markdown("### ✅ Bugün Çözüldü 💖")
