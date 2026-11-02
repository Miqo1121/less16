# სავარჯიშო 1 — წიგნი

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        print(f"{self.title} — {self.author}, {self.pages} გვ.")


book1 = Book("ვეფხისტყაოსანი", "შოთა რუსთაველი", 250)
book2 = Book("კადმოსის მემკვიდრენი", "ჯემალ ქარჩხაძე", 320)
book3 = Book("ბახტრიონი", "ილია ჭავჭავაძე", 180)

book1.info()
book2.info()
book3.info()

print()


# სავარჯიშო 2 — მანქანები და ბორბლები

class Car:
    wheels = 4  

    def __init__(self, brand, color, year):
        self.brand = brand    
        self.color = color
        self.year = year


car1 = Car("BMW", "შავი", 2020)
car2 = Car("Toyota", "თეთრი", 2018)

print(car1.brand, car1.wheels)
print(car2.brand, car2.wheels)

car2.wheels = 3 

print(car1.wheels)
print(car2.wheels)
print(Car.wheels)



print()


# სავარჯიშო 3 — მოთამაშეების მთვლელი

class Player:
    players_count = 0  

    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        Player.players_count += 1  


print(Player.players_count)

p1 = Player("ანა")
p2 = Player("დავითი", 5)
p3 = Player(name="მარიამი", level=3)

print("სულ მოთამაშე:", Player.players_count)
print(p1.name, p1.level)
print(p2.name, p2.level)
print(p3.name, p3.level)