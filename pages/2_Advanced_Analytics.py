
import streamlit as st
import pandas as pd
from scripts.visualization.kpi_charts import plot_correlation_heatmap
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Advanced Analytics", page_icon="📈", layout="wide")

st.title("📈 Phase 2: Statistical Discovery")
st.markdown("---")

if 'data' not in st.session_state:
    st.error("❌ No data found. Please run 'Data Processing' first.")
    st.stop()

df = st.session_state['data']
numeric_df = df.select_dtypes(include='number')

tab1, tab2 = st.tabs(["🔥 Correlation Matrix", "🧬 PCA Reduction"])

with tab1:
    st.markdown("### Identifying Steam Consumption Drivers")
    if not numeric_df.empty:
        fig = plot_correlation_heatmap(numeric_df)
        st.pyplot(fig)
    else:
        st.warning("No numeric columns found for correlation.")

with tab2:
    st.markdown("### Principal Component Analysis (PCA)")
    n_components = st.slider("Select PC Components", 2, min(5, len(numeric_df.columns)), 2)
    
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_df)
    
    pca = PCA(n_components=n_components)
    pca_result = pca.fit_transform(scaled_data)
    
    st.info(f"Cumulative Explained Variance: {sum(pca.explained_variance_ratio_):.2f}")
    
    pca_df = pd.DataFrame(pca_result, columns=[f"PC{i+1}" for i in range(n_components)])
    st.dataframe(pca_df.head(), use_container_width=True)
    
    # Simple Scatter Plot for PC1 vs PC2
    import matplotlib.pyplot as plt
    fig2, ax2 = plt.subplots()
    ax2.scatter(pca_df["PC1"], pca_df["PC2"], alpha=0.5, color='teal')
    ax2.set_xlabel("Principal Component 1")
    ax2.set_ylabel("Principal Component 2")
    st.pyplot(fig2)
