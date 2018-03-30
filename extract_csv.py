import csv


def csv_reader(filename):
	data = []
	with open(filename) as f:
		reader = csv.reader(f, delimiter=',')
		# print(reader)
		for row in reader:
			for i in range(len(row)):
				row[i] = row[i].strip()
			data.append(row)
			# print(row, end=',\n')
	return data

def filter_2(data):
	res = []
	title = ['Year']
	for row in data:
		if row == data[0]:
			continue
		if row[1] in title:
			continue
		title.append(row[1])
	title.remove(title[1])
	title.append('Average')
	res.append(title)

	for i in range(2,len(data[0])):
		# print(data[0][i])
		# res.append([data[0][i], 100, 200, 300, 400])
		res.append([data[0][i], 0, 0, 0, 0,0])

	region_counter = [0,0,0,0,0]
	for i in range(1,len(data)):
		if data[i][1] in title:
			region_index = title.index(data[i][1])
			region_counter[region_index] += 1
			# print(region_index,title[region_index])
			# print(data[i])
			for j in range(1,len(res)):
				# # year = res[j][region_index]
				# revenue = data[i][j+1]
				if data[i][j+1] != '':
					# print(res[j][region_index], data[i][j+1])
					res[j][region_index] += int(data[i][j+1])
				# print(revenue)
				# print(data[i], res[index])
	
	print(res)
	
	for i in range(1,len(res)):
		sum_revenues = 0
		for j in range(1,len(res[i])-1):
			print(res[i][j], region_counter[j],sum(region_counter))
		# print(res[i])
			sum_revenues += res[i][j] * region_counter[j]
		res[i][5] = sum_revenues/sum(region_counter)
	# print(region_counter)
	print(res)

revenue_50_58 = csv_reader('revenue_50_58.csv')
filter_2(revenue_50_58)