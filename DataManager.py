import json

class User:
  def __init__(self, id, firstName, lastName, email, books):
    self.id = id
    self.firstName = firstName
    self.lastName = lastName
    self.email = email
    self.books = books

class Book:
  def __init__(self, name, author, description, isbn, borrow, genre, pages, borrowUntil):
    self.name = name
    self.author = author
    self.description = description
    self.isbn = isbn
    self.borrow = borrow
    self.genre = genre
    self.pages = pages
    self.borrowUntil = borrowUntil

def getBooks():
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

def getUsers():
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

def changeUserData(id, firstName, lastName, email):
  with open("data.json", "r") as file:
    data = file.read()
  data = json.loads(data)
  data["users"][id]["firstName"] = firstName
  data["users"][id]["lastName"] = lastName
  data["users"][id]["email"] = email
  with open("data.json", "w") as file:
    json.dump(data, file)

def addUser(id, firstName, lastName, email):
  with open("data.json", "r") as file:
    data = file.read()
  data = json.loads(data)
  data["users"].update({id: {"firstName": firstName, "lastName": lastName, "email": email, "books": []}})
  with open("data.json", "w") as file:
    json.dump(data, file)

def removeUser(id):
  with open("data.json", "r") as file:
    data = file.read()
  data = json.loads(data)
  del(data["users"][id])
  with open("data.json", "w") as file:
    json.dump(data, file)

def removeBook(name):
  with open("data.json", "r") as file:
    data = file.read()
  data = json.loads(data)
  del(data["books"][name])
  with open("data.json", "w") as file:
    json.dump(data, file)

def addBook(name, author, description, isbn, genre, pages):
  with open("data.json", "r") as file:
    data = file.read()
  data = json.loads(data)
  data["books"].update({name: {"author": author, "description": description, "isbn": isbn, "borrow": False, "genre": genre, "pages": pages, "borrowUntil": 0}})
  with open("data.json", "w") as file:
    json.dump(data, file)

def borrowBook(userID, bookName, borrowUntil):
  with open("data.json", "r") as file:
    data = file.read()
  data = json.loads(data)
  data["books"][bookName]["borrowUntil"] = borrowUntil
  data["books"][bookName]["borrow"] = True
  data["users"][userID]["books"].append(bookName)
  with open("data.json", "w") as file:
    json.dump(data, file)

def lenghtenBook(bookName, borrowUntil):
  with open("data.json", "r") as file:
    data = file.read()
  data = json.loads(data)
  data["books"][bookName]["borrowUntil"] = borrowUntil
  with open("data.json", "w") as file:
    json.dump(data, file)

def giveBackBook(bookName, userID):
  with open("data.json", "r") as file:
    data = file.read()
  data = json.loads(data)
  data["books"][bookName]["borrowUntil"] = 0
  data["books"][bookName]["borrow"] = False
  del(data["users"][userID]["books"][data["users"][userID]["books"].index(bookName)])
  with open("data.json", "w") as file:
    json.dump(data, file)