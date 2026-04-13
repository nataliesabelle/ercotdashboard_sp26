import streamlit as st
import streamlit.components.v1 as components

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Energy Systems Dashboard",
    page_icon="⚡",
    layout="wide",
)

# -----------------------------
# APP TITLE
# -----------------------------
st.title("⚡ Energy Systems Dashboard Hub")
st.caption("Interactive dashboards for electricity generation, infrastructure, and planning")

# -----------------------------
# DASHBOARD REGISTRY
# Add new dashboards here only
# -----------------------------
DASHBOARDS = {
    "Texas Generation (ArcGIS)": {
        "description": "Statewide electricity generation map for Texas",
        "url": "https://www.arcgis.com/apps/mapviewer/index.html?configurableview=true&webmap=4ca140dcd1cd4cbcaa5d38a77e273397&theme=light&heading=true&legend=true&share=true&center=-97.66697648907267,31.510804989798014&scale=4622324.434309",
        "height": 600,
        "width": 700,
    },

    # Example placeholders – enable later
    # "Transmission Infrastructure": {
    #     "description": "High-voltage transmission network",
    #     "url": "https://...",
    #     "height": 700,
    # },

    # "Storage & DERs": {
    #     "description": "Battery storage and distributed energy resources",
    #     "url": "https://...",
    #     "height": 700,
    # },
}

# -----------------------------
# SIDEBAR CONTROLS
# -----------------------------
st.sidebar.header("Dashboard Selection")

selected_dashboard = st.sidebar.selectbox(
    label="Choose a dashboard",
    options=list(DASHBOARDS.keys()),
)

st.sidebar.markdown("---")
st.sidebar.caption("Powered by Streamlit + ArcGIS")

# -----------------------------
# DISPLAY SELECTED DASHBOARD
# -----------------------------
dashboard = DASHBOARDS[selected_dashboard]

st.subheader(selected_dashboard)
st.write(dashboard["description"])  

# Embed the external URL using an iframe
html_code = f'''\n<iframe width="{dashboard['width']}" height="{dashboard['height']}" allow="local-network-access; geolocation" title="{selected_dashboard}" src="{dashboard['url']}" frameborder="0" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>\n'''  

components.html(
    html_code,
    height=dashboard["height"],
    scrolling=True,
)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption(
    "MVP hosted on Streamlit Cloud • Public data sources • For research and demonstration purposes"
)