from sympy import isprime 
con = False

month = [31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  #各月の日数


for n in range(12):

    for m in range(month[n]):

        if True == isprime(n) and isprime(m):
            num = n*100 + m
           
            if True == isprime(num):  #合計が素数の場合
                print(str(n)+"月"+str(m)+"日")
                con += 1

