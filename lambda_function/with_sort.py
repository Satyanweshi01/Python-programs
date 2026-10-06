values = [(3,'c',"ok"),(1,'b',"hello"),(2,'a',"world")]

sorted_values = sorted(values,key=lambda x:x[1])
sorted_values1 = sorted(values,key=lambda x:x[0])
print(sorted_values)
print(sorted_values1)