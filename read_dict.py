data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0: # %是用來求跟1000的餘數
			print(len(data)) #印出目前讀到1000倍數的資料
print('檔案讀取完了, 總共有', len(data), '筆資料') #印出總共有幾筆資料

#print(data) # 印出一百萬筆資料
#print(data[0]) # 印出第一筆的資料內容
#print('----------------')
#print(data[1])


sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
#	print(sum_len) # 可以印出總共有多少字數

print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '留言提到 good')
print(good[0])

# list comprehension 清單快寫法

#good = [d for d in data if 'good' in d] # 第一個d可換成1,表示不印出留言內容
#print(good)

# output = [(number-1) for number in reference if number % 2 == 0]
#              運算          變數        清單          篩選條件


#bad = ['bad' in d for d in data]
#print(bad)

bad = []
for d in data:
	bad.append('bad'in d)
print(bad)


print(data[0])


# 文字計數
wc = {} # word_count
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

print(len(wc))
print(wc['Andy'])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:	
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔!')

print('感謝使用本查詢功能')






