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
# Minimal CSS for subtle spacing
# -----------------------------
st.markdown("""
<style>
/* Add small padding around the main container */
.main-container {
    padding: 2rem 1rem;
}

/* Add slight shadow to feedback boxes */
.feedback-box {
    border-radius: 12px;
    padding: 1.5rem;
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)
#DBDDD2"
# -----------------------------
# Page Header
# -----------------------------
st.markdown("<h1 style='text-align:center; color:#DBDDD2;'>Product Verification Portal</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#DBDDD2;'>Enter your product code below to verify authenticity.</p>", unsafe_allow_html=True)

st.markdown("---")  # separator line
#query_params = st.experimental_get_query_params()
code_from_url = st.query_params.get("code", [""])
# -----------------------------
# Input Form
# -----------------------------
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
                    st.success(f"✅ Verified: Your **{veracity[1]}** is authentic!")

            # Already verified
            elif veracity[3] == veracity[4][3] and veracity[3] == True:
                with st.container():
                    st.info(f"ℹ️ Already Verified: Your **{veracity[1]}** has already been verified.")

            # False code
            elif veracity[2] == False:
                with st.container():
                    st.error("❌ False Code: This code does not exist.")

        except Exception as e:
            with st.container():
                st.error("❌ False Code: This code does not exist.")
    else:
        st.warning("⚠️ Please enter a product code before submitting.")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown("<p style='text-align:center; color:#95A5A6; font-size:0.9rem;'>Powered by CUAU Verification System</p>", unsafe_allow_html=True)


