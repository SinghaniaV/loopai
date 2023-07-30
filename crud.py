import secrets
import string
from fastapi import Response
from asyncio import Event, sleep
import pandas as pd
from pathlib import Path
from database.db_utils import get_connection


def generate_randon_report_id(length: int) -> str:
    characters = string.ascii_letters
    random_str = ''.join(secrets.choice(characters) for _ in range(length))
    return random_str


async def trigger_report_gen(new_report_id: str, status_event: Event) -> None:
    # TODO
    engine = get_connection()
    await sleep(30)
    status_event.set()


def generate_report_csv(report_id: str) -> None:
    """
    search for the report_id in database and if found create a {report_id}.csv file else return.
    :param report_id: str
    :return: None
    """
    data = {
        "Name": ["John", "Alice", "Bob"],
        "Age": [30, 25, 28],
        "City": ["New York", "Los Angeles", "Chicago"]
    }

    # Create a Pandas DataFrame
    report_df = pd.DataFrame(data)
    filepath = Path(f'./generated_csv/{report_id}.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    report_df.to_csv(filepath)
