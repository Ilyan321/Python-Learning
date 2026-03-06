import pandas as pd
# Series
# series=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
# print(series)

# # DataFrame
# df=pd.DataFrame({"Name":["Ilyan","Klaus","Elijah"],"age":[25,30,35]})
# print(df)

csv=pd.read_csv("tasks.csv")
# print(csv)
# print(csv.head())
# print(csv.tail())
# print(csv.info())
# print(csv["Task_ID"])
print(csv.iloc[0])