#immutable_var = (1,2, 'green')
#print(immutable_var)
#immutable_var [1] = 'string'
#print(immutable_var)
#нельзя изменить, так как элементы менять в не невозможно
mutable_list = ["green", "blue", "red"]
print(mutable_list)
mutable_list.append("orange")
print(mutable_list)
mutable_list.extend(["white",36])
print(mutable_list)