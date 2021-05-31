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
print('第一筆資料: ', data[0])

wc = {}
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1	

# 註解快捷鍵: ctrl + /
# for word in wc:
# 	if wc[word] > 1000:
# 		print(word, wc[word])

while True:
	word = input('請問要查詢的字: ')
	if word == 'q':
		break
	elif word in wc:
		print(word, wc[word], '次')
	else:
		print('該字未包含於文章中！')


