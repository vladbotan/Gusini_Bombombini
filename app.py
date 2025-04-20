import streamlit as st
from PIL import Image
import random
import os
import io
import base64
import streamlit.components.v1 as components
from gtts import gTTS

# --- Quiz Data ---
quiz_data = [
    {
        "image": "images/Sombraruote.webp",
        "options": [
            "Sombraruote Frratatà",
            "Guillermasso Bocadazzo",
            "Rugginato LupoGT (Il Cannone Stradale)",
            "Chef Crabracadabra",
        ],
        "answer": "Sombraruote Frratatà",
    },
    {
        "image": "images/Rugginato_LupoGT.webp",
        "options": [
            "Sombraruote Frratatà",
            "Piccione Macchina",
            "Gambero Spero",
            "Rugginato LupoGT (Il Cannone Stradale)",
        ],
        "answer": "Rugginato LupoGT (Il Cannone Stradale)",
    },
    {
        "image": "images/Chefcrabracadabra.webp",
        "options": [
            "Chef Crabracadabra",
            "Ballerina Cappuccina",
            "Piccione Macchina",
            "Gambero Spero",
        ],
        "answer": "Chef Crabracadabra",
    },
    {
        "image": "images/Piccione_Macchina.webp",
        "options": [
            "Piccione Macchina",
            "Bombombini Gusini",
            "Tralalero Tralala",
            "Talpa Di Ferro",
        ],
        "answer": "Piccione Macchina",
    },
    {
        "image": "images/Gambero_Spero.webp",
        "options": [
            "Gambero Spero",
            "Ballerino Lololo",
            "Bombardiere Lucertola",
            "Crocodilo Ananasino",
        ],
        "answer": "Gambero Spero",
    },
    {
        "image": "images/Tralalero_tralala.webp",
        "options": [
            "Tralalero Tralala",
            "Brr brr Patapim",
            "Trippi Troppi",
            "Talpa Di Ferro",
        ],
        "answer": "Tralalero Tralala",
    },
    {
        "image": "images/Ballerina_Cappucina.webp",
        "options": [
            "Ballerina Cappuccina",
            "Ballerino Lololo",
            "Bombombini Gusini",
            "Rotoliglio Rotola Srotola Srola",
        ],
        "answer": "Ballerina Cappuccina",
    },
    {
        "image": "images/BallerinoLololo.webp",
        "options": [
            "Ballerino Lololo",
            "Bobritto bandito",
            "Rantasanta Chinaranta",
            "Ballerina Cappuccina",
        ],
        "answer": "Ballerino Lololo",
    },
    {
        "image": "images/Bombini_Gusini.webp",
        "options": [
            "Bombombini Gusini",
            "Bombardiere Lucertola",
            "Brr brr Tarflem",
            "Quesadilla Crocodila",
        ],
        "answer": "Bombombini Gusini",
    },
    {
        "image": "images/Bombardiere.webp",
        "options": [
            "Bombardiere Lucertola",
            "Bombardiro Crocodillo",
            "Coscodrillo Robloxino",
            "Chef Crabracadabra",
        ],
        "answer": "Bombardiere Lucertola",
    },
    {
        "image": "images/640.webp",
        "options": [
            "Trippi Troppi",
            "La vaca saturno saturnita",
            "Zhuzhuli Buffo",
            "Brr brr Patapim",
        ],
        "answer": "Trippi Troppi",
    },
    {
        "image": "images/Brr_Brr_Patapim.webp",
        "options": [
            "Brr brr Patapim",
            "Tric Trac baraboom",
            "Tralalero Tralala",
            "Coccodrilli Faerini",
        ],
        "answer": "Brr brr Patapim",
    },
    {
        "image": "images/CA.webp",
        "options": [
            "Cappuccino Assassino",
            "Crocodilo Ananasino",
            "Quesadilla Crocodila",
            "Burbaloni Luliloli",
        ],
        "answer": "Cappuccino Assassino",
    },
    {
        "image": "images/3F3F3F3F3F3F3F3F3F.webp",
        "options": [
            "Crocodilo Ananasino",
            "Serpentini Toiletini",
            "La vaca saturno saturnita",
            "Rotoliglio Rotola Srotola Srola",
        ],
        "answer": "Crocodilo Ananasino",
    },
    {
        "image": "images/D28146d6115611f0a74582963e3c41a8_1.webp",
        "options": [
            "Talpa Di Ferro",
            "Tracotocutulo",
            "Graipussi Medussi",
            "Bombombini Gusini",
        ],
        "answer": "Talpa Di Ferro",
    },
    {
        "image": "images/Trulimero_Trulichina.webp",
        "options": [
            "Trulimero Truliccina",
            "Rotoliglio Rotola Srotola Srola",
            "Burbaloni Luliloli",
            "Zhuzhuli Buffo",
        ],
        "answer": "Trulimero Truliccina",
    },
    {
        "image": "images/1743772723433-249.webp",
        "options": [
            "Zhuzhuli Buffo",
            "Tortitilli Mortiri",
            "Quesadilla Crocodila",
            "Brr brr Tarflem",
        ],
        "answer": "Zhuzhuli Buffo",
    },
    {
        "image": "images/1743823818351-632.webp",
        "options": [
            "Tortitilli Mortiri",
            "Bombardiro Crocodillo",
            "Trippi Troppi",
            "Frulli Frulla",
        ],
        "answer": "Tortitilli Mortiri",
    },
    {
        "image": "images/Cocosatic_Bungus.webp",
        "options": [
            "Cocosatic Bungus",
            "Frulli Frulla",
            "Camelrino Tazzino",
            "Quesadilla Crocodila",
        ],
        "answer": "Cocosatic Bungus",
    },
    {
        "image": "images/Frulli_Frulla.webp",
        "options": [
            "Frulli Frulla",
            "Bri Bri Bicus Dicus",
            "La vaca saturno saturnita",
            "Gambero Spero",
        ],
        "answer": "Frulli Frulla",
    },
    {
        "image": "images/Saturno_Saturnita.webp",
        "options": [
            "La vaca saturno saturnita",
            "Serpentini Toiletini",
            "Gametino Aereoplanino",
            "Bombombini Gusini",
        ],
        "answer": "La vaca saturno saturnita",
    },
    {
        "image": "images/Coccodrilli_Faerini.webp",
        "options": [
            "Coccodrilli Faerini",
            "Hansana Germana",
            "Il Ragioniere del Vuoto",
            "Brr brr Patapim",
        ],
        "answer": "Coccodrilli Faerini",
    },
    {
        "image": "images/Bri_bri_bricus_dicus.webp",
        "options": [
            "Bri Bri Bicus Dicus",
            "Bobritto bandito",
            "Lirilì Larilà",
            "Cocosatic Bungus",
        ],
        "answer": "Bri Bri Bicus Dicus",
    },
    {
        "image": "images/Lirili_rili_ralila.webp",
        "options": [
            "Lirilì Larilà",
            "Brr brr Patapim",
            "Talpa Di Ferro",
            "Giraffa Celeste",
        ],
        "answer": "Lirilì Larilà",
    },
    {
        "image": "images/Screenshot_2025-04-03_at_3.11.50_PM.webp",
        "options": [
            "Serpentini Toiletini",
            "Bobritto bandito",
            "Brr brr Tarflem",
            "La vaca saturno saturnita",
        ],
        "answer": "Serpentini Toiletini",
    },
    {
        "image": "images/Bomborito_bandito.webp",
        "options": [
            "Bobritto bandito",
            "Emo Struzzo Paparazzi",
            "Coccodrillo Formaggioso",
            "Il Ragioniere del Vuoto",
        ],
        "answer": "Bobritto bandito",
    },
    {
        "image": "images/ChimpanziniBananini.webp",
        "options": [
            "Chimpanzini Bananini",
            "Orangutini Ananasini",
            "Ballerino Lololo",
            "Gamb                                                                                        ",
        ],
        "answer": "Chimpanzini Bananini",
    },
    {
        "image": "ChatGPT_Image_18_kwi_2025%2C_15_15_47.webp",
        "options": [
            "Bicicletta Del Gatto Santo",
            "Orangutini Ananasini",
            "Emo Struzzo Paparazzi",
            "Il Ragioniere del Vuoto",
        ],
        "answer": "Bicicletta Del Gatto Santo",
    },
]

# --- Configurable Crop Size ---
CROP_W, CROP_H = 300, 300

# --- Initialize Session State ---
for key, default in {
    "score": 0,
    "high_score": 0,
    "q_index": 0,
    "shuffled": random.sample(quiz_data, len(quiz_data)),
    "show_feedback": False,
    "correct": False,
}.items():
    if key not in st.session_state:
        st.session_state[key] = default


def restart_quiz():
    # Here you could write st.session_state.score to your DB before resetting
    st.session_state.score = 0
    st.session_state.q_index = 0
    st.session_state.shuffled = random.sample(quiz_data, len(quiz_data))
    st.session_state.show_feedback = False
    st.session_state.correct = False
    # Clear cached crops
    for k in list(st.session_state):
        if k.startswith("crop_"):
            del st.session_state[k]


# --- Display Scores ---
st.markdown(
    f"**Score:** {st.session_state.score}    &nbsp;&nbsp;  "
    f"**High Score:** {st.session_state.high_score}"
)

# --- Load Current Question ---
qi = st.session_state.q_index
item = st.session_state.shuffled[qi]
img_path = item["image"]
if not os.path.exists(img_path):
    st.error(f"Image not found: {img_path}")
    st.stop()

full_img = Image.open(img_path)
w, h = full_img.size
cw, ch = min(CROP_W, w), min(CROP_H, h)

# --- Cache One Random Crop Per Question ---
crop_key = f"crop_{qi}"
if crop_key not in st.session_state:
    x = random.randint(0, w - cw) if w > cw else 0
    y = random.randint(0, h - ch) if h > ch else 0
    st.session_state[crop_key] = (x, y)
x, y = st.session_state[crop_key]
cropped = full_img.crop((x, y, x + cw, y + ch))

# --- Two‑Column Layout ---
col_img, col_ctrl = st.columns([2, 1])

with col_img:
    st.image(cropped, use_column_width=True)
    if st.session_state.show_feedback:
        st.image(full_img, caption="Full Image", use_column_width=True)

with col_ctrl:
    if not st.session_state.show_feedback:
        # Form for single-click submit
        with st.form(key=f"form_{qi}", clear_on_submit=False):
            choice = st.radio("Who is this character?", item["options"])
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.session_state.correct = choice == item["answer"]
                if st.session_state.correct:
                    st.session_state.score += 1
                else:
                    # Update high score if needed
                    if st.session_state.score > st.session_state.high_score:
                        st.session_state.high_score = st.session_state.score
                st.session_state.show_feedback = True
                st.rerun()

    else:
        # Feedback area
        if st.session_state.correct:
            st.success("✅ Correct!")
            # Play Italian TTS automatically
            tts = gTTS(text=item["answer"], lang="it")
            buf = io.BytesIO()
            tts.write_to_fp(buf)
            buf.seek(0)
            b64 = base64.b64encode(buf.read()).decode()
            components.html(
                f"""<audio autoplay>
  <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
</audio>""",
                height=30,
            )
            # Offer Next Question
            if st.button("Next Question"):
                st.session_state.q_index += 1
                st.session_state.show_feedback = False
                st.rerun()

        else:
            st.error(
                f"❌ Wrong! The correct answer was '{item['answer']}'. Your final score: {st.session_state.score}"
            )
            st.markdown(f"**High Score:** {st.session_state.high_score}")
            # Only Restart on wrong
            if st.button("Restart Quiz"):
                restart_quiz()
                st.rerun()
