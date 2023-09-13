class Solution:
    def fib(self, n: int) -> int:

## Fibnocci series = 0, 1, 1, 2, 3, 5.......
## Recursion

        if n ==0:
           return 0

        elif n == 1:
            return 1

        else:
             return Solution.fib(self,n-1) + Solution.fib(self, n-2)


##Dynamic programming

#a=0, b = 1, a+b = 0+1 = 1
#a=1, b =1, a+b = 1+1 = 2
#a=1, b =2, a+b = 1+2 = 3
#a=2, b =3, a+b = 2+3 = 5

### step 0: store the values of b in a temp variable
### step 1: adding a and b
###step 2: shift a and b ('b' is already shifting through step 1)

           a = 0
           b = 1

           for i in range(0,n-1):
               temp = b
               b = a+b
               a = temp
           return b
 
 

               
