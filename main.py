import random
from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk


# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootpassword",
    port="3306",
    database="carrental")


class HomePage:
    def __init__(self):
        self.frame = Tk()
        self.frame.title("Car Rental App")
        self.frame.geometry("1366x730")

        # Load image
        image = Image.open("Car Logo.png")  # Car Logo Image
        image = image.resize((1370, 710))  # Resize the image as needed
        self.photo = ImageTk.PhotoImage(image)

        # Create label to display the image
        self.label_image = Label(self.frame, image=self.photo)
        self.label_image.place(x=0, y=0)

        # Define color themes
        self.theme1 = {"bg": "white", "fg": "black", "button_bg": "blue", "button_fg": "white"}
        self.theme2 = {"bg": "black", "fg": "white", "button_bg": "green", "button_fg": "white"}
        self.theme3 = {"bg": "white", "fg": "black", "button_bg": "red", "button_fg": "white"}

        self.label1 = Label(self.frame, text="Car Rental App", font=("Helvetica", 40), bg="white")
        self.label1.place(x=525, y=80)

        self.button1 = Button(self.frame, text="Sign Up", font=("Verdana", 12), width=20, height=2,
                              command=self.go_to_signup)
        self.button1.place(x=50, y=200)

        self.button2 = Button(self.frame, text="Login", font=("Verdana", 12), width=20, height=2,
                              command=self.go_to_login)
        self.button2.place(x=1150, y=200)

        self.button3 = Button(self.frame, text="Rent A Car", font=("Verdana", 12), width=20, height=2,
                              command=self.go_to_Rent_A_Car)
        self.button3.place(x=600, y=200)

        self.button4 = Button(self.frame, text="Admin", font=("Verdana", 12), width=20, height=2,
                              command=self.go_to_admin)
        self.button4.place(x=600, y=600)
        self.frame.mainloop()

    def go_to_signup(self):
        self.frame.destroy()
        Signup()

    def go_to_login(self):
        self.frame.destroy()
        Login()

    def go_to_Rent_A_Car(self):
        self.frame.destroy()
        RentACar()

    def go_to_admin(self):
        self.frame.destroy()
        Admin()

    def show_homepage(self):
        pass


class Signup:
    pass


class Signup:
    def __init__(self):
        self.frame = Tk()
        self.frame.title("Sign Up")
        self.frame.geometry("400x300")

        self.label1 = Label(self.frame, text="Sign Up", font=("Verdana", 20))
        self.label1.place(x=150, y=20)

        self.label2 = Label(self.frame, text="First Name:", font=("Verdana", 12))
        self.label2.place(x=50, y=80)
        self.entry1 = Entry(self.frame, font=("Verdana", 12))
        self.entry1.place(x=200, y=80)

        self.label3 = Label(self.frame, text="Last Name:", font=("Verdana", 12))
        self.label3.place(x=50, y=120)
        self.entry2 = Entry(self.frame, font=("Verdana", 12))
        self.entry2.place(x=200, y=120)

        self.label4 = Label(self.frame, text="Email:", font=("Verdana", 12))
        self.label4.place(x=50, y=160)
        self.entry3 = Entry(self.frame, font=("Verdana", 12))
        self.entry3.place(x=200, y=160)

        self.label5 = Label(self.frame, text="Password:", font=("Verdana", 12))
        self.label5.place(x=50, y=200)
        self.entry4 = Entry(self.frame, show="*", font=("Verdana", 12))
        self.entry4.place(x=200, y=200)

        self.label6 = Label(self.frame, text="Confirm Password:", font=("Verdana", 12))
        self.label6.place(x=40, y=240)
        self.entry5 = Entry(self.frame, show="*", font=("Verdana", 12))
        self.entry5.place(x=200, y=240)

        self.button1 = Button(self.frame, text="Sign Up", font=("Verdana", 12), width=10, height=2,
                              command=self.signup)
        self.button1.place(x=250, y=280)

        self.button2 = Button(self.frame, text="Back to Home Page", font=("Verdana", 12), width=0, height=2,
                              command=self.go_to_HomePage)
        self.button2.place(x=20, y=280)

        self.frame.mainloop()

    def signup(self):
        # Get input values from entry fields
        first_name = self.entry1.get()
        last_name = self.entry2.get()
        email = self.entry3.get()
        password = self.entry4.get()
        confirm_password = self.entry5.get()

        # Check if password and confirm password match
        if password != confirm_password:
            messagebox.showerror("Error", "Password and Confirm Password do not match!")
            return

        # Connect to MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rootpassword",
            port="3306",
            database="carrental"
        )
        mycursor = mydb.cursor()

        # Insert user data into the database
        sql = "INSERT INTO users (id, first_name, last_name, email, password) VALUES (%s, %s, %s, %s, %s)"
        id = 1
        val = (id, first_name, last_name, email, password)
        mycursor.execute(sql, val)

        # Commit the transaction and close the database connection
        mydb.commit()
        mydb.close()

        # Show success message
        messagebox.showinfo("Success", "Registration successful!")

        # Clear input fields
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)

    def go_to_HomePage(self):
        # Close the Sign Up window and go back to Home Page
        self.frame.destroy()
        HomePage()

    # Create an instance of the Signup class
    signup_window = Signup()



class Login:
    def __init__(self):
        self.frame = Tk()
        self.frame.title("Login")
        self.frame.geometry("400x300")

        self.label1 = Label(self.frame, text="Login", font=("Verdana", 20))
        self.label1.place(x=150, y=20)

        self.label2 = Label(self.frame, text="Email:", font=("Verdana", 12))
        self.label2.place(x=50, y=80)
        self.entry1 = Entry(self.frame, font=("Verdana", 12))
        self.entry1.place(x=200, y=80)

        self.label3 = Label(self.frame, text="Password:", font=("Verdana", 12))
        self.label3.place(x=50, y=120)
        self.entry2 = Entry(self.frame, show="*", font=("Verdana", 12))
        self.entry2.place(x=200, y=120)

        self.button1 = Button(self.frame, text="Login", font=("Verdana", 12), width=20, height=2,
                              command=self.login)
        self.button1.place(x=200, y=180)

        self.button2 = Button(self.frame, text="Back to Home Page", font=("Verdana", 12), width=0, height=2,
                              command=self.go_to_HomePage)
        self.button2.place(x=20, y=180)

        self.frame.mainloop()

    def login(self):
        # Get input values from entry fields
        email = self.entry1.get()
        password = self.entry2.get()

        # You can perform validation and processing of the input data here
        # For example, you can check if the email and password match in the database, etc.
        # You can also implement authentication and authorization logic based on your specific requirements.

        print("Login successful!")
        print("Welcome back, " + email)

        # After successful login, you can redirect to the home page or any other page as needed
        self.frame.destroy()
        HomePage()

    def go_to_HomePage(self):
        # Implement the logic to go back to the home page
        self.frame.destroy()
        HomePage()
        pass


# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootpassword",
    port="3306",
    database="carrental"
)

# Create a cursor object to interact with MySQL
cursor = mydb.cursor()

# Define the SQL query to fetch data from the users table
query = "SELECT * FROM users"

# Execute the SQL query
cursor.execute(query)

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the fetched data
for row in rows:
    print(row)

# Close the cursor and database connection
cursor.close()
mydb.close()

# Create an instance of the Login class
login = Login()

class RentACar:
    def __init__(self):
        self.frame = Tk()
        self.frame.title("Rent A Car")
        self.frame.geometry("400x300")

        self.label1 = Label(self.frame, text="Rent A Car", font=("Verdana", 20))
        self.label1.place(x=150, y=20)

        self.label2 = Label(self.frame, text="Car Model:", font=("Verdana", 12))
        self.label2.place(x=50, y=80)
        self.entry1 = Entry(self.frame, font=("Verdana", 12))
        self.entry1.place(x=200, y=80)

        self.label3 = Label(self.frame, text="Car Make:", font=("Verdana", 12))
        self.label3.place(x=50, y=120)
        self.entry2 = Entry(self.frame, font=("Verdana", 12))
        self.entry2.place(x=200, y=120)

        self.label4 = Label(self.frame, text="Duration (in days):", font=("Verdana", 12))
        self.label4.place(x=50, y=150)
        self.entry3 = Entry(self.frame, font=("Verdana", 12))
        self.entry3.place(x=200, y=150)

        self.button1 = Button(self.frame, text="Rent", font=("Verdana", 12), width=20, height=2,
                              command=self.rent_car)
        self.button1.place(x=200, y=180)

        self.button2 = Button(self.frame, text="Back to Home Page", font=("Verdana", 12), width=0, height=2,
                              command=self.go_to_HomePage)
        self.button2.place(x=20, y=180)

    def generate_random_rate(self):
        # Generate a random rate between $20 and $100
        rate = random.randint(20, 100)

        # Return the random rate
        return rate

    def rent_car(self):
        car_model = self.entry1.get()
        car_make = self.entry2.get()
        duration_days = int(self.entry3.get())  # Convert duration to integer

        # Establish database connection
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rootpassword",
            port="3306",
            database="carrental"
        )

        # Create a cursor object to interact with MySQL
        cursor = mydb.cursor()

        # Define rate schedule
        rate_per_day = random.randint(30, 100)  # Generate a random rate per day between 30 and 100
        rate_for_first_days = random.randint(50, 150)  # Generate a random rate for first days between 50 and 150
        rate_for_subsequent_days = random.randint(20,
                                                  100)  # Generate a random rate for subsequent days between 20 and 100

        # Check if car is available
        if self.check_availability(car_model, car_make):
            rental_cost = self.calculate_rental_cost(car_model, duration_days)
            self.display_rental_details(car_model, car_make, duration_days, rental_cost)
        else:
            messagebox.showinfo("Car Unavailable", "The selected car is currently not available.")

        # Update the GUI labels with generated random rates
        self.label2.config(text="Car Model: " + car_model + ", Rate Per Day: $" + str(rate_per_day))
        self.label3.config(text="Car Make: " + car_make + ", Rate for First " + str(
            duration_days) + " Days: $" + str(rate_for_first_days))
        self.label4.config(text="Duration (in days): " + str(duration_days) + ", Rate for Subsequent Days: $" + str(
            rate_for_subsequent_days))

    def check_availability(self, car_model, car_make):
        # Establish database connection
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rootpassword",
            port="3306",
            database="carrental"
        )

        # Create a cursor object to interact with MySQL
        cursor = mydb.cursor()

        # Check if car is available in the database
        cursor.execute("SELECT * FROM cars WHERE car_model = %s AND car_make = %s", (car_model, car_make))
        result = cursor.fetchone()
        cursor.fetchall()  # Fetch all results from cursor
        cursor.close()  # Close the cursor
        mydb.close()  # Close the database connection

        if result is None:
            return False
        else:
            return True

    def display_rental_details(self, car_model, car_make, duration_days, rental_cost):
        messagebox.showinfo("Rental Details",
                            "Car Model: {}\n"
                            "Car Make: {}\n"
                            "Duration (in days): {}\n"
                            "Rental Cost: ${}".format(car_model, car_make, duration_days, rental_cost))

    def go_to_HomePage(self):
        self.frame.destroy()
        home_page = HomePage()  # Create an instance of the HomePage class
        home_page.frame.mainloop()


if __name__ == "__main__":
    rent_a_car = RentACar()
    rent_a_car.frame.mainloop()


class Admin:
    def __init__(self):
        self.frame = Tk()
        self.frame.title("Admin")
        self.frame.geometry("400x300")

        self.label1 = Label(self.frame, text="Admin Login", font=("Verdana", 20))
        self.label1.place(x=120, y=20)

        self.label2 = Label(self.frame, text="Username:", font=("Verdana", 12))
        self.label2.place(x=50, y=80)
        self.entry1 = Entry(self.frame, font=("Verdana", 12))
        self.entry1.place(x=200, y=80)

        self.label3 = Label(self.frame, text="Password:", font=("Verdana", 12))
        self.label3.place(x=50, y=120)
        self.entry2 = Entry(self.frame, show="*", font=("Verdana", 12))
        self.entry2.place(x=200, y=120)

        self.button1 = Button(self.frame, text="Login", font=("Verdana", 12), width=15, height=2, command=self.admin_login)
        self.button1.place(x=150, y=180)

        self.frame.mainloop()

    def admin_login(self):
        # Retrieve the username and password entered in the Entry widgets
        username = self.entry1.get()
        password = self.entry2.get()

        # Perform the username and password check
        if username == "Admin" and password == "12345":
            messagebox.showinfo("Login Successful", "Welcome Admin!")
            self.frame.destroy()
            self.admin_page()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def admin_page(self):
        self.frame = Tk()
        self.frame.title("Admin Page")
        self.frame.geometry("400x300")

        self.label1 = Label(self.frame, text="Admin Page", font=("Verdana", 20))
        self.label1.place(x=120, y=20)

        self.button1 = Button(self.frame, text="Update Record", font=("Verdana", 12), width=15, height=2, command=self.update_record)
        self.button1.place(x=50, y=100)

        self.button2 = Button(self.frame, text="Delete Record", font=("Verdana", 12), width=15, height=2, command=self.delete_record)
        self.button2.place(x=250, y=100)

        self.button3 = Button(self.frame, text="Search Record", font=("Verdana", 12), width=15, height=2, command=self.search_record)
        self.button3.place(x=250, y=180)

        self.button4 = Button(self.frame, text="Logout", font=("Verdana", 12), width=0, height=2,
                              command=self.go_to_HomePage)
        self.button4.place(x=50, y=180)

        self.frame.mainloop()

    def update_record(self):
        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rootpassword",
            port="3306",
            database="carrental"
        )
        cursor = db.cursor()

        # Retrieve the record ID and updated values from the user
        record_id = 0  # Example: assuming record ID is 1
        updated_car_model = "Civic"  # Example: assuming column1 needs to be updated with "Toyota Corolla"
        updated_car_make = "Honda"  # Example: assuming column2 needs to be updated with "Toyota"

        # Perform update operation
        query = f"UPDATE cars SET car_model = '{updated_car_model}', car_make = '{updated_car_make}' WHERE id = {record_id}"
        cursor.execute(query)

        db.commit()
        messagebox.showinfo("Update Record", "Record updated successfully")

        cursor.close()
        db.close()

    def delete_record(self):
        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rootpassword",
            port="3306",
            database="carrental"
        )
        cursor = db.cursor()

        # Add your delete query here
        # Example: cursor.execute("DELETE FROM cars WHERE condition")

        db.commit()
        messagebox.showinfo("Delete Record", "Record deleted successfully")

        cursor.close()
        db.close()

    def search_record(self):
        search_window = Toplevel(self.frame)
        search_window.title("Search Record")
        search_window.geometry("300x150")

        label1 = Label(search_window, text="Enter Record ID:", font=("Verdana", 12))
        label1.place(x=50, y=30)
        entry1 = Entry(search_window, font=("Verdana", 12))
        entry1.place(x=180, y=30)

        button1 = Button(search_window, text="Search", font=("Verdana", 12), width=10,
                         command=lambda: self.perform_search(entry1.get()))
        button1.place(x=100, y=80)

        # Add your delete query here
        # Example: cursor.execute("DELETE FROM cars WHERE condition")

        mydb.commit()
        messagebox.showinfo("Delete Record", "Record deleted successfully")

        cursor.close()
        mydb.close()

    def search_record(self):
        search_window = Toplevel(self.frame)
        search_window.title("Search Record")
        search_window.geometry("300x150")

        label1 = Label(search_window, text="Enter Record ID:", font=("Verdana", 12))
        label1.place(x=50, y=30)
        entry1 = Entry(search_window, font=("Verdana", 12))
        entry1.place(x=180, y=30)

        button1 = Button(search_window, text="Search", font=("Verdana", 12), width=10,
                         command=lambda: self.perform_search(entry1.get()))
        button1.place(x=100, y=80)

    def perform_search(self, record_id):
        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rootpassword",
            port="3306",
            database="carrental"
        )
        cursor = db.cursor()

        # Perform search operation
        # Add your search query here
        # Example: cursor.execute("SELECT * FROM cars WHERE id = %s", (record_id,))
        # Note: Replace "cars" with your actual table name and "id" with your actual primary key column name

        cursor.execute("SELECT * FROM cars WHERE id = %s", (record_id,))

        # Fetch the result
        result = cursor.fetchone()

        if result is not None:
            messagebox.showinfo("Record Found",
                                f"Record ID: {result[0]}\nMake: {result[1]}\nModel: {result[2]}\nRent/: {result[3]}")
        else:
            messagebox.showerror("Record Not Found", f"No record found with ID: {record_id}")

        cursor.close()
        db.close()

    def go_to_HomePage(self):
        # Implement the logic to go back to the home page
        self.frame.destroy()
        HomePage()
        pass

if __name__ == "__main__":
    admin = Admin()
