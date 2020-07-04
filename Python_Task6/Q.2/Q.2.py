# initialize list of tuples
list = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

# removed empty tuples
list = [i for i in list if i]

print(list)
