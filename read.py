data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0: # %是用來求跟1000的餘數
			print(len(data)) #印出目前讀到1000倍數的資料
print(len(data)) #印出總共有幾筆資料

#print(data) # 印出一百萬筆資料
print(data[0]) # 印出第一筆的資料內容
print('----------------')
print(data[1])



