#დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.
def get_fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
        
    return sequence

print(get_fibonacci_sequence(10))

# დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები ანაგრამები (ანაგრამი არის სიტყვა ან შესიტყვება, რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით). მაგ.: race და care ანაგრამებია.
def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)

print(is_anagram("race", "care"))  # True
print(is_anagram("სასწორი", "სწორასი"))  # True
print(is_anagram("hello", "world"))  # False

# დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.
def factorial(n):
    if n < 0:
        return "ფაქტორიალი უარყოფითი რიცხვებისთვის არ არსებობს"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
        
    return result

user_num = int(input("შეიყვანეთ რიცხვი: "))

final_answer = factorial(user_num)
print(f"პასუხი: {final_answer}")

#დაწერეთ პითნის ფუნქცია რომელიც მიიღებს  ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს. ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს  მისი რაოდენობა.
def count_character(text, char):
    count = 0
    for s in text:
        if s == char:
            count += 1
    return count

user_text = input("შეიყვანეთ სტრიქონი: ")
user_char = input("შეიყვანეთ საძიებო სიმბოლო: ")


result = count_character(user_text, user_char)
print(f"სიმბოლო '{user_char}' მეორდება {result}-ჯერ")