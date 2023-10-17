import pandas as pd
import json

df = pd.read_excel(r"C:\Users\HITEN MITTAL\Desktop\iris.xls")

data = df.to_dict()

data_json = json.dumps(data)
print(data_json)
