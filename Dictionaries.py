# a = {'the':2,'a':4,1000:5,10:'str','dict':{1:2},'list':[1,2]}
#
# print(type(a))
#
# print(a)
#
# print(len(a))
#
# print()
#
# b = a.copy()
# print(b)
#
# print()
#
# c = dict()
# print(type(c))
#
# print()
#
# e = dict.fromkeys(['the',3,'asdf',112],10) ###only pass keys in list no value assigned so gives None
# # if you mention another parameter in fn then it assigns all key values as that parameter here 10
# print(e)


# d = dict([('the',3),('a',4),(10,'str')]) #pass (key,value) pair in list
# print(d)
#
# # print(d[10]) #dictionay[key] = value
# # print(d['b'])  #it throws error if key not present
# print(d.get('',3)) #todo get in python dictionaries , instead of error it gives none,if key not present
# print(d.get('a',3))
# print(d.get(2,3))
# print(d.keys())
# print(d.values())
# print(d.items()) #it gives (key,value) pairs
#
# #for loop in dictionary
# for i in d:
#     print(i,d[i]) #prints space seperated key value pairs
#     # print(i) #prints keys
#
# print()
# for i in d.values():
#     print(i)
#
# print('the' in d) #to check key in dict exist or not ,returns boolean
# print('sr' in d)  #prints false



### adding data
# di = {'the':3,4:3}
#
# di['asdf'] = 12
# print(di)
#
# ci = {2:'sd',4:6}
# di.update(ci)
# ci.update(di)
#
# print(di)
# print(ci)
# ###deleting or removing
# di.pop('asdf')
# print(di)
#
# del di[4]
# print(di)
#
# di.clear()
# print(di)
#
# del di
# # print(di) #throws name error coz deleted in above line



# s = 'this is a word have many many word'
# k = 2
# words = s.split()
# print(words)
#
# d = {}
# for w in words:
#     if w in d:
#         d[w] = d[w]+1
#     else:
#         d[w] = 1
# print(d)
#
#
# # for w in words:
# #     d[w] = d.get(w,0)
# # print(d)
#
# for w in d:
#     if d[w] == k:
#         print(w)
#


# def kfrequency(s,k):
#     words = s.split()
#     d = {}
#     for w in words:
#         if w in d:
#             d[w] = d[w]+1
#         else:
#             d[w] = 1
#     # print(d)
#     for w in d:
#         if d[w] == k:
#             print(w)
#
#
# s = 'this is a word have many many word'
# kfrequency(s,2)



# d = {'Theodore': 1, 'Roxanne': 22, 'Mathew': 24, 'Betty': 20}
# max = -1
# min = 101
# for i in d.values():
#     if i > max:
#         max = i
#     if i < min:
#         min = i
# print(max)
# print(min)
#
# #     ls.append(d[i])
# # print(max(ls))
#
# ar=[12.33,45,666.12]
# print(ar[1])
# key_value = {}
# key_value[2] = '64'
# key_value[1] = '69'
# key_value[4] = '23'
# key_value[5] = '65'
# key_value[6] = '34'
# key_value[3] = '76'
# for i in sorted(key_value.keys()):
#     print(i,end=' ')
#
# for i in sorted(key_value.values()):
#     print(i)



# s = 'MISSISSIPPI'
# d = {}
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)
#
# for i in sorted(d):
#     print(i,d[i], end=' ')
#
# for i in sorted(d.values()):
#     print(i)
#
# print(sorted(d.items(), key=lambda x: (x[1], x[0])))


# d = {i:i for i in range(4)} #todo dictionary creation
# print(d)

# def twoSum(nums,target) :
    # d = {}
    # for i in range(len(nums)):
    #     x = target - nums[i]
    #     if x in d:
    #         return [i,d[x]]
    #     else:
    #         d[nums[i]] = i #todo as initially hashmap is empty, fill it till we get the sum until then we check using
                            # x , values of nums as keys.

    # d = {}
    # for i in nums: #todo create a dictionary for array using values as key and index as values
    #     d[i] = nums.index(i)
    # print(d)
    # for i in range(len(nums)):
    #     x = target - nums[i]
    #     if x in d and d[x] != i:
    #         return [d[x],i]


#     # for i in range(len(nums)): #todo to create a dictionary for array using indexes as key
#     #     d[i] = nums[i]
#     # print(d)
#
# nums = [3,3]
# target = 6
# print(twoSum(nums,target))
