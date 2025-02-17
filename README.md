🚀 AutoStreamML: Automated Machine Learning Framework
AutoStreamML is a Streamlit-based Machine Learning framework that automates the entire ML pipeline, from data upload to model training and downloading the best model. The framework utilizes PyCaret, YData Profiling, and Streamlit to simplify the ML process for users with minimal coding knowledge.

📌 Features
✅ User-Friendly Interface – Streamlit-powered UI for seamless navigation
✅ Data Upload – Supports CSV file uploads for training models
✅ Automated EDA – Generates interactive profiling reports using YData Profiling
✅ ML Model Training – Supports Regression & Classification using PyCaret
✅ Model Selection & Comparison – Automatically selects the best ML model
✅ Model Download – Export the best-trained model as a .pkl file

📁 Project Structure

AutoStreamML/
├── Home.py            # Main landing page with navigation
├── pages/             # Folder containing all sub-pages
│   ├── Upload.py      # Upload dataset page
│   ├── Profiling.py   # EDA & profiling page
│   ├── ML.py          # ML training page
│   ├── Download.py    # Model download page
├── sourcedata.csv     # Example dataset (optional)
├── requirements.txt   # Dependencies
└── README.md          # Documentation

📜 Usage Guide
🔹 Step 1: Upload Data
Navigate to the Upload page
Upload a CSV file
View the dataset preview
🔹 Step 2: Data Profiling
Go to the Profiling page
The app automatically generates a detailed EDA report
🔹 Step 3: Train ML Models
Select the target column
Choose the model type – Regression or Classification
Click Run Modeling, and PyCaret will train multiple models and select the best one
🔹 Step 4: Download Model
Navigate to the Download page
Click the Download Model button to save the best model as a .pkl file

🛠 Future Enhancements
🔹 Add clustering & anomaly detection
🔹 Include hyperparameter tuning for better model performance
🔹 Support for time-series forecasting models
🔹 Improve UI/UX with animations

