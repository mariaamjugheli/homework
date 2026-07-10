#დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს სტრიქონის UTF-8 დაშიფრულ ვერსიას.
text = input ("შეიყვანეთ სტრიქონი: ")
encoded = text.encode("utf-8")
print("დაშიფრული (bytes):", encoded)
print("დაშიფრული (hex):", encoded.hex)

#დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. ჩამოაშორეთ ზედმეტი ინტერვალები. ყველა სიმბოლო გადაიყვანეთ პატარა ასოებში და დაუმატეთ ქვესტრიქონი 'Python'. თუ შეყვანილ სტრიქონში არსებობს სიტყვა "python", ჩაანაცვლეთ "Python"-ით.

text = input("შეიყვანეთ ტექსტი: ")
text = text.strip()
text = text.lower()
text = text.replace("python", "Python")
print("შედეგი:", text)

#დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. პროგრამამ უნდა დააბრუნოს ახალი სტრიქონი, რომელიც შედგება შეყვანილი სტრიქონის პირველი ნახევრისგან.
text = input("შეიყვანეთ სტრიქონი: ")
length = len(text)
half = text [:length // 2]
print("პირველი ნახევარი:", half)

"""
 დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
string მოდულის გამოყენებით დაწერეთ შემოწმება.
სტრიქონი ვალიდურია მაშინ, როდესაც ის შეიცავს მინიმუმ ერთ ლათინურ ასოსა და
მინიმუმ ერთ ციფრს და ამავე დროს არ შეიცავს დამატებით სიმბოლოებს: '!', '~', '#', '$' და ა.შ.
"""
import string
text = input("შეიყვანეთ სტრიქონი: ")
has_letter = any(c in string.ascii_letters for c in text)
has_digit = any(c in string.digits for c in text)
allowed = string.ascii_letters + string.digits + string.whitespace
is_valid = has_letter and has_digit and all(c in allowed for c in text)

if is_valid:
    print("სტრიქონი ვალიდურია")
else:
    print("სტრიქონი არავალიდურია")


"""
 დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს,
სტრიქონი გადაყავს ბაიტებში, ბეჭდავს მნიშვნელობას და შემდეგ კი
გადაყავს ბაიტებიდან სტრიქონში და ბეჭდავს სტრიქონს.
"""
text = input("შეიყვანეთ სტრიქონი:")
bytes_value = text.encode("utf-8")
print(f"ბაიტები: {bytes_value}")
decoded_text = bytes_value.decode("utf-8")
print(f"სტრიქონი: {decoded_text}")
