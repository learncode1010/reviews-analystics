data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count +1
		if count % 100000 == 0:
			print('目前讀入筆數: ', len(data))
print('總共有', len(data), '筆資料')


