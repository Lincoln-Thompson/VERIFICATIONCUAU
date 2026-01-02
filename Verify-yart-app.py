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
# CSS for adaptive theme
# -----------------------------
st.markdown("""
<style>
/* Main container padding */
.main-container {
    padding: 2rem 1rem;
}

/* Adaptive text color for headers & paragraphs */
.adaptive-text {
    text-align: center;
    color: #111111; /* Light mode */
}

/* Feedback boxes */
.feedback-box {
    border-radius: 12px;
    padding: 1.5rem;
    margin-top: 1rem;
}

/* Input styling */
.stTextInput>div>div>input {
    border-radius: 8px;
    padding: 0.5rem;
    border: 1px solid #ccc;
    background-color: #fff;
    color: #111;
}

/* Button styling */
.stButton>button {
    border-radius: 8px;
    padding: 0.5rem 1rem;
    background-color: #DBDDD2;
    color: #111;
    border: none;
}

/* Footer text */
.footer-text {
    text-align: center;
    font-size: 0.9rem;
    color: #95A5A6; /* Light mode */
}

/* Dark mode overrides */
@media (prefers-color-scheme: dark) {
    .adaptive-text {
        color: #DBDDD2; /* Light text for dark mode */
    }

    .stTextInput>div>div>input {
        background-color: #1a1a1a;
        color: #DBDDD2;
        border: 1px solid #555;
    }

    .stButton>button {
        background-color: #DBDDD2;
        color: #111;
    }

    .feedback-box {
        background-color: #12121a;
        color: #DBDDD2;
    }

    .footer-text {
        color: #888;
    }
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Page Header
# -----------------------------
st.markdown("""
<h1 class="adaptive-text">Product Verification Portal</h1>
<p class="adaptive-text">Enter your product code below to verify authenticity.</p>
""", unsafe_allow_html=True)

st.markdown("---")  # separator line

# -----------------------------
# Input Form
# -----------------------------
code_from_url = st.query_params.get("code", [""])

with st.container():
    user_input = st.text_input(
        "Enter Product Code",
        placeholder="Type product code here...",
        value=code_from_url
    )

    submitted = st.button("Verify Product")

# -----------------------------
# Verification Logic / Feedback
# -----------------------------
if submitted:
    if user_input.strip():
        try:
            veracity = verifytag(user_input)

            # Verified first time
            if veracity[3] != veracity[4][3] and veracity[3] == True:
                st.balloons()
                with st.container():
                    st.success(f"✅ Verified: Your **{veracity[1]}** is authentic!", icon="✅")

            # Already verified
            elif veracity[3] == veracity[4][3] and veracity[3] == True:
                with st.container():
                    st.info(f"ℹ️ Already Verified: Your **{veracity[1]}** has already been verified.", icon="ℹ️")

            # False code
            elif veracity[2] == False:
                with st.container():
                    st.error("❌ False Code: This code does not exist.", icon="❌")

        except Exception as e:
            with st.container():
                st.error("❌ False Code: This code does not exist.", icon="❌")
    else:
        st.warning("⚠️ Please enter a product code before submitting.", icon="⚠️")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown('<p class="footer-text">Powered by CUAU Verification System</p>', unsafe_allow_html=True)



