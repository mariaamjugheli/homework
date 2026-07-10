# 1 კონსოლიდან შეიტანეთ მიმდევრობა. დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე (set).
sequence = input("1. შეიყვანეთ მიმდევრობა (გამოყავით მძიმით): ").split(",")
unique_set = set(item.strip() for item in sequence)
print(f"set: {unique_set}")

print()

# 2 დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე, რომლის შეცვლაც შეუძლებელი იქნება (frozenset).
sequence2 = input("2. შეიყვანეთ მიმდევრობა (გამოყავით მძიმით): ").split(",")
frozen = frozenset(item.strip() for item in sequence2)
print(f"frozenset: {frozen}")

print()

# 3 აიღეთ set ტიპის ორი მონაცემი. ელემენტები თავად განსაზღვრეთ. დაბეჭდეთ გაერთიანებული მონაცემები კორტეჟის სახით (tuple).
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
united_tuple = tuple(set1 | set2)
print(f"3. set1: {set1}")
print(f"   set2: {set2}")
print(f"   გაერთიანება (tuple): {united_tuple}")

print()

# 4 კონსოლიდან შევიტანოთ რიცხვების მიმდევრობა როგორც კორტეჟი (tuple). დავბეჭდოთ მხოლოდ უნიკალური ელემენტები სიის სახით (list).

numbers = input("4. შეიყვანეთ რიცხვები (გამოყავით მძიმით): ").split(",")
numbers_tuple = tuple(int(n.strip()) for n in numbers if n.strip().isdigit())
unique_list = list(set(numbers_tuple))
print(f"   tuple: {numbers_tuple}")
print(f"   უნიკალური list: {unique_list}")

print()

""" მოცემულია სია, რომლის ელემენტები წარმოადგენენ კორტეჟს:
[("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

დაბეჭდეთ შემდეგი ფორმატით:

Name: Gega, Age: 24
Name: Gaga, Age: 21
Name: Goga, Age: 19
Name: Giga, Age: 27
Name: Gagi, Age: 11 """

people = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]
print("5.")
for name, age in people:
    print(f"Name: {name}, Age: {age}")

print()

# 6
"""
მოცემულია მომხმარებლების სია: ["Irakli", "Giorgi", "Nona", "Oto"].
ასევე გვაქვს სხვა მომხმარებლებიც: ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
დავბეჭდოთ თანხვედრა.
"""
users1 = ["Irakli", "Giorgi", "Nona", "Oto"]
users2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
common = set(users1) & set(users2)
print(f"6. თანხვედრა: {common}")