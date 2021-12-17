data = []

count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1	#count = count +1
		if count % 1000 == 0:
			print(len(data))

print('檔案讀取完了, 總共有', len(data), '筆資料')

print(data[0])
print('-----------------------------------')
print(data[4])

sum_len = 0
for d in data:
	sum_len += len(d)	# sum_len = sumn_len + len(d)
	#print(sum_len)

print('平均留言的長度是: ', sum_len/len(data))
