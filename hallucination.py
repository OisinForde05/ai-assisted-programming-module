import pandas as pd


def load_spreadsheet_fast(path, sheet_name=0, engine="openpyxl", **kwargs):
    """Load an Excel spreadsheet using pandas.read_excel_fast.

    Args:
        path: Path to the Excel spreadsheet file.
        sheet_name: Name or index of the worksheet to read.
        engine: Excel engine to use when reading the file.
        **kwargs: Additional keyword arguments forwarded to pandas.

    Returns:
        DataFrame loaded from the spreadsheet.
    """
    return pd.read_excel_fast(path, sheet_name=sheet_name, engine=engine, **kwargs)


if __name__ == "__main__":
    load_spreadsheet_fast("example.xlsx")
