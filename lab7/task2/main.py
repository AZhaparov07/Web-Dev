from models import Animal, Pig, Cat

def main():
    a1 = Animal("Animal General", 3, "Boy")
    p1 = Pig("Josh", 2, "Girl", "Very dirty",True)
    c1 = Cat("Oreo", 1, "Boy", 9)

    animals = [a1, p1, c1]

    for i in animals:
        print(i)
        print(i.sleep())
        print(i.make_sound())
        print(i.grow())

    print(p1.roll_in_mud())
    print(p1.check_hunger())
    print(c1.go_haunting())
    print(c1.play())


if __name__ == "__main__":
    main()