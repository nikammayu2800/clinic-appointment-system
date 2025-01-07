# import re
# from tkinter import messagebox
# from PIL import Image
# import customtkinter as ctk
# from bcrypt import hashpw, gensalt
# from landing_page import landing_page
# from db_connection import connect_db
# from login_screen import show_login

# def show_signup_page(root):
#     error_labels = {}

#     # Clear the main window
#     for widget in root.winfo_children():
#         widget.destroy()

#     # Initialize CustomTkinter appearance
#     ctk.set_appearance_mode("light")
#     ctk.set_default_color_theme("blue")

#     # Set up the main frame
#     root.columnconfigure(0, weight=1)
#     root.rowconfigure(0, weight=1)

#     signup_frame = ctk.CTkFrame(root, fg_color="#f0f4f8", corner_radius=10, width=600)
#     signup_frame.pack(fill="both", expand=True)
#     signup_frame.columnconfigure(0, weight=1)
#     signup_frame.columnconfigure(1, weight=1)

#     # Header Frame
#     header_frame = ctk.CTkFrame(signup_frame, fg_color="#3b8ed0", corner_radius=10)
#     header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
#     header_frame.grid_columnconfigure(0, weight=1)

#     title_label = ctk.CTkLabel(header_frame, text="Sign-Up Form", font=ctk.CTkFont("Helvetica", 24, "bold"), text_color="white")
#     title_label.grid(row=0, column=0,  padx=20, pady=10, sticky="nsew")

#     # Fields Frame
#     fields_frame = ctk.CTkFrame(signup_frame, fg_color="#f0f4f8", width=600)
#     fields_frame.grid(row=1, column=0, columnspan=2, padx=50, sticky="nsew")
#     fields_frame.columnconfigure(0, weight=1)
#     fields_frame.columnconfigure(1, weight=1)

#     # Username
#     username_label = ctk.CTkLabel(fields_frame, text="Username:", font=ctk.CTkFont(size=12), text_color="black")
#     username_label.grid(row=0, column=0, padx=25, pady=(15, 0), sticky="n")
#     entry_username = ctk.CTkEntry(fields_frame, width=200, font=ctk.CTkFont(size=12), placeholder_text="Enter Username")
#     entry_username.grid(row=1, column=0, padx=25, pady=(0, 20), sticky="n")
#     error_labels["username"] = ctk.CTkLabel(fields_frame, text="", text_color="red", font=("Arial", 13))
#     error_labels["username"].grid(row=1, column=0, pady=(35,0), padx=30, sticky="n")
 
#     # Password
#     password_label = ctk.CTkLabel(fields_frame, text="Password:", font=ctk.CTkFont(size=12), text_color="black")
#     password_label.grid(row=2, column=0, padx=25, pady=(15, 0), sticky="n")
#     entry_password = ctk.CTkEntry(fields_frame, width=200, font=ctk.CTkFont(size=12), show="*", placeholder_text="Enter Password")
#     entry_password.grid(row=3, column=0, padx=25, pady=(0, 20), sticky="n")
#     error_labels["password"] = ctk.CTkLabel(fields_frame, text="", text_color="red", font=("Arial", 13))
#     error_labels["password"].grid(row=3, column=0, pady=(35,0), padx=30, sticky="n")
 
#     # Role
#     role_label = ctk.CTkLabel(fields_frame, text="Role:", font=ctk.CTkFont(size=12), text_color="black")
#     role_label.grid(row=4, column=0, padx=25, pady=(15, 0), sticky="n")
#     entry_role = ctk.CTkEntry(fields_frame, width=200, font=ctk.CTkFont(size=12), placeholder_text="Enter Role")
#     entry_role.grid(row=5, column=0, padx=25, pady=(0, 20), sticky="n")
#     error_labels["role"] = ctk.CTkLabel(fields_frame, text="", text_color="red", font=("Arial", 13))
#     error_labels["role"].grid(row=5, column=0, pady=(35,0), padx=30, sticky="n")
 
#     # First Name
#     first_name_label = ctk.CTkLabel(fields_frame, text="First Name:", font=ctk.CTkFont(size=12), text_color="black")
#     first_name_label.grid(row=0, column=1, padx=25, pady=(15, 0), sticky="n")
#     entry_first_name = ctk.CTkEntry(fields_frame, width=200, font=ctk.CTkFont(size=12), placeholder_text="Enter First Name")
#     entry_first_name.grid(row=1, column=1, padx=25, pady=(0, 20), sticky="n")
#     error_labels["first_name"] = ctk.CTkLabel(fields_frame, text="", text_color="red", font=("Arial", 13))
#     error_labels["first_name"].grid(row=1, column=1, pady=(35,0), padx=30, sticky="n")
 
#     # Last Name
#     last_name_label = ctk.CTkLabel(fields_frame, text="Last Name:", font=ctk.CTkFont(size=12), text_color="black")
#     last_name_label.grid(row=2, column=1, padx=25, pady=(15, 0), sticky="n")
#     entry_last_name = ctk.CTkEntry(fields_frame, width=200, font=ctk.CTkFont(size=12), placeholder_text="Enter Last Name")
#     entry_last_name.grid(row=3, column=1, padx=25, pady=(0, 20), sticky="n")
#     error_labels["last_name"] = ctk.CTkLabel(fields_frame, text="", text_color="red", font=("Arial", 13))
#     error_labels["last_name"].grid(row=3, column=1, pady=(35,0), padx=30, sticky="n")
 
#     def navigate_to(screen_func):
#         for widget in root.winfo_children():
#             widget.destroy()
#         screen_func(root)

#     def validate_fields():
#         print("in validate")
#         username = entry_username.get().strip()
#         password = entry_password.get().strip()
#         first_name = entry_first_name.get().strip()
#         last_name = entry_last_name.get().strip()

#         # Clear all previous error messages
#         for error_label in error_labels.values():
#             error_label.configure(text="")

#         valid = True

#         # Username
#         if not re.match(r"^[a-zA-Z0-9_]{4,20}$", username):
#             error_labels["username"].configure(text="Username must be 4-20 characters long and contain only letters, numbers, or underscores.")
#             valid = False
#         if username.startswith("_") or username.endswith("_"):
#             error_labels["username"].configure(text="Username cannot start or end with an underscore.")
#             valid = False

#         # Password
#         if len(password) < 8 or len(password) > 20:
#             error_labels["password"].configure(text="Password must be 8-20 characters long.")
#             valid = False
#         if not re.search(r"[A-Z]", password):
#             error_labels["password"].configure(text="Password must contain at least one uppercase letter.")
#             valid = False
#         if not re.search(r"[a-z]", password):
#             error_labels["password"].configure(text="Password must contain at least one lowercase letter.")
#             valid = False
#         if not re.search(r"[0-9]", password):
#             error_labels["password"].configure(text="Password must contain at least one number.")
#             valid = False
#         if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
#             error_labels["password"].configure(text="Password must contain at least one special character.")
#             valid = False
#         if re.search(r"\s", password):
#             error_labels["password"].configure(text="Password must not contain spaces.")
#             valid = False
        
#         # First Name
#         if not re.match(r"^[a-zA-Z][a-zA-Z ]{1,29}$", first_name.strip()):
#             error_labels["first_name"].configure(text="First name must be 2-30 characters long and contain only letters and spaces.")
#             valid = False

#         # Last Name
#         if not re.match(r"^[a-zA-Z][a-zA-Z ]{1,29}$", last_name.strip()):
#             error_labels["last_name"].configure(text="Last name must be 2-30 characters long and contain only letters and spaces.")
#             valid = False


#         # Show success message if all fields are valid
#         if valid:
#             return True
#         else:
#             return False


#     def signup():
#         if not validate_fields():
#             return
        
#         # Clear all previous error messages
#         for error_label in error_labels.values():
#             error_label.configure(text="")

#         username = entry_username.get().strip()
#         password = entry_password.get().strip()
#         hashed_password = hashpw(password.encode('utf-8'), gensalt())
#         role = entry_role.get().strip()
#         first_name = entry_first_name.get().strip()
#         last_name = entry_last_name.get().strip()

#         conn = connect_db()
#         if conn:
#             try:
#                 cursor = conn.cursor()
#                 cursor.execute(
#                     "INSERT INTO staff (username, password, first_name, last_name, role)"
#                     "VALUES (%s, %s, %s, %s, %s)",
#                     (username, hashed_password, first_name, last_name, role))
#                 conn.commit()
#                 navigate_to(show_login)
#                 messagebox.showinfo("Success", "Staff registered successfully!")
#             except Exception as e:
#                 messagebox.showerror("Database Error", f"An error occurred: {e}")
#             finally:
#                 conn.close()

#     # Buttons
#     button_frame = ctk.CTkFrame(signup_frame, fg_color="#f0f4f8")
#     button_frame.grid(row=2, column=0, columnspan=2, pady=20)

#     submit_button = ctk.CTkButton(button_frame, text="Submit", command= lambda: signup())
#     submit_button.pack(side=ctk.LEFT, padx=10)

#     cancel_button = ctk.CTkButton(button_frame, text="Cancel", command= lambda: landing_page(root))
#     cancel_button.pack(side=ctk.LEFT, padx=10)

#     # Load the illustration
#     illustration_img = Image.open("logos/sign_up.png")  # Update with your illustration path
#     illustration_img = ctk.CTkImage(illustration_img, size=(300, 300))

#     # Illustration Label
#     illustration_label = ctk.CTkLabel(signup_frame, image=illustration_img, text="")
#     illustration_label.grid(row=3, column=0, rowspan=3, padx=20, pady=20, sticky="w")


import re
from tkinter import messagebox
from PIL import Image
import customtkinter as ctk
from bcrypt import hashpw, gensalt
from landing_page import landing_page
from db_connection import connect_db
from login_screen import show_login

def show_signup_page(root):
    error_labels = {}

    # Clear the main window
    for widget in root.winfo_children():
        widget.destroy()

    # Initialize CustomTkinter appearance
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    # Configure root window for responsiveness
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Main frame
    signup_frame = ctk.CTkFrame(root, fg_color="#f0f4f8", corner_radius=10)
    signup_frame.grid(row=0, column=0, sticky="nsew")
    signup_frame.columnconfigure(0, weight=1)
    signup_frame.rowconfigure(1, weight=1)  # For fields_frame
    signup_frame.rowconfigure(3, weight=1)  # For illustration

    # Header Frame
    header_frame = ctk.CTkFrame(signup_frame, fg_color="#3b8ed0", corner_radius=10)
    header_frame.grid(row=0, column=0, sticky="ew")
    header_frame.columnconfigure(0, weight=1)

    title_label = ctk.CTkLabel(header_frame, text="Sign-Up Form", font=ctk.CTkFont("Helvetica", 24, "bold"), text_color="white")
    title_label.grid(row=0, column=0, padx=20, pady=10)

    # Fields Frame
    fields_frame = ctk.CTkFrame(signup_frame, fg_color="#f0f4f8")
    fields_frame.grid(row=1, column=0, padx=20, pady=5, sticky="nsew")
    fields_frame.columnconfigure(0, weight=1)
    fields_frame.columnconfigure(1, weight=1)

    # Responsive Fields
    def add_field(label_text, placeholder, row, column, error_key, show=""):
        label = ctk.CTkLabel(fields_frame, text=label_text, font=ctk.CTkFont(size=12), text_color="black")
        label.grid(row=row, column=column, padx=10, pady=(15, 0), sticky="w")
        entry = ctk.CTkEntry(fields_frame, font=ctk.CTkFont(size=12), width=200, placeholder_text=placeholder, show=show)
        entry.grid(row=row + 1, column=column, padx=10, pady=(0, 15), sticky="ew")
        error_labels[error_key] = ctk.CTkLabel(fields_frame, text="", text_color="red", font=("Arial", 11))
        error_labels[error_key].grid(row=row + 2, column=column, padx=10, sticky="w")
        return entry

    entry_username = add_field("Username:", "Enter Username", 0, 0, "username")
    entry_password = add_field("Password:", "Enter Password", 3, 0, "password", show="*")
    entry_role = add_field("Role:", "Enter Role", 6, 0, "role")
    entry_first_name = add_field("First Name:", "Enter First Name", 0, 1, "first_name")
    entry_last_name = add_field("Last Name:", "Enter Last Name", 3, 1, "last_name")

    # Buttons Frame
    button_frame = ctk.CTkFrame(signup_frame, fg_color="#f0f4f8")
    button_frame.grid(row=2, column=0, pady=10, sticky="ew")
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)

    submit_button = ctk.CTkButton(button_frame, text="Submit", command=lambda: signup())
    submit_button.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    cancel_button = ctk.CTkButton(button_frame, text="Cancel", command=lambda: landing_page(root))
    cancel_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    # Illustration
    illustration_img = Image.open("logos/sign_up.png")  # Update with your illustration path
    illustration_img = ctk.CTkImage(illustration_img, size=(300, 300))
    illustration_label = ctk.CTkLabel(signup_frame, image=illustration_img, text="")
    illustration_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    def validate_fields():
        username = entry_username.get().strip()
        password = entry_password.get().strip()
        first_name = entry_first_name.get().strip()
        last_name = entry_last_name.get().strip()

        # Clear all previous error messages
        for error_label in error_labels.values():
            error_label.configure(text="")

        valid = True

        # Username
        if not re.match(r"^[a-zA-Z0-9_]{4,20}$", username):
            error_labels["username"].configure(text="Username must be 4-20 characters long and contain only letters, numbers, or underscores.")
            valid = False
        if username.startswith("_") or username.endswith("_"):
            error_labels["username"].configure(text="Username cannot start or end with an underscore.")
            valid = False

        # Password
        if len(password) < 8 or len(password) > 20:
            error_labels["password"].configure(text="Password must be 8-20 characters long.")
            valid = False
        if not re.search(r"[A-Z]", password):
            error_labels["password"].configure(text="Password must contain at least one uppercase letter.")
            valid = False
        if not re.search(r"[a-z]", password):
            error_labels["password"].configure(text="Password must contain at least one lowercase letter.")
            valid = False
        if not re.search(r"[0-9]", password):
            error_labels["password"].configure(text="Password must contain at least one number.")
            valid = False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            error_labels["password"].configure(text="Password must contain at least one special character.")
            valid = False
        if re.search(r"\s", password):
            error_labels["password"].configure(text="Password must not contain spaces.")
            valid = False
        
        # First Name
        if not re.match(r"^[a-zA-Z][a-zA-Z ]{1,29}$", first_name.strip()):
            error_labels["first_name"].configure(text="First name must be 2-30 characters long and contain only letters and spaces.")
            valid = False

        # Last Name
        if not re.match(r"^[a-zA-Z][a-zA-Z ]{1,29}$", last_name.strip()):
            error_labels["last_name"].configure(text="Last name must be 2-30 characters long and contain only letters and spaces.")
            valid = False


        # Show success message if all fields are valid
        if valid:
            return True
        else:
            return False

    def signup():
        if not validate_fields():
            return
        
        # Clear all previous error messages
        for error_label in error_labels.values():
            error_label.configure(text="")

        username = entry_username.get().strip()
        password = entry_password.get().strip()
        hashed_password = hashpw(password.encode('utf-8'), gensalt())
        role = entry_role.get().strip()
        first_name = entry_first_name.get().strip()
        last_name = entry_last_name.get().strip()

        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO staff (username, password, first_name, last_name, role)"
                    "VALUES (%s, %s, %s, %s, %s)",
                    (username, hashed_password, first_name, last_name, role))
                conn.commit()
                navigate_to(show_login)
                messagebox.showinfo("Success", "Staff registered successfully!")
            except Exception as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")
            finally:
                conn.close()

    def navigate_to(screen_func):
        for widget in root.winfo_children():
            widget.destroy()
        screen_func(root)
