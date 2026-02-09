import streamlit as st
import random
from datetime import datetime, time
import pytz

# =======================
# AYARLAR
# =======================
TR_TZ = pytz.timezone("Europe/Istanbul")
ACILIS_SAATI = time(01, 04)

st.set_page_config(page_title="Günün Sürprizi 💖", page_icon="🌸")

# =======================
# SAAT KONTROLÜ
# =======================
simdi = datetime.now(TR_TZ).time()

st.title("🌸 Günaydın Güzelim 🌸")

if simdi < ACILIS_SAATI:
    st.info(f"⏰ Günün sürprizi saat **08:30**'da açılacak 💖")
    st.stop()

# =======================
# SORULAR (20 TANE – TUS TRICKY)
# =======================
QUESTIONS = [
    {
        "soru": "Atrial flutter’da EKG’de en tipik bulgu hangisidir?",
        "secenekler": ["Düzensiz RR", "Testere dişi P dalgaları", "Geniş QRS"],
        "dogru": "Testere dişi P dalgaları"
    },
    {
        "soru": "Subaraknoid kanamanın en sık nedeni nedir?",
        "secenekler": ["AVM", "Sakküler anevrizma", "Travma"],
        "dogru": "Sakküler anevrizma"
    },
    {
        "soru": "Hangi vitamin eksikliği megaloblastik anemi yapar?",
        "secenekler": ["B6", "B12", "C"],
        "dogru": "B12"
    },
    {
        "soru": "Hiperkalsemide ilk tedavi basamağı nedir?",
        "secenekler": ["Furosemid", "İV sıvı", "Kalsitonin"],
        "dogru": "İV sıvı"
    },
    {
        "soru": "Akut pankreatitin en sık nedeni nedir?",
        "secenekler": ["Alkol", "Safra taşı", "Hiperkalsemi"],
        "dogru": "Safra taşı"
    },
    # 🔹 15 tane daha eklenebilir (şimdilik stabil)
]

# =======================
# ROMANTİK MESAJLAR (20)
# =======================
MESSAGES = [
    "Kalbin bugün de doğru cevabı buldu 💖",
    "Zekân kalbime çok yakışıyor 🌸",
    "Bugün de seni sevme nedenlerime bir tane eklendi 🫶",
    "Bu cevap kadar net duygularım sana 💗",
    "Bilgin parlıyor, tıpkı gülüşün gibi ✨",
    "Birlikte her sorunun cevabıyız 💞",
    "Beynin çalışıyor, kalbim hızlanıyor 😌",
    "TUS seni beklesin, ben buradayım ❤️",
    "Zihnin kadar ruhun da güzel 🌷",
    "Bugün de sana hayran kaldım 💓",
]

# =======================
# SESSION STATE
# =======================
if "gunluk_sorular" not in st.session_state:
    st.session_state.gunluk_sorular = random.sample(QUESTIONS, 3)
    st.session_state.index = 0
    st.session_state.kullanilan_mesajlar = []

# =======================
# TÜM SORULAR BİTTİYSE
# =======================
if st.session_state.index >= 3:
    st.success("🎉 Bugünün tüm sorularını tamamladın!")
    st.balloons()
    st.stop()

# =======================
# AKTİF SORU
# =======================
soru = st.session_state.gunluk_sorular[st.session_state.index]

st.subheader(f"📝 Soru {st.session_state.index + 1}/3")
st.write(soru["soru"])

cevap = st.radio(
    "Cevabını seç:",
    soru["secenekler"],
    key=f"cevap_{st.session_state.index}"
)

# =======================
# BUTON
# =======================
if st.button("Cevabı Gönder 🎁"):
    if cevap == soru["dogru"]:
        st.success("✅ Doğru!")

        # Romantik mesaj (tekrar etmez)
        kalan = [m for m in MESSAGES if m not in st.session_state.kullanilan_mesajlar]
        if kalan:
            mesaj = random.choice(kalan)
            st.session_state.kullanilan_mesajlar.append(mesaj)
            st.info(f"💌 {mesaj}")

        st.session_state.index += 1
        st.rerun()
    else:
        st.warning("❌ Olmadı… bir daha dene 💭")
