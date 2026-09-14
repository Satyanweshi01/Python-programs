#5.Write a program to sort the elements of a tuple in ascending and descending order both.
a = input("Enter tuple:")
a = tuple(map(int,a))
print(f"Unsorted: {a}")
a = list(a)
a.sort()
as_sort = tuple(a)

a.sort(reverse=True)
de_sort = tuple(a)

print(f"Ascending: {as_sort}")
print(f"Descending: {de_sort}")
