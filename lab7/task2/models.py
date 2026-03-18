class Animal:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def eat(self):
        return f"{self.name} is eating."
    
    def make_sound(self):
        return f"{self.name} is making sound."
    
    def __str__(self):
        return f"Animal: {self.name}, Age: {self.age}, Gender: {self.gender}"
    
class Pig(Animal):
    def __init__(self, name, age, gender, dirty):
        super().__init__(name, age, gender)
        self.dirty = dirty
    
    def eat(self):
        return f"{self.name} is eating."
    
    def make_sound(self):
        return f"{self.name} is saying 'Hru Hru'."
    
    def roll_in_mud(self):
        return f"{self.name} is rolling on the mud."

    def __str__(self):
        return f"Pig: {self.name}, Age: {self.age}, Gender: {self.gender}, How dirty: {self.dirty}"
    
class Cat(Animal):
    def __init__(self, name, age, gender, lives):
        super().__init__(name, age, gender)
        self.lives = lives
    
    def eat(self):
        return f"{self.name} is eating."
    
    def make_sound(self):
        return f"{self.name} is saying 'Meow Meow'."
    
    def go_haunting(self):
        return f"{self.name} went haunting for a mouse."

    def __str__(self):
        return f"Cat: {self.name}, Age: {self.age}, Gender: {self.gender}, How many lives left: {self.lives}"
    

    




