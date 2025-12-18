# tasks/task6.py

def solve():
# Ниже пишите решение задачи
    a, b, c =map(int,input().split())
    a2 = a**2
    b2 = b**2
    c2 = c**2
    n = (a2 + b2 == c2) or (a2 + c2 == b2) or (b2 + c2 == a2)
    print(n)
   
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()