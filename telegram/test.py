import csv
from array import *

"""
import question 
[0][вопрос 1, ответ 1, 1]
[1][вопрос 2, ответ 2, 1]
[2][вопрос 3, ответ 3, 2]
[вопрос 1, ответ 1, 1],[вопрос 2, ответ 2, 1],[вопрос 3, ответ 3, 2]
"""

a = [[]]
with open("q.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for row in reader:
        a.append([row["question"],row["answer"],row["type"]])
csvfile.close()
a.pop(0)
print(a)
print(len(a))
for i in range(len(a)):
    print(a[i][0])
D = ["апельсин","слива","яблоко", "груша"]
d = 'ябл'
z = [print(i) for i in range(len(D)) if d in D[i]]

input = "Компьютер не работает"
"""
Компьютер -  
не - 
работает - 

"""