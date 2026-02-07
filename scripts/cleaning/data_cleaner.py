
import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from typing import Dict, Any

class DataSanitizer:
    """
    Advanced Industrial Data Sanitizer.
    Combines fuzzy role detection, semantic null handling, and IQR outlier removal.
    """

    SEMANTIC_NULLS = [
        "no data", "n/a", "null", "none", "--", "-", "missing", "vide",
        "pas de données", "indisponible", "indispo", ""
    ]

    def __init__(self, raw_data: pd.DataFrame):
        self.df = raw_data.copy()
        self.metadata = {}

    def clean(self, threshold: float = 0.7) -> pd.DataFrame:
        """
        Executes the intelligent cleaning pipeline.
        Threshold: Keep rows with at least X% non-NA values.
        """
        self._normalize_semantic_nulls()
        self._standardize_column_names()
        self._handle_missing_values(threshold)
        self._detect_column_roles()
        self._remove_outliers_iqr()
        return self.df

    def _normalize_semantic_nulls(self):
        """Replaces common industrial null strings with np.nan."""
        self.df = self.df.applymap(
            lambda x: np.nan if isinstance(x, str) and x.strip().lower() in self.SEMANTIC_NULLS else x
        )

    def _standardize_column_names(self):
        """Standardizes column names and converts to numeric where possible."""
        self.df.columns = [str(c).lower().strip().replace(' ', '_') for c in self.df.columns]
        self.df = self.df.apply(lambda col: pd.to_numeric(col, errors='ignore'))

    def _handle_missing_values(self, threshold: float):
        """Forward-fills operational data and drops heavily empty rows."""
        self.df.fillna(method='ffill', limit=5, inplace=True)
        # Drop rows that are too empty
        limit = int(threshold * self.df.shape[1])
        self.df.dropna(thresh=limit, inplace=True)

    def _detect_column_roles(self):
        """Uses fuzzy matching to identify column roles (Temperature, Flow, etc.)."""
        for col in self.df.columns:
            name = col.lower()
            role = "unknown"
            
            if fuzz.partial_ratio(name, "température") > 80 or "temp" in name:
                role = "temperature"
            elif fuzz.partial_ratio(name, "débit") > 80 or "flow" in name:
                role = "flow"
            elif "pression" in name or "pressure" in name:
                role = "pressure"
            elif "timestamp" in name or "date" in name or "heure" in name:
                role = "timestamp"
            
            self.metadata[col] = {"role": role, "dtype": str(self.df[col].dtype)}

    def _remove_outliers_iqr(self):
        """Removes statistical outliers using the Interquartile Range (IQR) method."""
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            self.df = self.df[~((self.df[col] < (Q1 - 1.5 * IQR)) | (self.df[col] > (Q3 + 1.5 * IQR)))]

    def get_metadata(self) -> Dict[str, Any]:
        return self.metadata

if __name__ == "__main__":
    print("Intelligent Data Sanitizer Loaded")
