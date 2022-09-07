from random import randint

from q import *
n = 5 # randint(1, 10)
print("Generate random number N:", n)
print("Generate N cards...")
queue = Q()
print("-----------")
for i in range(n):
    queue.push(i)  # randint(1, 1000))
    # print("Q count", queue.size())

    print("q.back", queue.back.data)
    print("q front", queue.front.data)
    print("-----------")
print(queue)
for i in range(n):
    queue.pop()  # randint(1, 1000))
    # print("Q count", queue.size())

    print("q.back", queue.back.data)
    print("q front", queue.front.data)
    print("-----------")

