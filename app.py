import streamlit as st
import streamlit.components.v1 as components

# Configuration
st.set_page_config(
    page_title="Texas Electric Generation and Load Growth Dashboard",
    layout="wide",
    page_icon="⚡"
)

# Constants
MAP_URL = "https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/"
IFRAME_HEIGHT = 900

# Title
st.title("Texas Electric Generation and Load Growth Dashboard")

# Main content
st.markdown("""
This dashboard embeds an interactive Leaflet web map visualizing electric generation growth and spatial infrastructure context across Texas. The map provides critical insights into the geographic distribution of generation facilities and their relevance to ERCOT system planning, helping stakeholders understand the evolving energy landscape.

Key features of the embedded map include:
- **Electric Generation Growth**: Visualization of generation capacity expansion over time
- **Spatial Infrastructure Context**: Mapping of transmission lines, substations, and key infrastructure
- **ERCOT System Planning**: Contextual data supporting reliability and planning decisions
""")

# Embed the iframe
components.iframe(MAP_URL, height=IFRAME_HEIGHT, scrolling=True)

# Sidebar
with st.sidebar:
    st.header("Dashboard Information")

    with st.expander("Project Overview", expanded=True):
        st.markdown("""
        This dashboard connects spatial generation data with comprehensive ERCOT system analysis. By embedding an externally hosted Leaflet map, it provides a centralized view of Texas's electric infrastructure while linking to specialized analytical dashboards for deeper insights into load growth and generation trends.
        """)

    with st.expander("Related Dashboards & Analyses"):
        st.markdown("""
        **Rafael's Dashboard**: Focuses on new electric load and demand growth, tracking large load interconnections and their impact on ERCOT's transmission system.

        **Abby's Dashboard**: Provides detailed ERCOT data analysis and trends, including generation mix, fuel type breakdowns, and historical performance metrics.
        """)

    with st.expander("Data Sources & Attribution"):
        st.markdown("""
        **Spatial Data**: Generated using QGIS and qgis2web for web-compatible Leaflet maps.

        **ERCOT Datasets**: Incorporates high-level ERCOT planning data, transmission infrastructure information, and generation capacity details (sourced from public ERCOT reports and planning documents).
        """)

    with st.expander("Contact / Credits"):
        st.markdown("""
        **Developed by**: ERCOT Dashboard Team

        **Contact**: [Placeholder - Contact information]

        **Credits**: Built with Streamlit, Leaflet, and QGIS. Data attribution to ERCOT and public sources.
        """)