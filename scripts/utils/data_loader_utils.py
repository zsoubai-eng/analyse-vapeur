
import pandas as pd
from typing import Tuple, List

def parse_industrial_headers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handles complex multi-level headers from YOKOGAWA DCS exports.
    Combines row 0 (Equipment/Category) and row 1 (Parameter Name).
    """
    if len(df) < 2:
        return df

    # Detect if we have a multi-row header (usually row 0 has groups like 'Echelon J')
    # If the first row has many empty cells but the second doesn't, it's likely a group header
    top_row = df.iloc[0].fillna("")
    second_row = df.iloc[1].fillna("")

    combined_headers = []
    seen = {}

    for i, (group, label) in enumerate(zip(top_row, second_row)):
        # Synthesize name: "Group - Label"
        name = f"{group} - {label}".strip(" -") if group else label
        
        # Handle empty or duplicate names
        if not name or str(name).lower() in ["nan", ""]:
            name = f"sensor_{i}"
        
        if name in seen:
            seen[name] += 1
            name = f"{name}_{seen[name]}"
        else:
            seen[name] = 0
            
        combined_headers.append(name)

    df.columns = combined_headers
    # Drop the used header rows and reset
    df = df.drop(index=[0, 1]).reset_index(drop=True)
    return df

def load_industrial_excel(file_path: str) -> pd.DataFrame:
    """Loads and auto-parses headers for an Industrial Excel export."""
    df_raw = pd.read_excel(file_path)
    return parse_industrial_headers(df_raw)
