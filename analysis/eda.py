import pandas as pd

def basic_eda(df):
    summary = {
        "shape": df.shape,
        "columns": list(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "data_types": df.dtypes.astype(str).to_dict(),
        "describe": df.describe().to_dict()
    }
    return summary
