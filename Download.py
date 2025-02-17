import streamlit as st
import os
import base64

st.set_page_config(layout="wide")
st.title("Download Your Model 💾")

# Function to encode the image to base64
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Path to your image
img_path = r"C:\Users\nandh\OneDrive\Desktop\AutoStreamML\ml.jpg"
bg_img = get_base64(img_path)

# Apply background image and completely remove sidebar
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_img}");
        background-size: cover;
        background-position: top;
        animation: zoomIn 15s infinite;
    }}

    @keyframes zoomIn {{
        0% {{ transform: scale(1); }}
        50% {{ transform: scale(1.05); }}
        100% {{ transform: scale(1); }}
    }}

    /* COMPLETELY HIDE SIDEBAR */
    [data-testid="stSidebar"], [data-testid="stSidebarNav"], .css-1d391kg, .css-1gulkj5 {{
        display: none !important;
        visibility: hidden !important;
        width: 0px !important;
    }}

    /* Button Styling */
    .stButton>button {{
        transition: 0.3s;
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
    }}
    .stButton>button:hover {{
        transform: scale(1.1);
        background-color: #ff7878;
    }}
    /* Pulse effect on file uploader */
    .stFileUploader>div {{
        animation: pulse 2s infinite;
    }}

    @keyframes pulse {{
        0% {{ transform: scale(1); }}
        50% {{ transform: scale(1.05); }}
        100% {{ transform: scale(1); }}
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.info("Download the best trained model based on performance")

if os.path.exists('best_model.pkl'):
    with open('best_model.pkl', 'rb') as f:
        st.download_button('Download Model', f, file_name="best_model.pkl")
else:
    st.warning("No model found. Please run an ML pipeline first.")

st.page_link("Home.py", label="Go Back", icon="🏠")
