import pandas as pd
df = pd.read_csv('revenue_50_58.csv')
# print(df)
regions = df.Region.unique()
years = df.columns[2::]

res = [['Year']]
for region in regions:
    res[0].append(region)

for year in years:
    revenue_one_year = [year]
    for region in regions:
        revenue_region = df[df.Region==region][year].mean()
        revenue_one_year.append(revenue_region)
    res.append(revenue_one_year)
print(res)
