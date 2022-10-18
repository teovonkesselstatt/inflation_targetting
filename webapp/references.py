import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

def run_app():

    st.title('References')
    st.write("""
    * Inflation Data:
        * https://www.worldbank.org/en/research/brief/inflation-database
    * Target Data:
        * https://www.worldbank.org/en/research/publication/inflation-in-emerging-and-developing-economies
        * https://www.elibrary-areaer.imf.org
    * Terms of Trade Data:
        * https://data.imf.org/?sk=2CDDCCB8-0B59-43E9-B6A0-59210D5605D2&sId=1390030341854
    * Real Exchange Rate:
        * https://www.bruegel.org/publications/datasets/real-effective-exchange-rates-for-178-countries-a-new-database/
    * Main Trading Partners:
        * https://www.trademap.org/Index.aspx"""
    )
