import pickle

# 1. Создание базового класса Animal
class Animal:
    def __init__(self, name, age):
        """Инициализирует общее имя и возраст для всех животных."""
        self.name = name
        self.age = age

    def make_sound(self):
        """Звук, который издает животное (по умолчанию)."""
        return "Some generic sound"

    def eat(self):
        """Метод кормления для всех животных."""
        return f"{self.name} is eating."

    def __str__(self):
        """Строковое представление животного."""
        return f"{self.name}, age {self.age}"

# 2. Создание подклассов Bird, Mammal и Reptile
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        """Специфический звук птицы."""
        return "Chirp chirp"

    def fly(self):
        """Метод, специфичный для птиц."""
        return f"{self.name} is flying with a wingspan of {self.wing_span} meters."

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        """Специфический звук млекопитающего."""
        return "Grrr"

class Reptile(Animal):
    def __init__(self, name, age, scales_pattern):
        super().__init__(name, age)
        self.scales_pattern = scales_pattern

    def make_sound(self):
        """Специфический звук рептилии."""
        return "Hiss"

# 3. Функция animal_sound для демонстрации полиморфизма
def animal_sound(animals):
    """Принимает список животных и вызывает метод make_sound() для каждого из них."""
    for animal in animals:
        print(f"{animal}: {animal.make_sound()}")

# 4. Класс Zoo с использованием композиции и сохранения состояния
class Zoo:
    def __init__(self):
        """Инициализирует зоопарк с пустыми списками животных и сотрудников."""
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        """Добавляет животное в зоопарк."""
        self.animals.append(animal)
        print(f"Animal added: {animal}")

    def add_employee(self, employee):
        """Добавляет сотрудника в зоопарк."""
        self.employees.append(employee)
        print(f"Employee added: {employee}")

    def list_animals(self):
        """Список всех животных в зоопарке."""
        for animal in self.animals:
            print(animal)

    def list_employees(self):
        """Список всех сотрудников в зоопарке."""
        for employee in self.employees:
            print(employee)

    def save_zoo(self, filename):
        """Сохраняет состояние зоопарка в файл."""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Zoo data saved to {filename}")

    @staticmethod
    def load_zoo(filename):
        """Загружает состояние зоопарка из файла."""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            print(f"No such file: {filename}")
            return Zoo()

# 5. Классы для сотрудников ZooKeeper и Veterinarian
class ZooKeeper:
    def __init__(self, name):
        """Инициализация зоокипера с именем."""
        self.name = name

    def feed_animal(self, animal):
        """Кормление животного."""
        return f"{self.name} is feeding {animal.name}."

    def __str__(self):
        """Строковое представление зоокипера."""
        return f"ZooKeeper: {self.name}"

class Veterinarian:
    def __init__(self, name):
        """Инициализация ветеринара с именем."""
        self.name = name

    def heal_animal(self, animal):
        """Лечение животного."""
        return f"{self.name} is treating {animal.name}."

    def __str__(self):
        """Строковое представление ветеринара."""
        return f"Veterinarian: {self.name}"

# Пример использования программы
# Загружаем данные из файла или создаем новый зоопарк
zoo = Zoo.load_zoo("zoo_OB03")

# Создаем новых животных и добавляем их в зоопарк
eagle = Bird("Eagle", 5, 2.5)
lion = Mammal("Lion", 8, "Golden")
snake = Reptile("Snake", 3, "Striped")
zoo.add_animal(eagle)
zoo.add_animal(lion)
zoo.add_animal(snake)

# Создаем новых сотрудников и добавляем их в зоопарк
keeper = ZooKeeper("Sam")
vet = Veterinarian("Dr. Smith")
zoo.add_employee(keeper)
zoo.add_employee(vet)

# Демонстрация работы сотрудников
print(keeper.feed_animal(lion))
print(vet.heal_animal(eagle))

# Список всех животных и сотрудников
print("\nAnimals in the zoo:")
zoo.list_animals()
print("\nEmployees in the zoo:")
zoo.list_employees()

# Демонстрация полиморфизма
print("\nAnimal sounds:")
animal_sound([eagle, lion, snake])

# Сохраняем текущее состояние зоопарка в файл
zoo.save_zoo("zoo_OB03")
