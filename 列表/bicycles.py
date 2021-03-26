# -*-coding:utf-8-*-
# @software   : PyCharm      
# @file       :   bicycles.py
# @Time       :   2021/3/26 21:33
bicycles=['ashd','add','afafasf','fnakhfn']
print(bicycles[0].title()) #从0开始索引 最后一个可以表示为-1
bicycles.append('sange') #在列表的后面添加一个元素
print(bicycles)
bicycles.insert(0,'bye_bye') #在列表的指定位置添加一个元素
print(bicycles)
del bicycles[3]  #删除一个指定位置的元素
print(bicycles)
poped_b=bicycles.pop()  #使用pop方法可以输出去任意指定位置的一个 但是可以使用另外的变量储存起来
print(bicycles)
print(poped_b)

# 使用remove可以删除去知道值是什么但是不知道所在列表索引的
bicycles.remove('ashd')
print(bicycles)

bicycles.sort(reverse=True)#会永久性的对列表进行排序 回复不了原来的索引  默认reverse=Fasle 也可以指定参数reverse=True这样就会是倒序
print(bicycles)
# 使用sorted() 对列表进行临时性排序 不会改变原来的列表
# 使用reverse() 对列表进行倒转打印 但是 不会是进行排序仅仅是从后面往前面打印
for i in bicycles:
    print(i)

spy=[value**2 for value in range(1,8)] #这是一种方法
print(spy)
print('Good night! Everyone!')
