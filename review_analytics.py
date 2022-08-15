#清單讀取、
data = []
count = 0
sum_len = 0
with open('reviews.txt', 'r') as p:
	for line in p:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print(data[0])


#程式加總
for d in data:
	sum_len += len(d)
print('總字數:', sum_len)
print('平均字數:', sum_len / len(data))#

#篩選法
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '數小於100')
print(new[0])
print(data[3])#

good = [] 
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '留言包含good')
print(good[0])#

# 篩選快速法
good = [d for d in data if 'good' in d]




#程式計數
wc = {}
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] +=1
		else:
			wc[word] = 1 
for word in wc:
	if wc[word] > 10000:
		print(word, wc[word])
print(len(wc))
while True:
	word = input('輸入想搜尋的字')
	if word == 'q':
		print('感謝查詢')
		break
	elif word not in wc:
		print('文字沒有出現過')
	else:
		print(word, '一共出現', wc[word], '次')











 