import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

def run_app():

    df = pd.read_csv("db.csv")

    corr_ToT = df.groupby('country')[['inflation', 'deviation']].corrwith(df['ToT'])
    corr_ToT.rename(columns = {'inflation':'Inflation/ToT', \
        'deviation':'Deviation/ToT'}, inplace = True)
    corr_Var = df.groupby('country')[['inflation', 'deviation']].corrwith(df['VarToT'])
    corr_Var.rename(columns = {'inflation':'Inflation/VarToT', \
        'deviation':'Deviation/VarToT'}, inplace = True)
    corrs = corr_ToT.merge(corr_Var, on='country', how='left').dropna()

    st.dataframe(corrs.style.background_gradient(cmap='RdYlGn'))
