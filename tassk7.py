
#1)
my_list = ["tarteel", "Asmaa", "Ahmed"]

my_list.insert(0,"sabrin")
print(my_list)

my_list.pop()
print( my_list)
my_list.append("hamda")
print(my_list)
del my_list[2]
print(my_list)
#2)
list1 = ["adel","ahmed"]
list2 = ["samah","amjad"]
list3 = ["ali","basma"]
merged_list = list1 + list2 + list3
print( merged_list)
#3)
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
new_dict = {**dict1, **dict2, **dict3}
print( new_dict)

#4)
square_dict = {}
for num in range(1, 16):
    square_dict[num] = num ** 2
print(square_dict)

#5)
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 150, 'b': 200, 'd': 400}
combined_dict = {}
for key, value in dict1.items():
    combined_dict[key] = value + dict2.get(key, 0)
for key, value in dict2.items():
    if key not in dict1:
        combined_dict[key] = value
print("Combined dictionary:", combined_dict)

#6)
list1 = ['ten', 'twenty', 'thirty']
list2 = [10, 20, 30]
result_dict = {}
for i in range(len(list1)):
    result_dict[list1[i]] = list2[i]
print("Resulting dictionary:", result_dict)

#7)
sampledict = {
    "class": {
        "student": {
            "name": "mike",
            "marks": {
                "phy": 70,
                  "history": 80
            }
        }
    }
}
value = sampledict['class']['student']['marks']['history']
print(value)

#8)
my_dict = {1: "alaa", 5: "hadeel", 7: "hanin", 13: "malak"}
new_dict = {key: value for key, value in my_dict.items() if key < 10}
output = " -> ".join(new_dict.values())
print(output)