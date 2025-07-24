import streamlit as st
from blinkit_scraper import search_blinkit
from zepto_scraper import search_zepto

st.title("🛒 Grocery Price Comparison")
st.caption("Compare prices from Blinkit and Zepto instantly")

query = st.text_input("🔍 Enter item to search", placeholder="e.g., Amul Butter")
location = st.text_input("📍 Enter your pincode", value="122001")

if st.button("Compare Prices") and query:
    st.subheader("🔎 Results:")

    blinkit = search_blinkit(query, location)
    zepto = search_zepto(query, location)

    st.write("## 🟡 Blinkit")
    if blinkit:
        for item in blinkit:
            st.write(f"{item['name']} - {item['price']}")
    else:
        st.warning("No results from Blinkit")

    st.write("## 🟣 Zepto")
    if zepto:
        for item in zepto:
            st.write(f"{item['name']} - {item['price']}")
    else:
        st.warning("No results from Zepto")
