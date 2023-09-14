class Solution:
    def climbStairs(self, n: int) -> int:

# Step 0: 1
# Step 1: 1
# Step 2: 1+1 or 2 = 2
# Step 3: 1+1+1 or 1+2 or 2+1 = 3
# Step 4: 1+1+1+1 or 1+2+1 or 2+1+1 or 1+1+2 or 2+2 = 5

# [0,1,2,3,4] --> [1, 1, 2, 3, 5]

##fibnocci series - 0,1,1,2,3,5,8........

## step 0 = f, step 1 = s
       
        f, s = 1,1

        if n==0: 
            return f
        elif n==1:
            return s
        elif n>1:
            for i in range(2, n+1):
                temp = s
                s = s+f
                f = temp
        return s

             



        
