
import streamlit as st
import pandas as pd
from scripts.cleaning.data_cleaner import DataSanitizer
from scripts.utils.data_loader_utils import parse_industrial_headers

st.set_page_config(page_title="Data Processing", page_icon="🧼", layout="wide")

st.title("🧼 Phase 1: Data Ingestion & Sanitation")
st.markdown("---")

uploaded_file = st.file_uploader("📂 Upload Raw Excel (DCS Export)", type=["xlsx"])

if uploaded_file:
    # Ingestion
    raw_df = pd.read_excel(uploaded_file)
    st.info(f"Loaded raw file: {raw_df.shape[0]} rows x {raw_df.shape[1]} columns")
    
    # 1. Header Parsing
    with st.status("Parsing complex headers...", expanded=True) as status:
        parsed_df = parse_industrial_headers(raw_df)
        status.update(label="Headers parsed successfully!", state="complete", expanded=False)
    
    # 2. Smart Cleaning
    sanitizer = DataSanitizer(parsed_df)
    cleaned_df = sanitizer.clean()
    metadata = sanitizer.get_metadata()
    
    st.success(f"✅ Sanitation Complete: {len(cleaned_df)} operational rows remaining.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Cleaned Dataset Preview**")
        st.dataframe(cleaned_df.head(100), use_container_width=True)
    
    with col2:
        st.markdown("**Fuzzy Role Detection**")
        meta_df = pd.DataFrame.from_dict(metadata, orient='index')
        st.dataframe(meta_df, use_container_width=True)
        
    st.session_state['data'] = cleaned_df
    st.session_state['metadata'] = metadata

else:
    st.warning("Please upload a file to begin.")
