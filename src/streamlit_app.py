import streamlit as st
from blinkit_scraper import search_blinkit
from zepto_scraper import search_zepto

st.set_page_config(page_title="Grocery Price Compare", layout="centered")
st.title("🛒 Grocery Price Comparison")

products = [
    "Amul Salted Butter",
    "Veeba Tomato Ketchup Chef's Special",
    "Coca Cola Soft Drink"
]

location = st.text_input("📍 Enter Your Pincode (default: 122001)", "122001")

if st.button("Compare Prices"):
    for product in products:
        st.markdown(f"### 🔍 {product}")

        blinkit_results = search_blinkit(product, location)
        zepto_results = search_zepto(product, location)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🟡 Blinkit")
            if blinkit_results:
                for item in blinkit_results:
                    st.write(f"{item['name']} – {item['price']}")
            else:
                st.write("No results found.")

        with col2:
            st.subheader("🟣 Zepto")
            if zepto_results:
                for item in zepto_results:
                    st.write(f"{item['name']} – {item['price']}")
            else:
                st.write("No results found.")
