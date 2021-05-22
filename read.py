data = []
count = 0
with open('reviews.txt', 'r') as f:
	print('開始讀入資料...')
	for line in f:
		data.append(line)
		count = count +1
		if count % 100000 == 0:
			print( len(data))
print('總共讀入', len(data), '筆資料')


