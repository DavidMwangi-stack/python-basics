#Conditional statement

#age = 11
#if age >= 18:
 #   print("You are an Adult")
#elif age > 12:
 #   print("you are a teenager")
#else:
 #   print("you are a child")

# for Loop
# for q in range (5):
#    print(f"q is {q}")
    
#while loop
#count = 0
#while count < 5:
 #   print(f"count is {count}")
  #  count += 1

#functions 
#def greet (name):
 #   return f"Hello, {name}!"
#print(greet("David"))

#def add(a, b):
 #   return a + b
#result = add(11.4, 13.5)
#print(result)

#lambda functions 
#multiply = lambda c, b: c * b
#print (multiply (2, 5))

#import a specific function in a math
# from math import sqrt 
# use the imported function 
# result = sqrt(16)
# print(result)

# using the sys module to access command line arguments
# import sys
# print("Script name:", sys.argv[0])
# if len(sys.argv) >1:
#     print("First argument:",sys.argv[1])

#Using the datetime module to work with dates and times
# import datetime
 
# current_time = datetime.datetime.now()
# print("Current time:", current_time)

# import numpy as np 
# import pandas as pd
# #NumPy array
# arr = np.array([1,2,3,4,5])
# print(arr)

# #Pandas DataFrame
# data = {'Name':['Alice','Bob','Charlie'],'Age':[25, 30, 35]}
# df = pd.DataFrame(data)
# print(df)

#simple plot using Matplotlib
# import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y = [2,3,5,7,11]
# plt.plot(x,y)
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.title('Simple Plot')
# plt.show()

languages = ['Python', 'Java', 'C++', 'French', 'C']
# access item at index 1
print(languages[1])

print(languages[1:3])   

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[0])