import pandas as pd
import matplotlib.pyplot as plt

data = [["Bob", 54], ["Alex", 35], ["Eric", 72]]
df = pd.DataFrame(data, columns=["Name", "Age"])
print(df)