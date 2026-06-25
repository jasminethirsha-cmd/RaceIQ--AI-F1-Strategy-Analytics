"""
database.py
-------------
Handles all database connections and data loading
for the RaceIQ application.
"""

import pandas as pd
from sqlalchemy import create_engine

# SQLite Database Connection
engine = create_engine("sqlite:///raceiq.db")


def load_table(table_name):
    """
    Load any table from the SQLite database.

    Parameters:
        table_name (str): Name of the table

    Returns:
        pandas.DataFrame
    """

    query = f"SELECT * FROM {table_name}"
    return pd.read_sql(query, engine)


def load_races():
    """Load races table"""
    return load_table("races")


def load_results():
    """Load race results table"""
    return load_table("results")


def load_qualifying():
    """Load qualifying table"""
    return load_table("qualifying")


def load_driver_standings():
    """Load driver standings"""
    return load_table("driver_standings")


def load_constructor_standings():
    """Load constructor standings"""
    return load_table("constructor_standings")