import pandas as pd
import regex as re

df = pd.read_csv("E:\Phani\pandas-master\pokemon_data.csv")
#Read headers
#print(df.columns)

#print(df)

#Read multiple columns
#print(df[['Name', 'Type 1']])

#Read each row
#print(df.head(5))

#Read specific location
# print(df.iloc[4,2])
# print(df.iloc[3,1])

# for index, row in df.iterrows():
#     print(index, row[['Name', 'Type 1', 'HP']])

#Filter the rows
#print(df.loc[df['Type 1'] == 'Grass'].head(5))

#print(df.loc[(df['Type 1'] == 'Grass') & (df['HP'] > 70)])

#print(df.sort_values(['Type 1', 'HP']))

#print(df.sort_values(['Name', 'Type 1', 'HP']))

#print(df.sort_Values(['Name', 'Type 1'], ascending=[0, 1]))

# df_sort = df.sort_values(['Name', 'Type 1'], ascending=[0, 1])
# print(df_sort)
# print(df.head(3))
# print(df.columns)
# df['Total'] = df['HP']+ df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# print(df)

# df = df.drop(columns=['Total'])
# print(df)

# df['Total'] = df.iloc[:, 4:10].sum(axis=1)
# df = df.head(5)
# print(df)
# df.to_csv('E:\Phani\pandas-master\modified.txt', index=False, sep='\t')

# cols = list(df.columns)
# df = df[cols[0:4] + [cols[12]] + cols[4:12]]
# print(df)
# print(df.columns)

'''Filtering Data'''
# df_filter = df.loc[df['Type 1'] == 'Grass']
# print(df_filter)


# df_filter = df.loc[(df['Type 1'] == 'Grass') & (df['HP'] > 70)]
# print(df_filter)

# df_filter = df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')]
# print(df_filter)

# df = df.loc[df['Name'].str.contains('Mega')]
# print(df)

# df = df.loc[~df['Name'].str.contains('Mega')]
# print(df)

#df = pd.read_csv('E:\Phani\pandas-master\pokemon_data.csv')
# df = df.loc[df['Type 1'].str.contains('Fire | Grass', regex=True)]
# print(df)

# df = df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
# print(df)

'''Conditional Changes'''
#
# df.loc[df['Type 1'] == 'Fire', 'Type 1']='Flamer'
# print(df)

#df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True
#print(df)

# df['Total'] = df.iloc[:, 4:10].sum(axis=1)
#
# df.loc[df['Total']>500, ['Generation','Legendary']]=['Test1','Test2']
# print(df)
#

'''Aggregate Statistics'''

#df = df.groupby(['Type 1']).mean()

#df = df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False)

#df = df.groupby(['Type 1']).sum()

df = df.groupby(['Type 1']).count()
print(df)