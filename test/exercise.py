# 列出1,2,3,4四个数字组成的互不相同的3位数,并进行倒序排序
listSort = []
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if (a !=b) and (a !=c ) and (b !=c):
                listSort.append(a*100+b*10+c)
print(listSort[::-1])

# 平方根
import math
a = 3 **2
print(f'开平方为:{math.sqrt(a)}')

# 生成一个随机数
import random
a = random.choice(range(10000))
print(a)

# 判断字符串是否为数字
import re
a = '123'
reg = r'\d'
if re.match(reg, a):
    print('是数字')
else:
    print('不是数字')

# 移除字符串中指定位置字符
a = 'hello world'
print(a[:2] + a[3:])
