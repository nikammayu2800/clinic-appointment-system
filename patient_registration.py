import customtkinter as ctk
from tkcalendar import DateEntry
from datetime import datetime
from tkinter import Toplevel, messagebox
import tkinter as tk
from tkcalendar import Calendar
from PIL import Image, ImageTk  # For handling images
from db_connection import connect_db
import re


def show_registration(root, staff_id):
    from home_page import create_home_page

    # Define placeholders and error labels dictionary
    error_labels = {}

    def open_calendar(entry_widget):
            try:
                calendar_window = Toplevel()
                calendar_window.title("Select Date")
                cal = Calendar(calendar_window, selectmode="day", date_pattern="y-mm-dd")
                cal.pack(padx=10, pady=10)

                def select_date():
                    entry_widget.delete(0, tk.END)
                    entry_widget.insert(0, cal.get_date())
                    calendar_window.destroy()

                select_button = tk.Button(calendar_window, text="Select", command=select_date)
                select_button.pack(pady=5)
            except Exception as e:
                print(f"Error opening calendar: {e}")
                messagebox.showerror("Error", "Failed to open the calendar widget.")

    # Initialize CustomTkinter appearance
    ctk.set_appearance_mode("light")  # Change to "dark" for dark mode
    ctk.set_default_color_theme("blue")  # Customize the color theme if desired

    # Clear the main window
    for widget in root.winfo_children():
        widget.destroy()

    # Set up the main frame and configure the layout weights
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    # Set up main registration frame
    reg_frame = ctk.CTkFrame(root, fg_color="#f0f4f8", corner_radius=10, width=600)
    reg_frame.pack(fill="both", expand=True)
    reg_frame.grid_columnconfigure(0, weight=1)
    reg_frame.grid_rowconfigure(0, weight=2)
    reg_frame.grid_rowconfigure(1, weight=2)
    reg_frame.grid_rowconfigure(2, weight=2)

    # Header Frame
    header_frame = ctk.CTkFrame(reg_frame, fg_color="#3b8ed0", corner_radius=10)
    header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
    header_frame.grid_columnconfigure(1, weight=1) 
    header_frame.grid_rowconfigure(0, weight=1)

    # Header Title
    title_label = ctk.CTkLabel(header_frame, text="Patient Registration Form", font=ctk.CTkFont("Helvetica", 24, "bold"), text_color="white")
    title_label.grid(row=0, column=1, pady=10, sticky="nsew")
    
    # Adjust fields_frame to allow expansion
    fields_frame = ctk.CTkFrame(reg_frame, fg_color="#f0f4f8", width=600)
    fields_frame.grid(row=1, column=0, columnspan=2)
    fields_frame.grid_columnconfigure(0, weight=1)
    fields_frame.grid_columnconfigure(1, weight=1)
    fields_frame.grid_rowconfigure(0, weight=1)
    fields_frame.grid_rowconfigure(1, weight=1)
    fields_frame.grid_rowconfigure(2, weight=1)
    fields_frame.grid_rowconfigure(3, weight=1)
    fields_frame.grid_rowconfigure(4, weight=1)
    fields_frame.grid_rowconfigure(5, weight=1)
    fields_frame.grid_rowconfigure(6, weight=1)
    fields_frame.grid_rowconfigure(7, weight=1)
    fields_frame.grid_rowconfigure(8, weight=1)
    fields_frame.grid_rowconfigure(9, weight=1)
    fields_frame.grid_rowconfigure(10, weight=1)
    fields_frame.grid_rowconfigure(11, weight=1)


    # First Name Field Setup
    fn_asterisk_label = ctk.CTkLabel(fields_frame, text="*", text_color="red", font=ctk.CTkFont(size=12, weight="bold"))
    fn_asterisk_label.grid(row=0, column=0, sticky="w", padx=25, pady=(15, 0))
    first_name_label = ctk.CTkLabel(fields_frame, text="First Name:", font=ctk.CTkFont(size=12), text_color="black")
    first_name_label.grid(row=0, column=0, sticky="w", padx=35, pady=(10, 0))
    entry_first_name = ctk.CTkEntry(fields_frame, width=200, font=ctk.CTkFont(size=12), placeholder_text="Enter First Name")
    entry_first_name.grid(row=1, column=0, pady=(0, 20), padx=25, sticky="w")
    error_labels["first_name"] = ctk.CTkLabel(fields_frame, text="", text_color="red", font=("Arial", 10))
    error_labels["first_name"].grid(row=1, column=0, pady=(35,0), padx=30, sticky="w")

    # Last Name
    ln_asterisk_label = ctk.CTkLabel(fields_frame, text="*", text_color="red", font=ctk.CTkFont(size=12, weight="bold"))
    ln_asterisk_label.grid(row=2, column=0, sticky="w", padx=25, pady=(15,0))
    last_name_label = ctk.CTkLabel(fields_frame, text="Last Name:")
    last_name_label.grid(row=2, column=0, sticky="w", padx=35, pady=(10,0))
    entry_last_name = ctk.CTkEntry(fields_frame, width=200, font=ctk.CTkFont(size=12), placeholder_text="Enter Last Name")
    entry_last_name.grid(row=3, column=0, pady=(0,20), padx=25, sticky="w")
    error_labels["last_name"] = ctk.CTkLabel(fields_frame, text="", text_color="red", font=("Arial", 10))
    error_labels["last_name"].grid(row=3, column=0, pady=(35,0), padx=30, sticky="w")

    # Date of Birth
    dob_label = ctk.CTkLabel(fields_frame, text="Date of Birth:")
    dob_label.grid(row=4, column=0, padx=25, pady=(15,0), sticky="w")
    dob_frame = ctk.CTkFrame(fields_frame, fg_color="#f0f4f8", width=600)
    dob_frame.grid(row=5, column=0, pady=(0,20), padx=25, sticky="w")
    dob_frame.grid_rowconfigure(0, weight=1)
    dob_frame.grid_columnconfigure(0, weight=1)
    dob_frame.grid_columnconfigure(1, weight=1)
    entry_dob = ctk.CTkEntry(dob_frame, placeholder_text="YYYY-MM-DD")
    entry_dob.grid(row=0, column=0, pady=(0,20), sticky="w")
    # Button to open the calendar
    open_calendar_button = ctk.CTkButton(dob_frame, text="Pick a Date", command=lambda: open_calendar(entry_dob))
    open_calendar_button.grid(row=0, column=1, padx=20, pady=(0,20), sticky="w")
    error_labels["dob"] = ctk.CTkLabel(dob_frame, text="", text_color="red", font=("Arial", 10))
    error_labels["dob"].grid(row=0, column=0, pady=(35,0), padx=30, sticky="w")

    # Gender
    g_asterisk_label = ctk.CTkLabel(fields_frame, text="*", text_color="red", font=ctk.CTkFont(size=12, weight="bold"))
    g_asterisk_label.grid(row=6, column=0, sticky="w", padx=25, pady=(15, 0))
    gender_label = ctk.CTkLabel(fields_frame, text="Gender:")
    gender_label.grid(row=6, column=0, sticky="w", padx=35, pady=(10,0))
    gender_frame = ctk.CTkFrame(fields_frame, fg_color="#f0f4f8", width=600)
    gender_frame.grid(row=7, column=0, pady=(0,20), padx=25, sticky="w")
    gender_frame.grid_rowconfigure(0, weight=1)
    gender_frame.grid_columnconfigure(0, weight=1)
    gender_frame.grid_columnconfigure(1, weight=1)
    gender_frame.grid_columnconfigure(2, weight=1)
    gender_var = ctk.StringVar(value=None)
    ctk.CTkRadioButton(gender_frame, text="Male", variable=gender_var, value="Male").grid(row=0, column=0, pady=(5, 10), sticky="w")
    ctk.CTkRadioButton(gender_frame, text="Female", variable=gender_var, value="Female").grid(row=0, column=1, padx=20, pady=(5, 10), sticky="w")
    ctk.CTkRadioButton(gender_frame, text="Other", variable=gender_var, value="Other").grid(row=0, column=2, padx=20 , pady=(5, 10), sticky="w")
    error_labels["gender"] = ctk.CTkLabel(fields_frame, text="", text_color="red", font=("Arial", 10))
    error_labels["gender"].grid(row=7, column=0, pady=(35,0), padx=30, sticky="w")

    # Phone Number
    pn_asterisk_label = ctk.CTkLabel(fields_frame, text="*", text_color="red", font=ctk.CTkFont(size=12, weight="bold"))
    pn_asterisk_label.grid(row=8, column=0, sticky="w", padx=25, pady=(15, 0))
    phone_label = ctk.CTkLabel(fields_frame, text="Phone Number:")
    phone_label.grid(row=8, column=0, sticky="w", padx=35, pady=(10,0))
    entry_phone = ctk.CTkEntry(fields_frame, width=200, font=ctk.CTkFont(size=12), placeholder_text="Enter Phone Number")
    entry_phone.grid(row=9, column=0, pady=(0,20), padx=25, sticky="w")
    error_labels["phone"] = ctk.CTkLabel(fields_frame, text="", text_color="red", font=("Arial", 10))
    error_labels["phone"].grid(row=9, column=0, pady=(35,0), padx=30, sticky="w")

    # Email
    em_asterisk_label = ctk.CTkLabel(fields_frame, text="*", text_color="red", font=ctk.CTkFont(size=12, weight="bold"))
    em_asterisk_label.grid(row=10, column=0, sticky="w", padx=25, pady=(15, 0))
    email_label = ctk.CTkLabel(fields_frame, text="Email:")
    email_label.grid(row=10, column=0, sticky="w", padx=35, pady=(10,0))
    entry_email = ctk.CTkEntry(fields_frame, width=200, font=ctk.CTkFont(size=12), placeholder_text="Enter Email")
    entry_email.grid(row=11, column=0, pady=(0,20), padx=25, sticky="w")
    error_labels["email"] = ctk.CTkLabel(fields_frame, text="", text_color="red", font=("Arial", 10))
    error_labels["email"].grid(row=11, column=0, pady=(35,0), padx=30, sticky="w")

    # Addrees Line 1
    al1_asterisk_label = ctk.CTkLabel(fields_frame, text="*", text_color="red", font=ctk.CTkFont(size=12, weight="bold"))
    al1_asterisk_label.grid(row=0, column=1, sticky="w", padx=25, pady=(15, 0))
    address1_label = ctk.CTkLabel(fields_frame, text="Address Line 1:")
    address1_label.grid(row=0, column=1, sticky="w", padx=35, pady=(10,0))
    entry_address1 = ctk.CTkEntry(fields_frame, width=200, font=ctk.CTkFont(size=12), placeholder_text="Enter Address Line 1")
    entry_address1.grid(row=1, column=1, pady=(0,20), padx=25, sticky="w")
    error_labels["address1"] = ctk.CTkLabel(fields_frame, text="", text_color="red", font=("Arial", 10))
    error_labels["address1"].grid(row=1, column=1, pady=(35,0), padx=30, sticky="w")

    address2_label = ctk.CTkLabel(fields_frame, text="Address Line 2:")
    address2_label.grid(row=2, column=1, sticky="w", padx=35, pady=(10,0))
    entry_address2 = ctk.CTkEntry(fields_frame, width=200, font=ctk.CTkFont(size=12), placeholder_text="Enter Address Line 2")
    entry_address2.grid(row=3, column=1, pady=(0,20), padx=25, sticky="w")
   
    # City
    c_asterisk_label = ctk.CTkLabel(fields_frame, text="*", text_color="red", font=ctk.CTkFont(size=12, weight="bold"))
    c_asterisk_label.grid(row=4, column=1, sticky="w", padx=25, pady=(15, 0))
    c_label = ctk.CTkLabel(fields_frame, text="City:")
    c_label.grid(row=4, column=1, sticky="w", padx=35, pady=(10,0))
    entry_city = ctk.CTkEntry(fields_frame, width=200, font=ctk.CTkFont(size=12), placeholder_text="Enter City")
    entry_city.grid(row=5, column=1, pady=(0,20), padx=25, sticky="w")
    error_labels["city"] = ctk.CTkLabel(fields_frame, text="", text_color="red", font=("Arial", 10))
    error_labels["city"].grid(row=5, column=1, pady=(35,0), padx=30, sticky="w")

    # State
    s_asterisk_label = ctk.CTkLabel(fields_frame, text="*", text_color="red", font=ctk.CTkFont(size=12, weight="bold"))
    s_asterisk_label.grid(row=6, column=1, sticky="w", padx=25, pady=(15, 0))
    s_label = ctk.CTkLabel(fields_frame, text="State:")
    s_label.grid(row=6, column=1, sticky="w", padx=35, pady=(10,0))
    entry_state = ctk.CTkEntry(fields_frame, width=200, font=ctk.CTkFont(size=12), placeholder_text="Enter State")
    entry_state.grid(row=7, column=1, pady=(0,20), padx=25, sticky="w")
    error_labels["state"] = ctk.CTkLabel(fields_frame, text="", text_color="red", font=("Arial", 10))
    error_labels["state"].grid(row=7, column=1, pady=(35,0), padx=30, sticky="w")

    # Zip Code
    zc_asterisk_label = ctk.CTkLabel(fields_frame, text="*", text_color="red", font=ctk.CTkFont(size=12, weight="bold"))
    zc_asterisk_label.grid(row=8, column=1, sticky="w", padx=25, pady=(15, 0))
    zc_label = ctk.CTkLabel(fields_frame, text="Zip Code:")
    zc_label.grid(row=8, column=1, sticky="w", padx=35, pady=(10,0))
    entry_zip = ctk.CTkEntry(fields_frame, width=200, font=ctk.CTkFont(size=12), placeholder_text="Enter Zip Code")
    entry_zip.grid(row=9, column=1, pady=(0,20), padx=25, sticky="w")
    error_labels["zip"] = ctk.CTkLabel(fields_frame, text="", text_color="red", font=("Arial", 10))
    error_labels["zip"].grid(row=9, column=1, pady=(35,0), padx=30, sticky="w")

    # Clear Field
    def clear_fields():
        entry_first_name.delete(0, ctk.END)
        entry_last_name.delete(0, ctk.END)
        entry_dob.delete(0, ctk.END)
        gender_var.set(None)
        entry_phone.delete(0, ctk.END)
        entry_email.delete(0, ctk.END)
        entry_address1.delete(0, ctk.END)
        entry_address2.delete(0, ctk.END)
        entry_city.delete(0, ctk.END)
        entry_state.delete(0, ctk.END)
        entry_zip.delete(0, ctk.END)

        # Clear all previous error messages
        for error_label in error_labels.values():
            error_label.configure(text="")

    # Validate Field
    def validate_fields():
    # Clear all previous error messages
        for error_label in error_labels.values():
            error_label.configure(text="")

        # Track validation status
        valid = True

        # Validate First Name
        first_name = entry_first_name.get().strip()
        if not first_name.isalpha():
            error_labels["first_name"].configure(text="First name must only contain letters.")
            valid = False

        # Validate First Name
        last_name = entry_last_name.get().strip()
        if not last_name.isalpha():
            error_labels["last_name"].configure(text="Last name must only contain letters.")
            valid = False

        dob = entry_dob.get()
        if not dob:
            error_labels["dob"].configure(text="Please select a date..")
            valid = False

        if dob:
            dob_date = datetime.strptime(dob, "%Y-%m-%d").date()
            today = datetime.today().date() # Get today's date without the time part
            if dob_date > today:
                error_labels["dob"].configure(text="The selected date cannot be in the future.")
                valid = False

        gender = gender_var.get()
        if not gender:
            error_labels["gender"].configure(text="Select the gender.")
            valid = False


        # # Validate Email
        email = entry_email.get().strip()
        if not email or "@" not in email or "." not in email:
            error_labels["email"].configure(text="Enter a valid email address.")
            valid = False

        # # Validate Phone Number
        phone = entry_phone.get().strip()
        if not phone.isdigit() or len(phone) != 10:
            error_labels["phone"].configure(text="Phone number must be 10 digits.")
            valid = False

        address1 = entry_address1.get().strip()
        if not address1:
            error_labels["address1"].configure(text="Enter a address 1")
            valid = False

        city_pattern = r'^[a-zA-Z\s]+$'
        city = entry_city.get().strip()
        if not re.match(city_pattern, city):
            error_labels["city"].configure(text="City should only contain alphabetic characters and spaces.")
            valid = False

        state = entry_state.get().strip()
        if not re.match(city_pattern, state):  # Using the same pattern as for city
            error_labels["state"].configure(text="State should only contain alphabetic characters and spaces.")
            valid = False

        zip = entry_zip.get().strip()
        if not zip.isdigit() or not (len(zip) == 5 or len(zip) == 9):
            error_labels["zip"].configure(text="Zip code should be a valid 5 or 9-digit number.")
            valid = False

        # Show success message if all fields are valid
        if valid:
            return True
        else:
            return False

    # Validation and Registration
    def register_patient():
        if not validate_fields():
            return

        # Fetch and trim input values
        first_name = entry_first_name.get().strip()
        last_name = entry_last_name.get().strip()
        dob_str = entry_dob.get()
        gender = gender_var.get()
        phone = entry_phone.get().strip()
        email = entry_email.get().strip()
        address1 = entry_address1.get().strip()
        address2 = entry_address2.get().strip()
        city = entry_city.get().strip()
        state = entry_state.get().strip()
        zip_code = entry_zip.get().strip()

        # Insert data into database
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO patients (first_name, last_name, dob, gender, phone, email, address1, address2, city, state, zip_code) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (first_name, last_name, dob_str, gender, phone, email, address1, address2, city, state, zip_code)
                )
                conn.commit()
                clear_fields()
                messagebox.showinfo("Success", "Patient registered successfully!")
            except Exception as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")
            finally:
                conn.close()

    # Go back to the main screen
    def go_back():
        reg_frame.destroy()
        create_home_page(root, staff_id)

    # Button Actions and Frame
    button_frame = ctk.CTkFrame(reg_frame, fg_color="#f0f4f8")
    button_frame.grid(row=3, column=0, columnspan=2, pady=(0,10), padx=10)
    button_frame.grid_columnconfigure((0, 1, 2), weight=1) 
    button_frame.grid_rowconfigure(1, weight=1)

    submit_btn = ctk.CTkButton(button_frame, text="Save", command=register_patient)
    submit_btn.grid(row=0, column=0, padx=10)

    reset_btn = ctk.CTkButton(button_frame, text="Clear", command=clear_fields)
    reset_btn.grid(row=0, column=1, padx=10)

    back_btn = ctk.CTkButton(button_frame, text="Back", command=go_back)
    back_btn.grid(row=0, column=2, padx=10)

      # Ensure that when the window size changes, widgets resize accordingly
    root.update_idletasks()
