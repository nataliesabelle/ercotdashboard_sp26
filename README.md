# Texas Electric Generation and Load Growth Dashboard

## Overview

This Streamlit dashboard provides a centralized platform for visualizing and analyzing Texas's electric generation and load growth through an embedded interactive Leaflet web map. The dashboard contextualizes spatial generation data within the broader ERCOT system analysis framework.

The embedded map complements specialized analytical dashboards by offering geospatial insights into generation infrastructure:

- **Rafael's Dashboard**: Tracks new electric load and demand growth, focusing on large load interconnections and their transmission system impacts.
- **Abby's Dashboard**: Delivers detailed ERCOT data analysis and trends, including generation mix breakdowns, fuel type performance, and historical metrics.

Together, these tools support comprehensive ERCOT planning and policy decisions.

## Architecture

The dashboard follows a modular architecture:

- **Leaflet Map Hosting**: The interactive web map is hosted on GitHub Pages, generated from QGIS using qgis2web for optimal web compatibility.
- **Streamlit Embedding**: The main dashboard uses Streamlit to embed the map via a secure HTTPS iframe, ensuring seamless integration without re-implementing map functionality.
- **Contextual Analysis**: Sidebar sections provide project overview, related analyses, data sources, and credits for a complete user experience.

## Deployment

### Local Development

1. Ensure Python 3.8+ is installed
2. Install dependencies:
   ```bash
   pip install streamlit
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```
4. Access the dashboard at `http://localhost:8501`

### Streamlit Community Cloud

The application is designed for deployment on Streamlit Community Cloud:

1. Push the repository to GitHub
2. Connect the repository to Streamlit Community Cloud
3. Deploy directly from the main branch
4. The app will be accessible via the provided Streamlit URL

## Data Notes

This dashboard integrates multiple data sources for comprehensive ERCOT analysis:

- **Spatial Generation Data**: Geographic information on electric generation facilities, processed through QGIS for web mapping
- **ERCOT Planning Data**: High-level transmission infrastructure and system planning information from public ERCOT reports
- **Infrastructure Context**: Transmission corridors, substations, and key energy infrastructure details

All data is sourced from public, non-sensitive ERCOT documents and planning materials.

## Attribution

- **Map Technology**: Leaflet.js and QGIS/qgis2web
- **Dashboard Framework**: Streamlit
- **Data Sources**: ERCOT public reports and planning documents
- **Development**: ERCOT Dashboard Team

For questions or contributions, please contact the development team. 
