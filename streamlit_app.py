import streamlit as st


st.set_page_config(page_title="employee retention and recruitment model", layout="wide")


st.title("employee retention and recruitment model")

app_choice = st.radio("Select an Application:", ["employee retention", "employee recruitment","Employee Promotion"])


if app_choice == "employee retention":
    st.page_link("https://blank-app-ztexj6vr8xi.streamlit.app/", label="EMPLOYEE RETENTION APPLICATION")


elif app_choice == "employee recruitment":
    st.page_link("https://blank-app-r88p17uu5ea.streamlit.app/", label="EMPLOYEE RECRUITMENT APPLICATION")

elif app_choice == "Employee Promotion":
    st.page_link("https://blank-app-0xeqw2zp56na.streamlit.app/",label="EMPLOYEE PROMOTION MODEL") 
