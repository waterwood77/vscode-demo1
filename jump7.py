a=0 #从1-100跳7的数字

while a<100:
    a+=1
    if a%7==0:#7的倍数
        pass
    elif a%10==7:#各位上有7
        pass
    elif a//10==7:#十位数上有7
        pass
    else:
        print(a)
   
        """你好你好
        哈哈哈哈哈哈
        略略"""
        #以上为注释

#除法
35 / 5  # => 7.0
5 / 3  # => 1.6666666666666667
#向下取整，取商整数
5 // 3     # => 1
5.0 // 3.0 # => 1.0 # 浮点数也可以
-5 // 3  # => -2
-5.0 // 3.0 # => -2.0
#模除取余
7 % 3 # => 1
# 用not取非
not True  # => False
not False  # => True

# 逻辑运算符，注意and和or都是小写
True and False # => False
False or True # => True

# 整数也可以当作布尔值
0 and 2 # => 0
-5 or 0 # => -5
0 == False # => True
2 == True # => False
1 == True # => True

# 字符串用单引双引都可以
"这是个字符串"
'这也是个字符串'

#！！！！important
"hello"+"world!"#="hello world"

"This is a string"[3] #='s'
#用format来格式化字符串
"{} can be {}".format("strings","interpolated")
#strings can be interpolated
#可以重复调参数以节省时间
"{0} be nimble,{0} be quick,{0} jump over the {1}".format("Jack","candle stick")
# => "Jack be nimble, Jack be quick, Jack jump over the candle stick"

"{name} wants to eat {food}".format(name="bob",food="lasagna")
# => "Bob wants to eat lasagna"

# 如果你的Python3程序也要在Python2.5以下环境运行，也可以用老式的格式化语法
"%s can be %s the %s way" % ("strings", "interpolated", "old")

# None是一个对象
None  # => None

# 当与None进行比较时不要用 ==，要用is。is是用来比较两个变量是否指向同一个对象。
"etc" is None  #=False
None is None   #=True

# None，0，空字符串，空列表，空字典都算是False
# 所有其他值都是True
print(bool(True))    # Output: True
print(bool(False))   # Output: False
print(bool(0))       # Output: False
print(bool(1))       # Output: True
print(bool([]))      # Output: False
print(bool([1, 2])) # Output: True
print(bool(None))    # Output: False
print(bool(""))      # Output: False
print(bool("hello")) # Output: True

# 传统的变量命名是小写，用下划线分隔单词
some_var = 5
some_var  # => 5

# 访问未赋值的变量会抛出异常
# 参考流程控制一段来学习异常处理
#some_unknown_var  # 抛出NameError

#在 Python 中,try-except 块是一种常见的异常处理机制。它允许您捕获和处理可能发生的异常,而不是让程序因为异常而中断。
try:
    result = 10 / 0  # 会引发 ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero")

#用列表（list）储存序列
li =[] 
#创建列表时也可以同时赋给元素
other_li = [4,5,6]

#用apppend在列表最后追加元素
li.append(1) 
li.append(2)
li.append(4)
li.append(3)
#li现在是[1,2,4,3]


"""
li.append(1)
起初 li 是一个空列表 []
调用 append(1) 方法,将数字 1 添加到列表末尾
此时 li 变成 [1]
li.append(2)
列表 li 现在是 [1]
调用 append(2) 方法,将数字 2 添加到列表末尾
此时 li 变成 [1, 2]
li.append(4)
列表 li 现在是 [1, 2]
调用 append(4) 方法,将数字 4 添加到列表末尾
此时 li 变成 [1, 2, 4]
li.append(3)
列表 li 现在是 [1, 2, 4]
调用 append(3) 方法,将数字 3 添加到列表末尾
此时 li 变成 [1, 2, 4, 3]
"""


#用pop从列表尾部删除
li.pop() #=3 li=[1,2,4]
li.append(3) #li=[1,2,4,3]
#列表存取跟数组一样
li[0] #=1
li[-1] #=3
"""
li[0]
这里使用了方括号 [] 来访问列表中的元素。
列表的索引从 0 开始,所以 li[0] 表示访问列表 li 中的第 1 个元素。
根据之前的代码,li 的值是 [1, 2, 4, 3]。
因此 li[0] 的值就是 1。
li[-1]
这里使用了负索引 -1 来访问列表中的元素。
负索引是从列表的末尾开始计数的。
-1 表示访问列表中的最后一个元素,-2 表示倒数第二个元素,依此类推。
根据之前的代码,li 的值是 [1, 2, 4, 3]。
因此 li[-1] 的值就是 3。
"""

# 越界存取会造成IndexError
li[4]  # 抛出IndexErro,因为li只有0，1，2，3

#列表有切割语法,li[1,2,4,3]
li[1:3] #=[2,4]
li[2:] #=[4,3]
li[:3] #=[1,2,4]
li[::2] #=[1,4]
li[::-1] #=[3,4,2,1]
# 可以用三个参数的任何组合来构建切割
# li[始:终:步伐]   li[start:stop:step]

#用del删除任何一个元素,li=[1,2,4,3]
del li[2] #0,1,2,3  li is now [1,2,3]

#li= [1,2,3]
#other_li = [4,5,6]
#列表可以相加
#注意：li和other_li的值都不变
li + other_li  #=[1,2,3,4,5,6]
#用extend拼接列表
li.extend(other_li)   #li现在是[1,2,3,4,5,6]
"""extend() 方法可以用来将两个列表拼接在一起,形成一个新的列表。它与 append() 方法不同,append() 方法只能添加单个元素,而 extend() 方法可以一次性添加多个元素。
这个操作在需要合并多个列表的场景下很常用。比如,你可能从不同的数据源获取了多个列表,使用 extend() 可以将它们高效地合并到一个列表中。
总之, li.extend(other_li) 这行代码的作用就是将 other_li 列表中的所有元素添加到 li 列表的末尾,生成一个新的包含所有元素的 li 列表。这是 Python 中常见的列表拼接操作。"""

#用in测试列表是否包含值
1 in li  #=True

#用len取列表长度,li=[1,2,3,4,5,6]
len(li)  #=6

#