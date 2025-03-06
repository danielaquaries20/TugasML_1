class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

# # instantiate the Parrot class
papi = Parrot("Papi", 3)
greeny = Parrot("Greeny", 5)

# access the class attributes
print("Papi is a " + papi.species)
print("Greeny is also a " + greeny.species)

# access the instance attributes
print(papi.name + " is " + str(papi.age) + " years old")
print(greeny.name + " is " + str(greeny.age) + " years old")