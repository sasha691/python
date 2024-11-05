from faker import Faker
import random

class Human():
    def __init__(self) -> None:
        self.fake = Faker('uk_UA')
        self.gender = random.choice(['male', 'female'])
        self.age = random.randint(18, 99)
        self.city = self.fake.city()
        street = self.fake.street_name()
        buildingNumber = self.fake.building_number()
        apartmentNumber = self.fake.random_int(min=1, max=100)
        self.address = f"{street}, {buildingNumber}, {apartmentNumber}"
        if self.gender == 'male':
            self.name = str(self.fake.first_name_male())
            self.lastname = str(self.fake.last_name_male())
        else: 
            self.name = str(self.fake.first_name_female())
            self.lastname = str(self.fake.last_name_female())

    def __str__(self):
        return f"{self.lastname} - {self.city}, {self.address}"

    def getFullName(self) -> str:
        return self.name + " " + self.lastname
    