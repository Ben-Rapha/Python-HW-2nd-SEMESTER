#KINGSLEY OTTO
#CSI 33
#Give a theta analysis of the time efficiency of the following code fragments. 

a) n = input('enter n: ')
   for i in range(n) : # n iteration
       x = 2 * n # 1 step 
       while x > 1: 
           x = x / 2 # 2 steps
    T(n) = 3log2n + 1
    T(n) = Θ(log n) 


b) n = input('enter n: ')
   total = 0 # 1 step
   for i in range(n) : # n iteration 
       for j in range(10000): # 1 step
           total += j # 1 step 
           print total # 1 step
    T(n) = n * 10000 * 1 * 1 
    T(n) = Θ(n)

c) total = 0 # 1 step 
   n = input('enter n: ')
   for i in range(2 * n) : # n iteration
       for j in range(i, n) : # n iteration 
           total += j # 1 step
    for j in range(n) : #n iteration 
        total += j # 1 step
    print j # 1 step

    T(n) = 2n*n*1+n+n + 1
    T(n) = Θ(n^2)
