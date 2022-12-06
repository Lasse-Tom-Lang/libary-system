"""
  The WindowManager handels creating new windows
"""

import PySimpleGUI as sg

backgroundColor = "#343434"
elementColor = "#404040"
textColor = "#FFFFFF"

def mainWindow() -> sg.Window:
  """
    Returns a new main window as a PySimpleGUI window

    :return: (sg.Window)
  """
  mainLayout = [
    [
      sg.Column(
        [
          [
            sg.Input(
              background_color=elementColor,
              text_color=textColor,
              font="Arial 16",
              size=(15, 1),
              key="-IDINPUT-",
              enable_events=True
            ),
            sg.Button(
              "Profile",
              font="Arial 16",
              button_color=(textColor, elementColor),
              key="-PROFILE-",
              disabled=True
            )
          ],
          [
            sg.Listbox(
              [],
              background_color = elementColor,
              text_color=textColor,
              expand_x=True,
              expand_y=True,
              sbar_arrow_color=textColor,
              sbar_background_color=backgroundColor,
              enable_events=True,
              horizontal_scroll = True,
              font="Arial 16",
              key="-PROFILELIST-"
            )
          ]
        ], 
        background_color = backgroundColor,
        expand_x=True,
        expand_y=True
      ),
      sg.VSeperator(),
      sg.Column(
        [
          [
            sg.Input(
              background_color=elementColor,
              text_color=textColor,
              font="Arial 16",
              size=(1, 1),
              key="-BOOKINPUT-",
              enable_events=True,
              expand_x=True
            ),
            sg.Button(
              "Settings",
              font="Arial 16",
              button_color=(textColor, elementColor),
              key="-SETTINGS-"
            )
          ],
          [
            sg.Listbox(
              [],
              background_color = elementColor,
              text_color=textColor,
              expand_x=True,
              expand_y=True,
              sbar_arrow_color=textColor,
              sbar_background_color=backgroundColor,
              enable_events=True,
              horizontal_scroll = True,
              font="Arial 16",
              key="-INFOLIST-"
            )
          ],
          [
            sg.Button(
              "Borrow",
              font="Arial 16",
              button_color=(textColor, elementColor),
              key="-BORROW-",
              expand_x=True,
              disabled=True
            ),
            sg.Button(
              "Lengthen",
              font="Arial 16",
              button_color=(textColor, elementColor),
              key="-LENGTHEN-",
              expand_x=True,
              disabled=True
            ),
            sg.Button(
              "Give back",
              font="Arial 16",
              button_color=(textColor, elementColor),
              key="-GIVEBACK-",
              expand_x=True,
              disabled=True
            )
          ]
        ],
        background_color=backgroundColor,
        expand_x=True,
        expand_y=True
      )
    ]
  ]
  return sg.Window(
    "Libary system",
    mainLayout,
    location=(100, 100),
    size=(800, 600),
    resizable=True,
    background_color=backgroundColor
  )

def settingsWindow() -> sg.Window:
  """
    Returns a new settings window as a PySimpleGUI window

    :return: (sg.Window)
  """
  settingsLayout = [
    [
      sg.Button(
        "Add book",
        font="Arial 16",
        button_color=(textColor, elementColor),
        key="-ADDBOOK-",
        expand_x=True,
        expand_y=True
      )
    ],
    [
      sg.Button(
        "Add user",
        font="Arial 16",
        button_color=(textColor, elementColor),
        key="-ADDUSER-",
        expand_x=True,
        expand_y=True
      )
    ],
    [
      sg.Button(
        "Overdrawn books",
        font="Arial 16",
        button_color=(textColor, elementColor),
        key="-OVERDRAWN-",
        expand_x=True,
        expand_y=True
      )
    ],
    [
      sg.Button(
        "Delete book",
        font="Arial 16",
        button_color=(textColor, elementColor),
        key="-DELETEBOOK-",
        expand_x=True,
        expand_y=True
      )
    ],
    [
      sg.Button(
        "Close",
        font="Arial 16",
        button_color=(textColor, elementColor),
        key="EXIT",
        expand_x=True,
        expand_y=True
      )
    ]
  ]
  return sg.Window(
    "Settings",
    settingsLayout,
    location=(110, 100),
    size=(180, 230),
    background_color=backgroundColor
  )

def bookWindow() -> sg.Window:
  """
    Returns a new window for adding books as a PySimpleGUI window

    :return: (sg.Window)
  """
  bookLayout = [
    [
      sg.Text(
        "Add book",
        text_color=textColor,
        background_color=backgroundColor,
        font="Arial 25"
      )
    ],
    [
      sg.Text(
        "Name:",
        text_color=textColor,
        background_color=backgroundColor,
        font="Arial 16",
        size=(5, 1)
      ),
      sg.In(
        key="-BOOKNAME-",
        background_color=elementColor,
        text_color=textColor,
        expand_x=True,
        font="Arial 16"
      )
    ],
    [
      sg.Text(
        "Author:",
        text_color=textColor,
        background_color=backgroundColor,
        font="Arial 16",
        size=(5, 1)
      ),
      sg.In(
        key="-BOOKAUTHOR-",
        background_color=elementColor,
        text_color=textColor,
        expand_x=True,
        font="Arial 16"
      )
    ],
    [
      sg.Text(
        "Genre:",
        text_color=textColor,
        background_color=backgroundColor,
        font="Arial 16",
        size=(5, 1)
      ),
      sg.In(
        key="-BOOKGENRE-",
        background_color=elementColor,
        text_color=textColor,
        expand_x=True,
        font="Arial 16"
      )
    ],
    [
      sg.Text(
        "Pages:",
        text_color=textColor,
        background_color=backgroundColor,
        font="Arial 16",
        size=(5, 1)
      ),
      sg.In(
        key="-BOOKPAGES-",
        background_color=elementColor,
        text_color=textColor,
        expand_x=True,
        font="Arial 16"
      )
    ],
    [
      sg.Text(
        "ISBN:",
        text_color=textColor,
        background_color=backgroundColor,
        font="Arial 16",
        size=(5, 1)
      ),
      sg.In(
        key="-BOOKISBN-",
        background_color=elementColor,
        text_color=textColor,
        expand_x=True,
        font="Arial 16"
      )
    ],
    [
      sg.Text(
        "Description:",
        text_color=textColor,
        background_color=backgroundColor,
        font="Arial 16",
        size=(10, 1)
      ),
      sg.In(
        key="-BOOKDESCRIPTION-",
        background_color=elementColor,
        text_color=textColor,
        expand_x=True,
        font="Arial 16"
      )
    ],
    [
      sg.Button(
        "Exit",
        font="Arial 16",
        button_color=(textColor, elementColor),
        key="EXIT",
        expand_x=True
      ),
      sg.Button(
        "Save",
        font="Arial 16",
        button_color=(textColor, elementColor),
        key="-BOOKSAVE-",
        expand_x=True
      )
    ]
  ]
  return sg.Window(
    "Add book",
    bookLayout,
    location=(120, 100),
    size=(350, 260),
    resizable=True,
    background_color=backgroundColor,
    element_justification="center"
  )

def userWindow(id: int) -> sg.Window:
  """
    Returns a new window to add users as a PySimpleGUI window

    :param id: An id for the new user
    :type id: (int)
    :return: (sg.Window)
  """
  userLayout = [
    [
      sg.Text(
        "Add user",
        text_color=textColor,
        background_color=backgroundColor,
        font="Arial 25"
      )
    ],
    [
      sg.Text(
        "First name:",
        text_color=textColor,
        background_color=backgroundColor,
        font="Arial 16",
        size=(10, 1)
      ),
      sg.In(
        key="-FIRSTNAME-",
        background_color=elementColor,
        text_color=textColor,
        expand_x=True,
        font="Arial 16"
      )
    ],
    [
      sg.Text(
        "Last name:",
        text_color=textColor,
        background_color=backgroundColor,
        font="Arial 16",
        size=(10, 1)
      ),
      sg.In(
        key="-LASTNAME-",
        background_color=elementColor,
        text_color=textColor,
        expand_x=True,
        font="Arial 16"
      )
    ],
    [
      sg.Text(
        "Email:",
        text_color=textColor,
        background_color=backgroundColor,
        font="Arial 16",
        size=(10, 1)
      ),
      sg.In(
        key="-EMAIL-",
        background_color=elementColor,
        text_color=textColor,
        expand_x=True,
        font="Arial 16"
      )
    ],
    [
      sg.Text(
        "ID:",
        text_color=textColor,
        background_color=backgroundColor,
        font="Arial 16",
        size=(10, 1)
      ),
      sg.In(
        id,
        key="-ID-",
        background_color=elementColor,
        text_color=textColor,
        expand_x=True,
        font="Arial 16",
        disabled=True
      )
    ],
    [
      sg.Button(
        "Exit",
        font="Arial 16",
        button_color=(textColor, elementColor),
        key="EXIT",
        expand_x=True
      ),
      sg.Button(
        "Save",
        font="Arial 16",
        button_color=(textColor, elementColor),
        key="-USERSAVE-",
        expand_x=True
      )
    ]
  ]
  return sg.Window(
    "Add user",
    userLayout,
    location=(120, 100),
    size=(350, 260),
    resizable=True,
    background_color=backgroundColor,
    element_justification="center"
  )

def profileWindow(firstName: str, lastName: str, email: str) -> sg.Window:
  """
    Returns a new window with the data from a user as a PySimpleGUI window

    :param firstName: The first name of the user
    :type firstName: (str)
    :param lastName: The last name of the user
    :type lastName: (str)
    :param email: The email address of the user
    :type email: (str)
    :return: (sg.Window)
  """
  profileLayout = [
    [
      sg.Text(
        "Profile",
        text_color=textColor,
        background_color=backgroundColor,
        font="Arial 25"
      )
    ],
    [
      sg.Text(
        "First name:",
        text_color=textColor,
        background_color=backgroundColor,
        font="Arial 16",
        size=(9, 1)
      ),
      sg.In(
        firstName,
        key="-FIRSTNAME-",
        background_color=elementColor,
        text_color=textColor,
        expand_x=True,
        font="Arial 16"
      )
    ],
    [
      sg.Text(
        "Last name:",
        text_color=textColor,
        background_color=backgroundColor,
        font="Arial 16",
        size=(9, 1)
      ),
      sg.In(
        lastName,
        key="-LASTNAME-",
        background_color=elementColor,
        text_color=textColor,
        expand_x=True,
        font="Arial 16"
      )
    ],
    [
      sg.Text(
        "Email:",
        text_color=textColor,
        background_color=backgroundColor,
        font="Arial 16",
        size=(9, 1)
      ),
      sg.In(
        email,
        key="-EMAIL-",
        background_color=elementColor,
        text_color=textColor,
        expand_x=True,
        font="Arial 16"
      )
    ],
    [
      sg.Button(
        "Delete Account",
        font="Arial 16",
        button_color=(textColor, elementColor),
        key="-DELTEACCOUNT-",
        expand_x=True
      )
    ],
    [
      sg.Button(
        "Exit",
        font="Arial 16",
        button_color=(textColor, elementColor),
        key="EXIT",
        expand_x=True
      ),
      sg.Button(
        "Save",
        font="Arial 16",
        button_color=(textColor, elementColor),
        key="-USERSAVE-",
        expand_x=True
      )
    ]
  ]
  return sg.Window(
    "Profile",
    profileLayout,
    location=(120, 100),
    size=(350, 200),
    resizable=True,
    background_color=backgroundColor,
    element_justification="center"
  )

def confirmDeleteWindow() -> sg.popup_yes_no:
  """
    Returns a new popup to confirm delete as a PySimpleGUI popup

    :return: (sg.popup_yes_no)
  """
  return sg.popup_yes_no(
    "Are you sure to delete this?",
    button_color=(textColor, elementColor),
    background_color=backgroundColor,
    location=(130, 100),
    text_color=textColor,
    no_titlebar=True
  )

def overdrawnWindow(overdrawnBooks: list) -> sg.Window:
  """
    Returns a new window with all overdrawn books from a user as a PySimpleGUI window

    :param overdrawnBooks: A list of all overdrawn books
    :type overdrawnBooks: (list)
    :return: (sg.Window)
  """
  overdrawnLayout = [
    [
      sg.Text(
        "Overdrawn books",
        text_color=textColor,
        background_color=backgroundColor,
        font="Arial 25"
      )
    ],
    [
      sg.Listbox(
        overdrawnBooks,
        background_color = elementColor,
        text_color=textColor,
        expand_x=True,
        expand_y=True,
        sbar_arrow_color=textColor,
        sbar_background_color=backgroundColor,
        enable_events=True,
        horizontal_scroll = True,
        font="Arial 16",
        key="-BOOKLIST-"
      )
    ],
    [
      sg.Text(
        "",
        expand_x=True,
        key="-USER-",
        font="Arial 16",
        text_color=textColor,
        background_color=backgroundColor
      )
    ],
    [
      sg.Button(
        "Exit",
        font="Arial 16",
        button_color=(textColor, elementColor),
        key="EXIT",
        expand_x=True
      )
    ]
  ]
  return sg.Window(
    "Overdrawn",
    overdrawnLayout,
    location=(120, 100),
    size=(300, 400),
    resizable=True,
    background_color=backgroundColor,
    element_justification="center"
  )

def deleteBookWindow(books: list) -> sg.Window:
  """
    Returns a new window to delete books as a PySimpleGUI window

    :param books: Books that can be deleted
    :type books: (list)
    :return: (sg.Window)
  """
  deleteBookLayout = [
    [
      sg.Text(
        "Delete books",
        text_color=textColor,
        background_color=backgroundColor,
        font="Arial 25"
      )
    ],
    [
      sg.Listbox(
        books,
        background_color = elementColor,
        text_color=textColor,
        expand_x=True,
        expand_y=True,
        sbar_arrow_color=textColor,
        sbar_background_color=backgroundColor,
        enable_events=True,
        horizontal_scroll = True,
        font="Arial 16",
        key="-BOOKLIST-"
      )
    ],
    [
      sg.Button(
        "Delete book",
        font="Arial 16",
        button_color=(textColor, elementColor),
        key="-CONFIRM-",
        expand_x=True
      )
    ],
    [
      sg.Button(
        "Exit",
        font="Arial 16",
        button_color=(textColor, elementColor),
        key="EXIT",
        expand_x=True
      )
    ]
  ]
  return sg.Window(
    "Delete book",
    deleteBookLayout,
    location=(120, 100),
    size=(300, 400),
    resizable=True,
    background_color=backgroundColor,
    element_justification="center"
  )