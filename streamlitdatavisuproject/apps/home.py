import streamlit as st


def app():
    st.write('My linkedin: https://www.linkedin.com/in/colard-nathalie/')
    st.write('My Github: https://github.com/nathaa13')
    st.title("Summary of Nathalie COLARD's personal data 📊")
    st.subheader('By Nathalie COLARD')
    st.write("An application that analyzes Nathalie Colard's personal data with visual graphics. For now, two types of data are available: step data and spotify data. Select the data you want to view in the sidebar!")

    st.subheader('Good viewing!')
    st.image("analyse.jpg")



