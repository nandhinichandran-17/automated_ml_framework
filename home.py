import streamlit as st
import base64

# Set Streamlit page config
st.set_page_config(page_title="AutoStreamML", layout="wide")

# Function to encode the image to base64
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Path to your image
img_path = r"C:\Users\nandh\OneDrive\Desktop\AutoStreamML\ml.jpg"
bg_img = get_base64(img_path)

# Apply background image and remove sidebar
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

    /* Hide Sidebar */
    [data-testid="stSidebar"], [data-testid="stSidebarNav"] {{
        display: none !important;
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

st.title("Welcome to AutoStreamML 🌐")
st.write(
        "This is an automatic machine learning framework. "
        "Upload your dataset, perform exploratory data analysis (EDA), "
        "train machine learning models, and download the best-performing model!"
    )
st.write("Navigate using the buttons below:")

# Navigation Buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.page_link(r"C:\Users\nandh\OneDrive\Desktop\AutoStreamML\pages\Upload.py", label="Upload Data", icon="📂")

with col2:
    st.page_link(r"C:\Users\nandh\OneDrive\Desktop\AutoStreamML\pages\Profiling.py", label="Data Profiling", icon="🔍")

with col3:
    st.page_link(r"C:\Users\nandh\OneDrive\Desktop\AutoStreamML\pages\ML.py", label="Train ML Models", icon="🤖")

with col4:
    st.page_link(r"C:\Users\nandh\OneDrive\Desktop\AutoStreamML\pages\Download.py", label="Download Model", icon="💾")
