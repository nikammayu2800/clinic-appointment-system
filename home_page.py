# from datetime import datetime
# import tkinter as tk
# import customtkinter as ctk
# from tkinter import ttk
# from PIL import Image, ImageTk, ImageOps # For adding logos
# from db_connection import connect_db  
# from our_community import our_community
# from patient_registration import show_registration
# from appointment_booking import show_appointment_booking
# from appointment_management import show_appointment_management
# from appointment_cancellation import show_appointment_cancellation
# from daily_view import show_daily_appointments

# def create_home_page(root, staff_id):
#     # Initialize CustomTkinter appearance
#     ctk.set_appearance_mode("light")  # Change to "dark" for dark mode
#     ctk.set_default_color_theme("blue")  # Customize the color theme if desired

#     # Clear existing widgets
#     for widget in root.winfo_children():
#         widget.destroy()

#     # Set up the main frame and configure the layout weights
#     root.columnconfigure(0, weight=1)
#     root.rowconfigure(0, weight=1)

#     # Set up main home page frame
#     home_frame = ctk.CTkFrame(root, fg_color="#f0f4f8", corner_radius=10, width=600)
#     home_frame.pack(fill="both", expand=True)
#     home_frame.columnconfigure(0, weight=1)
#     home_frame.columnconfigure(1, weight=1)

#     # Header Frame
#     header_frame = ctk.CTkFrame(home_frame, fg_color="#3b8ed0", corner_radius=10)
#     header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
#     # Configure the columns of the header_frame
#     header_frame.columnconfigure(0, weight=1)  # Left side (user info)
#     header_frame.columnconfigure(1, weight=1)  # Center (title)
#     header_frame.columnconfigure(2, weight=1)  # Right side (logout button) 

#     # Header Title
#     title_label = ctk.CTkLabel(header_frame, text="Patient Registration Form", font=ctk.CTkFont("Helvetica", 24, "bold"), text_color="white")
#     title_label.grid(row=0, column=1, pady=10, sticky="nsew")

#     # Display logged-in user info
#     conn = connect_db()
#     if conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT first_name, last_name, role FROM staff WHERE staff_id = %s", (staff_id,))
#         user_info = cursor.fetchone()
#         conn.close()
    
#     if user_info:
#         user_first_name, user_last_name, user_role = user_info
#         # Get the current timestamp
#         login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format it to a readable form
    
#         user_info_label = ctk.CTkLabel(header_frame, text=f"  Logged in as: {user_first_name} {user_last_name} ({user_role})\nLogged in at: {login_time}", font=ctk.CTkFont("Helvetica", 14, "bold"), text_color="white")
#         user_info_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

#     # Logout button
#     logout_logo = ctk.CTkImage(Image.open('logos/logout.png'), size=(30, 30))
#     logout_btn = ctk.CTkButton(header_frame, image=logout_logo, text="", command=lambda: logout(root), fg_color="#3b8ed0", hover_color="#3b8ed0")
#     logout_btn.grid(row=1, column=2, padx=5, pady=5, sticky="e")

#     # Title with horizontal lines
#     title_frame = ctk.CTkFrame(home_frame, fg_color="#ffffff")
#     title_frame.grid(row=2, column=0, pady=20, padx=10)
#     title_frame.columnconfigure(0, weight=1)
#     title_frame.columnconfigure(1, weight=1)
#     title_label = ctk.CTkLabel(title_frame, text="What would you like to do?", font=("Arial", 24, "bold"), text_color="#2C3E50")
#     title_label.grid(row=0, column=1, padx=20, sticky="ew")

#     # Left and Right Lines
#     line_left = ctk.CTkLabel(title_frame, text="―" * 13, text_color="#d3d3d3", font=("Arial", 24))
#     line_left.grid(row=0, column=0, sticky="ew")
#     line_right = ctk.CTkLabel(title_frame, text="―" * 13, text_color="#d3d3d3", font=("Arial", 24))
#     line_right.grid(row=0, column=2, sticky="ew")

#     # Create navigation section with menu logos
#     nav_frame = ctk.CTkFrame(home_frame, fg_color='#f0f4f8', width=600)
#     nav_frame.grid(row=3, column=0, columnspan=2, padx=50, sticky="nsew")
#     nav_frame.columnconfigure(0, weight=1)
#     nav_frame.columnconfigure(1, weight=1)

#     # Load the illustration
#     illustration_img = Image.open("logos/welcome.png")  # Update with your illustration path
#     illustration_img = ctk.CTkImage(illustration_img, size=(450, 300))

#     # Illustration Label
#     illustration_label = ctk.CTkLabel(home_frame, image=illustration_img, text="")
#     illustration_label.grid(row=4, column=0, rowspan=3, padx=20, pady=(30,20), sticky="e")

#     # Menu options with paths to your icons
#     menu_options = [
#         ("Register Patient", "logos/user_plus.png", lambda: show_registration(root, staff_id)),
#         ("Book Appointment", "logos/calendar_check.png", lambda: show_appointment_booking(root, staff_id)),
#         ("Manage Appointments", "logos/clipboard_list.png", lambda: show_appointment_management(root, staff_id)),
#         ("Daily View", "logos/calendar_day.png", lambda: show_daily_appointments(root, staff_id)),
#         ("Our Communities", "logos/our_community.png", lambda: our_community(root, staff_id))
#     ]

#     for idx, (name, icon_path, action) in enumerate(menu_options):
#         # Load the icon using CTkImage for HighDPI support
#         icon_image = ctk.CTkImage(Image.open(icon_path), size=(80, 80))
        
#         # Create a button with the icon only
#         logo_button = ctk.CTkButton(nav_frame, image=icon_image, command=action,
#                                     fg_color="transparent", hover_color="#f0f4f8",
#                                     text="", corner_radius=10, width=100, height=100)
#         logo_button.grid(row=0, column=idx, padx=40, pady=(10, 5))

#         # Create a label for the menu name
#         label = ctk.CTkLabel(nav_frame, text=name, font=("Arial", 14, "bold"),
#                             text_color="#2C3E50")
#         label.grid(row=1, column=idx, pady=(0, 20))

#     root.mainloop()

# def logout(root):
#     """Clears the home screen and shows the login screen."""
#     for widget in root.winfo_children():
#         widget.destroy()

#     # Local import to avoid circular dependency
#     from login_screen import show_login
#     # Force an update to refresh UI elements
#     root.update_idletasks()
#     show_login(root)  # Call your function that renders the login page


from datetime import datetime
import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk  # For adding logos
from db_connection import connect_db
from our_community import our_community
from patient_registration import show_registration
from appointment_booking import show_appointment_booking
from appointment_management import show_appointment_management
from appointment_cancellation import show_appointment_cancellation
from daily_view import show_daily_appointments


def create_home_page(root, staff_id):
    # Initialize CustomTkinter appearance
    ctk.set_appearance_mode("light")  # Change to "dark" for dark mode
    ctk.set_default_color_theme("blue")  # Customize the color theme if desired

    # Clear existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Configure root to expand with resizing
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Set up main frame
    home_frame = ctk.CTkFrame(root, fg_color="#f0f4f8", corner_radius=10)
    home_frame.grid(row=0, column=0, sticky="nsew")
    home_frame.columnconfigure(0, weight=1)
    home_frame.rowconfigure(3, weight=1)  # Make nav_frame expandable vertically

    # Header Frame
    header_frame = ctk.CTkFrame(home_frame, fg_color="#3b8ed0", corner_radius=10)
    header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
    header_frame.columnconfigure(0, weight=1)  # Left side (user info)
    header_frame.columnconfigure(1, weight=1)  # Center (title)
    header_frame.columnconfigure(2, weight=1)  # Right side (logout button)

    # Header Title
    title_label = ctk.CTkLabel(header_frame, text="Welcome to Lakside Health Clinic",
                               font=ctk.CTkFont("Helvetica", 24, "bold"), text_color="white")
    title_label.grid(row=0, column=1, pady=10, sticky="nsew")

    # Display logged-in user info
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT first_name, last_name, role FROM staff WHERE staff_id = %s", (staff_id,))
        user_info = cursor.fetchone()
        conn.close()

    if user_info:
        user_first_name, user_last_name, user_role = user_info
        login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format it to a readable form
        user_info_label = ctk.CTkLabel(header_frame, text=f"  Logged in as: {user_first_name} {user_last_name} ({user_role})\nLogged in at: {login_time}",
                                       font=ctk.CTkFont("Helvetica", 14, "bold"), text_color="white")
        user_info_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    # Logout button
    logout_logo = ctk.CTkImage(Image.open('logos/logout.png'), size=(30, 30))
    logout_btn = ctk.CTkButton(header_frame, image=logout_logo, text="", command=lambda: logout(root),
                                fg_color="#3b8ed0", hover_color="#3b8ed0")
    logout_btn.grid(row=1, column=2, padx=5, pady=5, sticky="e")

    # Title with horizontal lines
    title_frame = ctk.CTkFrame(home_frame, fg_color="#ffffff")
    title_frame.grid(row=1, column=0, pady=20, padx=10, sticky="ew")
    title_frame.columnconfigure(0, weight=1)
    title_label = ctk.CTkLabel(title_frame, text="What would you like to do?",
                               font=("Arial", 24, "bold"), text_color="#2C3E50")
    title_label.grid(row=0, column=0, padx=20, sticky="ew")

    # Create navigation section
    nav_frame = ctk.CTkFrame(home_frame, fg_color='#f0f4f8')
    nav_frame.grid(row=2, column=0, padx=50, pady=10, sticky="nsew")
    nav_frame.columnconfigure((0, 1, 2, 3, 4), weight=1)

    # Menu options
    menu_options = [
        ("Register Patient", "logos/user_plus.png", lambda: show_registration(root, staff_id)),
        ("Book Appointment", "logos/calendar_check.png", lambda: show_appointment_booking(root, staff_id)),
        ("Manage Appointments", "logos/clipboard_list.png", lambda: show_appointment_management(root, staff_id)),
        ("Daily View", "logos/calendar_day.png", lambda: show_daily_appointments(root, staff_id)),
        ("Our Communities", "logos/our_community.png", lambda: our_community(root, staff_id))
    ]

    for idx, (name, icon_path, action) in enumerate(menu_options):
        # Load the icon
        icon_image = ctk.CTkImage(Image.open(icon_path), size=(80, 80))

        # Create a button
        logo_button = ctk.CTkButton(nav_frame, image=icon_image, command=action,
                                    fg_color="transparent", hover_color="#d9d9d9",
                                    text="", corner_radius=10, width=100, height=100)
        logo_button.grid(row=0, column=idx, padx=20, pady=(10, 5), sticky="n")

        # Create a label for the menu name
        label = ctk.CTkLabel(nav_frame, text=name, font=("Arial", 14, "bold"),
                             text_color="#2C3E50")
        label.grid(row=1, column=idx, pady=(0, 20), sticky="n")

         # Load the illustration
    illustration_img = Image.open("logos/welcome.png")  # Update with your illustration path
    illustration_img = ctk.CTkImage(illustration_img, size=(450, 300))

    # Illustration Label
    illustration_label = ctk.CTkLabel(home_frame, image=illustration_img, text="")
    illustration_label.grid(row=3, column=0, padx=20, pady=(30, 20), sticky="ew")

    root.mainloop()


def logout(root):
    """Clears the home screen and shows the login screen."""
    for widget in root.winfo_children():
        widget.destroy()

    from login_screen import show_login  # Avoid circular imports
    root.update_idletasks()
    show_login(root)

