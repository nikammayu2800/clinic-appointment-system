# import re
# import customtkinter as ctk
# import tkinter as tk
# from tkinter import messagebox
# from bcrypt import checkpw
# from PIL import Image
# from bcrypt import hashpw, gensalt
# from db_connection import connect_db
# from home_page import create_home_page

# def show_login(root):
#     error_labels = {}

#     # Initialize CustomTkinter appearance
#     ctk.set_appearance_mode("light")  # Change to "dark" for dark mode
#     ctk.set_default_color_theme("blue")  # Customize the color theme if desired

#     # Clear root frame
#     for widget in root.winfo_children():
#         widget.destroy()

#     # Set up the main frame and configure the layout weights
#     root.columnconfigure(0, weight=1)
#     root.rowconfigure(0, weight=1)

#     # Create the main frame for the login
#     login_frame = ctk.CTkFrame(root, fg_color="#f0f4f8")
#     login_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
#     # Center the login frame
#     login_frame.grid_propagate(False)  # Prevent resizing of the frame
#     login_frame.grid_columnconfigure(0, weight=1)

#     # Header Label
#     header_label = ctk.CTkLabel(login_frame, text="Sign In", font=ctk.CTkFont(size=24, weight="bold"), text_color="#2C3E50")
#     header_label.grid(row=0, column=0, pady=(10, 20), sticky="n")

#     # Create username entry field
#     username_label = ctk.CTkLabel(login_frame, text="Username:", font=ctk.CTkFont(size=14), text_color="#2C3E50")
#     username_label.grid(row=1, column=0, padx=20, sticky="n")

#     username_entry = ctk.CTkEntry(login_frame, placeholder_text="Enter your username", width=400, height=35)
#     username_entry.grid(row=2, column=0, padx=20, pady=5)

#     # Create password entry field
#     password_label = ctk.CTkLabel(login_frame, text="Password:", font=ctk.CTkFont(size=14), text_color="#2C3E50")
#     password_label.grid(row=3, column=0, padx=20, sticky="n")

#     password_entry = ctk.CTkEntry(login_frame, placeholder_text="Enter your password", show="*", width=400, height=35)
#     password_entry.grid(row=4, column=0, padx=20, pady=5)

#     # Show password toggle
#     show_password_var = ctk.BooleanVar()
#     def toggle_password():
#         password_entry.configure(show="" if show_password_var.get() else "*")
#     show_password_checkbox = ctk.CTkCheckBox(login_frame, text="Show Password", variable=show_password_var, command=toggle_password, text_color="#2C3E50")
#     show_password_checkbox.grid(row=5, column=0, padx=20, pady=5, sticky="n")

#     # Error Label (initially hidden)
#     error_label = ctk.CTkLabel(login_frame, text="", text_color="red")
#     error_label.grid(row=6, column=0, pady=5)

#     # Login functionality
#     def login():
#         username = username_entry.get().strip()
#         password = password_entry.get().strip()
#         conn = connect_db()
#         if conn:
#             cursor = conn.cursor()
#             cursor.execute("SELECT password, staff_id FROM staff WHERE username=%s", (username,))
#             result = cursor.fetchone()
#             conn.close()

#             if result:
#                 stored_hashed_password = result[0]
#                 staff_id = result[1]

#                 # Verify password
#                 if checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
#                     messagebox.showinfo("Login Success", "Login successful!")
#                     for widget in root.winfo_children():
#                         widget.destroy()
#                     create_home_page(root, staff_id)
#                 else:
#                     error_label.configure(text="Incorrect password. Please try again.")
#             else:
#                 error_label.configure(text="Username not found. Please check and try again.")
#         else:
#             error_label.configure(text="Connection error. Please try again.")

#     # Clear fields
#     def clear_fields():
#         username_entry.delete(0, "end")
#         password_entry.delete(0, "end")
#         error_label.configure(text="")

#     # Buttons
#     button_frame = ctk.CTkFrame(login_frame, fg_color="#f0f4f8")
#     button_frame.grid(row=7, column=0, pady=20)

#     login_button = ctk.CTkButton(button_frame, text="Login", command=login, width=150, height=40, fg_color="#1ABC9C", text_color="white", hover_color="#16A085")
#     login_button.grid(row=0, column=0, padx=10)

#     reset_button = ctk.CTkButton(button_frame, text="Reset", command=clear_fields, width=150, height=40, fg_color="#E74C3C", text_color="white", hover_color="#C0392B")
#     reset_button.grid(row=0, column=1, padx=10)

#     forgot_password_button = ctk.CTkButton(button_frame, text="Forgot Password?", command=lambda: forgot_password(root), width=150, height=40, fg_color="#3498DB", text_color="white", hover_color="#2980B9")
#     forgot_password_button.grid(row=0, column=2, padx=10)

#     # Load the illustration
#     illustration_img = Image.open("logos/login.png")  # Update with your illustration path
#     illustration_img = ctk.CTkImage(illustration_img, size=(350, 350))

#     # Illustration Label
#     illustration_label = ctk.CTkLabel(login_frame, image=illustration_img, text="")
#     illustration_label.grid(row=8, column=0, rowspan=3, padx=20, pady=20, sticky="e")



#     def forgot_password(root):
#         # Create Toplevel window for password reset
#         reset_window = tk.Toplevel(root)
#         reset_window.title("Reset Password")
#         reset_window.geometry("400x350")

#         # Username Label and Entry
#         tk.Label(reset_window, text="Enter Username:", font=("Arial", 14)).pack(pady=10)
#         username_entry = tk.Entry(reset_window, width=30)
#         username_entry.pack(pady=5)

#         # Password Label and Entry
#         tk.Label(reset_window, text="Enter New Password:", font=("Arial", 14)).pack(pady=10)
#         new_password_entry = tk.Entry(reset_window, width=30, show="*")
#         new_password_entry.pack(pady=5)

#         # Password validation error message
#         error_label = tk.Label(reset_window, text="", fg="red", font=("Arial", 12))
#         error_label.pack(pady=5)

#         # Show Password Checkbox
#         def toggle_password():
#             if show_password_var.get():
#                 new_password_entry.config(show="")
#             else:
#                 new_password_entry.config(show="*")

#         show_password_var = tk.BooleanVar()
#         tk.Checkbutton(reset_window, text="Show Password", variable=show_password_var, command=toggle_password).pack(pady=5)

#         # Validate password fields
#         def validate_fields():
#             password = new_password_entry.get().strip()

#             if len(password) < 8 or len(password) > 20:
#                 error_label.config(text="Password must be 8-20 characters long.")
#                 return False
#             if not re.search(r"[A-Z]", password):
#                 error_label.config(text="Password must contain at least one uppercase letter.")
#                 return False
#             if not re.search(r"[a-z]", password):
#                 error_label.config(text="Password must contain at least one lowercase letter.")
#                 return False
#             if not re.search(r"[0-9]", password):
#                 error_label.config(text="Password must contain at least one number.")
#                 return False
#             if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
#                 error_label.config(text="Password must contain at least one special character.")
#                 return False
#             if re.search(r"\s", password):
#                 error_label.config(text="Password must not contain spaces.")
#                 return False

#             error_label.config(text="")  # Clear any previous errors
#             return True

#         # Reset password in the database
#         def submit_reset_password():
#             if not validate_fields():
#                 return

#             username = username_entry.get().strip()
#             new_password = new_password_entry.get().strip()
#             hashed_password = hashpw(new_password.encode('utf-8'), gensalt()).decode('utf-8')

#             conn = connect_db()
#             if conn:
#                 cursor = conn.cursor()
#                 cursor.execute("UPDATE staff SET password=%s WHERE username=%s", (hashed_password, username))
#                 conn.commit()
#                 if cursor.rowcount == 0:  # No rows updated means username not found
#                     messagebox.showerror("Error", "Username not found. Please try again.")
#                 else:
#                     messagebox.showinfo("Success", "Password reset successfully!")
#                     reset_window.destroy()
#                 conn.close()
#             else:
#                 messagebox.showerror("Error", "Connection error. Please try again.")

#         # Submit Button
#         tk.Button(reset_window, text="Submit", command=submit_reset_password, width=20).pack(pady=20)


import re
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from bcrypt import checkpw
from PIL import Image, ImageTk
from bcrypt import hashpw, gensalt
from db_connection import connect_db
from home_page import create_home_page

def show_login(root):
    error_labels = {}

    # Initialize CustomTkinter appearance
    ctk.set_appearance_mode("light")  # Change to "dark" for dark mode
    ctk.set_default_color_theme("blue")  # Customize the color theme if desired

    # Clear root frame
    for widget in root.winfo_children():
        widget.destroy()

    # Configure root layout for responsiveness
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Create main login frame
    login_frame = ctk.CTkFrame(root, fg_color="#f0f4f8")
    login_frame.grid(row=0, column=0, sticky="nsew")
    login_frame.grid_rowconfigure(0, weight=1)  # Top spacing
    login_frame.grid_rowconfigure(1, weight=3)  # Content area
    login_frame.grid_columnconfigure(0, weight=1)  # Center alignment

    # Header Label
    header_label = ctk.CTkLabel(login_frame, text="Sign In", font=ctk.CTkFont(size=24, weight="bold"), text_color="#2C3E50")
    header_label.grid(row=0, column=0, pady=(10, 20), sticky="n")

    # Create username entry field
    username_label = ctk.CTkLabel(login_frame, text="Username:", font=ctk.CTkFont(size=14), text_color="#2C3E50")
    username_label.grid(row=1, column=0, padx=20, sticky="n")

    username_entry = ctk.CTkEntry(login_frame, placeholder_text="Enter your username", width=400, height=35)
    username_entry.grid(row=2, column=0, padx=20, pady=5)

    # Create password entry field
    password_label = ctk.CTkLabel(login_frame, text="Password:", font=ctk.CTkFont(size=14), text_color="#2C3E50")
    password_label.grid(row=3, column=0, padx=20, sticky="n")

    password_entry = ctk.CTkEntry(login_frame, placeholder_text="Enter your password", show="*", width=400, height=35)
    password_entry.grid(row=4, column=0, padx=20, pady=5)

    # Show password toggle
    show_password_var = ctk.BooleanVar()
    def toggle_password():
        password_entry.configure(show="" if show_password_var.get() else "*")
    show_password_checkbox = ctk.CTkCheckBox(login_frame, text="Show Password", variable=show_password_var, command=toggle_password, text_color="#2C3E50")
    show_password_checkbox.grid(row=5, column=0, padx=20, pady=5, sticky="n")

    # Error Label (initially hidden)
    error_label = ctk.CTkLabel(login_frame, text="", text_color="red")
    error_label.grid(row=6, column=0, pady=5)

    # Login functionality
    def login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT password, staff_id FROM staff WHERE username=%s", (username,))
            result = cursor.fetchone()
            conn.close()

            if result:
                stored_hashed_password = result[0]
                staff_id = result[1]

                # Verify password
                if checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
                    messagebox.showinfo("Login Success", "Login successful!")
                    for widget in root.winfo_children():
                        widget.destroy()
                    create_home_page(root, staff_id)
                else:
                    error_label.configure(text="Incorrect password. Please try again.")
            else:
                error_label.configure(text="Username not found. Please check and try again.")
        else:
            error_label.configure(text="Connection error. Please try again.")

    # Clear fields
    def clear_fields():
        username_entry.delete(0, "end")
        password_entry.delete(0, "end")
        error_label.configure(text="")

    # Buttons
    button_frame = ctk.CTkFrame(login_frame, fg_color="#f0f4f8")
    button_frame.grid(row=7, column=0, pady=20)

    login_button = ctk.CTkButton(button_frame, text="Login", command=login, width=150, height=40, fg_color="#1ABC9C", text_color="white", hover_color="#16A085")
    login_button.grid(row=0, column=0, padx=10)

    reset_button = ctk.CTkButton(button_frame, text="Reset", command=clear_fields, width=150, height=40, fg_color="#E74C3C", text_color="white", hover_color="#C0392B")
    reset_button.grid(row=0, column=1, padx=10)

    forgot_password_button = ctk.CTkButton(button_frame, text="Forgot Password?", command=lambda: forgot_password(root), width=150, height=40, fg_color="#3498DB", text_color="white", hover_color="#2980B9")
    forgot_password_button.grid(row=0, column=2, padx=10)

    # Load and resize the illustration
    illustration_img = Image.open("logos/login.png")
    illustration_img = ctk.CTkImage(illustration_img, size=(350, 350))

    # Illustration Label
    illustration_label = ctk.CTkLabel(login_frame, image=illustration_img, text="")
    illustration_label.grid(row=8, column=0, padx=20, pady=20, sticky="e")

    def forgot_password(root):
        # Create Toplevel window for password reset
        reset_window = tk.Toplevel(root)
        reset_window.title("Reset Password")
        reset_window.geometry("400x350")

        # Username Label and Entry
        tk.Label(reset_window, text="Enter Username:", font=("Arial", 14)).pack(pady=10)
        username_entry = tk.Entry(reset_window, width=30)
        username_entry.pack(pady=5)

        # Password Label and Entry
        tk.Label(reset_window, text="Enter New Password:", font=("Arial", 14)).pack(pady=10)
        new_password_entry = tk.Entry(reset_window, width=30, show="*")
        new_password_entry.pack(pady=5)

        # Password validation error message
        error_label = tk.Label(reset_window, text="", fg="red", font=("Arial", 12))
        error_label.pack(pady=5)

        # Show Password Checkbox
        def toggle_password():
            if show_password_var.get():
                new_password_entry.config(show="")
            else:
                new_password_entry.config(show="*")

        show_password_var = tk.BooleanVar()
        tk.Checkbutton(reset_window, text="Show Password", variable=show_password_var, command=toggle_password).pack(pady=5)

        # Validate password fields
        def validate_fields():
            password = new_password_entry.get().strip()

            if len(password) < 8 or len(password) > 20:
                error_label.config(text="Password must be 8-20 characters long.")
                return False
            if not re.search(r"[A-Z]", password):
                error_label.config(text="Password must contain at least one uppercase letter.")
                return False
            if not re.search(r"[a-z]", password):
                error_label.config(text="Password must contain at least one lowercase letter.")
                return False
            if not re.search(r"[0-9]", password):
                error_label.config(text="Password must contain at least one number.")
                return False
            if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
                error_label.config(text="Password must contain at least one special character.")
                return False
            if re.search(r"\s", password):
                error_label.config(text="Password must not contain spaces.")
                return False

            error_label.config(text="")  # Clear any previous errors
            return True

        # Reset password in the database
        def submit_reset_password():
            if not validate_fields():
                return

            username = username_entry.get().strip()
            new_password = new_password_entry.get().strip()
            hashed_password = hashpw(new_password.encode('utf-8'), gensalt()).decode('utf-8')

            conn = connect_db()
            if conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE staff SET password=%s WHERE username=%s", (hashed_password, username))
                conn.commit()
                if cursor.rowcount == 0:  # No rows updated means username not found
                    messagebox.showerror("Error", "Username not found. Please try again.")
                else:
                    messagebox.showinfo("Success", "Password reset successfully!")
                    reset_window.destroy()
                conn.close()
            else:
                messagebox.showerror("Error", "Connection error. Please try again.")

        # Submit Button
        tk.Button(reset_window, text="Submit", command=submit_reset_password, width=20).pack(pady=20)

    # Responsive resizing logic
    root.bind("<Configure>", lambda event: adapt_layout(event, root))

def adapt_layout(event, root):
    width = root.winfo_width()
    height = root.winfo_height()
    # Adjust UI elements based on the window's size
    # Example: resize entry boxes, reposition elements, etc.
