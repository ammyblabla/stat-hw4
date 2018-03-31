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

			for j in range(1,len(res)):
				if data[i][j+1] != '':		
					res[j][region_index] += int(data[i][j+1])

	
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

def problem2():
	revenue_50_58 = csv_reader('revenue_50_58.csv')
	filter_2(revenue_50_58)

def filter3(data):
	res_dict = {}
	for row in data:
		if row == data[0]:
			continue
		elif row[1] not in res_dict:
			res_dict[row[1]] = int(row[5])
		else:
			res_dict[row[1]] += int(row[5])
	res = []
	res.append(['Region', 'Number of vehicles'])
	for key in res_dict:
		res.append([key, res_dict[key]])
	print(res)

def problem3():
	econ2558 = csv_reader('econ2558.csv')
	filter3(econ2558)

def filter_1(data):
	res = []
	title = ['Year']
	for row in data:
		if row == data[0]:
			continue
		if row[1] in title:
			continue
		title.append(row[1])
	# title.remove(title[1])
	# title.append('Average')
	res.append(title)

	for i in range(2,len(data[0])):
		# print(data[0][i])
		# res.append([data[0][i], 100, 200, 300, 400])
		res.append([data[0][i], 0, 0, 0, 0,0])

	# region_counter = [0,0,0,0,0]
	for i in range(0,len(data)):
		if data[i][1] in title:
			region_index = title.index(data[i][1])
			# region_counter[region_index] += 1

			for j in range(1,len(res)):
				if data[i][j+1] != '':		
					res[j][region_index] += int(data[i][j+1])	
	# print(res)
	
	# for i in range(1,len(res)):
	# 	sum_revenues = 0
	# 	for j in range(1,len(res[i])-1):
	# 		print(res[i][j], region_counter[j],sum(region_counter))
	# 	# print(res[i])
	# 		sum_revenues += res[i][j] * region_counter[j]
	# 	res[i][5] = sum_revenues/sum(region_counter)
	# # print(region_counter)
	print(res)

def problem1():
	revenue_50_58 = csv_reader('revenue_50_58.csv')
	filter_1(revenue_50_58)

problem1()
