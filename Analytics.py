import streamlit as st
import pandas as pd

# Page title
st.title("📊 Analytics Dashboard")

# Load dataset
df = pd.read_csv("cleaned_house_data.csv")

# Show data
st.subheader("🏠 House Dataset")
st.dataframe(df.head())

# Metrics
st.subheader("📌 Project Insights")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Houses", len(df))

with col2:
    st.metric("Average Price", f"₹ {int(df['Price'].mean())}")

with col3:
    st.metric("Average Area", f"{int(df['Area'].mean())} sqft")

# Charts
st.subheader("📈 Price Distribution")
st.bar_chart(df["Price"])

st.subheader("📊 Area Distribution")
st.line_chart(df["Area"])

# Location count
st.subheader("🌍 Houses by Location")

location_count = df["Location"].value_counts()

st.bar_chart(location_count)

# Correlation
st.subheader("📌 Correlation Matrix")

numeric_df = df.select_dtypes(include='number')

st.write(numeric_df.corr())
