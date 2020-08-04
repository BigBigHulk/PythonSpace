''''''''''''''''数字'''''''''''''''''''''
# 1.删除语句del
var1 = 1
#del var1
print(var1)

# 2.十进制输出
var1 = 0x0a
print(var1)
var1 = 0o37
print(var1)
var1 = 0b1111
print(var1) 

# 3.强制转换
a = '3'
print(int(a))
print(float(a))
print(complex(a))
print(bool(a))
a = 3.1
print(int(a))
print(float(a))
print(complex(a))
print(bool(a))

# 4.数字运算
print(4 + 3)
print(4.0 + 3)
print(4 * 3)
print(4 / 3)
print(4 // 3)
print(4.0 // 3)
print(4 // 3.0)
print(4 % 3)
print(4 ** 3.0)

# 5.数学函数
print(abs(-1.0)) # 绝对值

import math
print(math.ceil(1.1))   # 上入整数
print(math.floor(2.1))  # 下舍整数
print(math.exp(2))      # e的2次幂
print(math.fabs(-10))   # 浮点类型的绝对值
print(math.log(math.e)) # log函数
print(math.log10(100))  # log10函数
print(max(1,2,3))
print(min(1,2,3))
print(math.modf(-1.5))  # 整数部分与小数部分分离,返回浮点类型,小数位在前
print(pow(2, 3))        # 2的3次方
print(round(2.5))
print(round(1.5))       # 四舍五入,奇进偶舍
print(math.sqrt(4))     # 平方根,返回值为浮点类型

# 6. 三角函数

# 7. 随机数函数
import random
print(random.choice([1,2,3]))
print(random.choices([1,2,3]))
print(random.randrange(2, 10, 2)) # 2到10随机选取一个偶数
print(random.random()) # 生成一个[0,1)之间的随机数
#random.seed(10) # 重设随机数种子之后形成的随机数都是固定的
print(random.random())
print(random.random())
a = [1,2,3,4,5]
random.shuffle(a) # 列表中的值随机排列
print(a)

''''''''''''''''字符串'''''''''''''''''''''
# 1.字符串截取,替换
a = 'hello'
b = 'word'
print(a[0])
print(a[:])
print(a[:3])
print(a[1:])
print(a[1:3])
print(a[0:-1])
print(a + ' ' + b)
c = a + ' ' + b
print(c[:6] + 'didi')

# 2.字符串转义
print('hello\
    a')             # 续行符
print('hello\\')    # \字符
print('hello\'')
print('hello\"')
print('hello\a')    # 响铃符号

# 3.字符串运算
a = 'hello'
print('hello' + 'word')
print('hello' * 2)
print('h' in a)
print('h' not in a)
print(r'hello\\')   # 输出原字符串
print(R'hello\\')   # 输出原字符串
print('he%so' %('ll'))

# 4.字符串3引号,所见即所得
print('''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
''')

# 5.f-string
b = 'word'
c = 'didi'
print(f'hello {b}')
print(f'{1 + 1}')
print(f'{1 + 1 = }')

''''''''''''''''列表'''''''''''''''''''''
# 1.列表操作
a = ['Google', 'Runoob', 1997, 2000]
print(a[2])
print(a[:2])

a[2] = 2020             # 更新列表中的元素
print(a)

del a[2]                # 删除列中的元素
print(a)

print(len(a))           # 获取列表中元素的个数

print('Google' in a)    # 元素是否在列表中

# 2.迭代
a = ['Google', 'Runoob', 1997, 2000]
for x in a:
    print(x, end=' ')

# 3.嵌套
a = ['Google', 'Runoob', 1997, 2000, [1, 2, 3]]
print(a[4][0])

# 4.列表函数
a = [1, 2, 3, 4]
print(max(a))
print(min(a))
print(len(a))
b = (5,4,3,2,1)
print(b)
print(list(b))                  # 将元组转换成列表

a = [1, 2, 3, 4, 4]
a.append(5)                     # 在尾部添加元素
print(a)
print(a.count(4))               # 统计4在列表中出现的次数
b = ['hello','word']
a.extend(b)                     # 列表合并
print(a)
print(a.index(4))               # 返回列表中第一次出现4的位置
a.insert(4, 5)                  # 将数字5插入列表中的第五个位置
print(a)
a.pop(4); print(a)              # 移除列表中的元素,参数缺省默认移除最后一个
a.remove(4); print(a)           # 移除列表中第一个4
a.remove('hello'); print(a)
a.remove('word'); print(a)
a.reverse(); print(a)           # 翻转列表
a.sort(); print(a)              # 列表排序
c = a; print(c)                 # 复制列表
d = a.copy(); print(d)                    
a.clear(); print(a)             # 清空列表

''''''''''''''''元组'''''''''''''''''''''
a = (1, 2, 3, 4, 'hello', 'word')
b = 'ha', 'ha', 'ha'; print(type(b))            # 元组初始化可以不用加括号
c = ('name',);print(type(c))                    # 元组中只有一个元素的时候需要在元素后面加","
c = ('name');print(type(c))
print(a[2])
print(a[:3])
print(a + b)
del b                                           # 删除元组
b = ('ha',) * 4; print(b)                       # 元组复制
b = [1, 2, 3]; print(tuple(b))                  # 列表转换成元组

''''''''''''''''字典'''''''''''''''''''''
a = {'name':'Tony', 'age':25, 'sexy': 'man'}
print(a['name'])
a['name'] = 'Thor'
print(a['name'])
del a['sexy']; print(a)                    # 根据key删除字典中的一项

# 1.字典函数
a = {'name':'Tony', 'age':25, 'sexy': 'man'}
b = a.fromkeys([1,2,3], 10)                # 新建字典,key为第一个参数中的元素,val为第二个参数,若缺省第二个参数则val默认为None
print(b)
print(a.get('name'))                        # 获取key对应的val,若key值不存在则返回None
print('name' in a)                          # 如果key在字典中则返回True
print(a.items())                            # 返回键值对元组列表

for i,j in a.items():                       # 可以利用items函数打印键值对
    print(i,':\t',j)                        

print(list(a.keys()))                       # 返回字典的key,可用list()函数转换成列表
print(a.values())                           # 返回字典的val,可用list()函数转换成列表
print(a.setdefault('name'))                 # 和get函数相同,但是如果key不在字典中则将其添加至字典并设置val为None

a.update(b)                                 # 将字典b添加到字典a中
print(a)

print(a.pop('name'))                        # 移除并返回Key对应的val
print(a.pop('job','nokey'))                 # 如果所移除的key不存在于该字典中,则需要在使用pop函数的时候需要补充第二个参数为val,否则报错
print(a)
print(a.popitem(), a)                       # 返回并删除字典中最后一对键值对

a.clear()                                   # 清空字典,字典变成空,但是仍然存在,区别于del

# 2. 深拷贝和浅拷贝的区别
import copy
a = {'name':'Tony', 'age':25, 'num':[1,2,3]}
b = a.copy()                        # 等同于copy.copy,更新子元素
c = a                               # 原字典变成啥,这个就是啥
d = copy.deepcopy(a)                # 深拷贝,和原字典没有关系
e = copy.copy(a)                    # 一级元素不变,更新子元素

a['name'] = 'Thor'
a['num'].append(4)

print('原字典为:', a)
print('字典拷贝后为:', b)
print('=拷贝后为:', c)
print('深拷贝后为:', d)
print('浅拷贝后为:', e)

''''''''''''''''集合'''''''''''''''''''''
# 集合是一个无序不重复的元素序列

# 1.集合的初始化方式,如果需要创建一个空集合必须使用set函数
a = set()
a = {'a', 'b', 'c'}
a = set('abca')                         # 有重复元素自动剔除
a = set(('apple'));print(a)             # 二者的区别在于a是将字符拆分创建,b是整体作为一个元素创建
b = set(('apple',));print(b)

# 2.集合运算
a = {'a', 'b', 'c'}
b = {1, 2, 3, 'a'}
print(a - b)            # 取a有b没有的集合
print(a | b)            # 取a和b的总集,不支持加法运算
print(a ^ b)            # 取a和b交集意外的集合
print(a & b)            # 取a和b的交集

# 3.集合推导式
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# 4.集合函数
a = set('abcaf')
b = set('123a')
print(a.issubset(b))                    # 判断a是否是b的子集
print(a.issuperset(b))                  # 判断b是否是a的子集
print(a.isdisjoint(b))                  # 判断两个集合是否有相同元素,如果有返回False
print(a.difference(b))                  # 返回值等同于 a-b
print(a.difference_update(b),a)         # 等同于 a-b
print(a.intersection(b))                # 返回值等同于 a&b
print(a.intersection_update(b))         # 等同于a&b
print(a.symmetric_difference(b))        # 返回值等同于 a^b
print(a.symmetric_difference_update(b)) # 等同于 a^b
print(a.union(b))                       # 返回值等同于a|b
a.add('d');print(a)                     # 添加元素至集合中,如果集合中已经有该元素则不进行任何操作
a.update([1,2,3]);print(a)              # 添加元素至集合中,可以是列表,元组,字典等,可以添加多个,用逗号隔开,如果没有各种括号的话则全添加
a.update([1,2,3],(4,5));print(a)    
a.remove('a');print(a)                  # 移除集合中的元素,如果元素不存在则报错
a.discard('e');print(a)                 # 移除集合中的元素,如果元素不存在不会报错
print(a.pop(), a)                       # 随机删除集合中的元素并返回删除的值
print(len(a))                           # 计算集合中元素个数
print('b' in a)                         # 判断元素是否存在于集合中

''''''''''''''''条件控制&循环语句'''''''''''''''''''''
control = input('玩不玩Y/N')
count = 0
userInfo = {'Tony':'123', 'Thor':'321', 'Hulk':'hahaha'}

if control != 'Y' and control != 'y':
    control = input('试一次嘛,很好玩的N/Y')
    if control != 'Y' and control != 'y':
        print('那你下次来记得试一下哦')
        exit()
account = input('请输入游戏账号')
if account in userInfo.keys():
    passwd = input('请输入密码')
    print(f'userInfo[{account}] is {userInfo[account]}')
    print(f'passwd is {passwd}')
    if userInfo[account] == passwd:
        print('登录成功,游戏开始')
    else:
        print('密码错误,游戏结束')
        exit()
else:
    print('用户不存在,游戏结束')
    exit()

while control == 'Y'or control == 'y':
    count = count + 1
    try:
        age = int(input('请输入狗狗的年龄:'))
        if age < 1:
            print('你在逗我')
        elif age == 1:
            print('狗狗的年龄相当于人类的14岁')
        elif age == 2:
            print('狗狗的年龄相当于人类的22岁')
        else:
            print(f'狗狗的年龄详单与人类的{22 + (age - 2)*5}岁')
    except ValueError:
            print('请输入合法的年龄')
    if count < 2:
        control = input('是否继续N/Y?')
    else:
        control = input('再玩一次可以获得累计奖励哦,是否继续N/Y')
    if control != 'Y' and control != 'y':
        print('游戏结束,欢迎下次再来')
        break
    else:
        continue
else:
    pass
input('输入Enteger结束游戏')

''''''''''''''''迭代器&生成器'''''''''''''''''''''
# 1.迭代器创建使用
a = [1,2,3,4]
b = iter(a)         # 利用iter函数创建迭代器对象
print(next(b))      # 通过next函数获取迭代器的下一个值
print(next(b))
for x in b:         # 通过for循环也可以遍历迭代器,但是是从当前位置开始
    print(x, end=' ')

 # 2.创建类的迭代器
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

count = MyNumbers()
myIter = iter(count)
for x in myIter:
    print(x)

# 3.生成器yield
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print (next(f), end=" ")
    except :
        exit()

''''''''''''''''函数'''''''''''''''''''''
# 1. 函数创建
def myprint(text):
    print(text)
# 2.函数调用
myprint('hello')

# 3. 函数可变参数&不可变参数
def myFun(a):       # 传递不可变参数则只在函数内部改变值,类似于c++的传值
    a = 10
    print(a)
a = 2
myFun(a)
print(a)

def myAppend(a):    # 传递可变参数则改变其值,类似于c++的传址
    a.append([4,5,6])
    print(a)
a = [1,2,3]
myAppend(a)
print(a)

# 4.函数参数类型
# 必须参数,调用时不传参数或者参数数量不匹配会报错
def myFun1(a):
    print(a)

# 关键字参数,调用时不需要关注参数的位置
def myFun2(name,age):
    print(name,age)
myFun2(age = 26, name = 'Tony')

# 默认参数,调用时如果不填写,则默认使用缺省值,填写则覆盖缺省值
def myFun3(name, age = 26):
    print(name,age)
myFun3('Tony')  
myFun3(age = 27, name = 'Thor')

# 不定长参数
def myFun4(name, *argv):                # *表示后面的参数为不定长的元组,不填写则为空
    print(name)
    print(argv)
myFun4('Tony','1',2,3,'hello')
myFun4('Tony')

def myFun5(name, **argv):               # **表示以字典的形式导入不定长参数
    print(name)
    print(argv)
myFun5('Tony')
myFun5('Tony',Thor = 27, Hulk = 28)

def myFun6(a,b,*,c):                    # *可以单独作为参数传入,但是*之后的参数必须使用关键字参数进行传递
    print(a,b,c)
myFun6(1,2,c = 3)

# 强制位置参数
def myFun7(a,b,/,c,*,d,e):              # /之前的参数必须使用位置参数,使用关键字参数会报错
    print(a, b, c, d, e)
myFun7(1,2,3,d = 4, e = 5)

# 5.匿名函数,Python使用lambda来表示匿名函数,匿名函数无法调用其参数列表之外以及全局变量
mySum = lambda a, b : a + b
print(mySum(3, 4))
print(mySum(a = 3, b = 4))

# 6. 函数装饰器
def zhuangshi(func):
    def Temp(a):
        print(f'{func.__name__} is running')
        return func(a)
    return Temp
@zhuangshi
def myFun8(a):
    print(a)
myFun8('hello')

''''''''''''''''数据结构'''''''''''''''''''''
# 列表作为堆栈使用(后进先出)
a = [1,2,3]
a.append(4)
a.append(5)
print(a)
a.pop()
print(a)

# 列表作为队列使用(后进后出)
a = [1,2,3]
a.append(4)
a.append(5)
print(a)
a.pop(0)
print(a)

# 输入输出
print()
input()
print('%5.4f'% 333.1415) # 5.4中的5表示占位符,.4表示保留小数点后4位

name = 'Tony'
age = 26
print('name is %s, age is %d' % (name, age))
print('name is {}, age is {}'.format(name, age))
print(f'name is {name}, age is {age}')

''''''''''''''''文件'''''''''''''''''''''
a = open('C:/Users/duchaobo/Desktop/test.txt','a+',encoding = 'UTF-8')     # 文件打开并写入字符串,windows环境下需要用/分割路径,a+表示追加读写,w+表示从头
a.write('hello\n哈哈哈')
print(a.tell())                                         # 返回文件指针当前的位置
a.writelines('\nqqq\nwwww')                             # 多行写入
a.flush()                                               # 刷新并清空缓冲区
a.close()
b = open('C:/Users/duchaobo/Desktop/test.txt','r+',encoding = 'UTF-8')     # 文件打开并从头读取,文件中指针的位置会随之变动
b.seek(5)                                               # 移动文件指针到第6个字节
b.seek(-3,2)                                            # 从文件末尾移动文件指针到倒数第三个字节,第二个参数0表示头,1表示当前,2表示尾
print(b.read())                                         # read的参数可以为字节数,如果不带参数或者参数为负数则表示全部读取
print(b.readline(-1))                                   # 读取一行,参数可以为字节数,不带参数或者参数为复数则表示读取当前行所有
for line in b.readlines():                              # 读取若干行,参数可以为字节数,也可以为负数或不带参数
    line = line.strip()                                 # 除去行首尾的空白
    print(line)
b.close()

''''''''''''''''OS'''''''''''''''''''''
import os
print(os.access('C:/Users/duchaobo/Desktop/test.txt',os.F_OK))  # 检测文件权限,F_OK是否存在,R_OK是否可读,W_OK是否可写,X_OK是否可执行
print(os.getcwd())                                              # 返回当前工作目录
os.chdir('C:/Users/duchaobo/Desktop')                           # 改变当前工作目录
print(os.getcwd())

''''''''''''''''错误和异常'''''''''''''''''''''
try:
    print('hello')
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('这句话，无论异常是否发生都会执行。')

''''''''''''''''面向对象'''''''''''''''''''''
# 1.类对象
class person:
    high = 0
    __weight = 0
    def __init__(self,high,weight):
        self.high = high
        self.__weight = weight

    def speek(self):
        print('i am a person')
        print(f'i am {self.__class__}')

    def speekW(self):
        print(f'体重是{self.__weight}')

    def speekh(self):
        print(f'身高是{self.high}')

a = person(170, 130)
a.speek()
a.speekW()


# 2.单继承
class student(person):
    grade = 0
    def __init__(self, h, w, g):
        person.__init__(self,h,w)
        self.grade = g
    def speek(self):
        print(f'身高为{self.high},成绩为{self.grade}')

b = student(170, 130, 99)
b.speek()
b.speekh()
b.speekW()

# 3.多继承,
class speeker():
    name = ''
    topic = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speek(self):
        print(f'我的名字是{self.name},我是一名演说家,我演讲的主题是{self.topic}')

class sample(speeker, student):
    def __init__(self,n,t,h,w,g):
        speeker.__init__(self,n,t)
        student.__init__(self,h,w,g)
test = sample('Tony','Python',160,120,100)
test.speek()

# 4.方法重写
class parent:
    def myMethod(self):
        print('调用父类方法')
class child(parent):
    def myMethod(self):
        print('调用子类方法')
a = child()
a.myMethod()
super(child,a).myMethod()

# 5.运算符重载
class vertor:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return f'{self.a, self.b}'

    def __add__(self,other):
        return vertor(self.a + other.a, self.b + other.b)

a = vertor(1,2)
b = vertor(3,4)
print(a + b)

''''''''''''''''作用域'''''''''''''''''''''
# 1.global关键字,修改全局变量
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num) 
    num = 123
    print(num)
fun1()
print(num)

# 2.nonlocal关键字,修改闭包中的变量
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()

''''''''''''''''正则表达式'''''''''''''''''''''
import re
url = 'www.baidu.com'
print(re.match('www', url).span())   # match用于从头匹配
#print(re.match('com', url))         # 由于是从头匹配,所以没匹配到,无法调用span函数
print(re.search('com', url).span())  # serch是全字符匹配
line = 'Cats are smarter than dogs'
searchObj  = re.search(r'(.*) are (.*?) .*', line, re.M|re.I) # I忽略大小写,M多行模式,
if searchObj:
    print(searchObj.group())
    print(searchObj.group(1))
    print(searchObj.group(2))

phone = '010-8550-3340 # 这是操作岗的电话'
print(re.sub(r'#.*$', '', phone))

a = re.compile(r'\d+')      # 查找数字
print(a.findall('baidu 123sougou456'))          # 将匹配值作为列表返回

a = re.finditer(r'\d+','baidu 123sougou456')    # 将匹配值作为迭代器返回
for x in a:
    print(x.group())