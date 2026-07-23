"""
1. შექმენით პითონის კლასი Car, ატრიბუტებით: ბრენდი, მოდელი და წელი. ასევე, შექმენით მეთოდი car_info(), რომელიც დაბეჭდავს ატრიბუტების ინფორმაციას.

2. Car კლასში დაამატეთ მეთოდი age_of_car, რომელიც დაითვლის მანქანის ასაკს. ავტომობილის ასაკი დაბეჭდეთ car_info() მეთოდიდან.

3. შექმენით კლასი ElectricCar, რომელიც მემკვიდრეობით მიიღებს Car კლასს. დაამატეთ ახალი ატრიბუტი battery_life და მეთოდი battery_info(), რომელიც დაბეჭდავს შემდეგ სტრიქონს "ელემენტის ხანგრძლივობა შეადგენს [battery_life] საათს".

4. დაამატეთ Car კლასს ატრიბუტი number_of_cars, რომელიც დაითვლის მანქანების სრულ რაოდენობას. გაზარდეთ ეს ცვლადი ყოველ ჯერზე, მანქანის შექმნისას.

5. Car კლასს დაამატეთ კლასის მეთოდი total_cars(), რომელიც გამოიტანს მანქანების მთლიან რაოდენობას.

"""

from datetime import datetime


class Car:
    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

        Car.number_of_cars += 1

    def age_of_car(self):
        current_year = datetime.now().year
        return current_year - self.year

    def car_info(self):
        print(f"ბრენდი: {self.brand}")
        print(f"მოდელი: {self.model}")
        print(f"წელი: {self.year}")
        print(f"მანქანის ასაკი: {self.age_of_car()} წელი")

    @classmethod
    def total_cars(cls):
        print(f"მანქანების სრული რაოდენობა: {cls.number_of_cars}")


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def battery_info(self):
        print(
            f"ელემენტის ხანგრძლივობა შეადგენს "
            f"{self.battery_life} საათს"
        )


car1 = Car("Toyota", "Camry", 2020)
car2 = ElectricCar("Tesla", "Model 3", 2023, 8)

car1.car_info()

print()

car2.car_info()
car2.battery_info()

print()

Car.total_cars()