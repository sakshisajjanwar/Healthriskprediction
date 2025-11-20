🏥 Lifestyle & Health Risk Dashboard
An Interactive Streamlit App for Exploring Factors Affecting Health

This project is a Streamlit-based interactive dashboard designed to analyze how lifestyle habits such as diet, exercise, sleep, and daily routines impact overall health risks.
Users can filter, explore, visualize, and interpret key insights from the dataset—all through a clean and intuitive UI.

👩‍💻 Author

sakshi sajjanwar
 Python | SQL

📘 Project Overview

The Lifestyle & Health Risk Dashboard provides:

📊 Interactive data visualizations

🔍 Smart filtering for deep exploration

📈 Statistical summaries of lifestyle factors

💡 Key insights on how habits affect health risk

The dashboard is fully built using Streamlit, integrating pandas, seaborn, and matplotlib for analytics and visualization.

🧩 Features
✔️ 1. Data Filters

Filter by demographic and lifestyle categories using a sidebar panel.

✔️ 2. Dataset Overview

View total records, column count, unique values, and a preview.

✔️ 3. Data Explorer

Get descriptive statistics, column-level details, and distribution summaries.

✔️ 4. Visualizations

Choose from multiple interactive charts:

Histogram

Box Plot

Line Chart

✔️ 5. Insights Section

A curated takeaway section to help users interpret relationships between lifestyle factors and their health outcomes.

📂 Dataset

Loaded from Health_dataset.csv inside the project folder.
Columns include:

Feature	Description
Age	Age of individual
Gender	Male / Female / Other
Lifestyle Habits	Diet, exercise, sleep, smoking, etc.
Medical Indicators	Heart rate, blood pressure, BMI, etc.
Health_Risk	Target variable indicating risk category
🛠️ Technologies Used
Category	Tools
Language	Python
Libraries	Streamlit, Pandas, Seaborn, Matplotlib
Environment	Jupyter Notebook / VS Code
Version Control	Git & GitHub
📁 Project Structure
📦 Health-Risk-Dashboard
 ┣ 📄 healthrisk.py
 ┣ 📄 Health_dataset.csv
 ┣ 📄 README.md
 ┣ 📁 assets/
 ┗ 📄 requirements.txt

🚀 How to Run the Project
Step 1 — Clone the Repository
git clone https://github.com/YourUsername/Health-Risk-Dashboard.git
cd Health-Risk-Dashboard

Step 2 — Install Dependencies
pip install -r requirements.txt


Or install manually:

pip install streamlit pandas seaborn matplotlib

Step 3 — Run the Streamlit App
streamlit run healthrisk.py

📸 App Preview

The dashboard is divided into four intuitive tabs:

🏠 Overview

📋 Data Explorer

📊 Visualizations

💡 Insights

The Streamlit script powering this project is located in:
healthrisk.py 

healthrisk

💡 Future Enhancements

🔹 Add machine learning–based health risk prediction
🔹 Add correlation heatmaps
🔹 Enable user-uploaded datasets
🔹 Enhance UI with custom themes & animations

🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss what you'd like to modify.

⭐ Support

If you like this project, please ⭐ star the repo
