# class konspekt:
#     """
#     [obj, c, b, d]

#     mro

#     Mixins - Примеси

#     В конце название хранить Mixins

#     PostMixin

#     Не должен хранить состоянии



#     """

# class CreateMixin:
#     def create(self):
#         print("Create")

# class UpdateMixin:
#     def update(self):
#         print("Update")

# class DeleteMixin:
#     def delete(self):
#         print("Delete")

# class Restoran(CreateMixin,
#                UpdateMixin,
#                DeleteMixin
#                ):
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
    
#     # def create_restoran(self):
#     #     self.create()


# restoran1 = Restoran("Freshbox", "Isanova")
# restoran1.create()
# restoran1.delete()
# restoran1.update()


            # class LoginRuquiredMixin:
            #     pass

            # @login_required


# from multiprocessing import AuthenticationError


# users = {
#     "user1": 123,
#     "user2": 321,
# }

# def login_required(func):
#     def wrapper(user):
#         print(user)
#         if user not in users.values():
#             raise AuthenticationError("User is not Authenticated")
#         func(user)
#         print("Успешно авторизован")
#         return
#     return wrapper
# @login_required
# def some_page(user):
#     pass
# some_page(123)





# from multiprocessing import AuthenticationError


# class View:
#     def __init__(self) -> None:
#         self.users = ["john", "raychel"]

#     # def dispatch(self):
#     #     print("Метод диспач")
#     #     self.users

# class LoginRequiredMixin:
#     def dispatch(self, request, user):
#         if user not in self.users:
#             raise AuthenticationError("User is not Authenticated")
#         return self.users

# class AboutPage(View, LoginRequiredMixin):
#     pass

# obj = AboutPage()
# obj.dispatch("test", "john")



# Композиция

# class Author:
#     def __init__(self) -> None:
#         self.name = "John"
    
#     def get(self):
#         pass

# class Restoran:
#     def __init__(self, name , address):
#         self.name = name
#         self.address = address
#         self.owner = Author()
    
# res = Restoran("test", "test")
# print(res.owner.name)       
# res.owner.get()


# class Author:
#     def __init__(self) -> None:
#         self.name = "John"

# class Restoran:
#     def __init__(self, name , address, author):
#         self.name = name
#         self.address = address
#         self.owner = author
    
# author = Author()
# res = Restoran("test", "test", author)



# ООП

# class 

# instance -> объект -> экземпляр класса

# self

# __new__(cls)

# class var vs instance var

# что такое Полиморфизм

# DRY = don't repeat yourself

# KISS - keep it simple stupid



# SOLID

# S single responsibility

# RetrieveUpdateDeleteView






































