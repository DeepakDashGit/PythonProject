# Create a Person class where we will have five attributes and five behaviors.
# Make sure that each type of function is used, and I want you to also create
# the print function, which will print all the instance variable values.

class Person:
    # 🏫 Class variable
    species = "Human"
    def __init__(self, name, age, city, job, salary):
        self.name = name
        self.age = age
        self.city = city
        self.job = job
        self.salary = salary

        # ✅ 1. Instance Method

    def introduce(self):
        print(f"Hi, I am {self.name} from {self.city}.")

        # ✅ 2. Instance Method

    def work(self):
        print(f"{self.name} is working as a {self.job}.")

        # ✅ 3. Instance Method
    def update_salary(self, amount):
        self.salary += amount
        print(f"{self.name}'s new salary is {self.salary}")

        # ✅ 4. Class Method
    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species
        print("Species changed to:", cls.species)

        # ✅ 5. Static Method
    @staticmethod
    def is_adult(age):
        return age >= 18


    def display_details(self):
        print("\nPerson Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)
        print("Job:", self.job)
        print("Salary:", self.salary)

p1 = Person("Deepak", 34, "Cuttack", "QA Engineer", 80000)

p1.introduce()
p1.work()
p1.update_salary(110000)

print(f"Is {p1.name} an adult? {p1.is_adult(35)}")

p1.change_species("Human")
p1.display_details()

