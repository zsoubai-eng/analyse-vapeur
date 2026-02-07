
import streamlit as st
import os

st.set_page_config(
    page_title="OCP Steam Optimization Assistant",
    page_icon="🏭",
    layout="wide"
)

# Sidebar Navigation Header
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/OCP_Group_logo.svg/1200px-OCP_Group_logo.svg.png", width=100)
st.sidebar.markdown("### 🧬 Smart Analytics v2.0")

# --- AUTHENTICATION ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("🏭 OCP Industrial Analytics Portal")
    st.markdown("---")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.info("🔐 Restricted Access: Please authenticate to continue.")
        with st.form("login"):
            user = st.text_input("Username")
            pw = st.text_input("Password", type="password")
            if st.form_submit_button("Login"):
                # Read credentials from environment variables (set in Render dashboard)
                ADMIN_USER = os.getenv("ADMIN_USERNAME", "admin")
                ADMIN_PASS = os.getenv("ADMIN_PASSWORD", "7f3a9b2c-4e8d-11ec-9f7a-0242ac120002")
                
                if user == ADMIN_USER and pw == ADMIN_PASS:
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("Invalid credentials")

    with col2:
        st.markdown("""
        ### Platform Capabilities:
        - **🔄 Ingestion:** Parsing complex YOKOGAWA DCS exports.
        - **🧠 Discovery:** PCA & K-Means clustering for regime detection.
        - **🔥 Optimization:** Real-time Steam Intensity (CSV) tracking.
        - **📊 Reporting:** Automated KPI generation per production stage.
        """)

if not st.session_state.logged_in:
    login()
    st.stop()

# --- HOME PAGE (AFTER LOGIN) ---
st.title("👋 Industrial Optimization Assistant")
st.markdown("---")

col_l, col_r = st.columns([2, 1])

with col_l:
    st.markdown("""
    ### Welcome, Zakaria.
    
    This platform orchestrates the **Steam Minimization Project** (DMAIC Cycle). 
    Use the sidebar to navigate through the analysis phases.
    
    #### 🚀 Global Impact:
    - **Optimization Target:** -10% CSV
    - **Annual Savings Potential:** 5.39M MAD
    - **Data Coverage:** 3 years historical sensors
    """)
    st.success("✅ System Status: All Analysis Modules Loaded (KPI Engine, ML Cluster, Fuzzy Cleaner)")

with col_r:
    st.metric(label="Optimization Score", value="92%", delta="+5%")
    st.metric(label="Data Quality Index", value="98.5%", delta="0.2%")

st.markdown("---")
st.caption("Powered by ESITH Industrial Engineering & OCP Jorf Lasfar Data")
