import pandas as pd

df = pd.read_excel(r"C:\Myfolder\UTEHY\Python\PythonCoBan\Exerscies\data\12423TN_.xlsx")
df.to_csv("data.txt",sep=",",index=False)
df.to_csv("data2.txt",sep=",",index=True)

