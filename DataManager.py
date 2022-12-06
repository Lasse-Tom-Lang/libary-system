"""
  The DataManager handels the reading and writing to the json file
"""

import json
from datetime import date

class Book:
  """
    The definition of a book
  """
  def __init__(self, name: str, author: str, description: str, isbn: str, borrow: bool, genre: str, pages: int, borrowUntil: date):
    self.name = name
    self.author = author
    self.description = description
    self.isbn = isbn
    self.borrow = borrow
    self.genre = genre
    self.pages = pages
    self.borrowUntil = borrowUntil

class User:
  """
    The definition of a user
  """
  def __init__(self, id: int, firstName: str, lastName: str, email: str, books: list[Book]):
    self.id = id
    self.firstName = firstName
    self.lastName = lastName
    self.email = email
    self.books = books

def getBooks() -> list[Book]:
  """
    Returns all books from the json file

    :return: (list)
  """

  with open("data.json", "r") as file:
    data = file.read()
  data = json.loads(data)["books"]
  books = []
  for elements in data:
    books.append(Book(
      elements,
      data[elements]["author"],
      data[elements]["description"],
      data[elements]["isbn"],
      data[elements]["borrow"],
      data[elements]["genre"],
      data[elements]["pages"],
      data[elements]["borrowUntil"]
    ))
  return books

def getUsers() -> list[User]:
  """
    Returns all users from the json file

    :return: (list)
  """
  with open("data.json", "r") as file:
    data = file.read()
  data = json.loads(data)["users"]
  users = []
  for elements in data:
    users.append(User(
      elements,
      data[elements]["firstName"],
      data[elements]["lastName"],
      data[elements]["email"],
      data[elements]["books"]
    ))
  return users

def changeUserData(id: int, firstName: str, lastName: str, email: str):
  """
    Changes user data and saves it to the json file
    :param id: The id of the user
    :type id: (int)
    :param firstName: The first name of the user
    :type firstName: (str)
    :param lastName: The last name of the user
    :type lastName: (str)
    :param email: The email address of the user
    :type email: (str)
  """
  with open("data.json", "r") as file:
    data = file.read()
  data = json.loads(data)
  data["users"][id]["firstName"] = firstName
  data["users"][id]["lastName"] = lastName
  data["users"][id]["email"] = email
  with open("data.json", "w") as file:
    json.dump(data, file)

def addUser(id: int, firstName: str, lastName: str, email: str):
  """
    Adds a user to the json file

    :param id: The id of the new user
    :type id: (int)
    :param firstName: The first name of the new user
    :type firstName: (str)
    :param lastName: The last name of the new user
    :type lastName: (str)
    :param email: The email address of the new user
    :type email: (str)
  """
  with open("data.json", "r") as file:
    data = file.read()
  data = json.loads(data)
  data["users"].update({id: {"firstName": firstName, "lastName": lastName, "email": email, "books": []}})
  with open("data.json", "w") as file:
    json.dump(data, file)

def removeUser(id: int):
  """
    Removes a user from the json file

    :param id: The id of the user to delete
    :type id: (int)
  """
  with open("data.json", "r") as file:
    data = file.read()
  data = json.loads(data)
  del(data["users"][id])
  with open("data.json", "w") as file:
    json.dump(data, file)

def removeBook(name: str):
  """
    Removes a book from the json file

    :param name: The name of the book to delete
    :type name: (str)
  """
  with open("data.json", "r") as file:
    data = file.read()
  data = json.loads(data)
  del(data["books"][name])
  with open("data.json", "w") as file:
    json.dump(data, file)

def addBook(name: str, author: str, description: str, isbn: str, genre: str, pages: int):
  """
    Adds a book to the json file

    :param name: The name of the new book
    :type name: (str)
    :param author: The author of the new book
    :type author: (str)
    :param description: The description of the new book
    :type description: (str)
    :param isbn: The isbn of the new book
    :type isbn: (str)
    :param genre: The genre of the new book
    :type genre: (str)
    :param pages: The count of pages of the new book
    :type pages: (int)
  """
  with open("data.json", "r") as file:
    data = file.read()
  data = json.loads(data)
  data["books"].update({name: {"author": author, "description": description, "isbn": isbn, "borrow": False, "genre": genre, "pages": pages, "borrowUntil": 0}})
  with open("data.json", "w") as file:
    json.dump(data, file)

def borrowBook(userID: int, bookName: str, borrowUntil: date):
  """
    Borrows a book as a specific user

    :param userID: The id of user who borrows the book
    :type userID: (int)
    :param bookName: The name of the book
    :type bookName: (str)
    :param borrowUntil: Until when the book is borrowed
    :type borrowUntil: (date)
  """
  with open("data.json", "r") as file:
    data = file.read()
  data = json.loads(data)
  data["books"][bookName]["borrowUntil"] = borrowUntil
  data["books"][bookName]["borrow"] = True
  data["users"][userID]["books"].append(bookName)
  with open("data.json", "w") as file:
    json.dump(data, file)

def lenghtenBook(bookName: str, borrowUntil: date):
  """
    Lenghtens a book

    :param bookName: The name of the book
    :type bookName: (str)
    :param borrowUntil: Until when the book is borrowed
    :type borrowUntil: (date)
  """

  with open("data.json", "r") as file:
    data = file.read()
  data = json.loads(data)
  data["books"][bookName]["borrowUntil"] = borrowUntil
  with open("data.json", "w") as file:
    json.dump(data, file)

def giveBackBook(bookName: str, userID: int):
  """
    Gives back a book as a specific user

    :param bookName: The name of the book
    :type bookName: (str)
    :param userID: The id of the user
    :type userID: (int)
  """
  with open("data.json", "r") as file:
    data = file.read()
  data = json.loads(data)
  data["books"][bookName]["borrowUntil"] = 0
  data["books"][bookName]["borrow"] = False
  del(data["users"][userID]["books"][data["users"][userID]["books"].index(bookName)])
  with open("data.json", "w") as file:
    json.dump(data, file)