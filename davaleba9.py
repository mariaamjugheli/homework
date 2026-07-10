#შექმენით გლობალური ცვლადი int_list = [10,20,30,40] და დაწერეთ პითონის ფუნქცია, რომელიც  მიიღებს რიცხვს პარამეტრად და გლობალურ int_list სიაში ჩაამატებს პარამეტრად მიღებულ რიცხვს.
int_list = [10, 20, 30, 40]

def add_to_list(number):
    global int_list
    int_list.append(number)

user_num = int(input("შეიყვანეთ ჩასამატებელი რიცხვი: "))

add_to_list(user_num)

print(f"განახლებული სია: {int_list}")

#დაწერეთ პითნის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და აბრუნებს რიცხვების ჯამს. პარამეტრად უნდა მიიღოს შემდეგი სია [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10].
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
my_list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

result = calculate_sum(my_list)
print(f"სიის რიცხვების ჯამია: {result}")

#შექმენით გლობალური ცვლადი gl_str = "Global" და დაწერეთ პითონის ფუნქცია რომელიც ქმნის ლოკალურ ცვლადს იგივე სახელით რაც გლობალურ ცვლადს აქვს  (gl_str) და აბრუნებს ლოკალური ცვლადის მნიშვნელობას.
# გლობალური ცვლადი
gl_str = "Global"

def get_local_string():
    gl_str = "Local"
    return gl_str

print(get_local_string())
print(gl_str)

#რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს number და დააბრუნებს  ციფრების ჯამს (მაგალითად თუ ფუნქციამ მიიღო რიცხვი 12345, უნდა დააბრუნოს 15. რადგან 1+2+3+4+5 უდრის 15-ს).
def sum_of_digits(number):
    
    if number < 10:
        return number
    

    return (number % 10) + sum_of_digits(number // 10)

user_num = int(input("შეიყვანეთ რიცხვი: "))

print(f"ციფრების ჯამია: {sum_of_digits(user_num)}")

#რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრიქონს და დააბრუნებს მის შებრუნებულ (revers) სტრიქონს (მაგალითად  input: Hello   Output: olleH)
def reverse_string(text):
    if len(text) <= 1:
        return text
    
    return text[-1] + reverse_string(text[:-1])

user_input = input("შეიყვანეთ სტრიქონი: ")

print(f"შებრუნებული სტრიქონი: {reverse_string(user_input)}")