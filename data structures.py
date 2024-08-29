my_list = ["toyota", "bmw", "subaru", "range"]
my_list.append("mazda")
print(my_list)
print(my_list[0])
my_list[1] ="mercedes"
print(my_list[1])
print(f"{my_list[1]} is manufactured in Germany")

thislist = ["56", "44", "23"]
thislist.insert(1, "60")
print(thislist)
print(type(my_list))

# tuple datastructures
my_tuples=("banana", "oranges", "mangoes")
print(my_tuples)
# my_tuples[2] = "Grapes"
print(f"{my_tuples[2]},I love eating it")

# set data structure
this_set ={"North", "East", "West", "South"}
print(this_set)


# dictionaries data structures
my_dict ={"name":"District","Age":20,"Gender":"male"}
print(my_dict)
print(my_dict["Age"])
print(f"{my_dict ['Age']} ,is my years" )
print(f"{my_dict ['name']} ,is my surname" )

my_dictionary ={"breakfirst":"milk","lunch":"Banana","supper":"Meat"}
print(my_dictionary)
print(my_dictionary["lunch"])
