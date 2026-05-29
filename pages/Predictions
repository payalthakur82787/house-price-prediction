import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Data Insights",
    page_icon="📊"
)

st.title("📊 Housing Data Insights")

# Sample dataset
data = pd.DataFrame({
    "Area": [1000, 1200, 1500, 1800, 2200],
    "Price": [3000000, 4000000, 5000000, 6500000, 8000000]
})

st.subheader("Dataset Preview")
st.dataframe(data)

# Chart
st.subheader("Area vs Price")

fig, ax = plt.subplots()

ax.plot(data["Area"], data["Price"], marker='o')

ax.set_xlabel("Area")
ax.set_ylabel("Price")

st.pyplot(fig)

st.info("Larger houses generally have higher prices.")
