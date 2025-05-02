# pip install pandas
import pandas as pd

data = [
        ["김일남", "1951.01.01", "2025-001"],
        ["김이남", "1952.02.01", "2025-002"],
        ["김삼남", "1953.03.01", "2025-003"],
        ["김사남", "1954.04.01", "2025-004"],
        ["김오남", "1955.05.01", "2025-005"]
    ]

df = pd.DataFrame(data)

print(df.values.tolist())

# pip install openpyxl 해야 함
df.to_excel('certificate.xlsx', index=False, header=False)
