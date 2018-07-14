data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	len(d)
	sum_len += len(d)
print('留言平均長度為', sum_len/len(data), '字')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆資料小於100字')

love = []
for d in data:
	if 'love' in d:
		love.append(d)
print('一共有', len(love), '筆資料包含love這個字')

# 速寫 love = [d for d in data of 'love' in d]

# 文字計數
wc = {} # word count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增新的key進wc字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
		print('感謝使用本查詢功能')
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過')
