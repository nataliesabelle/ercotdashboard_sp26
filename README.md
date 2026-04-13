# ERCOT Multi-Dashboard Hub

A unified Streamlit platform for analyzing Texas's electric generation and large load growth through interconnected analytical dashboards.

## Overview

This repository contains an integrated dashboard hub that combines two complementary analytical perspectives:

- **📊 Abby's Generation Dashboard**: Historical ERCOT generation analysis by fuel type (solar, wind, natural gas, nuclear, etc.)
- **⚡ Rafael's Large Load Interconnection (LLI) Dashboard**: Tracking of large electronic loads (data centers, AI facilities) and their transmission impacts

Both dashboards draw from publicly available ERCOT data to support grid planning, reliability analysis, and policy decisions.

## Architecture

### Multi-Page Structure

```
ercotdashboard_sp26/
├── app.py                        # Hub home page
├── requirements.txt             # Root dependencies
├── pages/
│   ├── 1_📊_Abby_Generation.py   # Generation dashboard page
│   └── 2_⚡_Rafael_LLI.py        # Large load dashboard page
├── abby_dashboard/
│   ├── app.py                   # Generation analysis logic
│   ├── cleaned.csv              # Generation data
│   └── requirements.txt         # Dashboard dependencies
└── rafael_dashboard/
    ├── app.py                   # LLI analysis logic
    ├── data/
    │   ├── projects.csv         # LLI project data
    │   ├── queue_categories.csv # Queue history
    │   └── transmission_backbone.json  # Infrastructure
    └── requirements.txt         # Dashboard dependencies
```

### Navigation

The main app (`app.py`) serves as the home/hub page with buttons to navigate to:
1. **Generation Dashboard** (pages/1_📊_Abby_Generation.py)
2. **LLI Dashboard** (pages/2_⚡_Rafael_LLI.py)

Streamlit's built-in sidebar provides seamless page navigation.

## Dashboards

### 📊 Generation Dashboard (Abby)

Comprehensive analysis of ERCOT generation patterns:
- **Metrics**: Peak generation, average generation, total energy, top fuel type
- **Visualizations**: 
  - Total generation over time
  - Daily generation trends
  - Generation by fuel type
  - Monthly and yearly patterns
  - Fuel mix composition
- **Data**: Daily generation by fuel (2022+)
- **Interactivity**: Year selector to filter KPIs

### ⚡ Large Load Interconnection Dashboard (Rafael)

Policy decision-support tool for tracking large electronic loads:
- **Coverage**: ~30+ major projects (data centers, AI facilities, crypto mining)
- **Features**:
  - Interactive map with project locations
  - Status filtering (Operational, Under Review, To Be Operational)
  - Sector analysis (AI/Data Center, Crypto Mining, Other)
  - Transmission infrastructure overlay
  - Owner/Developer breakdown
  - Queue category timeline
- **Data**: ERCOT LLI public data, TAC reports, PUCT filings
- **Interactivity**: Year slider, multi-select filters, detailed project table

## Deployment

### Local Development

1. **Clone and setup**:
   ```bash
   git clone https://github.com/nataliesabelle/ercotdashboard_sp26.git
   cd ercotdashboard_sp26
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run locally**:
   ```bash
   streamlit run app.py
   ```

4. **Access**: Open `http://localhost:8501` in browser

### Streamlit Community Cloud

1. Connect repository to [Streamlit Community Cloud](https://streamlit.io/cloud)
2. Deploy from main branch
3. The app will be available at: `https://share.streamlit.io/nataliesabelle/ercotdashboard_sp26/main/app.py`

## Data Sources

- **Generation Data**: ERCOT historical generation CSV (cleaned.csv)
- **LLI Data**: ERCOT TAC reports, queue tracking, PUCT filings
- **Transmission Infrastructure**: ERCOT 2024 Constraints Report, Planning Guide
- **All data sourced from public ERCOT documents and announcements**

## Technical Stack

- **Framework**: Streamlit 1.32+
- **Visualization**: Plotly
- **Data Processing**: Pandas, NumPy
- **Python**: 3.8+
- **Deployment**: Streamlit Community Cloud

## File Structure Details

### Dashboard Pages
- Each page corresponds to a dashboard and is standalone
- Pages are located in `pages/` directory with numeric prefixes (Streamlit convention)
- Emoji icons in filenames appear in the sidebar navigation

### Data Directories
- **abby_dashboard/data**: `cleaned.csv` with daily ERCOT generation by fuel
- **rafael_dashboard/data**: 
  - `projects.csv`: LLI project details
  - `queue_categories.csv`: Historical queue size tracking
  - `transmission_backbone.json`: GeoJSON infrastructure data

## Usage Guide

### Home Hub
On launch, users see the hub page with:
- Overview of dashboard purposes
- Quick-access buttons to navigate to each dashboard
- Sidebar with additional information

### Navigating Between Pages
- Use the page selector in the left sidebar
- Or click dashboard buttons on the home page

### Generation Dashboard
- Select year to update KPI metrics
- Explore generation trends across all fuel types
- Compare daily, monthly, and yearly patterns

### LLI Dashboard
- Adjust year slider to see projects coming online
- Filter by status, sector, and owner
- Hover over map markers for project details
- Review detailed project table with search/sort

## Attribution & Credits

Built with:
- **Streamlit**: Interactive web framework
- **Plotly**: Advanced visualizations
- **ERCOT**: Public data and planning documents
- **UT Austin CE377K**: Energy Systems course (Spring 2026)

## Contact

For questions or suggestions, contact the ERCOT Dashboard Team.

---

**Last Updated**: April 2026  
**Status**: Production-ready for Streamlit Community Cloud 
