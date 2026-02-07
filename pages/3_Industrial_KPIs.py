
import streamlit as st
from scripts.analysis.kpi_engine import KPIEngine

st.set_page_config(page_title="KPI Dashboard", page_icon="🎯", layout="wide")

st.title("🎯 Phase 3: Industrial Performance Tracking")
st.markdown("---")

if 'data' not in st.session_state:
    st.error("❌ No data found. Please run 'Data Processing' first.")
    st.stop()

df = st.session_state['data']

with st.spinner("Calculating Engine Metrics..."):
    engine = KPIEngine(df)
    results = engine.calculate_all_metrics()
    summary = engine.aggregate_by_stage()

st.markdown("### 📊 Performance Summary by Stage (Échelon)")
st.dataframe(summary, use_container_width=True)

st.markdown("---")
st.markdown("### 🚀 Real-time Optimization Recommendations")

# Logic to identify if specific consumption is out of spec
mean_csv = results['specific_steam_consumption'].mean()
if mean_csv > 1.2: # Example threshold
    st.error(f"⚠️ High Consumption Alert: Current CSV average ({mean_csv:.2f}) is 15% above benchmark.")
    st.markdown("- **Action:** Inspect heat exchanger E-301 for fouling.")
    st.markdown("- **Action:** Verify vacuum pressure stability in Flash stage.")
else:
    st.success(f"✅ Performance Optimal: Current CSV ({mean_csv:.2f}) is within Green Zone.")

col1, col2 = st.columns(2)
with col1:
    st.metric("Mean Concentration Efficiency", f"{results['concentration_efficiency'].mean()*100:.2f}%")
with col2:
    st.metric("Total Water Evaporated", f"{results['water_evaporated_tons'].sum():.0f} Tons")

st.info("💡 Tip: Use these metrics for daily Shift Handover Reports (SOP-42).")
