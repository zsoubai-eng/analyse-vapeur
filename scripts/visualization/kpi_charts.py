
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set global style
sns.set_theme(style="whitegrid", context="talk")

def plot_kpi_distribution(df: pd.DataFrame, kpi_col: str, title: str = "KPI Distribution"):
    """
    Plots a histogram distribution for a specific KPI with a Kernel Density Estimate (KDE).
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(df[kpi_col], kde=True, color='teal', edgecolor='black')
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel(kpi_col.replace('_', ' ').title())
    plt.ylabel("Frequency")
    plt.grid(True, linestyle='--', alpha=0.7)
    return plt

def plot_correlation_heatmap(df: pd.DataFrame):
    """
    Generates a correlation heatmap for numerical variables to identify drivers.
    """
    plt.figure(figsize=(12, 10))
    corr = df.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    sns.heatmap(corr, mask=mask, cmap='RdBu_r', center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5},
                annot=True, fmt=".2f")
    
    plt.title("Process Variable Correlation Matrix", fontsize=16)
    return plt