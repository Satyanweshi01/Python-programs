import math
import time

start_time = time.perf_counter()

def prime_checker(num):
    if num<2:
        return False
    for m in range(2,int(math.sqrt(num))+1):
        if num % m == 0:
            return False
    return True
        

def prime_num_rep(num):
    j = 2
    while j <= num//2: # because half of the number set is just mirror number
            
        if prime_checker(j):
            k = num - j
            if prime_checker(k):
                return True
        j+=1
            # k = 1
            # while k < num:
            #     k+=1
            #     if prime_checker(k):
            #         if j + k == num:
            #             return True

        
                
    return False

for i in range(4,1000001,2):
        # check if i canbe represented by two prime number
        if prime_num_rep(i)==False:
            print(f"Finally this is the number {i}")
            break
print("This is the end")     
end_time = time.perf_counter()
execution_time = end_time-start_time
print(f"Execution time: {execution_time:.6f} seconds")
