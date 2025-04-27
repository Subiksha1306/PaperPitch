import streamlit as st
import base64

# Set page config
st.set_page_config(page_title="PaperPitch", layout="wide")

# Inject custom fonts and styles
st.markdown("""
    <style>
    @font-face {
        font-family: 'Emperator';
        src: url('assets/EmperatorClassicEssentialBlack.ttf') format('truetype');
    }
    @font-face {
        font-family: 'Molenilo';
        src: url('assets/MoleniloLow.ttf') format('truetype');
    }
    @font-face {
        font-family: 'Allenoire';
        src: url('assets/AllenoireRegular.ttf') format('truetype');
    }

    html, body, [class*="css"]  {
        height: 100%;
        margin: 0;
        padding: 0;
        background-image: url('pp bg.jpg');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
        font-weight: bold;
        color: black;
    }

    .rainbow-text {
        font-family: 'Molenilo', sans-serif;
        background: linear-gradient(to right, #ff0000, #ffa500, #ffff00, #00ff00, #0000ff, #4b0082, #ee82ee);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 50px;
        font-weight: bold;
    }

    .header-line {
        font-family: 'Emperator', serif;
        font-size: 38px;
        margin-top: 3rem;
    }

    .subheading {
        font-family: 'Allenoire', sans-serif;
        font-size: 20px;
        margin-bottom: 3rem;
    }

    .stTextInput > div > div > input {
        background-color: #ffffffcc;
        border-radius: 10px;
    }

    .stButton>button {
        background-color: #ffffffcc;
        color: black;
        font-weight: bold;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# UI Content
st.markdown('<div class="header-line">Turn sparks into research, pitch your next idea with</div>', unsafe_allow_html=True)
st.markdown('<div class="rainbow-text">PAPERPITCH</div>', unsafe_allow_html=True)
st.markdown('<div class="subheading">academic ideas, reimagined</div>', unsafe_allow_html=True)

# Input
keyword = st.text_input("Enter keywords")

# Button
if st.button("✨ Generate"):
    if keyword:
        st.success(f"✨ Your pitch for '{keyword}' is being generated...")
        # your original functionality here
    else:
        st.warning("Please enter some keywords to generate a pitch.")
import streamlit as st

# Inject custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/fonts.css")

# UI Elements
st.markdown("<h1 class='title'>Turn sparks into research;</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitle'>PAPERPITCH</h2>", unsafe_allow_html=True)
st.markdown("<p style='font-family:Allenoire;'>Academic ideas, reimagined.</p>", unsafe_allow_html=True)

with open('assets/fonts.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
