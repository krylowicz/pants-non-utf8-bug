from pathlib import Path

import pandas as pd

def increase_salary(df_path: Path) -> pd.DataFrame:
    df = pd.read_csv(df_path, delimiter=",", encoding="utf-8")

    df["salary"] *= 2

    return df


if __name__ == "__main__":
    path = Path("./test_files/utf8.txt")

    df = increase_salary(path)

    print(df)

