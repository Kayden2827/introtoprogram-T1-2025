#loop control practice

for i in range (21):
    if i == 15:
        break
    print (i)

for i in range(30):
    if i % 2 == 0:
        continue
    print (i)
    




for i in range (10, 1, -1):
    if i == 5:
        continue
    print (i)


add = [1,2,3,4,5,-6,7,8,9,-10]
sum = 0
for n in add:
    if n < 0:
        break
    sum += n
print (sum)