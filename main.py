n = int(input())

def prime():
    for i in range(n):
        a = int(input())

        while a % 2 == 0:
            a //= 2

        if a == 1:
            print("NO")
        else:
            print("YES")

prime()