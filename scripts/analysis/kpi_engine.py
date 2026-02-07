
import pandas as pd
import numpy as np
from typing import Optional, List

class KPIEngine:
    """
    Industrial Performance Calculation Engine.
    Handles calculation of thermal efficiency, evaporation rates, and specific consumption.
    """

    REQUIRED_COLUMNS = [
        'debit_acp28pct',  # Input Acid Flow (28%)
        'debit_acp54pct',  # Output Acid Flow (54%)
        'debit_de_la_vapeur_entre_echangeur'  # Steam Flow
    ]

    def __init__(self, data: pd.DataFrame):
        self.df = data.copy()
        self._validate_data()

    def _validate_data(self):
        """Ensures all required columns exist and are numeric."""
        for col in self.REQUIRED_COLUMNS:
            if col not in self.df.columns:
                raise ValueError(f"Missing required column: {col}")
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
        
        # Remove invalid operational data (zero flow)
        self.df = self.df[
            (self.df['debit_acp28pct'] > 0) & 
            (self.df['debit_acp54pct'] > 0) &
            (self.df['debit_de_la_vapeur_entre_echangeur'] > 0)
        ]

    def calculate_all_metrics(self) -> pd.DataFrame:
        """Runs the full suite of KPI calculations."""
        self.df['water_evaporated_tons'] = self.df['debit_acp28pct'] - self.df['debit_acp54pct']
        
        # Filter physical impossibilities (where output > input)
        self.df = self.df[self.df['water_evaporated_tons'] > 0]

        # 1. Concentration Efficiency (Output / Input)
        self.df['concentration_efficiency'] = self.df['debit_acp54pct'] / self.df['debit_acp28pct']

        # 2. Specific Steam Consumption (Steam / Water Evaporated)
        self.df['specific_steam_consumption'] = self.df['debit_de_la_vapeur_entre_echangeur'] / self.df['water_evaporated_tons']

        # 3. Steam Intensity (Steam / Acid Produced)
        self.df['steam_intensity_index'] = self.df['debit_de_la_vapeur_entre_echangeur'] / self.df['debit_acp54pct']

        return self.df

    def aggregate_by_stage(self, stage_col: str = 'echelon') -> pd.DataFrame:
        """Aggregates metrics by production stage (echelon)."""
        if 'water_evaporated_tons' not in self.df.columns:
            self.calculate_all_metrics()

        return self.df.groupby(stage_col)[[
            'concentration_efficiency',
            'water_evaporated_tons',
            'specific_steam_consumption',
            'steam_intensity_index'
        ]].agg(['mean', 'min', 'max', 'std']).round(3)

if __name__ == "__main__":
    # Test execution
    try:
        df = pd.read_excel("Cleaned_Real_Data.xlsx")
        engine = KPIEngine(df)
        results = engine.aggregate_by_stage()
        print("✅ KPI Calculation Successful")
        print(results.head())
    except Exception as e:
        print(f"⚠️ Test bypassed: {e}")
