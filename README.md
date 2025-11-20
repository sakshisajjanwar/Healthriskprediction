# 🏥 Lifestyle & Health Risk Dashboard
An Interactive Streamlit App for Exploring Factors Affecting Health

This project is a Streamlit-based interactive dashboard designed to analyze how lifestyle habits such as diet, exercise, sleep, and daily routines impact overall health risks.
Users can filter, explore, visualize, and interpret key insights from the dataset—all through a clean and intuitive UI.

--------------------------------------------------------------------------------------------------------------------------------------------------------
### 📘 Project Overview

The Lifestyle & Health Risk Dashboard provides:

📊 Interactive data visualizations

🔍 Smart filtering for deep exploration

📈 Statistical summaries of lifestyle factors

💡 Key insights on how habits affect health risk

The dashboard is fully built using Streamlit, integrating pandas, seaborn, and matplotlib for analytics and visualization.

-------------------------------------------------------------------------------------------------------------------------------
# 📂 Dataset

Loaded from Health_dataset.csv inside the project folder.
Columns include:

| Column Name          | Description                                             |
| -------------------- | ------------------------------------------------------- |
| Age                  | Age of individual                                       |
| Gender               | Male / Female / Other                                   |
| Sleep / Activity     | Sleep hours, exercise habits, routine data              |
| Medical Metrics      | Heart rate, blood pressure, BMI, etc.                   |
| Lifestyle Indicators | Diet rating, stress level, smoking/alcohol usage        |
| **Health_Risk**      | Target variable indicating risk level (Low/Medium/High) |


----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Project Workflow 

## 1️⃣ Data Loading
Imported required libraries (Streamlit, Pandas, Seaborn, Matplotlib)
Loaded Health_dataset.csv using a cached function
Identified numeric & categorical columns
Created a filtered dataset copy for analysis

## 2️⃣ Sidebar Filters
Added multi-select filters for all categorical columns
Updated dataset, metrics, and visualizations based on user selections

## 3️⃣ Dashboard Structure
The app contains 4 main tabs:

### 🏠 Overview
Project summary
Key statistics (records, columns, unique categories)
Dataset preview

### 📋 Data Explorer
Descriptive statistics
Column-level analysis (unique values & top categories)

### 📊 Visualizations
Histogram (numeric distributions)
Box Plot (numeric vs category)
Line Chart (trend analysis)

### 💡 Insights
Key patterns
Lifestyle-related risk factors
Summary of observations

## 4️⃣ Data Visualization
Generated dynamic charts using Seaborn & Matplotlib
All visuals update automatically based on filters

## 5️⃣ Insights Generation
Highlighted high-risk behavior patterns
Showed relationships between lifestyle and health metrics
Encouraged exploration to uncover trends

----------------------------------------------------------------------------------------------------------------------------------------------

# 🧩 Features
✔️ 1. Data Filters
Filter by demographic and lifestyle categories using a sidebar panel.

✔️ 2. Dataset Overview
View total records, column count, unique values, and a preview.

✔️ 3. Data Explorer
Get descriptive statistics, column-level details, and distribution summaries.

✔️ 4. Visualizations
Choose from multiple interactive charts:
* Histogram
* Box Plot
* Line Chart

✔️ 5. Insights Section

---------------------------------------------------------------------------------------------------------------------------------------
# 🛠️ Technologies Used
| Category        | Tools                                  |
| --------------- | -------------------------------------- |
| Programming     | Python                                 |
| Libraries       | Streamlit, Pandas, Seaborn, Matplotlib |
| IDE             | VS Code / Jupyter Notebook             |
| Version Control | Git & GitHub                           |

------------------------------------------------------------------------------------------------------------------------------------
🚀 How to Run the Project
Step 1 — Clone the Repository
git clone https://github.com/sakshisajjanwar/Health-Risk-Dashboard.git
cd Health-Risk-Dashboard

Step 2 — Install Dependencies
pip install -r requirements.txt

Or install manually:
pip install streamlit pandas seaborn matplotlib

Step 3 — Run the Streamlit App
streamlit run healthrisk

If you like this project, please ⭐ star the repo
