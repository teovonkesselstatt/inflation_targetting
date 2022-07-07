from webapp import country, correlations, references, database
import streamlit as st

def run_app():

    PAGES = {
            "Country": country,
            "Full Database": database,
            "Correlations": correlations,
            "References": references
        }

    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.run_app()