import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# PAGE details
st.set_page_config(
    page_title="🏥 Lifestyle & Health Risk Dashboard",
    layout="wide"
)

#LOAD DATA 
@st.cache_data
def load_data():#read and return your dataset.
    df = pd.read_csv("Health_dataset.csv")#reads your file and loads it into a DataFrame
    return df

df = load_data()#for filter pupose
st.markdown("### 🏥Factors Affecting our Healths")

st.image(
    "http://www.cardiacwellnessinstitute.com/heart-disease-treatment-prevention/wp-content/uploads/2020/08/StrokeRiskFactors_Infographic-1-1024x1016.jpg",
    use_container_width=200
)



# SIDEBAR 
st.sidebar.title("🔍 Data Filters")
st.sidebar.caption("Use these filters according to your preference.")

categorical_cols = df.select_dtypes(exclude='number').columns.tolist()
numeric_cols = df.select_dtypes(include='number').columns.tolist()

filtered_df = df.copy()# making copy of original dataget to avoid cahnge4s in original data set
for col in categorical_cols:
    options = df[col].dropna().unique().tolist()
    selected = st.sidebar.multiselect(f"Select {col}", options)
    
if selected:  # 👈 added this condition
    filtered_df = filtered_df[filtered_df[col].isin(selected)]



st.sidebar.divider()
st.sidebar.caption("Built with ❤️ using Streamlit")

# MAIN TABS 
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Overview", "📋 Data Explorer", "📊 Visualizations", "💡 Insights"])

#  TAB 1 OVERVIEW 
with tab1:
    st.title("🏥 Lifestyle & Health Risk Analysis Dashboard")

    st.markdown("""
    This interactive dashboard helps explore how lifestyle factors affect health risks.    
    """)  # Adjust ratio

    st.divider()#Adds a horizontal line
    st.subheader("📈 Key Statistics")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records", len(filtered_df))
    col2.metric("Columns", len(filtered_df.columns))
    col3.metric("Unique Categories", sum(df[col].nunique() for col in categorical_cols))#This line shows a metric card

    st.divider()#seperate the section a line type
    st.subheader("🩺 Dataset Preview")
    st.dataframe(filtered_df.head(), use_container_width=True)#the table stretch to the full width of the page    

#  TAB 2: DATA EXPLORER 
with tab2:
    st.subheader("🔬 Explore the Data")
    st.write("Below is the summary of numerical columns:")

    st.dataframe(filtered_df.describe().T.style.background_gradient(cmap="pink"), use_container_width=True)

    st.markdown("### View Column Details")
    col_selected = st.selectbox("Select a column to inspect:", df.columns)#list of all columns in your dataset.
    st.write(f"**Unique Values ({col_selected})**:", df[col_selected].nunique())#formatted string 
    st.write(df[col_selected].value_counts().head(10))

#  TAB 3: VISUALIZATIONS
with tab3:
    st.subheader("📊 Data Visualizations")
    st.markdown("It visualize relationships between lifestyle and health risk.")

    chart_type = st.radio("Select Chart Type:", ["Histogram", "Box Plot", "Line Chart"], horizontal=True)

    if chart_type == "Histogram":
        col = st.selectbox("Select column for histogram:", numeric_cols)# only numeric values
        fig, ax = plt.subplots()#one subplot (axis)
        sns.histplot(filtered_df[col], kde=True, color='skyblue', ax=ax)#create its own new axis
        ax.set_title(f"Distribution of {col}")
        st.pyplot(fig)

    elif chart_type == "Box Plot":
        num_col = st.selectbox("Numeric Column:", numeric_cols)
        cat_col = st.selectbox("Category Column:", categorical_cols)
        fig, ax = plt.subplots()
        sns.boxplot(data=filtered_df, x=cat_col, y=num_col, palette="Set2", ax=ax)
        ax.set_title(f"{num_col} by {cat_col}")
        st.pyplot(fig)

    elif chart_type == "Line Chart":
       x = st.selectbox("Select X-axis (Numeric):", numeric_cols)
       y = st.selectbox("Select Y-axis (Numeric):", numeric_cols, index=min(1, len(numeric_cols)-1))
       hue = st.selectbox("Select Category (optional):", [None] + categorical_cols)

       fig, ax = plt.subplots()
       sns.lineplot(data=filtered_df, x=x, y=y, hue=hue, marker="o", ci=None, ax=ax)
       ax.set_title(f"{y} vs {x}")
       st.pyplot(fig)

# -------------------- TAB 4: INSIGHTS --------------------
with tab4:
    st.subheader("💡 Key Insights & Takeaways")

    st.markdown("""
    - Analyze how **diet, exercise, and lifestyle habits** influence health risks.
    - Identify **high correlation** features using the heatmap.
    - Use the box plot to compare **risk levels across demographic groups**.
    - The scatter plot can reveal **linear or non-linear relationships** between features.

    **Tip:** Combine filters and visualization types to uncover patterns and outliers.
    """)

    st.success("✅ Explore trends to predict potential health risks and encourage healthy lifestyles.")
    
