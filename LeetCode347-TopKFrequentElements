# hashmap to store the vales and the corresponding occurances (key, value) = (integer, occurance) hashmap output = [1:3], [2:2], [3:1]] initialise the new array with len(nums)+ 1 to consider the edge cases such as nums=[1,1,1,1,1,1]

# new array ; indices = occurances. [0,0,0,0,0,0] [0,3,2,1]



#Step 1: Creating a hashmap 

        d = {}
        
        na = [[] for i in range(0,len(nums)+1)]

        for i in range(0,len(nums)):
            if nums[i] not in d:
               d[nums[i]] = 1

            else:
                d[nums[i]] +=1

#Step 2: Sorting the emenets and storing inside a new array 

        for  inte, occu in d.items():
             na[occu].append(inte)

# Step 3: Run a loop and store the reuired k-values into final array
        
        fa = []
        for i in range(len(na)-1, 0, -1):
            for lea in na[i]:
                fa.append(lea)
                if len(fa) ==k:
                    return fa







