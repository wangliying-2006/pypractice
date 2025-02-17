mylist=[1,2,3,4]
mylist.append(3)#在列表末尾增添新元素
mylist.insert(3,0)#在列表的第三个位置插入元素0
mylist.pop()#删除并返回列表中的最后一个元素
d=mylist.pop(1)#删除并返回列表中第1个位置的元素
mylist.sort()#将列表元素排序
mylist.reverse()#将列表元素倒序排列
del mylist[0]#删除列表中第0个位置的元素
e=mylist.index(1)#返回1第一次出现时的下标
mylist.count(3)#返回3在列表中出现的次数
mylist.remove(3)#从列表中移除第一次出现的3
a=len(mylist)#询问序列的元素个数
b=mylist[0:2]#取出序列的一部分（前闭后开）
c=5 in mylist#询问序列中是否有某元素
print(e)
print(a)
print(b)
print(c)
print(d)
print(mylist)