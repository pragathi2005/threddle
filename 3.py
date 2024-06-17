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

# Start the main page
main_page()
