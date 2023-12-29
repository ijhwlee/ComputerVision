list1 = [1,2,3,4]
list2 = [1, 1.5, 'a', 'a', '문자열']
tuple1 = (1,2)
tuple2 = (1, 1.5, 'b', 'b', '문자열', '이름')
dict1 = {'name': '이형원', 'email':'hwlee@inje.ac.kr', 'age':32}
set1, set2 = set(list2), set(tuple2)

list1[0] = 21
list2.insert(3, 'c')
dict1['email'] = 'ijhwlee@gmail.com'

print('list1 = {0}, type = {1}'.format(list1, type(list1)))
print('list2 = {0}, type = {1}'.format(list2, type(list2)))
print('tuple1 = {0}, type = {1}'.format(tuple1, type(tuple1)))
print('tuple2 = {0}, type = {1}'.format(tuple2, type(tuple2)))
print('set1 = {0}, type = {1}'.format(set1, type(set1)))
print('set2 = {0}, type = {1}'.format(set2, type(set2)))
print('intersection = {0}'.format(set1 & set2))
