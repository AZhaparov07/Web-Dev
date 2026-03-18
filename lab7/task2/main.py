from models import Animal, Pig, Cat

def main():
    animal1 = Animal("Animal General", 3, "Boy")
    pig1 = Pig("Josh", 2, "Girl", "Very dirty")
    cat1 = Cat("Oreo", 1, "Boy", 9)

    animals = [animal1, pig1, cat1]

    for i in animals:
        print(i)
        print(i.eat())
        print(i.make_sound())

    print(pig1.roll_in_mud())
    print(cat1.go_haunting())


if __name__ == "__main__":
    main()