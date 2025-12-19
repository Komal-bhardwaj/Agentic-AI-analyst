def generate_insights(df):
    insights = []

    if df.isnull().sum().sum() > 0:
        insights.append("Dataset contains missing values. Data cleaning is required.")

    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) > 1:
        insights.append("Multiple numerical columns detected. Correlation analysis recommended.")

    if df.shape[0] > 1000:
        insights.append("Large dataset detected. Sampling or optimization may be needed.")

    return insights
