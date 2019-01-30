Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> todos = [[177,145,167,190,140,150,180,130], # grupo 1
[165,176,145,189,170,189,159,190], # grupo 2
[145,136,178,200,123,145,145,134], # grupo 3
[201,110,187,175,156,165,156,135] # grupo 4
]
>>> [max(todos[0]), max(todos[1]), max(todos[2]), max(todos[3])].index(max([max(todos[0]), max(todos[1]), max(todos[2]), max(todos[3])]))+1
4
>>> 
