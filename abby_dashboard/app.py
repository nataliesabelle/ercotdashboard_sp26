"""
ERCOT Generation Dashboard - Analysis of historical generation by fuel type
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

DATA_PATH = Path(__file__).parent / "cleaned.csv"
TIME_COL = "interval_start"
FUEL_COL = "fuel_type"
VALUE_COL = "generation_mw"

FUEL_ORDER = ["BIOMASS", "COAL", "GAS", "GAS-CC", "HYDRO", "NUCLEAR", "OTHER", "SOLAR", "WIND", "WSL"]
FUEL_COLORS = {
    "BIOMASS": "#1f77b4", "COAL": "#ff7f0e", "GAS": "#2ca02c", "GAS-CC": "#d62728",
    "HYDRO": "#9467bd", "NUCLEAR": "#8c564b", "OTHER": "#e377c2", "SOLAR": "#7f7f7f",
    "WIND": "#bcbd22", "WSL": "#17becf",
}
FUEL_LABELS = {
    "BIOMASS": "Biomass", "COAL": "Coal", "GAS": "Natural Gas", "GAS-CC": "Natural Gas Combined Cycle",
    "HYDRO": "Hydroelectric", "NUCLEAR": "Nuclear", "OTHER": "Other", "SOLAR": "Solar", "WIND": "Wind", "WSL": "WSL",
}

st.set_page_config(page_title="ERCOT Generation Dashboard", layout="wide", page_icon="⚡")

@st.cache_data
def load_data(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    if "Date" not in df.columns:
        raise ValueError("CSV must have Date column")
    df = df.rename(columns={"Date": TIME_COL})
    fuel_columns = [c for c in df.columns if c not in [TIME_COL, "total_all_fuels"]]
    df = df.melt(id_vars=[TIME_COL], value_vars=fuel_columns, var_name=FUEL_COL, value_name=VALUE_COL)
    df[TIME_COL] = pd.to_datetime(df[TIME_COL], errors="coerce")
    df[FUEL_COL] = df[FUEL_COL].astype(str).str.upper().str.strip()
    df[VALUE_COL] = pd.to_numeric(df[VALUE_COL], errors="coerce")
    return df.dropna(subset=[TIME_COL, FUEL_COL, VALUE_COL]).copy().sort_values(TIME_COL).reset_index(drop=True)

@st.cache_data
def prepare_data(df):
    out = df.copy()
    out["date"] = out[TIME_COL].dt.floor("D")
    out["month"] = out[TIME_COL].dt.to_period("M")
    out["year"] = out[TIME_COL].dt.year
    return out

df = load_data(DATA_PATH)
data = prepare_data(df)

st.title("ERCOT Generation Dashboard")
st.markdown("Historical generation analysis by fuel type across ERCOT system")

col1, col2 = st.columns([1, 2])
with col1:
    years = sorted(data["year"].unique())
    selected_year = st.selectbox("Select Year:", years, index=len(years)-1 if years else 0)
with col2:
    latest = data[TIME_COL].max()
    st.markdown(f"**Data Last Updated:** {latest.strftime('%Y-%m-%d') if latest else 'N/A'}")

st.divider()
col1, col2, col3, col4 = st.columns(4)
year_data = data[data["year"] == selected_year]
if not year_data.empty:
    with col1:
        st.metric("Peak Generation", f"{year_data[VALUE_COL].max():,.0f} MW")
    with col2:
        st.metric("Avg Generation", f"{year_data[VALUE_COL].mean():,.0f} MW")
    with col3:
        st.metric("Total Energy", f"{year_data[VALUE_COL].sum():,.0f} MWh")
    with col4:
        top_fuel = year_data.groupby(FUEL_COL)[VALUE_COL].sum().idxmax()
        st.metric("Top Fuel", FUEL_LABELS.get(top_fuel, top_fuel))

st.divider()

fig1 = px.line(data.groupby(TIME_COL)[VALUE_COL].sum().reset_index(), x=TIME_COL, y=VALUE_COL, title="Total Generation Over Time")
fig1.update_layout(template="plotly_white", height=350, margin=dict(l=40, r=20, t=40, b=40))
st.plotly_chart(fig1, use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    daily = data.groupby("date")[VALUE_COL].sum().reset_index()
    fig2 = px.line(daily, x="date", y=VALUE_COL, title="Daily Generation")
    fig2.update_layout(template="plotly_white", height=350, margin=dict(l=40, r=20, t=40, b=40))
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    fuel_total = data.groupby(FUEL_COL)[VALUE_COL].sum().sort_values(ascending=False).reset_index()
    fig3 = px.bar(fuel_total, x=FUEL_COL, y=VALUE_COL, color=FUEL_COL, color_discrete_map=FUEL_COLORS, title="Total by Fuel Type")
    fig3.update_layout(template="plotly_white", height=350, margin=dict(l=40, r=20, t=40, b=40))
    st.plotly_chart(fig3, use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    monthly = data.groupby("month")[VALUE_COL].sum().reset_index()
    fig4 = px.line(monthly, x="month", y=VALUE_COL, markers=True, title="Monthly Generation")
    fig4.update_layout(template="plotly_white", height=350, margin=dict(l=40, r=20, t=40, b=40))
    st.plotly_chart(fig4, use_container_width=True)

with col2:
    fuel_time = data.groupby([TIME_COL, FUEL_COL])[VALUE_COL].sum().reset_index()
    fig5 = px.area(fuel_time, x=TIME_COL, y=VALUE_COL, color=FUEL_COL, color_discrete_map=FUEL_COLORS, title="Generation by Fuel Over Time")
    fig5.update_layout(template="plotly_white", height=350, margin=dict(l=40, r=20, t=40, b=40))
    st.plotly_chart(fig5, use_container_width=True)
