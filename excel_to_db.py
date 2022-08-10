import sqlite3
import pandas as pd

path = r"Databases\Matching_Philosophy\Decathlon_matching_philosophy_EN"


def create_sql_database(filename_path):
    ''' Creates sqlite database from Excel file for matching philosophy for Decathlon'''
    con = sqlite3.connect(f"{filename_path}.db")
    wb = pd.ExcelFile(filename_path + '.xlsx')
    for sheet in wb.sheet_names:
        df = pd.read_excel(filename_path + '.xlsx', sheet_name=sheet)
        df.to_sql(sheet, con, index=False, if_exists="replace")
        print(f"Adding {sheet} to database.")
    con.commit()
    con.close()


if __name__ == "__main__":
    create_sql_database(filename_path=path)
