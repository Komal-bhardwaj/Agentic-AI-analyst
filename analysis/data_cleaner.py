import pandas as pd

def refine_csv(
    df: pd.DataFrame,
    strategy: str = "mean",
    drop_columns: list = None,
    encode: bool = False
):
    """
    Cleans and refines the dataframe:
    - Fills missing values (mean / median / mode)
    - Drops unnecessary columns
    - Encodes categorical columns if requested
    """

    df = df.copy()

    # 🔹 Drop unnecessary columns
    if drop_columns:
        df.drop(columns=drop_columns, inplace=True, errors="ignore")

    # 🔹 Fill missing values
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype in ["int64", "float64"]:
                if strategy == "mean":
                    df[col].fillna(df[col].mean(), inplace=True)
                elif strategy == "median":
                    df[col].fillna(df[col].median(), inplace=True)
            else:
                df[col].fillna(df[col].mode()[0], inplace=True)

    # 🔹 Encode categorical columns
    if encode:
        df = pd.get_dummies(df, drop_first=True)

    return df
