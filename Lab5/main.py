import math


def ex1():
    class Shape:
        def __init__(self, name, color, description):
            self.name = name
            self.color = color
            self.description = description

        def __repr__(self):
            return f"{self.name} {self.color} {self.description}"

        def get_name(self):
            return f"The shape is a {self.name}."

        def get_color(self):
            return f"The {self.name} is {self.color}."

        def display_info(self):
            return f"{self.get_name()} {self.get_color()}"

    class Circle(Shape):
        def __init__(self, name, color, description, radius):
            super().__init__(name, color, description)
            self.radius = radius

        def area(self):
            return math.pi * self.radius ** 2

        def perimeter(self):
            return 2 * math.pi * self.radius

        def set_radius(self, radius):
            self.radius = radius

        def get_radius(self):
            return self.radius

    class Rectangle(Shape):
        def __init__(self, name, color, description, width, length):
            super().__init__(name, color, description)
            self.width = width
            self.length = length

        def area(self):
            return self.width * self.length

        def perimeter(self):
            return 2 * (self.width + self.length)

        def get_width(self):
            return self.width

        def set_width(self, width):
            self.width = width

        def get_height(self):
            return self.length

        def set_length(self, length):
            self.length = length

    class Triangle(Shape):
        def __init__(self, name, color, description, a, b, c):
            super().__init__(name, color, description)
            self.a = a
            self.b = b
            self.c = c

        def area(self):
            s = (self.a + self.b + self.c) / 2
            return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

        def perimeter(self):
            return self.a + self.b + self.c

        def get_a(self):
            return self.a

        def set_a(self, a):
            self.a = a

        def get_b(self):
            return self.b

        def set_side2(self, b):
            self.b = b

        def get_c(self):
            return self.c

        def set_side3(self, c):
            self.c = c

    circle = Circle(name="Circle", color="Red", description="A round shape", radius=5)
    rectangle = Rectangle(name="Rectangle", color="Blue", description="A four-sided shape", width=4, length=6)
    triangle = Triangle(name="Triangle", color="Green", description="A three-sided shape", a=3, b=4, c=5)

    print(circle.get_name())
    print(circle.get_color())
    print(circle.display_info())
    print(f"Area of the circle: {circle.area()}")
    print(f"Perimeter of the circle: {circle.perimeter()}")
    circle.set_radius(7)
    print(f"Updated {circle.display_info()} Area: {circle.area()}, Perimeter: {circle.perimeter()}")
    print("\n")

    print(rectangle.get_name())
    print(rectangle.get_color())
    print(rectangle.display_info())
    print(f"Area of the rectangle: {rectangle.area()}")
    print(f"Perimeter of the rectangle: {rectangle.perimeter()}")
    rectangle.set_width(8)
    print(f"Updated {rectangle.display_info()} Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")
    print("\n")

    print(triangle.get_name())
    print(triangle.get_color())
    print(triangle.display_info())
    print(f"Area of the triangle: {triangle.area()}")
    print(f"Perimeter of the triangle: {triangle.perimeter()}")
    triangle.set_a(6)
    print(f"Updated {triangle.display_info()} Area: {triangle.area()}, Perimeter: {triangle.perimeter()}")


def ex2():
    class Account:
        def __init__(self, account_number, account_holder, balance=0):
            self.account_number = account_number
            self.account_holder = account_holder
            self.balance = balance

        def deposit(self, amount):
            if amount > 0:
                self.balance += amount
                print(f"Deposit of ${amount} successful. New balance: ${self.balance}")
            else:
                print("Invalid deposit amount.")

        def withdraw(self, amount):
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
            else:
                print("Invalid withdrawal amount or insufficient funds.")

        def display_balance(self):
            print(f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: "
                  f"${self.balance}")

    class SavingsAccount(Account):
        def __init__(self, account_number, account_holder, balance=0, interest_rate=0.04, period=1):
            super().__init__(account_number, account_holder, balance)
            self.interest_rate = interest_rate
            self.period = period

        def calculate_interest(self):
            interest = self.balance * self.interest_rate * self.period
            self.balance += interest
            print(f"Interest of ${interest} added. New balance: ${self.balance}")

        def get_interest_rate(self):
            return self.interest_rate

        def set_interest_rate(self, interest_rate):
            self.interest_rate = interest_rate

        def get_period(self):
            return self.period

        def set_period(self, period):
            self.period = period

    class CheckingAccount(Account):
        def __init__(self, account_number, account_holder, balance=0, overdraft_limit=100):
            super().__init__(account_number, account_holder, balance)
            self.overdraft_limit = overdraft_limit

        def withdraw_with_overdraft(self, amount):
            if 0 < amount <= (self.balance + self.overdraft_limit):
                self.balance -= amount
                print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
            else:
                print("Invalid withdrawal amount or overdraft limit reached.")

        def get_overdraft_limit(self):
            return self.overdraft_limit

        def set_overdraft_limit(self, overdraft_limit):
            self.overdraft_limit = overdraft_limit

    savings_account = SavingsAccount(account_number="SA123", account_holder="John Doe", balance=1000,
                                     interest_rate=0.03)
    savings_account.display_balance()
    savings_account.deposit(500)
    savings_account.calculate_interest()
    savings_account.withdraw(200)
    print(f"Current Interest Rate: {savings_account.get_interest_rate()}")

    print("\n")

    checking_account = CheckingAccount(account_number="CA456", account_holder="Jane Smith", balance=500,
                                       overdraft_limit=200)
    checking_account.display_balance()
    checking_account.deposit(100)
    checking_account.withdraw_with_overdraft(700)
    print(f"Current Overdraft Limit: {checking_account.get_overdraft_limit()}")


def ex3():
    class Vehicle:
        def __init__(self, mark, model, year):
            self.mark = mark
            self.model = model
            self.year = year

        def display_info(self):
            return f"{self.year} {self.mark} {self.model}"

        def start_engine(self):
            return f"The engine of the {self.display_info()} is now running."

        def stop_engine(self):
            return f"The engine of the {self.display_info()} is now stopped."

    class Car(Vehicle):
        def __init__(self, mark, model, year, fuel_efficiency):
            super().__init__(mark, model, year)
            self.fuel_efficiency = fuel_efficiency

        def calculate_mileage(self, distance):
            return (f"The {self.display_info()} can travel {distance / self.fuel_efficiency: .2f} "
                    f"miles with the current fuel.")

        def open_trunk(self):
            return f"The {self.display_info()}'s trunk is now opened."

        def park(self):
            return f"The {self.display_info()} is now parked."

    class Motorcycle(Vehicle):
        def __init__(self, mark, model, year, fuel_efficiency):
            super().__init__(mark, model, year)
            self.fuel_efficiency = fuel_efficiency

        def calculate_mileage(self, distance):
            return (f"The {self.display_info()} can travel {distance / self.fuel_efficiency: .2f} "
                    f"miles with the current fuel.")

        @staticmethod
        def honk():
            return "Beep beep!"

        def toggle_headlight(self):
            return f"The headlights of the {self.display_info()} are turned on."

    class Truck(Vehicle):
        def __init__(self, mark, model, year, towing_capacity):
            super().__init__(mark, model, year)
            self.towing_capacity = towing_capacity

        def calculate_towing_capacity(self, weight):
            if weight <= self.towing_capacity:
                return f"The {self.display_info()} can tow {weight} pounds successfully."
            else:
                return f"The {self.display_info()} is not able to tow {weight} pounds. Exceeds towing capacity."

        def tow(self):
            return f"The {self.display_info()} is now towing something."

        def load_cargo(self):
            return f"Loading cargo into the {self.display_info()}."

    car = Car(mark="Toyota", model="Camry", year=2022, fuel_efficiency=30)
    motorcycle = Motorcycle(mark="Harley-Davidson", model="Sportster", year=2022, fuel_efficiency=50)
    truck = Truck(mark="Ford", model="F-150", year=2022, towing_capacity=8000)

    print(car.display_info())
    print(car.start_engine())
    print(car.stop_engine())
    print(car.calculate_mileage(150))
    print(car.open_trunk())
    print(car.park())
    print("\n")

    print(motorcycle.display_info())
    print(motorcycle.start_engine())
    print(motorcycle.stop_engine())
    print(motorcycle.calculate_mileage(100))
    print(motorcycle.honk())
    print(motorcycle.toggle_headlight())
    print("\n")

    print(truck.display_info())
    print(truck.start_engine())
    print(truck.stop_engine())
    print(truck.calculate_towing_capacity(7000))
    print(truck.tow())
    print(truck.load_cargo())


def ex4():
    class Employee:
        def __init__(self, name, employee_id, salary):
            self.name = name
            self.employee_id = employee_id
            self.salary = salary

        def display_info(self):
            print(f"Name: {self.name}\nEmployee ID: {self.employee_id}\nSalary: ${self.salary}")

        def take_vacation(self, days):
            print(f"Taking {days} days of vacation.")

        def update_salary(self, new_salary):
            print(f"Updating {self.name}'s salary information to {new_salary}")
            self.salary = new_salary

    class Manager(Employee):
        def __init__(self, name, employee_id, salary, department):
            super().__init__(name, employee_id, salary)
            self.department = department

        def display_info(self):
            super().display_info()
            print(f"Department: {self.department}")

        def organize_team_meeting(self):
            print(f"{self.name} is organizing a team meeting.")

        def approve_vacation(self):
            print(f"{self.name} is approving vacation requests.")

    class Engineer(Employee):
        def __init__(self, name, employee_id, salary, programming_language):
            super().__init__(name, employee_id, salary)
            self.programming_language = programming_language

        def display_info(self):
            super().display_info()
            print(f"Programming Language: {self.programming_language}")

        def write_code(self):
            print(f"{self.name} is writing code.")

        def debug_code(self):
            print(f"{self.name} is debugging code.")

    class Salesperson(Employee):
        def __init__(self, name, employee_id, salary, sales_target):
            super().__init__(name, employee_id, salary)
            self.sales_target = sales_target

        def display_info(self):
            super().display_info()
            print(f"Sales Target: ${self.sales_target}")

        def make_sales_pitch(self):
            print(f"{self.name} is making a sales pitch.")

        def close_deal(self):
            print(f"{self.name} is closing a deal.")

    manager1 = Manager("Calin Teodorescu", "21", 30000, "Programming")
    engineer1 = Engineer("Stefan Paulet", "78", 15000, "Python")
    salesperson1 = Salesperson("Eduard Zamfirache", "103", 75000, 100000)

    manager1.display_info()
    manager1.organize_team_meeting()
    manager1.approve_vacation()
    print()

    engineer1.display_info()
    engineer1.write_code()
    engineer1.debug_code()
    print()

    salesperson1.display_info()
    salesperson1.make_sales_pitch()
    salesperson1.close_deal()
    print()

    engineer1.update_salary(20000)
    engineer1.display_info()
    print()


def ex5():
    class Animal:
        def __init__(self, name, habitat, color):
            self.name = name
            self.habitat = habitat
            self.color = color

        def get_color(self):
            return f"{self.name} is {self.color}"

        def move(self):
            return f"{self.name} is moving in its {self.habitat} habitat."

        def sleep(self):
            return f"{self.name} is sleeping."

    class Mammal(Animal):
        def __init__(self, name, habitat, color, fur_color):
            super().__init__(name, habitat, color)
            self.fur_color = fur_color

        def get_fur_color(self):
            return f"{self.name}'s fur is {self.fur_color} color."

        def nurse_young(self):
            return f"{self.name} nurses its young with milk."

        def run(self):
            return f"{self.name} is running."

    class Bird(Animal):
        def __init__(self, name, habitat, color, feather_color):
            super().__init__(name, habitat, color)
            self.feather_color = feather_color

        def lay_eggs(self):
            return f"{self.name} lays eggs as a method of reproduction."

        def fly(self):
            return f"{self.name} is flying in the sky."

        def get_feather_color(self):
            return f"{self.name} has its feathers in {self.feather_color} color."

    class Fish(Animal):
        def __init__(self, name, habitat, color, scale_color):
            super().__init__(name, habitat, color)
            self.scale_color = scale_color

        def get_scale_color(self):
            return f"{self.name} has its scales in {self.scale_color} color."

        def swim(self):
            return f"{self.name} is swimming in the water."

        def gill_respiration(self):
            return f"{self.name} breathes through gills."

    lion = Mammal(name="Lion", habitat="Grassland", color="Yellow", fur_color="Brown")
    parrot = Bird(name="Parrot", habitat="Rainforest", color="Green", feather_color="Blue")
    shark = Fish(name="Shark", habitat="Ocean", color="Gray", scale_color="Silver")

    print(lion.get_color())
    print(lion.move())
    print(lion.sleep())
    print(lion.get_fur_color())
    print(lion.nurse_young())
    print(lion.run())
    print("\n")

    print(parrot.get_color())
    print(parrot.move())
    print(parrot.sleep())
    print(parrot.lay_eggs())
    print(parrot.fly())
    print(parrot.get_feather_color())
    print("\n")

    print(shark.get_color())
    print(shark.move())
    print(shark.sleep())
    print(shark.get_scale_color())
    print(shark.swim())
    print(shark.gill_respiration())


def ex6():
    class LibraryItem:
        def __init__(self, title, author, publication_year):
            self.title = title
            self.author = author
            self.publication_year = publication_year
            self.checked_out = False

        def display_info(self):
            return f"{self.title} by {self.author} ({self.publication_year})"

        def check_out(self):
            if not self.checked_out:
                self.checked_out = True
                return f"{self.display_info()} has been checked out."
            else:
                return f"{self.display_info()} is already checked out."

        def return_item(self):
            if self.checked_out:
                self.checked_out = False
                return f"{self.display_info()} has been returned."
            else:
                return f"{self.display_info()} is not checked out."

    class Book(LibraryItem):
        def __init__(self, title, author, publication_year, genre):
            super().__init__(title, author, publication_year)
            self.genre = genre

        def get_genre(self):
            return f"The genre of {self.display_info()} is {self.genre}."

        def read(self):
            return f"You can read {self.display_info()}."

        def borrow_time(self):
            return f"The borrowing time for {self.display_info()} is 21 days."

    class DVD(LibraryItem):
        def __init__(self, title, director, publication_year, runtime):
            super().__init__(title, director, publication_year)
            self.runtime = runtime

        def get_runtime(self):
            return f"The runtime of {self.display_info()} is {self.runtime} minutes."

        def watch(self):
            return f"You can watch {self.display_info()}."

        def borrow_time(self):
            return f"The borrowing time for {self.display_info()} is 7 days."

    class Magazine(LibraryItem):
        def __init__(self, title, publisher, publication_year, issue_number):
            super().__init__(title, publisher, publication_year)
            self.issue_number = issue_number

        def get_issue_number(self):
            return f"{self.display_info()} is Issue #{self.issue_number}."

        def flip_through(self):
            return f"You can flip through {self.display_info()}."

        def borrow_time(self):
            return f"The borrowing time for {self.display_info()} is 14 days."

    # Example usage:
    book = Book(title="Anna Karenina", author="Lev Tolstoi", publication_year=1878, genre="Realist novel")
    print(book.display_info())
    print(book.get_genre())
    print(book.check_out())
    print(book.borrow_time())
    print(book.read())
    print(book.return_item())
    print("\n")

    dvd = DVD(title="Airplane!", director="Jim Abrahams", publication_year=1980, runtime=148)
    print(dvd.display_info())
    print(dvd.get_runtime())
    print(dvd.check_out())
    print(dvd.borrow_time())
    print(dvd.watch())
    print(dvd.return_item())
    print("\n")

    magazine = Magazine(title="National Geographic", publisher="National Geographic Society", publication_year=2022,
                        issue_number=3)
    print(magazine.display_info())
    print(magazine.get_issue_number())
    print(magazine.check_out())
    print(magazine.borrow_time())
    print(magazine.flip_through())
    print(magazine.return_item())


print("Exercise 1")
ex1()
print()
print("\nExercise 2")
ex2()
print()
print("\nExercise 3")
ex3()
print()
print("\nExercise 4")
ex4()
print()
print("\nExercise 5")
ex5()
print()
print("\nExercise 6")
ex6()
