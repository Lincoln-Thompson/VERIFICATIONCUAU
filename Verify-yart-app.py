import streamlit as st
import sys, os
sys.path.append(os.path.dirname(__file__))
from verifyyartbackend import verifytag
# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Submission Portal",
    page_icon="✨",
    layout="centered"
)

# -----------------------------
# Custom Black & Gold CSS
# -----------------------------
st.markdown("""
<style>
html, body, [data-testid="stApp"] {
    background-color: #0b0b0f;
    color: #f5f5f5;
}

.gold-title {
    text-align: center;
    font-size: 2.4rem;
    font-weight: 600;
    margin-bottom: 1.5rem;
    background: linear-gradient(90deg, #b87333, #d4af37);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.input-container {
    background-color: #14141c;
    padding: 2rem;
    border-radius: 14px;
    border: 1px solid rgba(212, 175, 55, 0.25);
    box-shadow: 0 0 30px rgba(212, 175, 55, 0.08);
}

.stTextInput input {
    background-color: #0b0b0f !important;
    color: #f5f5f5 !important;
    border-radius: 10px;
    border: 1px solid rgba(212, 175, 55, 0.35);
}

.stButton button {
    width: 100%;
    background: linear-gradient(90deg, #b87333, #d4af37);
    color: #0b0b0f;
    font-weight: 600;
    border-radius: 12px;
    height: 3rem;
    margin-top: 1rem;
    border: none;
}

.stButton button:hover {
    opacity: 0.9;
    box-shadow: 0 0 18px rgba(212, 175, 55, 0.6);
}

.success-card {
    margin-top: 2rem;
    padding: 1.8rem;
    border-radius: 16px;
    background: radial-gradient(circle at top, #1a1a22, #0b0b0f);
    border: 1px solid rgba(212, 175, 55, 0.35);
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# UI
# -----------------------------
st.markdown('<div class="gold-title">Verify Product</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="input-container">', unsafe_allow_html=True)

    user_input = st.text_input(
        "Enter Code",
        placeholder="Type product code here..."
    )

    submitted = st.button("Submit")

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Success State
# -----------------------------
if submitted and user_input.strip():
    try:
        veracity=verifytag(user_input)
        print(veracity)
        if veracity[3]!=veracity[4][3] and veracity[3]==True:

            st.balloons()
        
            st.markdown("""
            <div class="success-card">
            <h2 style="color:#4C7540;">Verified</h2>
            <p>Your """+veracity[1]+""" has been successfully verified as authentic.</p>
            </div>
            """, unsafe_allow_html=True)
        elif veracity[3]==veracity[4][3] and veracity[3]==True:
            st.markdown("""
            <div class="success-card">
            <h2 style="color:#FFCC00;"> Already Verified</h2>
            <p>Your """+veracity[1]+""" has already been verified.</p>
            </div>
            """, unsafe_allow_html=True)
        elif veracity[2]==False:
             st.markdown("""
            <div class="success-card">
            <h2 style="color:#FF0000;"> False Code</h2>
            <p>This code does not exist.</p>
            </div>
            """, unsafe_allow_html=True)
    except:    
         st.markdown("""
            <div class="success-card">
            <h2 style="color:#FF0000;"> False Code</h2>
            <p> This code does not exist.</p>
            </div>
            """, unsafe_allow_html=True)

elif submitted:
    st.warning("Please enter some text before submitting.")
