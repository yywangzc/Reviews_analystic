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




