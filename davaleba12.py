"""
 დაწერეთ პითონის ფუნქცია, რომელიც იღებს პარამეტრად ერთიდაიგივე ზომის სიას (list) და zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.

params: [1, 2, 3], ['a', 'b', 'c']  
outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]
"""
def group_lists(list1, list2):
    return [str(item) for item in zip(list1, list2)]

list_a = [1, 2, 3]
list_b = ['a', 'b', 'c']

result = group_lists(list_a, list_b)
print(result)

"""
დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს. ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
ფუქნციის დასაწერად გამოიყენეთ lambda და  functools-ის reduce მეთოდი.  
"""
from functools import reduce

def multiply_list_elements(numbers):
    try:
        result = reduce(lambda x, y: x * y, numbers)
        return result
    except TypeError:
        
        return "შეცდომა: გთხოვთ მიაწოდოთ მხოლოდ რიცხვებისგან შემდგარი სია!"


# 1 სწორი შემთხვევა
print(multiply_list_elements([1, 2, 3, 4]))  
# output: 24

# 2 არასწორი ტიპის ელემენტი სიაში
print(multiply_list_elements([1, 2, 'a', 4]))  
# output: შეცდომა: გთხოვთ მიაწოდოთ მხოლოდ რიცხვებისგან შემდგარი სია!

# 3 არასწორი პარამეტრი (მაგალითად რიცხვი სიის ნაცვლად)
print(multiply_list_elements(5))  
# output: "შეცდომა: გთხოვთ მიაწოდოთ მხოლოდ რიცხვებისგან შემდგარი სია!"

"""
3. დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.

params: [1, 2, 3, 4, 5, 6, 7]
outputs: [1, 3, 5, 7]
"""

get_odd_numbers = lambda numbers: list(filter(lambda x: x % 2 != 0, numbers))

params = [1, 2, 3, 4, 5, 6, 7]
outputs = get_odd_numbers(params)

print(outputs)

"""
4. დაწერეთ პითონის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending). დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით. გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError), თუ სხვა გამონაკლისიც აღმოჩნდა ისიც გაითვალისწინეთ.

მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, რომელიც აბრუნებს სიტყვას, რომელიც მთავრდება რაღაც სიმბოლოებით...

"""
def filter_by_ending(string_list, ending):
    try:
        # list() მოექცა try ბლოკის შიგნით, რომ შეცდომა უეჭველად დაიჭიროს
        return list(filter(lambda x: x.endswith(ending), string_list))
    except TypeError:
        return "შეცდომა: არასწორი ტიპის პარამეტრი."
    except AttributeError:
        return "შეცდომა: სიის ელემენტი არ არის სტრიქონი."
    except Exception:
        return "მოხდა გაუთვალისწინებელი შეცდომა."

params = ['hello', 'world', 'coding', 'nod']
ending = 'ing'

print(filter_by_ending(params, ending))