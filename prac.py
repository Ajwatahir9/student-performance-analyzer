# def topper_student(students_dict):
#     topper= ""
#     highest_marks = 0
#     for name, marks in students_dict.items():
#         if marks > highest_marks:
#             highest_marks = marks
#             topper = name
#     return topper

# students = {"Ajwa":76,"Alice":85,"Bob":90,"Sara":88}
# print(f"The topper student is: {topper_student(students)}")

# my_students = {"Ali": 85, "Sara": 92, "Ahmed": 78, "Fatima": 88}
# print(topper_student(my_students)) 







# import csv
# with open("students.csv", "w", newline="") as file:
#     writer= csv.writer(file)
#     writer.writerow(["Name", "Age", "City", "Marks"])
#     writer.writerow(["Ali", 20, "Karachi", 85])
#     writer.writerow(["Sara", 22, "Lahore", 92])
#     writer.writerow(["Ahmed", 19, "Islamabad", 78])
#     writer.writerow(["Fatima", 21, "Multan", 88])
# print("File Saved")

# students_from_csv={}
# with open("students.csv","r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students_from_csv[row["Name"]] = int(row["Marks"])
# print(students_from_csv)

# def topper_student(students_dict):
#     topper =""
#     highest_marks = 0
#     for name, marks in students_dict.items():
#         if marks > highest_marks:
#             highest_marks = marks
#             topper = name
#     return topper
# print(f"The topper student is: {topper_student(students_from_csv)}")

# total = sum(students_from_csv.values())
# average = total/len(students_from_csv)
# print(f"The average marks of the students is: {average}")






# with open("numbers.txt","w") as file:
#     file.write("85\n")
#     file.write("92\n")
#     file.write("78\n")
#     file.write("88\n")
#     file.write("95\n")
# print("File Saved")


# with open("numbers.txt", "r") as file:
#     total = 0
#     count = 0
#     for line in file:
#         num = int(line.strip())
#         total = total +num
#         count = count +1
#     average = total/count
# print(f"The total of the numbers in the file is: {total}")
# print(f"The average of the numbers in the file is: {average}")





# with open("nums.txt", "w" ) as file:
#     for i in range(5):
#         num = input(f"number{i+1}: ")
#         file.write(num + "\n")
# print("numbers saved to nums.txt")

# with open("nums.txt","r") as file:
#     total = 0
#     count = 0
#     for line in file:
#         num = int(line.strip())
#         total += num
#         count += 1
#     average = total/count
# print(f"The total of the numbers in the file is: {total}")
# # print(f"The average of the numbers in the file is: {average}")
# print(f" Average: {total / count:.2f}")




# with open("fruits.txt","w") as file:
#     file.write("Apple\n")
#     file.write("Banana\n")
#     file.write("Mango\n")
#     file.write("Orange\n")
#     file.write("Grapes\n")
#     file.write("Pineapple\n")

# print("File Saved")

# with open("fruits.txt","r") as file:
#     for line in file:
#         fruit = line.strip()
#         print(f"I like {fruit}")
        
        
# with open("names.txt","w") as file:
#     for i in range(3):
#         name = input(f"Enter name {i+1}:")
#         file.write(name + "\n")
# print("Names saved to names.txt")

# with open("names.txt", "r") as file:
#     print("Names in the file:")
#     for line in file:
#         name = line.strip()
#         print(name)
        
        
# import csv 
# with open("employee.csv","w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Department", "Salary"])
#     writer.writerow(["Ali", "IT", 55000])
#     writer.writerow(["Sara", "HR", 60000])
#     writer.writerow(["Ahmed", "Finance", 50000])
#     writer.writerow(["Fatima", "Marketing", 58000])
# print("File Saved")

# with open("employee.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for i in reader:
#         print(f"{i['Name']} works in {i['Department']} and earns {i['Salary']} per month.")
        
    
# products = {
#     "Laptop": 80000,
#     "Smartphone": 50000,
#     "Tablet": 30000,
#     "Headphones": 5000,
#     "Smartwatch": 15000
# }

# with open("products.txt", "w") as file:
#     for product, price in products.items():
#         file.write(f"{product}:{price}\n")
# print("Products saved to products.txt")

# new_products = {}

# with open("products.txt", "r") as file:
#     for line in file:
#         product, price = line.strip().split(":")
#         new_products[product] = int(price)
# print("Products read from products.txt:")

# print("Product list:")
# for product, price in new_products.items():
#     print(f"{product}: {price}")



import csv
with open("marks.csv", "w", newline ="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Marks"])
    writer.writerow(["Ali", 85])
    writer.writerow(["Sara", 92])
    writer.writerow(["Ahmed", 78])
    writer.writerow(["Fatima", 88])
    writer.writerow(["Aisha", 95])
print("File Saved")


total = 0
count = 0
max_marks = 0
topper = ""



with open("marks.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["Name"]
        marks = int(row["Marks"])
        
        total = total + marks
        count = count + 1
        
        if marks > max_marks:
            max_marks = marks
            topper = name

average = total / count
print("Students below average marks:")

with open("marks.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        marks = int(row["Marks"])
        if marks < average:
            print(f"{row['Name']} has marks below average: {marks}")


    