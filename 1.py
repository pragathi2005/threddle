import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error

def open_tailor_page():
    main_page.destroy()  # Close the main page
    tailor_page()  # Open the tailor page

def open_customer_page():
    main_page.destroy()  # Close the main page
    customer_page()  # Open the customer page

# Function to create the main page
def main_page():
    global main_page
    main_page = tk.Tk()
    main_page.title("Tailor and Customer")
    main_page.geometry("800x600")

    # Load the background image
    bg_image = Image.open("background.jpg")  # Replace with your image path
    bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a canvas
    canvas = tk.Canvas(main_page, width=800, height=600)
    canvas.pack(fill="both", expand=True)

    # Set the background image on the canvas
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Create buttons
    tailor_button = tk.Button(main_page, text="Tailor", command=open_tailor_page, font=("Arial", 16), bg="black", fg="white")
    customer_button = tk.Button(main_page, text="Customer", command=open_customer_page, font=("Arial", 16), bg="black", fg="white")

    # Place buttons on the canvas
    canvas.create_window(400, 250, window=tailor_button)
    canvas.create_window(400, 350, window=customer_button)

    # Start the Tkinter event loop
    main_page.mainloop()

def tailor_page():
    global username_entry_tailor, password_entry_tailor
    tailor_win = tk.Tk()
    tailor_win.title("Tailor Page")
    tailor_win.geometry("800x600")

    # Load the background image
    bg_image = Image.open("background.jpg")  # Replace with your image path
    bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a canvas
    canvas = tk.Canvas(tailor_win, width=800, height=600)
    canvas.pack(fill="both", expand=True)

    # Set the background image on the canvas
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Add a label
    label = tk.Label(tailor_win, text="Welcome to the Tailor Page", font=("Arial", 24), bg="black", fg="white")
    canvas.create_window(400, 50, window=label)

    # Username label and entry
    username_label = tk.Label(tailor_win, text="Username:", font=("Arial", 16), bg="black", fg="white")
    canvas.create_window(300, 200, window=username_label)

    username_entry_tailor = tk.Entry(tailor_win, font=("Arial", 16))
    canvas.create_window(500, 200, window=username_entry_tailor)

    # Password label and entry
    password_label = tk.Label(tailor_win, text="Password:", font=("Arial", 16), bg="black", fg="white")
    canvas.create_window(300, 300, window=password_label)

    password_entry_tailor = tk.Entry(tailor_win, show="*", font=("Arial", 16))
    canvas.create_window(500, 300, window=password_entry_tailor)

    # Login button
    login_button = tk.Button(tailor_win, text="Login", font=("Arial", 16), bg="black", fg="white", command=tailor_login)
    canvas.create_window(400, 400, window=login_button)

    tailor_win.mainloop()

def customer_page():
    global username_entry_customer, password_entry_customer, address_entry_customer, customer_win
    customer_win = tk.Tk()
    customer_win.title("Customer Page")
    customer_win.geometry("800x600")

    # Load the background image
    bg_image = Image.open("background.jpg")  # Replace with your image path
    bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a canvas
    canvas = tk.Canvas(customer_win, width=800, height=600)
    canvas.pack(fill="both", expand=True)

    # Set the background image on the canvas
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Add a label
    label = tk.Label(customer_win, text="Welcome to the Customer Page", font=("Arial", 24), bg="black", fg="white")
    canvas.create_window(400, 50, window=label)

    # Username label and entry
    username_label = tk.Label(customer_win, text="Username:", font=("Arial", 16), bg="black", fg="white")
    canvas.create_window(300, 150, window=username_label)

    username_entry_customer = tk.Entry(customer_win, font=("Arial", 16))
    canvas.create_window(500, 150, window=username_entry_customer)

    # Password label and entry
    password_label = tk.Label(customer_win, text="Password:", font=("Arial", 16), bg="black", fg="white")
    canvas.create_window(300, 200, window=password_label)

    password_entry_customer = tk.Entry(customer_win, show="*", font=("Arial", 16))
    canvas.create_window(500, 200, window=password_entry_customer)

    # Address label and entry
    address_label = tk.Label(customer_win, text="Address:", font=("Arial", 16), bg="black", fg="white")
    canvas.create_window(300, 250, window=address_label)

    address_entry_customer = tk.Entry(customer_win, font=("Arial", 16))
    canvas.create_window(500, 250, window=address_entry_customer)

    # Login button
    login_button = tk.Button(customer_win, text="Login", font=("Arial", 16), bg="black", fg="white", command=customer_login)
    canvas.create_window(400, 350, window=login_button)

    customer_win.mainloop()

def tailor_login():
    username = username_entry_tailor.get()
    password = password_entry_tailor.get()
    rating = None  # Default rating

    try:
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL host
            user='root',  # Replace with your MySQL username
            password='system',  # Replace with your MySQL password
            database='threddle'  # Replace with your database name
        )

        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO tailors (username, password, rating)
                               VALUES (%s, %s, %s)"""
        cursor.execute(sql_insert_query, (username, password, rating))
        connection.commit()

        print(f"Tailor {username} logged in successfully")

    except mysql.connector.Error as error:
        print(f"Failed to insert record into MySQL table {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def customer_login():
    username = username_entry_customer.get()
    password = password_entry_customer.get()
    address = address_entry_customer.get()

    try:
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL host
            user='root',  # Replace with your MySQL username
            password='system',  # Replace with your MySQL password
            database='threddle'  # Replace with your database name
        )

        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO customers (username, password, address)
                               VALUES (%s, %s, %s)"""
        cursor.execute(sql_insert_query, (username, password, address))
        connection.commit()

        print(f"Customer {username} logged in successfully")
        customer_win.destroy()  # Close the customer login window
        customer_post_login_page()

    except mysql.connector.Error as error:
        print(f"Failed to insert record into MySQL table {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def customer_post_login_page():
    post_login_win = tk.Tk()
    post_login_win.title("Customer Dashboard")
    post_login_win.geometry("800x600")

    # Load the background image
    bg_image = Image.open("background.jpg")  # Replace with your image path
    bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a canvas
    canvas = tk.Canvas(post_login_win, width=800, height=600)
    canvas.pack(fill="both", expand=True)

    # Set the background image on the canvas
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Add a label
    label = tk.Label(post_login_win, text="Customer Dashboard", font=("Arial", 24), bg="black", fg="white")
    canvas.create_window(400, 50, window=label)

    # Create buttons
    view_button = tk.Button(post_login_win, text="View", font=("Arial", 16), bg="black", fg="white")
    feedback_button = tk.Button(post_login_win, text="Feedback", font=("Arial", 16), bg="black", fg="white")
    ratings_button = tk.Button(post_login_win, text="Ratings", font=("Arial", 16), bg="black", fg="white", command=display_ratings)
    orders_button = tk.Button(post_login_win, text="Orders", font=("Arial", 16), bg="black", fg="white")

    # Place buttons on the canvas
    canvas.create_window(400, 200, window=view_button)
    canvas.create_window(400, 300, window=feedback_button)
    canvas.create_window(400, 400, window=ratings_button)
    canvas.create_window(400, 500, window=orders_button)

    post_login_win.mainloop()

def display_ratings():
    try:
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL host
            user='root',  # Replace with your MySQL username
            password='system',  # Replace with your MySQL password
            database='threddle'  # Replace with your database name
        )

        cursor = connection.cursor()
        cursor.execute("SELECT username, rating FROM tailors")
        rows = cursor.fetchall()

        ratings_win = tk.Toplevel()
        ratings_win.title("Tailor Ratings")
        ratings_win.geometry("800x600")

        # Load the background image
        bg_image = Image.open("background.jpg")  # Replace with your image path
        bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)

        # Create a canvas
        canvas = tk.Canvas(ratings_win, width=800, height=600)
        canvas.pack(fill="both", expand=True)

        # Set the background image on the canvas
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")

        # Create a frame for the table
        table_frame = tk.Frame(ratings_win, bg='black')
        table_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Add headers
        tk.Label(table_frame, text="Username", font=("Arial", 16), bg="black", fg="white", width=20, anchor='w').grid(row=0, column=0, padx=10, pady=5)
        tk.Label(table_frame, text="Rating", font=("Arial", 16), bg="black", fg="white", width=10, anchor='w').grid(row=0, column=1, padx=10, pady=5)

        # Add rows to the table
        for i, row in enumerate(rows, start=1):
            tk.Label(table_frame, text=row[0], font=("Arial", 14), bg="black", fg="white", width=20, anchor='w').grid(row=i, column=0, padx=10, pady=5)
            tk.Label(table_frame, text=row[1], font=("Arial", 14), bg="black", fg="white", width=10, anchor='w').grid(row=i, column=1, padx=10, pady=5)

        print("Ratings displayed successfully")

    except mysql.connector.Error as error:
        print(f"Failed to retrieve records from MySQL table {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
def customer_post_login_page():
    def open_feedback_window():
        feedback_win = tk.Toplevel()
        feedback_win.title("Feedback")
        feedback_win.geometry("400x200")

        # Create a frame for the feedback form
        feedback_frame = tk.Frame(feedback_win)
        feedback_frame.pack(padx=20, pady=30)

        # Add a label and entry for the rating
        rating_label = tk.Label(feedback_frame, text="Rating:", font=("Arial", 16))
        rating_label.grid(row=0, column=0, padx=10, pady=5)

        rating_entry = tk.Entry(feedback_frame, font=("Arial", 16))
        rating_entry.grid(row=0, column=1, padx=10, pady=5)

        # Submit button for the feedback
        submit_button = tk.Button(feedback_frame, text="Submit", font=("Arial", 16), command=submit_feedback)
        submit_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    def submit_feedback():
        tailor_username = "tailor_username_from_form"  # Assuming you have a way to retrieve tailor username
        new_rating = float(rating_entry.get())  # Get the rating from the entry field

        try:
            connection = mysql.connector.connect(
                host='localhost',  # Replace with your MySQL host
                user='root',  # Replace with your MySQL username
                password='system',  # Replace with your MySQL password
                database='threddle'  # Replace with your database name
            )

            cursor = connection.cursor()
            cursor.execute("UPDATE tailors SET rating = %s WHERE username = %s", (new_rating, tailor_username))
            connection.commit()

            print(f"Rating for tailor {tailor_username} updated successfully")

        except mysql.connector.Error as error:
            print(f"Failed to update rating for tailor {tailor_username}: {error}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    post_login_win = tk.Tk()
    post_login_win.title("Customer Dashboard")
    post_login_win.geometry("800x600")

    # Load the background image
    bg_image = Image.open("background.jpg")  # Replace with your image path
    bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a canvas
    canvas = tk.Canvas(post_login_win, width=800, height=600)
    canvas.pack(fill="both", expand=True)

    # Set the background image on the canvas
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Add a label
    label = tk.Label(post_login_win, text="Customer Dashboard", font=("Arial", 24), bg="black", fg="white")
    canvas.create_window(400, 50, window=label)

    # Feedback button to open the feedback window
    feedback_button = tk.Button(post_login_win, text="Feedback", font=("Arial", 16), bg="black", fg="white", command=open_feedback_window)
    feedback_button.place(relx=0.5, rely=0.5, anchor="center")

    post_login_win.mainloop()
def open_feedback_window():
    def open_rating_window():
        selected_tailor = tailor_choice.get()  # Get the selected tailor username
        feedback_win.destroy()  # Close the feedback window

        rating_win = tk.Toplevel()
        rating_win.title("Update Rating")
        rating_win.geometry("400x200")

        def submit_rating():
            new_rating = float(rating_entry.get())  # Get the rating from the entry field

            try:
                connection = mysql.connector.connect(
                    host='localhost',  # Replace with your MySQL host
                    user='root',  # Replace with your MySQL username
                    password='system',  # Replace with your MySQL password
                    database='threddle'  # Replace with your database name
                )

                cursor = connection.cursor()
                cursor.execute("UPDATE tailors SET rating = %s WHERE username = %s", (new_rating, selected_tailor))
                connection.commit()

                print(f"Rating for tailor {selected_tailor} updated successfully")

            except mysql.connector.Error as error:
                print(f"Failed to update rating for tailor {selected_tailor}: {error}")

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        # Create a frame for the rating form
        rating_frame = tk.Frame(rating_win)
        rating_frame.pack(padx=20, pady=30)

        # Add a label and entry for the rating
        rating_label = tk.Label(rating_frame, text="Rating:", font=("Arial", 16))
        rating_label.grid(row=0, column=0, padx=10, pady=5)

        rating_entry = tk.Entry(rating_frame, font=("Arial", 16))
        rating_entry.grid(row=0, column=1, padx=10, pady=5)

        # Submit button for the rating
        submit_button = tk.Button(rating_frame, text="Submit", font=("Arial", 16), command=submit_rating)
        submit_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    feedback_win = tk.Toplevel()
    feedback_win.title("Feedback")
    feedback_win.geometry("400x200")

    # Create a frame for the feedback form
    feedback_frame = tk.Frame(feedback_win)
    feedback_frame.pack(padx=20, pady=30)

    # Retrieve all tailor usernames from the "tailors" table
    try:
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL host
            user='root',  # Replace with your MySQL username
            password='system',  # Replace with your MySQL password
            database='threddle'  # Replace with your database name
        )

        cursor = connection.cursor()
        cursor.execute("SELECT username FROM tailors")
        tailors = cursor.fetchall()
        tailor_usernames = [tailor[0] for tailor in tailors]

    except mysql.connector.Error as error:
        print(f"Failed to retrieve tailor usernames: {error}")
        tailor_usernames = []

    # Add a label and choice box for selecting the tailor
    tailor_label = tk.Label(feedback_frame, text="Select Tailor:", font=("Arial", 16))
    tailor_label.grid(row=0, column=0, padx=10, pady=5)

    tailor_choice = ttk.Combobox(feedback_frame, values=tailor_usernames, font=("Arial", 16))
    tailor_choice.grid(row=0, column=1, padx=10, pady=5)
    tailor_choice.current(0)  # Select the first option by default

    # Submit button for the feedback
    submit_button = tk.Button(feedback_frame, text="Submit", font=("Arial", 16), command=open_rating_window)
    submit_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Start the main page
main_page()
