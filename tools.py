"""
Utility tools for the AI Management Consultant project.

These helper functions are independent from the Streamlit UI
and can be reused by the AI agents when required.
"""

import pandas as pd


def get_numeric_columns(df: pd.DataFrame) -> list:
    """Return the numerical columns from a DataFrame."""
    return df.select_dtypes(include="number").columns.tolist()


def get_categorical_columns(df: pd.DataFrame) -> list:
    """Return the categorical columns from a DataFrame."""
    return df.select_dtypes(exclude="number").columns.tolist()


def dataset_summary(df: pd.DataFrame) -> dict:
    """Return basic information about the uploaded dataset."""
    return {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "missing_values": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
    }


def calculate_basic_metrics(df: pd.DataFrame) -> dict:
    """Calculate basic statistics for numerical columns."""
    numeric_columns = get_numeric_columns(df)

    metrics = {}

    for column in numeric_columns:
        metrics[column] = {
            "total": float(df[column].sum()),
            "average": float(df[column].mean()),
            "highest": float(df[column].max()),
            "lowest": float(df[column].min()),
        }

    return metrics


def detect_outliers(df: pd.DataFrame) -> dict:
    """Detect numerical outliers using the IQR method."""
    numeric_columns = get_numeric_columns(df)
    outliers = {}

    for column in numeric_columns:
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)

        iqr = q3 - q1
        lower_limit = q1 - 1.5 * iqr
        upper_limit = q3 + 1.5 * iqr

        count = int(
            ((df[column] < lower_limit) |
             (df[column] > upper_limit)).sum()
        )

        outliers[column] = {
            "count": count,
            "lower_limit": float(lower_limit),
            "upper_limit": float(upper_limit),
        }

    return outliers