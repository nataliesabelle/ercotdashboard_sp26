"""
ERCOT Spatial Generation & Infrastructure Map
Embedded Leaflet map showing geographic distribution of generation and transmission infrastructure
"""
import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="ERCOT Spatial Map",
    layout="wide",
    page_icon="🗺️"
)

# Constants
MAP_URL = "https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/"
IFRAME_HEIGHT = 900

# Title and description
st.title("🗺️ ERCOT Spatial Generation & Infrastructure Map")

st.markdown("""
This map displays the geographic distribution of electric generation facilities and transmission infrastructure across Texas. The visualization provides spatial context for understanding ERCOT's generation growth and infrastructure constraints.

**Key features:**
- **Electric Generation Facilities**: Geographic locations of generation capacity across fuel types
- **Transmission Infrastructure**: Major transmission corridors (345 kV, 765 kV) and substations
- **ERCOT System Planning**: Spatial relationships supporting grid reliability analysis

**Data Sources**: QGIS/qgis2web processed data, ERCOT infrastructure reports, public generation facilities data

---
""")

# Embed the iframe
st.markdown("### Interactive Map")
components.iframe(MAP_URL, height=IFRAME_HEIGHT, scrolling=True)

st.markdown("""
---

### How to Use This Map

1. **Zoom & Pan**: Use mouse scroll or touch to zoom; drag to pan the map
2. **Layer Toggle**: Enable/disable visualization layers using controls
3. **Hover/Click**: Hover over or click features for detailed information
4. **Integrate with Other Dashboards**: Compare spatial patterns with generation trends in the Generation Dashboard or infrastructure impacts in the LLI Dashboard

### Data Integration with Other Dashboards

- **Generation Dashboard** (📊): Explore time-series generation trends by fuel type
- **LLI Dashboard** (⚡): See large load projects and their transmission proximity
- **Spatial Map** (🗺️): Understand geographic distribution and infrastructure context

Together, these three perspectives enable comprehensive ERCOT energy analysis.
""")
