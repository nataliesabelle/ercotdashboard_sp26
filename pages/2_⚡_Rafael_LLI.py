"""
Rafael's ERCOT Large Electronic Load Dashboard
Multi-page wrapper for LLI tracking dashboard
"""
import sys
from pathlib import Path

# Add rafael dashboard to path so it can import data correctly
rafael_path = Path(__file__).parent.parent / "rafael_dashboard"
sys.path.insert(0, str(rafael_path))

# Change working directory for file operations
import os
os.chdir(rafael_path)

# Now import and run rafael's app
with open(rafael_path / "app.py") as f:
    code = f.read()
    # Skip the page config since multi-page handles it
    code = code.replace(
        'st.set_page_config(
    page_title="ERCOT Large Electronic Load Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)',
        '# Page config handled by multi-page framework'
    )
    exec(code)
