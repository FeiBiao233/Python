n = int(input()) # 读入n


class student: # 固定格式
    def __init__(self): # 固定格式
        self.name = ""
        self.num = ""
        self.sco = 0


from functools import cmp_to_key # 引入模块


def cmp(a, b): # 定义cmp
    if a.sco < b.sco: # 无需像C语言一样定义a与b的类型,直接用
        return -1 # 不调换
    else:
        return 1 # 调换


list1 = [] # 创建空列表
for i in range(0, n):
    list1.append(student())
    list1[i].name, list1[i].num, list1[i].sco = input().split()
    list1[i].sco = int(list1[i].sco)
list1.sort(key=cmp_to_key(cmp)) # 按照cmp来排序

print(list1[0].name, list1[0].num, list1[0].sco) # 输出特定元素