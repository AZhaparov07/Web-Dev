class Animal:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def sleep(self):
        return f"{self.name} is sleeping."
    
    def make_sound(self):
        return f"{self.name} is making sound."
    
    def grow(self):
        self.age += 1
        return f"{self.name} is now {self.age} years old."
    
    def __str__(self):
        return f"Animal: {self.name}, Age: {self.age}, Gender: {self.gender}"
    
class Pig(Animal):
    def __init__(self, name, age, gender, dirty, is_hungry):
        super().__init__(name, age, gender)
        self.dirty = dirty
        self.is_hungry = is_hungry
    
    def sleep(self):
        return f"{self.name} is sleeping."
    
    def make_sound(self):
        return f"{self.name} is saying 'Hru Hru'."
    
    def roll_in_mud(self):
        return f"{self.name} is rolling on the mud."

    def __str__(self):
        return f"Pig: {self.name}, Age: {self.age}, Gender: {self.gender}, How dirty: {self.dirty}"
    
    def check_hunger(self):
        if self.is_hungry:
            return f"{self.name} is hungry!"
        else:
            return f"{self.name} is not hungry!"
        
class Cat(Animal):
    def __init__(self, name, age, gender, lives):
        super().__init__(name, age, gender)
        self.lives = lives
    
    def sleep(self):
        return f"{self.name} is sleeping."
    
    def make_sound(self):
        return f"{self.name} is saying 'Meow Meow'."
    
    def go_haunting(self):
        return f"{self.name} went haunting for a mouse."
    
    def play(self):
        return f"{self.name} is playing with a toy."


    def __str__(self):
        return f"Cat: {self.name}, Age: {self.age}, Gender: {self.gender}, How many lives left: {self.lives}"
    

    




