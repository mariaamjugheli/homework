#შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], in-ის გამოყენებით დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეტანილი რიცხვი არის თუ არა სიაში.

num_list = [44, 23, 11, 8, 20, 56, 33, 55]
number = int(input("შეიყვანეთ რიცხვი: "))
if number in num_list:
    print(f"{number} არის სიაში")
else:
    print(f"{number} არ არის სიაში")

#დაწერეთ პროგრამა, რომელიც შეამოწმებს თქვენს მიერ მოყვანილი რიცხვის ლუწობასა და კენტობას
number = int(input("შეიყვანეთ რიცხვი: "))

if number % 2 == 0:
    print(f"{number} არის ლუწი")
else:
    print(f"{number} არის კენტი")

# შექმენით ორი სტრინგის ტიპის ცვლადი st1 და st2, შეადარეთ ისინი is-ის გამოყენებით, თუ ემთხვევა გამოიტანეთ ტექსტი "Same object", წინააღმდეგ შემთხვევაში "Different object"
# პირველი ვარიანტი:
st1 = "hello"
st2 = "hello"

if st1 is st2:
    print("same object")
else:
    print ("different object")

#მეორე ვარიანტი:
st1 = "hello"
st2 = "გამარჯობა"

if st1 is st2:
    print("same object")
else:
    print("different object")

"""
შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], შეიტანეთ რიცხვი და დაწერეთ შემდეგი პირობა:

* თუ შეტანილი რიცხვი მეტია სიაში არსებულ მე-3 ელემენტზე და ნაკლებია ბოლო ელემენტზე გამოიტანეთ ტექსტი "More than list elements";

* თუ შეტანილი რიცხვი უდრის სიის მე-6 ელემენტს გამოიტანეთ ტექსტი "Equal";

* სხვა ნებისმიერ შემთხვევაში გამოიტანეთ ტექსტი "None of the conditions were met".

რიცხვის შეტანის ოპერაციისთვის გამოიყენეთ input მეთოდი.
"""
num_list = [44, 23, 11, 8, 20, 56, 33, 55]

number = int(input("შეიყვანეთ რიცხვი: "))

if number > num_list[2] and number < num_list[-1]:
    print("more than list elements")

elif number == num_list[5]:
    print("equal")

else:
    print("none of the conditions were met")