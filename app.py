import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Luxury Sedan Market Analysis")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Market Overview", "Upload Your Data", "Insights"])

# Page 1: Market Overview
if page == "Market Overview":
    st.header("Global Luxury Sedan Market Overview")
    st.write("""
    Welcome to Regnant Motors' market analysis tool.  
    Explore trends, sales data, and insights for luxury sedans.
    """)
    
    # Display an image
    st.image(
        "https://images.unsplash.com/photo-1614790362262-f8b5f2e1aa82?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80",
        caption="Experience the Future of Luxury",
        use_column_width=True
    )

# Page 2: Upload Your Data
elif page == "Upload Your Data":
    st.header("Upload Your Sedan Market Data (CSV)")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.success("File Uploaded Successfully!")
        st.dataframe(data)

        if st.checkbox("Show Summary Statistics"):
            st.subheader("Summary Statistics")
            st.write(data.describe())

        if st.checkbox("Plot Sales Trend"):
            if "Year" in data.columns and "Sales" in data.columns:
                fig, ax = plt.subplots()
                ax.plot(data["Year"], data["Sales"], marker='o')
                ax.set_xlabel("Year")
                ax.set_ylabel("Sales Units")
                ax.set_title("Luxury Sedan Sales Trend")
                st.pyplot(fig)
            else:
                st.error("The CSV must contain 'Year' and 'Sales' columns.")

# Page 3: Insights
elif page == "Insights":
    st.header("Top Insights")
    st.write("""
    - Luxury sedans are showing strong growth in emerging markets.
    - Electric luxury sedans (EVs) are rising rapidly in demand.
    - Customers prefer eco-friendly and smart technology features.
    """)
    st.balloons()
