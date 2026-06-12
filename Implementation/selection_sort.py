NUMBERS = 10
array = []
print(("Give me ten numbers to sort: "))
for s in range(NUMBERS):
    input1 = int(input("Number:"))
    array.append(input1)

print(array)
for i in range(NUMBERS-1): # for each position
    smallest_num_index = i # assuming current value is the smallest hence taking its position as smallest_num_index 
    for j in range(i+1,NUMBERS): # reducing the unsorted portion with each iteration
        if array[smallest_num_index] > array[j]: # changing the smallest_num_index if found any value smaller
            smallest_num_index = j
    # swaping mechanism
    # temp = array[i]
    # array[i] = array[smallest_num_index]
    # array[smallest_num_index] = temp
    
    array[i], array[smallest_num_index] = array[smallest_num_index], array[i]
print(array) 