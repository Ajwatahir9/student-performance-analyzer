# def greet(name):
#     print(f"Hello,{name}")


# def greet_everone(names):
#     for name in names:
#         greet(name)
        
# friends = ["Ajwa","Alice", "Bob", "Ali"]
# greet_everone(friends)


# def goodbye(names):
#     for name in names:
#         print(f"Goodbye,{name}")

# goodbye(friends)

# def intro(name, city,age ):
#     print(f"My name is {name}, I am from {city} and I am {age} years old.")
    

# friends_info={
#     "Ajwa": {"city": "Lahore", "age": 21},
#     "Alice":{"city": "New york", "age": 24},
#     "Bob":{"city":"London", "age": 30},
#     "Ali":{"city":"Karachi", "age": 25},
#     "Sara":{"city":"Islamabad", "age": 22}
# }
    

    
# def line():
#     print("--------------------------------------------------")
    
# for key, value in friends_info.items():
#     intro(key, value["city"], value["age"])
#     line()
    
    
    
# def count_friends(freinds):
#    count = len(freinds)
#    print(f"You have {count} friends.")

# count_friends(friends_info)




def sum_numbers(numbers):
  total = 0
  for num in numbers:
      total = total+num
  return total
my_list = [10,20,30,40,50]
print(sum_numbers(my_list))


student ={
    "ali": 90,
    "sara": 85,
    "ahmed": 95
}


for name,marks in student.items():
    print(f"{name} scored {marks} marks.")
    
    
    
    
with open("myfile.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")
    
with open("myfile.txt", "r") as file:
    content = file.read()
    print (content)
    
with open("myfile.txt","a") as file:
    file.write("This is an appended line.\n")

with open("myfile.txt","r") as file:
    for line in file:
        print(f"line: {line.strip()}")
        
        

student = {
    "Ajwa": 76,
    "Alice": 85,
    "Bob": 90,
    "Sara": 88
}

with open("student.txt","w") as file:
    for name, marks in student.items():
        file.write(f"{name}: {marks}\n")
print("📚 STUDENTS FROM FILE:")

with open("student.txt", "r") as file:
    for line in file:
        name,marks = line.strip().split(":")
        print(f"{name} scored {marks} marks.")