import sqlite3
import pandas as pd

pd.set_option('display.max_columns', None)
path = r"Databases\Matching_Philosophy\Decathlon_matching_philosophy_EN"


def create_sql_database(filename_path):
    ''' Creates sqlite database from Excel file for matching philosophy for Decathlon'''
    con = sqlite3.connect(f"{filename_path}.db")
    df = pd.read_excel(f"{filename_path}.xlsx")

    df.to_sql('Decahtlon_matching_phylosophy', con, index=False, if_exists="replace")
    con.commit()
    con.close()


if __name__ == "__main__":
    create_sql_database(filename_path=path)
