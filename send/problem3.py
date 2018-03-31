import pandas as pd
df = pd.read_csv('econ2558.csv')
# print(df)
regions = df.Region.unique()
res = [['Region', 'Number of Vehicles']]
for region in regions:
    one_region = df[df.Region == region].NumVehicles
    # print(one_region)
    sum_vehicle_region = one_region.sum()
    # print(sum_vehicle_region)
    res.append([region, sum_vehicle_region])
print(res)