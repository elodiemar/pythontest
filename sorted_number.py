
from unittest import removeResult

def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))


print(Descending_Order(145678333))


def Reverse_Number(num):
   return str(num)[::-1]

print(Reverse_Number(145678333))
