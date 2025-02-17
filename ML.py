import streamlit as st
import pandas as pd
import pycaret.regression
import pycaret.classification
from pycaret.classification import setup
import time
import os
import base64


st.set_page_config(layout="wide")
st.title("Machine Learning Pipeline 🤖")
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

    target = st.selectbox("Select your Target", df.columns)
    model_choice = st.radio("Select Model Type", ["Regression", "Classification"], horizontal=True)

    if st.button("Run Modeling", key="run_model"):
        with st.spinner("Training models, please wait..."):
            time.sleep(3)  # Simulate processing time

            if model_choice == "Regression":
                pycaret.regression.setup(df, target=target)
                setup_df = pycaret.regression.pull()
                st.info("This is the ML Experiment settings")
                st.dataframe(setup_df)
                best_model = pycaret.regression.compare_models()
                compare_df = pycaret.regression.pull()
                st.info("This is the ML Model")
                st.dataframe(compare_df)
                pycaret.regression.save_model(best_model, 'best_model')

            elif model_choice == "Classification":
                setup(data=df, target=target)
                pycaret.classification.setup(df, target=target)
                setup_df = pycaret.classification.pull()
                st.info("This is the ML Experiment settings")
                st.dataframe(setup_df)
                best_model = pycaret.classification.compare_models()
                compare_df = pycaret.classification.pull()
                st.info("This is the ML Model")
                st.dataframe(compare_df)
                pycaret.classification.save_model(best_model, 'best_model')
else:
    st.warning("Please upload a dataset first.")

st.page_link("Home.py", label="Go Back", icon="🏠")
