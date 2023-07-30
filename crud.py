import secrets
import string
import pandas as pd
from pathlib import Path
from database.db_utils import get_connection


def generate_report_id(length: int) -> str:
    characters = string.ascii_letters
    random_str = ''.join(secrets.choice(characters) for _ in range(length))
    return random_str


def trigger_report_gen():
    # TODO
    engine = get_connection()
    new_report_id = generate_report_id(5)


def get_report_df(report_id: str) -> pd.DataFrame:
    data = {
        "Name": ["John", "Alice", "Bob"],
        "Age": [30, 25, 28],
        "City": ["New York", "Los Angeles", "Chicago"]
    }

    # Create a Pandas DataFrame
    df = pd.DataFrame(data)

    return df


def get_csv_file(report_id: str) -> str:
    # getting pd.DataFrame of the report
    report_df = get_report_df(report_id)
    # converting pd.DataFrame to csv and storing in a dir
    filepath = Path(f'./generated_csv/{report_id}.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    report_df.to_csv(filepath)
    # returning the path to csv
    return f'./generated_csv/{report_id}.csv'
