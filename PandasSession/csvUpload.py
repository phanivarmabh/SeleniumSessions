import pandas as pd

'''CSV'''
# df = pd.read_csv("E:\Phani\pandas-master\pokemon_data.csv")
# #print(df)
# # df.head(5)
# # print(df)

'''Excel'''
# df_excel = pd.read_excel("E:\Phani\pandas-master\pokemon_data.xlsx")
# df_excel.head()

'''Text'''
df_text = pd.read_csv("E:\Phani\pandas-master\pokemon_data.txt", delimiter='\t')
#df_text.head()
print(df_text)
