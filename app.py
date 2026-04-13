"""
ERCOT Multi-Dashboard Hub
Home page integrating generation analysis and large load interconnection tracking
"""
import streamlit as st

# Configuration
st.set_page_config(
    page_title="ERCOT Dashboard Hub",
    layout="wide",
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# Title and intro
st.title("🔌 ERCOT Energy Insights Dashboard Hub")

st.markdown("""
A unified platform for analyzing Texas's electric generation and large load growth through multiple complementary analytical lenses.
""")

st.divider()

# Three main dashboards
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🗺️ Spatial Map")
    st.markdown("""
    **Interactive geographic visualization** of ERCOT generation facilities and transmission infrastructure.
    
    ✅ Generation facility locations  
    ✅ Transmission corridors (345 kV, 765 kV)  
    ✅ Substation positions  
    ✅ ERCOT system layout  
    
    Navigate to explore spatial generation distribution.
    """)
    if st.button("🗺️ Open Spatial Map", use_container_width=True):
        st.switch_page("pages/0_🗺️_Spatial_Map.py")

with col2:
    st.subheader("📊 Generation Analysis")
    st.markdown("""
    **Comprehensive analysis** of ERCOT generation data across fuel types including solar, wind, natural gas, and nuclear.
    
    ✅ Historical generation trends (daily, monthly, yearly)  
    ✅ Fuel mix composition and shifts  
    ✅ Peak and average generation metrics  
    ✅ Year-over-year comparisons  
    
    Navigate to this dashboard to explore generation patterns and fuel diversity.
    """)
    if st.button("📊 Open Generation Dashboard", use_container_width=True):
        st.switch_page("pages/1_📊_Abby_Generation.py")

with col3:
    st.subheader("⚡ Large Load Interconnections")
    st.markdown("""
    **Policy decision-support tool** tracking large electronic loads (data centers, AI facilities, mining operations) interconnecting to ERCOT.
    
    ✅ ~30+ large load projects tracked  
    ✅ Capacity, status, and in-service timeline  
    ✅ Geographic distribution and transmission infrastructure  
    ✅ Sector breakdown and owner analysis  
    
    Navigate to this dashboard for infrastructure planning insights.
    """)
    if st.button("⚡ Open LLI Dashboard", use_container_width=True):
        st.switch_page("pages/2_⚡_Rafael_LLI.py")

st.divider()

# About section
st.subheader("About This Hub")
st.markdown("""
This multi-dashboard platform enables ERCOT stakeholders—planners, analysts, policymakers, and researchers—to understand Texas's evolving energy landscape from multiple perspectives:

- **Spatial Map**: Geographic visualization of generation facilities and transmission infrastructure across ERCOT
- **Generation Dashboard**: Understand fuel diversity, capacity trends, and system-wide generation patterns
- **Large Load Dashboard**: Track new large electronic loads and their infrastructure implications

All three dashboards integrate complementary views of ERCOT's generation and infrastructure data, supporting informed decision-making for grid reliability, planning, and policy.
""")

with st.sidebar:
    st.header("ℹ️ Dashboard Guide")
    
    with st.expander("Using This Hub", expanded=True):
        st.markdown("""
        Use the page selector in the left sidebar to navigate between:
        - **🗺️ Spatial Map** - Geographic generation & transmission visualization
        - **📊 Generation Dashboard** - Fuel-level analysis and trends
        - **⚡ LLI Dashboard** - Large load tracking and infrastructure
        """)
    
    with st.expander("Dashboard Descriptions"):
        st.markdown("""
        **🗺️ Spatial Map**: Interactive Leaflet-based map showing generation facilities, transmission corridors, and substations across ERCOT service territory.
        
        **📊 Generation Analysis**: Historical generation trends by fuel type, including daily, monthly, and yearly patterns plus KPIs.
        
        **⚡ Large Loads**: Projects interconnecting to ERCOT with 500+ MW capacity, including status, timeline, sector, and geographic distribution.
        """)
    
    with st.expander("Data Sources"):
        st.markdown("""
        - ERCOT public reports and planning data
        - QGIS/qgis2web spatial data
        - TAC reports and LLI queue information
        - PUCT filings and public announcements
        - Historical generation and demand data
        """)
    
    with st.expander("Technical Info"):
        st.markdown("""
        **Framework**: Streamlit 1.32+  
        **Visualization**: Plotly, Leaflet (via iframe)  
        **Data Processing**: Pandas, NumPy  
        **Deployment**: Streamlit Community Cloud
        """)