data = []
count = 0
sum_len = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
for d in data:
	sum_len += len(d)
print('總字數:', sum_len)
print('平均字數:', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '數小於100')
print(new[0])
print(data[3])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '留言包含good')
print(good[0])