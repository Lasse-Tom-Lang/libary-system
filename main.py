from random import randint
from datetime import date, timedelta, datetime
import PySimpleGUI as sg
import WindowManager
import DataManager

def main():

  users = DataManager.getUsers()
  books = DataManager.getBooks()

  user = ""

  bookShown = False

  mainWindow = WindowManager.mainWindow()
  while True:
    event, values = mainWindow.read()
    match event:
      case sg.WIN_CLOSED:
        break
      case "-SETTINGS-":
        settingsWindow = WindowManager.settingsWindow()
        while True:
          event, values = settingsWindow.read()
          match event:
            case sg.WIN_CLOSED | "EXIT":
              break
            case "-ADDBOOK-":
              bookWindow = WindowManager.bookWindow()
              while True:
                event, values = bookWindow.read()
                match event:
                  case sg.WIN_CLOSED:
                    break
                  case "EXIT":
                    break
                  case "-BOOKSAVE-":
                    if values["-BOOKNAME-"] != "" and values["-BOOKAUTHOR-"] != "" and values["-BOOKDESCRIPTION-"] != "" and values["-BOOKGENRE-"] != "" and values["-BOOKPAGES-"] != "" and values["-BOOKISBN-"] != "":
                      DataManager.addBook(values["-BOOKNAME-"], values["-BOOKAUTHOR-"], values["-BOOKDESCRIPTION-"], values["-BOOKISBN-"], values["-BOOKGENRE-"], values["-BOOKPAGES-"])
                      books.append(DataManager.Book(values["-BOOKNAME-"], values["-BOOKAUTHOR-"], values["-BOOKDESCRIPTION-"], values["-BOOKISBN-"], False, values["-BOOKGENRE-"], values["-BOOKPAGES-"], 0))
                      break
              bookWindow.close()
            case "-ADDUSER-":
              if (len(users) > 0):
                while True:
                  id = str(randint(10000000, 99999999))
                  for elements in users:
                    if elements.id == id:
                      break
                  else:
                    break
              else:
                id = str(randint(10000000, 99999999))
              userWindow = WindowManager.userWindow(id)
              while True:
                event, values = userWindow.read()
                match event:
                  case sg.WIN_CLOSED | "EXIT":
                    break
                  case "-USERSAVE-":
                    if values["-FIRSTNAME-"] != "" and values["-LASTNAME-"] != "" and values["-EMAIL-"] != "":
                      DataManager.addUser(id, values["-FIRSTNAME-"], values["-LASTNAME-"], values["-EMAIL-"])
                      users.append(DataManager.User(id, values["-FIRSTNAME-"], values["-LASTNAME-"], values["-EMAIL-"], []))
                      break
              userWindow.close()
            case "-OVERDRAWN-":
              overdrawnBooks = []
              for elements in books:
                if elements.borrow and datetime.strptime(elements.borrowUntil, '%Y-%M-%d') < datetime.strptime(str(date.today()), '%Y-%M-%d'):
                  overdrawnBooks.append(elements.name)
              overdrawnWindow = WindowManager.overdrawnWindow(overdrawnBooks)
              while True:
                event, values = overdrawnWindow.read()
                match event:
                  case sg.WIN_CLOSED | "EXIT":
                    break
                  case "-BOOKLIST-":
                    if len(values["-BOOKLIST-"]) == 1:
                      for elements in users:
                        if values["-BOOKLIST-"][0] in elements.books:
                          overdrawnWindow["-USER-"].update(f"{elements.lastName}, {elements.firstName}, {elements.email}")
                          break
              overdrawnWindow.close()
            case "-DELETEBOOK-":
              booksList = []
              for elements in books:
                booksList.append(elements.name)
              deleteBookWindow = WindowManager.deleteBookWindow(booksList)
              while True:
                event, values = deleteBookWindow.read()
                match event:
                  case sg.WIN_CLOSED | "EXIT":
                    break
                  case "-BOOKLIST-":
                    if len(values["-BOOKLIST-"]) == 1:
                      deleteBookWindow["-CONFIRM-"].update(disabled = False)
                  case "-CONFIRM-":
                    confirm = WindowManager.confirmDeleteWindow()
                    match confirm:
                      case "No":
                        pass
                      case "Yes":
                        if (books[booksList.index(values["-BOOKLIST-"][0])].borrow):
                          for elements in users:
                            if (values["-BOOKLIST-"][0] in elements.books):
                              DataManager.giveBackBook(values["-BOOKLIST-"][0], elements.id)
                              del(elements.books[elements.books.index(values["-BOOKLIST-"][0])])
                              break
                        del(books[booksList.index(values["-BOOKLIST-"][0])])
                        del(booksList[booksList.index(values["-BOOKLIST-"][0])])
                        DataManager.removeBook(values["-BOOKLIST-"][0])
                        deleteBookWindow["-BOOKLIST-"].update(booksList)
                        deleteBookWindow["-CONFIRM-"].update(disabled = True)
              deleteBookWindow.close()
        settingsWindow.close()
      case "-IDINPUT-":
        if len(values["-IDINPUT-"]) == 8:
          userExists = False
          for elements in users:
            if values["-IDINPUT-"] == elements.id:
              userExists = True
              user = elements
              mainWindow["-PROFILE-"].update(disabled = False)
              mainWindow["-PROFILELIST-"].update(user.books)
              break
          if (not userExists):
            user = ""
            mainWindow["-PROFILE-"].update(disabled = True)
            mainWindow["-PROFILELIST-"].update([])
            mainWindow["-BORROW-"].update(disabled = True)
            mainWindow["-LENGTHEN-"].update(disabled = True)
            mainWindow["-GIVEBACK-"].update(disabled = True)
        else:
          user = ""
          mainWindow["-PROFILE-"].update(disabled = True)
          mainWindow["-PROFILELIST-"].update([])
          mainWindow["-BORROW-"].update(disabled = True)
          mainWindow["-LENGTHEN-"].update(disabled = True)
          mainWindow["-GIVEBACK-"].update(disabled = True)
      case "-PROFILE-":
        profileWindow = WindowManager.profileWindow(user.firstName, user.lastName, user.email)
        while True:
          event, values = profileWindow.read()
          match event:
            case sg.WIN_CLOSED | "EXIT":
              break
            case "-USERSAVE-":
              DataManager.changeUserData(user.id, values["-FIRSTNAME-"], values["-LASTNAME-"], values["-EMAIL-"])
              user.firstName = values["-FIRSTNAME-"]
              user.lastName = values["-LASTNAME-"]
              user.email = values["-EMAIL-"]
              a = 0
              while a < len(users):
                if (users[a].id == user.id):
                  users[a] = user
                  break
              break
            case "-DELTEACCOUNT-":
              result = WindowManager.confirmDeleteWindow()
              match result:
                case "No":
                  pass
                case "Yes":
                  DataManager.removeUser(user.id)
                  a = 0
                  while a < len(users):
                    if (users[a].id == user.id):
                      del(users[a])
                      del(user)
                      break
                    a += 1
                  mainWindow["-IDINPUT-"].update("")
                  mainWindow["-PROFILE-"].update(disabled = True)
                  mainWindow["-PROFILELIST-"].update([])
                  break
        profileWindow.close()
      case "-PROFILELIST-":
        if (len(values["-PROFILELIST-"]) == 1):
          for elements in books:
            if (elements.name == values["-PROFILELIST-"][0]):
              book = elements
              break
          bookInfo = [
            f"Name: {book.name}",
            f"Description: {book.description}",
            f"Author: {book.author}",
            f"ISBN: {book.isbn}",
            f"Genre: {book.genre}",
            f"Pages: {book.pages}",
            f"Borrowed",
            f"Borrowed until: {book.borrowUntil}"
          ]
          mainWindow["-INFOLIST-"].update(bookInfo)
          bookShown = True
          mainWindow["-LENGTHEN-"].update(disabled = False)
          mainWindow["-GIVEBACK-"].update(disabled = False)
      case "-LENGTHEN-":
        DataManager.lenghtenBook(book.name, str(date.today() + timedelta(2)))
        bookInfo[7] = f"Borrowed until: {str(date.today() + timedelta(2))}"
        mainWindow["-INFOLIST-"].update(bookInfo)
        book.borrowUntil = str(date.today() + timedelta(2))
        for elements in books:
          if elements.name == book.name:
            elements.borrowUntil = str(date.today() + timedelta(2))
            break
      case "-GIVEBACK-":
        DataManager.giveBackBook(book.name, user.id)
        del(bookInfo[7])
        del(bookInfo[6])
        mainWindow["-INFOLIST-"].update(bookInfo)
        del(user.books[user.books.index(book.name)])
        mainWindow["-PROFILELIST-"].update(user.books)
        book.borrow = False
        book.borrowUntil = 0
        for elements in books:
          if elements.name == book.name:
            elements.borrowUntil = 0
            elements.borrow = False
            break
        mainWindow["-LENGTHEN-"].update(disabled = True)
        mainWindow["-GIVEBACK-"].update(disabled = True)
        mainWindow["-BORROW-"].update(disabled = False)
      case "-BORROW-":
        DataManager.borrowBook(user.id, book.name, str(date.today() + timedelta(2)))
        user.books.append(book.name)
        mainWindow["-PROFILELIST-"].update(user.books)
        bookInfo.append(f"Borrowed")
        bookInfo.append(f"Borrowed until: {str(date.today() + timedelta(2))}")
        mainWindow["-INFOLIST-"].update(bookInfo)
        for elements in books:
          if elements.name == book.name:
            elements.borrowUntil = str(date.today() + timedelta(2))
            elements.borrow = True
            break
        mainWindow["-BORROW-"].update(disabled = True)
        mainWindow["-LENGTHEN-"].update(disabled = False)
        mainWindow["-GIVEBACK-"].update(disabled = False)
      case "-INFOLIST-":
        if not bookShown and len(values["-INFOLIST-"]) == 1:
          for elements in books:
            if (elements.name == values["-INFOLIST-"][0]):
              book = elements
              break
          if book.borrow:
            bookInfo = [
              f"Name: {book.name}",
              f"Description: {book.description}",
              f"Author: {book.author}",
              f"ISBN: {book.isbn}",
              f"Genre: {book.genre}",
              f"Pages: {book.pages}",
              f"Borrowed",
              f"Borrowed until: {book.borrowUntil}"
            ]
            mainWindow["-INFOLIST-"].update(bookInfo)
            bookShown = True
            if (user != ""):
              if (book.name in user.books):
                mainWindow["-LENGTHEN-"].update(disabled = False)
                mainWindow["-GIVEBACK-"].update(disabled = False)
          else:
            bookInfo = [
              f"Name: {book.name}",
              f"Description: {book.description}",
              f"Author: {book.author}",
              f"ISBN: {book.isbn}",
              f"Genre: {book.genre}",
              f"Pages: {book.pages}"
            ]
            mainWindow["-INFOLIST-"].update(bookInfo)
            bookShown = True
            if (user != ""):
              mainWindow["-BORROW-"].update(disabled = False)
      case "-BOOKINPUT-":
        if (values["-BOOKINPUT-"] != ""):
          bookList = []
          for elements in books:
            if (elements.name.find(values["-BOOKINPUT-"]) != -1):
              bookList.append(elements.name)
          mainWindow["-INFOLIST-"].update(bookList)
          mainWindow["-BORROW-"].update(disabled = True)
          mainWindow["-LENGTHEN-"].update(disabled = True)
          mainWindow["-GIVEBACK-"].update(disabled = True)
          bookShown = False
  mainWindow.close()

if __name__ == "__main__":
  main()