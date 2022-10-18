import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

def run_app():

    df = pd.read_csv("db.csv")
    option = st.sidebar.selectbox(
        'Select a country',
        df['country'].unique())


    code = df[df['country'] == option]['imf_code'].iloc[0]
    country = df[df["imf_code"] == code]

    title = "Inflation Targetting in " + country["country"].iloc[0]
    st.title(title)


    metric2 = st.sidebar.selectbox(
        'Select Metric',
        ("ToT", "VarToT"))

    fig1, ax1 = plt.subplots(figsize=(12, 4))

    country.plot(x = "year", \
        y = ["inflation","upper","lower"], \
            style=['-','--','--'], \
                color=['r','gray','gray'],\
                    ax = ax1)

    country.plot('year',metric2,secondary_y=True, ax=ax1)

    st.pyplot(fig1)

    fig, ax = plt.subplots(figsize=(12, 4))

    country.plot(x = "year", \
        y = ["inflation","upper","lower","midpoint"], \
            style=['-','--','--','--'], \
                color=['r','gray','gray','black'],\
                    ax = ax)

    st.pyplot(fig)
