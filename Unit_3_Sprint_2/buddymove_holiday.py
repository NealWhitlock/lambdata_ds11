import numpy as np
import pandas as pd
import sqlite3

url = 'https://raw.githubusercontent.com/NealWhitlock/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv'

df = pd.read_csv(url)
df.head()