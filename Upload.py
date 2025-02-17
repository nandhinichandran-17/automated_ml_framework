import streamlit as st
import pandas as pd
import os
import base64

st.set_page_config(layout="wide")
st.title("Upload Your Data for Modeling! 📂")

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



if os.path.exists("sourcedata.csv"):
    df = pd.read_csv("sourcedata.csv", index_col=None)

file = st.file_uploader("Upload Your Dataset Here")

if file:
    df = pd.read_csv(file, index_col=None)
    df.to_csv("sourcedata.csv", index=None)
    st.success("File uploaded successfully!")
    st.dataframe(df)

st.page_link("Home.py", label="Go Back", icon="🏠")
