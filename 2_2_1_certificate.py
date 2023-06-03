# pip install pandas
import pandas as pd

df = pd.DataFrame(
    [
        ["김일남", "1950.01.01", "2023-001"],
        ["김이남", "1951.01.01", "2023-001"],
        ["김삼남", "1952.01.01", "2023-001"],
        ["김사남", "1953.01.01", "2023-001"],
        ["김오남", "1954.01.01", "2023-001"],
    ]
)

print(df.values.tolist())


# pip install openpyxl 해야 함
# df.to_excel('certificate.xlsx', index=False, header=False)
