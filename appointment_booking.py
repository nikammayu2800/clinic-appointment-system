import tkinter as tk
from tkinter import messagebox, ttk, END
from tkcalendar import DateEntry  # Ensure tkcalendar is installed
from db_connection import connect_db
from tkcalendar import Calendar
import re
from datetime import datetime
import customtkinter as ctk
import os
from tkinter import filedialog

def show_appointment_booking(frame, staff_id):
    from home_page import create_home_page

    # Define placeholders and error labels dictionary
    error_labels = {}
    staff_options = []
    staff_placeholder = "Select a staff.."
    patient_options = []
    patient_placeholder = "Select a patient.."
    time_slots = ["09:00 AM - 10:00 AM", "10:00 AM - 11:00 AM", "11:00 AM - 12:00 PM", "01:00 PM - 02:00 PM"] 
    time_slot_placeholder = "Select a time slot.."
    appointment_types = ["Check-Up", "Follow-Up", "Consultation"]
    appt_type_placeholder = "Select a appointment type.."

    # Function to create a calendar popup
    def open_calendar(entry_widget):
        # Create a Toplevel window as a pop-up
        calendar_window = ctk.CTkToplevel(frame)
        calendar_window.title("Select Date")
        
        # Create Calendar widget
        cal = Calendar(calendar_window, selectmode="day", date_pattern="y-mm-dd",
                    background="darkblue", foreground="white", headersbackground="gray",
                    normalbackground="lightgray", weekendbackground="lightblue")

        # Position the calendar widget in the popup
        cal.pack(padx=10, pady=10)

        # Confirm date selection
        def select_date():
            selected_date = cal.get_date()
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, selected_date)
            calendar_window.destroy()
        
        # Button to confirm date selection
        select_button = ctk.CTkButton(calendar_window, text="Select", command=select_date)
        select_button.pack(pady=5)

    # Initialize CustomTkinter appearance
    ctk.set_appearance_mode("System")
    ctk.set_appearance_mode("light")  # Change to "dark" for dark mode
    ctk.set_default_color_theme("blue")  # Customize the color theme if desired

    # Clear existing widgets
    for widget in frame.winfo_children():
        widget.destroy()

    # Set up the main frame and configure the layout weights
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)
    
    # Create a frame for the appointment booking form
    book_frame = ctk.CTkFrame(frame, fg_color='#f0f4f8', corner_radius=10, width=600)
    book_frame.pack(fill="both", expand=True)
    book_frame.grid_columnconfigure(0, weight=1)
    book_frame.grid_rowconfigure(0, weight=1)
    book_frame.grid_rowconfigure(1, weight=1)
    book_frame.grid_rowconfigure(2, weight=1)
    

    # Header Frame
    header_frame = ctk.CTkFrame(book_frame, fg_color="#3b8ed0", corner_radius=10)
    header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
    header_frame.grid_columnconfigure(1, weight=1)
    header_frame.grid_rowconfigure(0, weight=1)
    
    # # Header Logo
    # logo = tk.PhotoImage(file='logos/book_appointment.png')  # Ensure you have a logo image
    # logo_label = tk.Label(header_frame, image=logo, bg='#1565C0')
    # logo_label.image = logo  # Keep a reference to avoid garbage collection
    # logo_label.grid(row=0, column=0, padx=10)

    # Header Title label
    title_label = ctk.CTkLabel(header_frame, text="Book Appointment", font=ctk.CTkFont("Helvetica", 24, "bold"), text_color="white")
    title_label.grid(row=0, column=1, pady=10, sticky="nsew")

    # Adjust fields_frame to allow expansion
    fields_frame = ctk.CTkFrame(book_frame, fg_color="#f0f4f8")
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

    # Load patients into the dropdown
    def load_patients():
        global patient_options
        # print("l1", patient_options)
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT patient_id, CONCAT(first_name, ' ', last_name) FROM patients")
            patients = cursor.fetchall()
            patient_options = [f"{patient[0]} - {patient[1]}" for patient in patients]
            # Update combo box values dynamically
            patient_combo.configure(values=patient_options, state="normal")
            conn.close()

    def reset_patient_dropdown():
        global patient_options
        # Restore the placeholder when the field is empty
        if not patient_combo.get() :
            patient_combo.set(patient_placeholder)
        elif patient_combo.get() == patient_placeholder:
            patient_combo.set("")

        patient_combo.configure(values=patient_options)  # Ensure placeholder is the first value

    def check_patient_input(*args):
        global patient_options

        value = patient_search_var.get()  # Get current user input
        if value == patient_placeholder:  # Ignore placeholder
            patient_combo.configure(values=patient_options)
            return
        filtered_options = [option for option in patient_options if value.lower() in option.lower()]
        patient_combo.configure(values=filtered_options)  # Add placeholder back

    # # Patient Selection
    pn_asterisk_label = ctk.CTkLabel(fields_frame, text="*", text_color="red", font=ctk.CTkFont(size=12, weight="bold"))
    pn_asterisk_label.grid(row=0, column=0, sticky="w", padx=25, pady=(15,0))
    patient_name_label = ctk.CTkLabel(fields_frame, text="Patient Name:", font=ctk.CTkFont(size=12), text_color="black")
    patient_name_label.grid(row=0, column=0, sticky="w", padx=35, pady=(10,0))
    patient_search_var = tk.StringVar()
    patient_search_var.trace_add("write", check_patient_input)   # Bind filtering to input changes
    patient_combo = ctk.CTkComboBox(fields_frame, variable=patient_search_var, values=[patient_placeholder] + patient_options, width=300, height=25)
    patient_combo.grid(row=1, column=0, padx=25, pady=(0,20), sticky="w")
    load_patients()
    patient_combo.set(patient_placeholder)  # Set initial placeholder
    error_labels["patient"] = ctk.CTkLabel(fields_frame, text="", text_color="red", font=("Arial", 10))
    error_labels["patient"].grid(row=1, column=0, pady=(35,0), padx=30, sticky="w")
    patient_combo.bind("<FocusIn>", lambda e: reset_patient_dropdown())  # Reset values on focus
    patient_combo.bind("<FocusOut>", lambda e: reset_patient_dropdown())  # Reset placeholder on blur

    # Load staff into the dropdownx
    def load_staff():
        global staff_options
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT staff_id, CONCAT(first_name, ' ', last_name, ' - ', role) FROM staff")
            staff_members = cursor.fetchall()
            staff_options = [f"{staff[0]} - {staff[1]}" for staff in staff_members]
            staff_combo.configure(values=staff_options)
            conn.close()

    def reset_staff_dropdown():
        global staff_options
        
        # Restore the placeholder when the field is empty
        if not staff_combo.get() :
            staff_combo.set(staff_placeholder)
        elif staff_combo.get() == staff_placeholder:
            staff_combo.set("")

        staff_combo.configure(values=staff_options)  # Ensure placeholder is the first value

    def check_staff_input(*args):
        global staff_options

        value = staff_search_var.get()  # Get current user input
        if value == staff_placeholder:  # Ignore placeholder
            staff_combo.configure(values=staff_options)
            return
        filtered_options = [option for option in staff_options if value.lower() in option.lower()]
        staff_combo.configure(values=filtered_options)  # Add placeholder back

    sc_asterisk_label = ctk.CTkLabel(fields_frame, text="*", text_color="red", font=ctk.CTkFont(size=12, weight="bold"))
    sc_asterisk_label.grid(row=2, column=0, sticky="w", padx=25, pady=(15,0))
    staff_name_label = ctk.CTkLabel(fields_frame, text="Staff Name:", font=ctk.CTkFont(size=12), text_color="black")
    staff_name_label.grid(row=2, column=0, sticky="w", padx=35, pady=(10,0))
    staff_search_var = tk.StringVar()
    staff_search_var.trace_add("write", check_staff_input)
    staff_combo = ctk.CTkComboBox(fields_frame, variable=staff_search_var, values=[staff_placeholder] + staff_options, width=300, height=25)
    staff_combo.grid(row=3, column=0, padx=25, pady=(0,20), sticky="w")
    load_staff()
    staff_combo.set(staff_placeholder)
    error_labels["staff"] = ctk.CTkLabel(fields_frame, text="", text_color="red", font=("Arial", 10))
    error_labels["staff"].grid(row=3, column=0, pady=(40,0), padx=30, sticky="w")
    staff_combo.bind("<FocusIn>", lambda e: reset_staff_dropdown())  # Reset values on focus
    staff_combo.bind("<FocusOut>", lambda e: reset_staff_dropdown())  # Reset placeholder on blur


    # Appointment Date (Date Picker)
    fn_asterisk_label = ctk.CTkLabel(fields_frame, text="*", text_color="red", font=ctk.CTkFont(size=12, weight="bold"))
    fn_asterisk_label.grid(row=4, column=0, sticky="w", padx=25, pady=(15,0))
    appointment_date_label = ctk.CTkLabel(fields_frame, text="Appointment Date:")
    appointment_date_label.grid(row=4, column=0, sticky="w", padx=35, pady=(10,0))
    appt_date_frame = ctk.CTkFrame(fields_frame, fg_color="#f0f4f8", width=600)
    appt_date_frame.grid(row=5, column=0, pady=(0,20), padx=25, sticky="w")
    appt_date_frame.grid_rowconfigure(0, weight=1)
    appt_date_frame.grid_columnconfigure(0, weight=1)
    appt_date_frame.grid_columnconfigure(1, weight=1)
    appointment_date = ctk.CTkEntry(appt_date_frame, placeholder_text="YYYY-MM-DD")
    appointment_date.grid(row=0, column=0, pady=(0,20), sticky="w")
    # # Button to open the calendar
    open_calendar_button = ctk.CTkButton(appt_date_frame, text="Pick a Date", command=lambda: open_calendar(appointment_date))
    open_calendar_button.grid(row=0, column=1, padx=20, pady=(0,20), sticky="w")
    error_labels["appt_date"] = ctk.CTkLabel(appt_date_frame, text="", text_color="red", font=("Arial", 10))
    error_labels["appt_date"].grid(row=0, column=0, pady=(40,0), padx=30, sticky="w")
    

    # Prescription Field
    prescription_label = ctk.CTkLabel(fields_frame, text="Upload Prescription:")
    prescription_label.grid(row=6, column=0, padx=25, pady=(10,0), sticky="w")  
    prescription_frame = ctk.CTkFrame(fields_frame, fg_color="#f0f4f8", width=600)
    prescription_frame.grid(row=7, column=0, pady=(0,20), padx=25, sticky="w")
    prescription_frame.grid_rowconfigure(0, weight=1)
    prescription_frame.grid_columnconfigure(0, weight=1)
    prescription_frame.grid_columnconfigure(1, weight=1)
    # Function to upload prescription
    def upload_prescription():
        try:
            file_path = filedialog.askopenfilename(
                filetypes=[("PDF Files", "*.pdf"), ("Image Files", "*.jpg;*.jpeg;*.png"), ("All Files", "*.*")]
            )
            if file_path:
                selected_file_label.configure(text=os.path.basename(file_path), text_color="black")
                prescription_field["file_path"] = file_path
            else:
                selected_file_label.configure(text="No file selected", text_color="grey")
        except Exception as e:
            messagebox.showerror("File Dialog Error", f"An error occurred: {e}")

    # Dictionary to store prescription file path
    prescription_field = {"file_path": None}

    # Display selected file name
    selected_file_label = ctk.CTkLabel(prescription_frame, text="No file selected", text_color="grey", font=ctk.CTkFont(size=12))
    selected_file_label.grid(row=0, column=0, pady=(10,0), sticky="w")

    # Upload Button
    upload_button = ctk.CTkButton(prescription_frame, text="Upload File", command=upload_prescription)
    upload_button.grid(row=0, column=1, padx=(70,0), pady=(10,20), sticky="w")

    def reset_time_slot_dropdown():
        # Restore the placeholder when the field is empty
        if not time_slot_combo.get() :
            time_slot_combo.set(time_slot_placeholder)
        elif time_slot_combo.get() == time_slot_placeholder:
            time_slot_combo.set("")

        time_slot_combo.configure(values=time_slots)  # Ensure placeholder is the first value

    def check_time_slot_input(*args):
        # global time_slots
        value = time_slot_search_var.get()  # Get current user input
        if value == time_slot_placeholder:  # Ignore placeholder
            time_slot_combo.configure(values=time_slots)
            return
        
    # Time Slot
    ts_asterisk_label = ctk.CTkLabel(fields_frame, text="*", text_color="red", font=ctk.CTkFont(size=12, weight="bold"))
    ts_asterisk_label.grid(row=0, column=1, sticky="w", padx=25, pady=(15,0))
    time_slot_label = ctk.CTkLabel(fields_frame, text="Time Slot:", font=ctk.CTkFont(size=12), text_color="black")
    time_slot_label.grid(row=0, column=1, padx=35, pady=(10,0), sticky="w")
    time_slot_search_var = tk.StringVar()
    time_slot_search_var.trace_add("write", check_time_slot_input)
    time_slot_combo = ctk.CTkComboBox(fields_frame, values=[time_slot_placeholder] + time_slots, variable=time_slot_search_var, width=300, height=25)
    time_slot_combo.grid(row=1, column=1, padx=25, pady=(0,20), sticky="w")
    time_slot_combo.set(time_slot_placeholder)
    error_labels["time_slot"] = ctk.CTkLabel(fields_frame, text="", text_color="red", font=("Arial", 10))
    error_labels["time_slot"].grid(row=1, column=1, pady=(35,0), padx=30, sticky="w")
    time_slot_combo.bind("<FocusIn>", lambda e: reset_time_slot_dropdown())  # Reset values on focus
    time_slot_combo.bind("<FocusOut>", lambda e: reset_time_slot_dropdown())  # Reset placeholder on blur

    def reset_appt_type_dropdown():
        # Restore the placeholder when the field is empty
        if not appt_type_combo.get() :
            appt_type_combo.set(appt_type_placeholder)
        elif appt_type_combo.get() == appt_type_placeholder:
            appt_type_combo.set("")

        appt_type_combo.configure(values=appointment_types)  # Ensure placeholder is the first value

    def check_appt_type_input(*args):
        # global time_slots
        value = appointment_type_search_var.get()  # Get current user input
        if value == appt_type_placeholder:  # Ignore placeholder
            appt_type_combo.configure(values=appointment_types)
            return
        
    # Appointment Type
    at_asterisk_label = ctk.CTkLabel(fields_frame, text="*", text_color="red", font=ctk.CTkFont(size=12, weight="bold"))
    at_asterisk_label.grid(row=2, column=1, sticky="w", padx=25, pady=(15,0))
    at_type_label = ctk.CTkLabel(fields_frame, text="Appointment Type:", font=ctk.CTkFont(size=12), text_color="black")
    at_type_label.grid(row=2, column=1, padx=35, pady=(10,0), sticky="w")
    appointment_type_search_var = tk.StringVar()
    appointment_type_search_var.trace_add("write", check_appt_type_input)
    appt_type_combo = ctk.CTkComboBox(fields_frame, values=[appt_type_placeholder] + appointment_types, variable=appointment_type_search_var, width=300, height=25)
    appt_type_combo.grid(row=3, column=1, padx=25, pady=(0,20), sticky="w")
    appt_type_combo.set(appt_type_placeholder)
    error_labels["appt_type"] = ctk.CTkLabel(fields_frame, text="", text_color="red", font=("Arial", 10))
    error_labels["appt_type"].grid(row=3, column=1, pady=(35,0), padx=30, sticky="w")
    appt_type_combo.bind("<FocusIn>", lambda e: reset_appt_type_dropdown())
    appt_type_combo.bind("<FocusOut>", lambda e: reset_appt_type_dropdown())

    case_details_label = ctk.CTkLabel(fields_frame, text="Case Details:")
    case_details_label.grid(row=4, column=1, padx=25, pady=(10,0), sticky="w")
    case_details_frame = ctk.CTkFrame(fields_frame, fg_color="grey", corner_radius=5)
    case_details_frame.grid(row=5, column=1, rowspan=3, columnspan=2, padx=25, pady=(0,20), sticky="w")
    case_details_frame.grid_rowconfigure(0, weight=1)
    case_details_frame.grid_columnconfigure(0, weight=1)
    case_details = ctk.CTkTextbox(case_details_frame, width=300, height=100, font=ctk.CTkFont(size=12))
    case_details.grid(row=0, column=0, padx=2, pady=2, sticky="w")  # Padding to create the inner spacing

    # Clear all fields
    def clear_fields():
        global patient_options, staff_options
        # Reset CTkComboBox widgets to their placeholder
        patient_combo.set(patient_placeholder)
        patient_combo.configure(values=patient_options)
        staff_combo.set(staff_placeholder)
        staff_combo.configure(values=staff_options)
        time_slot_combo.set(time_slot_placeholder)
        time_slot_combo.configure(values=time_slots)
        appt_type_combo.set(appt_type_placeholder)
        appt_type_combo.configure(values=appointment_types)
        
        # Clear CTkEntry for date selection
        appointment_date.delete(0, ctk.END)
        # Clear CTkTextbox for case details
        case_details.delete("1.0", ctk.END)

        # Clear all previous error messages
        for error_label in error_labels.values():
            error_label.configure(text="")

    # Validate Field
    def validate_fields():

        # Clear all previous error messages
        for error_label in error_labels.values():
            error_label.configure(text="")

        valid = True

        selected_date = appointment_date.get()
        if not selected_date:
            error_labels["appt_date"].configure(text="Please select a date.")
            valid = False

        if selected_date:
            appt_date = datetime.strptime(selected_date, "%Y-%m-%d").date()
            today = datetime.today().date() # Get today's date without the time part
            if appt_date < today:
                error_labels["appt_date"].configure(text="The selected date cannot be in the past.")
                valid = False

        patient = patient_combo.get()
        if not patient or patient==patient_placeholder:
            error_labels["patient"].configure(text="Please select a patient.")
            valid = False

        staff = staff_combo.get()
        if not staff or staff==staff_placeholder:
            error_labels["staff"].configure(text="Please select a staff.")
            valid = False

        time_slot = time_slot_combo.get()
        if not time_slot or time_slot==time_slot_placeholder:
            error_labels["time_slot"].configure(text="Please select a time slot.")
            valid = False
        
        appt_type = appt_type_combo.get()
        if not appt_type or appt_type==appt_type_placeholder:
            error_labels["appt_type"].configure(text="Please select a appointment type.")
            valid = False

        # Show success message if all fields are valid
        if valid:
            return True
        else:
            return False
        

    # Validate appointment before inserting
    def validate_appointment(patient_id, staff_id, appointment_date_value, appointment_time):
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()

                # Check if an appointment already exists for the staff on the same date and time slot
                cursor.execute("""
                    SELECT COUNT(*) FROM appointments 
                    WHERE staff_id = %s AND appointment_date = %s AND appointment_time = %s
                """, (staff_id, appointment_date_value, appointment_time))

                result = cursor.fetchone()
                if result and result[0] > 0:
                    # Appointment already exists
                    return False

                return True
            except Exception as e:
                print(f"Error during validation: {e}")
                return False
            finally:
                conn.close()
        else:
            print("Database connection error.")
            return False
        

    # Validate and save appointment
    def save_appointment():
        if not validate_fields():
            return
        
        # Clear all previous error messages
        for error_label in error_labels.values():
            error_label.configure(text="")

        patient_id = patient_combo.get().split(" - ")[0]
        staff_id = staff_combo.get().split(" - ")[0]
        appointment_date_value = appointment_date.get()
        appointment_time = time_slot_combo.get()
        appt_type = appt_type_combo.get()
        case_details_value = case_details.get("1.0", tk.END).strip()
        prescription_file_path = prescription_field["file_path"]
        prescription_document_data = None

        # Assuming 'prescription_document' is a file (e.g., PDF or image)
        if prescription_file_path:
            with open(prescription_file_path, 'rb') as file:
                prescription_document_data = file.read()  # Read the file as binary

        # Database insertion if validation passes
        conn = connect_db()
        if conn:
            try:
                    # Validate appointment first
                if not validate_appointment(patient_id, staff_id, appointment_date_value, appointment_time):
                    messagebox.showwarning("Appointment Conflict", "We cannot create an appointment for this date and time slot. There is already a booking.")
                    return

                cursor = conn.cursor()

                cursor.execute(
                    "INSERT INTO appointments (patient_id, staff_id, appointment_date, appointment_time, appt_type, case_details, prescription_document) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (patient_id, staff_id, appointment_date_value, appointment_time, appt_type, case_details_value, prescription_document_data)
                )
                conn.commit()
                clear_fields()
                messagebox.showinfo("Success", "Appointment booked successfully!")
            except Exception as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")
            finally:
                conn.close()

    def go_back():
        book_frame.destroy()
        create_home_page(frame, staff_id)


    # Buttons
    button_frame = ctk.CTkFrame(book_frame, fg_color='#f0f4f8')
    button_frame.grid(row=2, column=0, columnspan=2, pady=30)
    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)
    button_frame.grid_columnconfigure(2, weight=1)
    button_frame.grid_rowconfigure(0, weight=1)

    submit_btn = ctk.CTkButton(button_frame, text="Save", command=save_appointment)
    submit_btn.grid(row=0, column=0, padx=10)

    reset_btn = ctk.CTkButton(button_frame, text="Clear", command=clear_fields)
    reset_btn.grid(row=0, column=1, padx=10)

    back_btn = ctk.CTkButton(button_frame, text="Back", command=go_back)
    back_btn.grid(row=0, column=2, padx=10)
