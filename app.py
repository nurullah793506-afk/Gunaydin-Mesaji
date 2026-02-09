import streamlit as st
import random

# Uygulama Teması ve Başlığı
st.set_page_config(page_title="Günün Sürprizi", page_icon="❤️ 🩺")

st.markdown("<h1 style='text-align: center; color: #e91e63;'>🌸 Günaydın Güzelim 🌸</h1>", unsafe_allow_status_code=True)

# Soru Havuzu (Tıp + Romantizm + Kişisel)
if 'soru_no' not in st.session_state:
    questions = [
        {
            "soru": "Acil serviste 'akut koroner sendrom' şüphesiyle gelen hastada çekilmesi gereken ilk tetkik nedir?",
            "cevap": "EKG",
            "odul": "Tıpkı bu EKG gibi, kalbim seninle her an ritim tutuyor! Bugünün çok huzurlu geçsin doktor hanım. ❤️"
        },
        {
            "soru": "Geveze ve Nazlıcan'ın en sevdiği meyve/sebze nedir? (Hadi bakalım kuşlarını ne kadar tanıyorsun?)",
            "cevap": "Maydanoz", # Burayı onun bildiği bir cevapla değiştirebilirsin
            "odul": "Kuşlarımızın cıvıltısı kadar neşeli bir gün dilerim! Seni görmeyi sabırsızlıkla bekliyorlar. 🐦"
        },
        {
            "vaka": "EKG'de 'Testere dişi' görünümü hangi ritim bozukluğuna işaret eder?",
            "secenekler": ["Atrial Fibrilasyon", "Atrial Flutter", "Ventriküler Taşikardi"],
            "dogru": "Atrial Flutter",
            "mesaj": "Kalbin ritmi gibi günün de harika aksın! Nazlıcan ve Geveze'nin neşesiyle dolu bir gün dilerim."
        },
        {
            "vaka": "Yenidoğanlarda K vitamini eksikliğine bağlı kanamayı önlemek için hangi kas içine enjeksiyon yapılır?",
            "secenekler": ["M. Deltoideus", "M. Gluteus Maximus", "M. Vastus Lateralis"],
            "dogru": "M. Vastus Lateralis",
            "mesaj": "Bilgin taze, zihnin benle dolsun.”
},
    ]
    st.session_state.soru_no = random.randint(0, len(questions) - 1)
    st.session_state.questions = questions

soru = st.session_state.questions[st.session_state.soru_no]

st.write(f"### 📝 Günün Sorusu:")
st.info(soru["soru"])

cevap = st.text_input("Buraya yazabilirsin:").strip().lower()

if st.button("Sürprizi Aç 🎁"):
    if soru["cevap"].lower() in cevap:
        st.balloons()
        st.success(soru["odul"])
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHp1ZjR4N3R4Z3R4Z3R4Z3R4Z3R4Z3R4Z3R4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l41lTfuxV3VfW2WME/giphy.gif")
    else:
        st.warning("Hımm, biraz daha düşünmen gerekebilir mi?

