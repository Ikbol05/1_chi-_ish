

# 1 chi masala

from abc import ABC,abstractmethod
class Animal(ABC):

    def __init__(self, nomi, uzunligi, ogirligi, tezligi):
        self.nomi = nomi
        self.uzunligi = uzunligi
        self.ogirligi = ogirligi
        self.tezligi = tezligi


    def get_nomi(self):
        pass

    @abstractmethod
    def get_uzunligi(self):
        pass

    @abstractmethod
    def get_ogirligi(self):
        pass

    @abstractmethod
    def get_tezligi(self):
        pass
#
#
# class Dog(Animal):
#
#     def __init__(self, nomi, uzunligi, ogirligi, tazligi):
#         super().__init__(nomi, uzunligi, ogirligi, tazligi)
#
#     def gat_nomi(self):
#         return self.nomi
#
#     def get_uzunligi(self):
#         return self.uzunligi
#
#     def get_ogirligi(self):
#         return self.ogirligi
#
#     def get_tezligi(self):
#         return self.tezligi
#
#     def dog_info(self):
#         return f"Nomi: {self.nomi}, Tezligi: {self.tezligi}km/s, Og'irligi: {self.ogirligi}kg"
#
#
# class Cat(Animal):
#
#     def __init__(self, nomi, uzunligi, ogirligi, tezligi):
#         super().__init__(nomi, uzunligi, ogirligi, tezligi)
#
#     def gat_nomi(self):
#         return self.nomi
#
#     def get_uzunligi(self):
#         return self.uzunligi
#
#     def get_ogirligi(self):
#         return self.ogirligi
#
#     def get_tezligi(self):
#         return self.tezligi
#
#     def cat_info(self):
#         return f"Nomi: {self.nomi}, Tezligi: {self.tezligi}km/s, Og'irligi: {self.ogirligi}kg"
#
#
# class Elephant(Animal):
#
#     def __init__(self, nomi, uzunligi, ogirligi, tezligi):
#         super().__init__(nomi, uzunligi, ogirligi, tezligi)
#
#     def gat_nomi(self):
#         return self.nomi
#
#     def get_uzunligi(self):
#         return self.uzunligi
#
#     def get_ogirligi(self):
#         return self.ogirligi
#
#     def get_tezligi(self):
#         return self.tezligi
#
#     def elephant_info(self):
#         return f"Nomi: {self.nomi}, Tezligi: {self.tezligi}km/s, Og'irligi: {self.ogirligi}t"
#
#
#
# user1 = Dog("reks", "60", "20", "40")
# print(user1.dog_info())
#
#
# user2 = Cat("Malish", 35, 5, 30)
# print(user2.cat_info())
#
#
# user3 = Elephant("Ikkikalla", 9, 5.4, 20)
# print(user3.elephant_info())

#=======================================================================================================================


# 2 chi masala
# import string
# class Tekshirish:
#
#     @staticmethod
#     def name_t(name):
#         for i in name:
#             if i not in string.ascii_letters:
#                 return False
#         return True
#
#
#     @staticmethod
#     def birdh_year(year):
#         for i in year:
#             if i not in string.digits:
#                 return False
#         return True
#
#
#     @staticmethod
#     def address(address):
#         for i in address:
#             if i is not string.ascii_letters:
#                 return False
#         return True
#
#
#
#     @staticmethod
#     def phon_n(phone: str):
#         if phon.startswith("+998") and len(phone) == 13:
#             if phone[4:].isdigit():
#                 return True
#             return False
#         else:
#             return False
#
#
#
#     @staticmethod
#     def passport(passport: str):
#         if passport[2:].isdigit():
#             if passport.startswith(string.ascii_uppercase):
#                 return True
#             return False
#         else:
#             return False
#
#
#
# class Questionnaria:
#     def __init__(self, full_name, birth_year, address, phone_number, passport):
#         self.full_name = full_name
#         self.birth_year = birth_year
#         self.address = address
#         self.phone_number = phone_number
#         self.passport = passport
#
#
#     def user_info(self):
#         if Tekshirish.name_t(self.full_name) and Tekshirish.birdh_year(self.birth_year) and Tekshirish.address(self.address) and Tekshirish.phon_n(self.phone_number) and Tekshirish.passport(self.passport):
#             return [self.full_name, self.birth_year, self.address, self.phone_number, self.passport]
#         print("Ma'lumotlar xato")
#
#
#
#
#
# import csv
# while True:
#     name = input("Ismni kriting: ")
#
#     if name.lower() == "stop":
#         break
#
#     year = input("Tug'ilgan yilini kriting: ")
#     address = input("Adresni kriting: ")
#     phon = input("Telefon raqamni kriting: ")
#     passport = input("Passportni kriting: ")
#
#
#
#     with open("percon_ingo.csv", mode="a") as file:
#         writer = csv.writer(file, lineterminator="\n")
#         writer.writerow(
#             Questionnaria(name, year, address, phon, passport).user_info()
# )







































