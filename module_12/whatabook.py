# Kyle Jones
# Module 12.3/WhatABook Application
# May 5 2022
# https://github.com/widg3tt/csd-310

import sys
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def show_menu():
    print("\n-- Main Menu --")

    print("1. View Books\n2. View Store Locations\n3. My Account\n4. Exit Application")

    try:
        choice = int(input('(Enter "1" to view all book listings): '))

        return choice
    except ValueError:
        print("\nInvalid number, program terminated...\n")

        sys.exit(0)

def show_books(_cursor):
    # Inner Join query
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    # Get all results from the cursor object
    books = _cursor.fetchall()

    print("\n-- DISPLAYING BOOK LISTINGS --")

    for book in books:
        print("Book Name: {}\nAuthor: {}\nDetails: {}\n".format(book[1], book[2], book[3]))

def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n-- DISPLAYING STORE LOCATIONS --")

    for location in locations:
        print("Locale: {}\n".format(location[1]))

def validate_user():
    # Validate the user's ID

    try:
        user_id = int(input('\nEnter a customer id (Enter "1" for user_id 1>: '))

        if user_id < 0 or user_id > 3:
            print("\nInvalid customer number, program terminated...\n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\nInvalid number, program terminated...\n")

        sys.exit(0)

def show_account_menu():
    # display the users account menu

    try:
        print("\n-- Customer Menu --")
        print("1. Wishlist\n2. Add Book\n3. Back to Main Menu")
        account_option = int(input('(Enter "1" for user wishlist): '))

        return account_option
    except ValueError:
        print("\nInvalid number, program terminated...\n")

        sys.exit(0)

def show_wishlist(_cursor, _user_id):
    # query the database for a list of books added to the users wishlist

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " +
                    "FROM wishlist " +
                    "INNER JOIN user ON wishlist.user_id = user.user_id " +
                    "INNER JOIN book ON wishlist.book_id = book.book_id " +
                    "WHERE user.user_id = {}".format(_user_id))

    wishlist = _cursor.fetchall()

    print("\n-- DISPLAYING CUSTOMER'S WISHLIST ITEMS --")

    for book in wishlist:
        print("Book Name: {}\nAuthor: {}\n".format(book[4], book[5]))

def show_books_to_add(_cursor, _user_id):
    # query the database for a list of books not in the users wishlist

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n-- DISPLAYING AVAILABLE BOOKS --")

    for book in books_to_add:
        print("Book Id: {}\nBook Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    # try/catch block for handling potential MySQL database errors

    db = mysql.connector.connect(**config) # connect to the WhatABook database

    cursor = db.cursor() # cursor for MySQL queries

    print("\nWelcome to the WhatABook Application! ")

    user_selection = show_menu() # show the main menu

    # while the user's selection is not 4
    while user_selection != 4:

        # if the user selects option 1, call the show_books method and display the books
        if user_selection == 1:
            show_books(cursor)

        # if the user selects option 2, call the show_locations method and display the configured locations
        if user_selection == 2:
            show_locations(cursor)

        # if the user selects option 3, call the validate_user method to validate the entered user_id
        # call the show_account_menu() to show the account settings menu
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            # while account option does not equal 3
            while account_option != 3:

                # if the use selects option 1, call the show_wishlist() method to show the current users
                # configured wishlist items
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                # if the user selects option 2, call the show_books_to_add function to show the user
                # the books not currently configured in the users wishlist
                if account_option == 2:

                    # show the books not currently configured in the users wishlist
                    show_books_to_add(cursor, my_user_id)

                    # get the entered book_id
                    book_id = int(input("\nEnter the id of the book you want to add: "))

                    # add the selected book the users wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit() # commit the changes to the database

                    print("\nBook id: {} was added to your wishlist!".format(book_id))

                # if the selected option is less than 0 or greater than 3, display an invalid user selection
                if account_option < 0 or account_option > 3:
                    print("\nInvalid option, please retry...")

                # show the account menu
                account_option = show_account_menu()

        # if the user selection is less than 0 or greater than 4, display an invalid user selection
        if user_selection < 0 or user_selection > 4:
            print("\nInvalid option, please retry...")

        # show the main menu
        user_selection = show_menu()

    print("\n\nProgram terminated...")

except mysql.connector.Error as err:
    # handle errors

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    # close the connection to MySQL
    db.close()
