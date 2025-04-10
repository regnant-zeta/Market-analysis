import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Luxury Sedan Market Analysis")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Market Overview", "Upload Your Data", "Insights"])

# Market Overview
if page == "Market Overview":
    st.header("Global Luxury Sedan Market Overview")
    st.write("""
    Welcome to Regnant Motors' market analysis tool.  
    Explore trends, sales data, and insights for luxury sedans.
    """)
    st.image("https://cdn.pixabay.com/photo/2016/11/23/14/45/audi-1853312_960_720.jpg", caption="Luxury Sedan", use_container_width=True)

# Upload Data
elif page == "Upload Your Data":
    st.header("Upload Your Sedan Market Data (CSV)")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.success("File Uploaded Successfully!")
        st.dataframe(data)

        if st.checkbox("Show Summary"):
            st.write(data.describe())

        if st.checkbox("Plot Sales Trend"):
            if "Year" in data.columns and "Sales" in data.columns:
                fig, ax = plt.subplots()
                ax.plot(data["Year"], data["Sales"], marker='o')
                plt.xlabel("Year")
                plt.ylabel("Sales Units")
                plt.title("Luxury Sedan Sales Trend")
                st.pyplot(fig)
            else:
                st.error("Columns 'Year' and 'Sales' not found in the data.")

# Insights
elif page == "Insights":
    st.header("Top Insights")
    st.write("""
    - Luxury sedans are showing growth in emerging markets.
    - Electric luxury sedans are rising in demand.
    - Consumers prefer eco-friendly and smart technology vehicles.
    """)
    st.balloons()
