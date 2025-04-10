import streamlit as st import pandas as pd import matplotlib.pyplot as plt

Dummy Data for MVP

luxury_sedan_data = { 'Brand': ['BMW', 'Mercedes', 'Audi', 'Tesla', 'Lexus'], 'Model': ['5 Series', 'E-Class', 'A6', 'Model S', 'ES'], 'Avg_Price_USD': [55000, 60000, 58000, 75000, 50000], 'Sales_2024': [45000, 40000, 38000, 52000, 30000], 'Top_Feature': ['Luxury Interior', 'Safety Tech', 'Drive Comfort', 'Autonomous', 'Hybrid Tech'] }

df = pd.DataFrame(luxury_sedan_data)

Streamlit App

st.set_page_config(page_title="Luxury Sedan Market Analysis", layout="centered")

st.title("Luxury Sedan Market Analysis") st.markdown("Explore trends, features, and pricing insights for luxury sedans.")

Sales Chart

st.header("Sales Trends") fig, ax = plt.subplots() ax.bar(df['Model'], df['Sales_2024'], color='skyblue') ax.set_xlabel("Sedan Model") ax.set_ylabel("Units Sold in 2024") ax.set_title("Luxury Sedan Sales Comparison") st.pyplot(fig)

Price Table

st.header("Pricing Overview") st.dataframe(df[['Brand', 'Model', 'Avg_Price_USD']])

Top Features

st.header("Top Desired Features") for idx, row in df.iterrows(): st.write(f"{row['Model']}: {row['Top_Feature']}")

Consumer Sentiment Summary

st.header("Consumer Sentiment Insights") st.success("Consumers prefer sedans with autonomous driving, luxurious interiors, and advanced hybrid technology.")

st.markdown("---") st.caption("Zeta Motors - Powered by AI Market Insights")

