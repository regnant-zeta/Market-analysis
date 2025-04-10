import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(
    page_title="Luxury Sedan Analysis",
    page_icon=":car:",  # You can change this emoji if you want!
    layout="centered",  # Other options: "wide", "centered"
    initial_sidebar_state="expanded",  # Opens the sidebar by default
)

# Title
st.title("Luxury Sedan Market Analysis")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Market Overview", "Upload Your Data", "Insights"])

# Big Luxury Car Image
st.image(
    "https://images.unsplash.com/photo-1614790362262-f8b5f2e1aa82?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80",
    caption="Experience the Future of Luxury",
    use_container_width=True
)

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
