# part (ia)
#OOP is the program that uses class and object to design a software

# part (ib)

# Class defines attributes. 
#Class contains objects while object is an instance of a class.

# part (ii)
def word_occurrences(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

sentence = "python exam"
word_occurrences = word_occurrences(sentence)

print(word_occurrences)

# part (iii)
def add_numbers(a, b):
    return a + b
result = add_numbers(3, 4)
print(result)

# part (iv)
class Car:
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name
        self.color = color
car = Car(brand="Toyota", name="Range Rover", color="Blue")
print(f"Car Brand: {car.brand}")
print(f"Car Name: {car.name}")
print(f"Car Color: {car.color}")

# part (v)
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def start_engine(self):
        print(f"The engine of the car {self.make} {self.model} has started.")
my_car = Car("Toyota", "Hilux")
my_car.start_engine()

