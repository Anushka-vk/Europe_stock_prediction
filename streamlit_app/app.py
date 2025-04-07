import streamlit as st

st.set_page_config(page_title="Europe Stock Exchange", layout="wide")

st.markdown("<h1 style='text-align: center; background-color: lightred; padding: 10px; border-radius: 10px;'>EUROPE STOCK EXCHANGE</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'><u>INDEX</u></h3>", unsafe_allow_html=True)

stocks = [
    ["LVMH", "HermesIntl", "Loreal", "SchneiderElectric"],
    ["TotalEnergies", "SAP", "DeutscheTelekom", "Siemens"],
    ["AllianzSE", "MunichRE", "IntesaSanpaolo", "Ferrari"],
    ["UniCredit", "ENEL", "Generali", "Nestle"],
    ["RocheHolding", "Novartis", "ZurichInsurance", "UBSGroup"]
]

cols = st.columns(4)
for row in stocks:
    for i, stock in enumerate(row):
        with cols[i]:
            if st.button(stock):
                st.session_state["selected_stock"] = stock
                st.switch_page(f"pages/{stock}.py") 


st.markdown("<p style='text-align: center;'>Anushka Kamble</p>", unsafe_allow_html=True)
