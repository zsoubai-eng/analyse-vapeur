# 🏭 Industrial Steam Optimization - OCP Phosphate Plant

> **Intelligent Assistant for Steam Consumption Optimization in Phosphoric Acid Production**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-Academic-green.svg)]()

## 📊 Project Overview

This project is a **full-stack industrial analytics platform** designed to optimize specific steam consumption (CSV) in the phosphoric acid concentration unit (CAP) at OCP Group. It features a **Streamlit-based dashboard** for real-time data visualization, statistical analysis, and machine learning insights.

### Business Impact
- **Estimated Annual Savings:** 5.39M MAD (~$540K USD)
- **Optimization Target:** 10% reduction in specific steam consumption
- **Technology:** Python, Streamlit, Scikit-learn, DMAIC Methodology

---

## 🛠️ System Architecture

The project is structured as a modular application with a Streamlit frontend and specialized backend scripts for analysis.

```
analyse-vapeur/
├── app.py                     # 🖥️ Main Streamlit Dashboard (Entry Point)
├── requirements.txt           # Dependency management
├── README.md                  # Documentation
│
├── scripts/                   # 🧩 Modular Logic
│   ├── analysis/
│   │   ├── kpi_engine.py      # Core KPI calculation logic
│   │   ├── pca_analysis.py    # Dimensionality reduction
│   │   ├── kmeans_clustering.py # Operating regime detection
│   │   └── ...
│   ├── cleaning/
│   │   ├── data_cleaner.py    # Raw data processing pipeline
│   │   └── ...
│   ├── visualization/
│   │   ├── kpi_charts.py      # Matplotlib/Seaborn plotters
│   │   └── ...
│   └── utils/
│       └── data_loader_utils.py
```

---

## 🚀 Features

### 1. **Interactive Dashboard (`app.py`)**
- Secure login for supervisors ("Encadrant" access)
- Step-by-step analysis workflow:
  1. Data Loading & Cleaning
  2. Exploratory Data Analysis (EDA)
  3. Correlation Matrix
  4. PCA (Principal Component Analysis)
  5. K-Means Clustering for Regime Detection

### 2. **KPI Engine (`scripts/analysis/kpi_engine.py`)**
Calculates critical industrial metrics:
- **Concentration Efficiency:** Output/Input acid ratio
- **Specific Steam Consumption:** Tons of steam per ton of evaporated water
- **Evaporation Rate:** Real-time water removal tracking

### 3. **Machine Learning Modules**
- **PCA:** Reduces dimensionality of 50+ sensor variables to identify primary variance drivers.
- **K-Means:** Clusters operating conditions to find "Optimal Zones" vs. "Inefficient Zones."

---

## 📈 Visualizations

### Dashboard Interface
The application provides interactive charts for:
- Frequency distribution of key variables
- Correlation heatmaps of process parameters
- Adaptive control charts for temperature monitoring

![Correlation Analysis](consommation_specifique%20_de_la_vapeur%20vs.%20Critical%20Parameters.png)

---

## 🔬 Methodology

This tool supports the **DMAIC** continuous improvement cycle:
- **Define:** Dashboard tracks the 10% reduction goal.
- **Measure:** Ingests raw Excel exports from YOKOGAWA DCS.
- **Analyze:** Auto-generates PCA and Correlation insights.
- **Improve:** Suggests optimal operating ranges based on clustering.
- **Control:** Monitors deviations in real-time.

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/zsoubai-eng/analyse-vapeur.git
cd analyse-vapeur

# Install dependencies
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

*Note: Requires proprietary OCP data files (Cleaned_Real_Data.xlsx) to function fully. The code is provided for portfolio demonstration.*

---

## 👤 Author

**Zakaria Soubai**  
Industrial Engineer | AI Builder  
[LinkedIn](https://linkedin.com/in/zakaria-soubai) | [GitHub](https://github.com/zsoubai-eng)

---

## 🙏 Acknowledgments

- **Partner:** OCP Group (Kofert)
- **Academic Supervisor:** Prof. Issam AMELLAL
- **Industrial Supervisor:** M. [Adding Name...]
