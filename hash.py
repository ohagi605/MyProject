def hash(s):

    for i in range(len(s)):
        ord_s.append(ord(s[i]))
    for p in range(len(s)):
        print(chr(ord_s[p]+3),end="")


def reverse(s):    

    for i in range(len(s)):
        ord_s.append(ord(s[i]))
    for p in range(len(s)):
        print(chr(ord_s[p]-3),end="")


n,s = input().split()
ord_s = []

if n == 'h': hash(s)
elif n == 'r': reverse(s)





 
