# # question 1
# from functools import reduce
# fib_series = lambda n: reduce(lambda x,_: x+[x[-1]+x[-2]],range(n-2), [0, 1])
# print(fib_series(4))

# # question 2
# str1="SOC 23 CTech 5 DSBS8 NWC 56 CINtel 20 5"
# str1_list=[i for i in str1.split(" ")]
# length=len(str1_list)
# num=sorted([int(i) for i in str1_list if i.isdigit()])
# for i in ((filter(lambda x:x>length,num))):
#     print(i,end=" ")

# # question 3
# def sort_numeric_strings(nums_str):
#     result = sorted(nums_str, key=lambda el: int(el))
#     return result
# nums_str = ['4','12','45','7','0','100','200','-12','-500']
# print(sort_numeric_strings(nums_str))

# # question 4
# from functools import reduce
# tuple1=(1,2,3,4,5,6,7)
# result=reduce(lambda x,y:x+y,tuple1)
# print(result/len(tuple1))

# # question 5
# list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# list2=[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
# def intersection_nested_lists(l1, l2):
#     result = [list(filter(lambda x: x in l1, sublist)) for sublist in l2]
#     return result
# print(intersection_nested_lists(list1, list2))

# # question 6
# list1=["subham","gupta","shreya","shrevastava"]
# def convert(x):
#     return list(x)
# list2=list(map(convert,list1))
# print(list2)

# # question 7
# list1=['a','e','A','c']
# def change_case(x):
#     return str(x).upper(),str(x).lower()
# list2=set(map(change_case,list1))
# print(list2)

# # question 8
# num1=[1,5,11]
# num2=[10,2,15]
# x=list(map(lambda x,y:x+y,num1,num2))
# y=list(map(lambda x,y:x-y,num1,num2))
# print(x)
# print(y)

# # question 9
# def func(alpha):
#     if alpha>=18:
#         return True
#     else:
#         return False
# y=list(filter(func,[1,12,18,15,23,32,10,65]))
# print(y)

# # question 10
# def func(alpha):
#     if(alpha=='a' or alpha=='e' or alpha=='i' or alpha=='o' or alpha=='u'):
#         return True
#     else:
#         return False
# y=list(filter(func,['a','b','c','d','e']))
# print(y)

# # question 11
# from functools import reduce
# def maximum(x,y):
#     if(x>y):
#         return x
#     else:
#         return y
# y=reduce(maximum,[110,18,32,23,21])
# print(y)

# # question 12
# from functools import reduce
# def mul(x,y):
#     return x*y
# y=reduce(mul,range(1,5))
# print(y)