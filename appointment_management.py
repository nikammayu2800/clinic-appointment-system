import os
import tkinter as tk
from tkinter import Toplevel, filedialog
import customtkinter as ctk
from tkinter import messagebox, ttk
from datetime import datetime
from tkcalendar import DateEntry
from tkcalendar import Calendar
from db_connection import connect_db

def show_appointment_management(frame, staff_id):
    from home_page import create_home_page

    # Define placeholders and error labels dictionary
    error_labels = {}
    appointment_details = None
    staff_options = []
    staff_placeholder = "Select a staff.."
    time_slots = ["09:00 AM - 10:00 AM", "10:00 AM - 11:00 AM", "11:00 AM - 12:00 PM", "01:00 PM - 02:00 PM"] 
    time_slot_placeholder = "Select a time slot.."
    appointment_types = ["Check-Up", "Follow-Up", "Consultation"]
    appt_type_placeholder = "Select a appointment type.."
    appointment_statuses = ["Scheduled", "Completed", "Cancel"]
    appt_status_placeholder = "Select a appointment status.."

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
    ctk.set_appearance_mode("System")
    ctk.set_appearance_mode("light")  # Change to "dark" for dark mode
    ctk.set_default_color_theme("blue")  # Customize the color theme if desired

    # Clear existing widgets
    for widget in frame.winfo_children():
        widget.destroy()

    # Set up the main frame and configure the layout weights
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)

    # Main frame styling
    manage_frame = ctk.CTkFrame(frame, fg_color='#f0f4f8', corner_radius=10, width=600)
    manage_frame.pack(fill="both", expand=True)
    manage_frame.grid_columnconfigure(0, weight=1)
    manage_frame.grid_rowconfigure(0, weight=1)
    manage_frame.grid_rowconfigure(1, weight=1)
    manage_frame.grid_rowconfigure(2, weight=1)
    manage_frame.grid_rowconfigure(3, weight=1)
    manage_frame.grid_rowconfigure(4, weight=1)


    # Header Frame
    header_frame = ctk.CTkFrame(manage_frame, fg_color="#3b8ed0", corner_radius=10)
    header_frame.grid(row=0, column=0, columnspan=2, sticky="ew",)
    header_frame.grid_columnconfigure(1, weight=1)
    header_frame.grid_rowconfigure(0, weight=1)

    # # Header Logo
    # logo = tk.PhotoImage(file="logos/manage_appointment.png")
    # logo_label = tk.Label(header_frame, image=logo, bg="#1565C0")
    # logo_label.image = logo  # Keep a reference to avoid garbage collection
    # logo_label.grid(row=0, column=0, padx=10)

    # Header Title
    title_label = ctk.CTkLabel(header_frame, text="Appointment Management Form", font=("Helvetica", 24, "bold"), text_color="white")
    title_label.grid(row=0, column=1, pady=10, sticky="nsew")

    search_frame = ctk.CTkFrame(manage_frame, fg_color="#f0f4f8", width=600)
    search_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=(20,0))
    search_frame.grid_columnconfigure(0, weight=1)
    search_frame.grid_columnconfigure(1, weight=1)
    search_frame.grid_columnconfigure(2, weight=1)
    search_frame.grid_columnconfigure(3, weight=1)
    search_frame.grid_rowconfigure(0, weight=1)

    def validate_fields():
        # Clear all previous error messages
        for error_label in error_labels.values():
            error_label.configure(text="")

        valid = True

        search_value = entry_search.get().strip()
        if not search_value:
            error_labels["search"].configure(text="Please enter patient name or ID...")
            valid = False

        # Show success message if all fields are valid
        if valid:
            return True
        else:
            return False

    # Search functionality
    def search_appointments():
        global appointment_details

        if not validate_fields():
            return
        
        # Clear all previous error messages
        for error_label in error_labels.values():
            error_label.configure(text="")

        search_value = entry_search.get().strip()

        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT a.appointment_id, CONCAT(p.first_name, ' ', p.last_name), s.staff_id, a.appointment_date, 
                        a.appointment_time, a.appt_type, a.case_details, a.status
                    FROM appointments a
                    JOIN patients p ON a.patient_id = p.patient_id
                    JOIN staff s ON a.staff_id = s.staff_id
                    WHERE p.first_name LIKE %s OR a.appointment_id = %s
                """, (f"%{search_value}%", search_value))
                appointment_details = cursor.fetchone()
                after_appt_search_save_btn_status = "normal" if appointment_details else "disabled"
                after_appt_search_save_btn_color = "#3b8ed0" if appointment_details else "grey"
                submit_btn.configure(state=after_appt_search_save_btn_status, fg_color=after_appt_search_save_btn_color)
                # messagebox.showinfo("Success", "Appointment successfully updated!")
            except Exception as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")
            finally:
                conn.close()

            if appointment_details:
                load_appointment(appointment_details)
            else:
                messagebox.showinfo("No Results", "No appointment found.")
                appt_searched = False

    def load_appointment(appointment):
        global staff_options
        entry_search.delete("0", tk.END)
        entry_search.insert("0", appointment[1])
        # Find and set the correct staff name based on staff_id
        staff_id = appointment[2]  # Retrieve staff_id from appointment details

        # Loop through the staff options and select the one that matches the staff_id
        for value in staff_options:
            # Assuming the format is "staff_id - staff_name"
            if value.startswith(f"{staff_id} -"):
                staff_combo.set(value)  # Set the staff name in combobox
                break  # Exit loop once the correct staff is found

        appointment_date.delete(0, tk.END)
        appointment_date.insert(0, appointment[3])
        time_slot_combo.set(appointment[4])
        appt_type_combo.set(appointment[5])
        case_details.delete("1.0", tk.END)
        case_details.insert("1.0", appointment[6])
        status_combo.set(appointment[7])

    # Patient Search Field with Placeholder and Error Label
    se_asterisk_label = ctk.CTkLabel(search_frame, text="*", text_color="red", font=ctk.CTkFont(size=12, weight="bold"))
    se_asterisk_label.grid(row=0, column=0, sticky='ew')
    se_label = ctk.CTkLabel(search_frame, text="Search by Patient Name or Appointment ID:", font=ctk.CTkFont(size=12), text_color="black")
    se_label.grid(row=0, column=1, padx=10)
    entry_search = ctk.CTkEntry(search_frame, width=300, font=ctk.CTkFont(size=12), placeholder_text="Enter Patient name or Appointment ID..")
    entry_search.grid(row=0, column=2, padx=10)
    error_labels["search"] = ctk.CTkLabel(search_frame, text="", text_color="red", font=("Arial", 10))
    error_labels["search"].grid(row=0, column=2, pady=(55,0), padx=15, sticky="w")
  

    search_btn = ctk.CTkButton(search_frame, text="Search", command=search_appointments)
    search_btn.grid(row=0, column=3, padx=10)

    # Horizontal Separator using CTkFrame
    separator = ctk.CTkFrame(manage_frame, height=2, fg_color="#E0E0E0", corner_radius=0)
    separator.grid(row=2, column=0, columnspan=4, sticky="ew", padx=5, pady=(20, 20))

    # Adjust fields_frame to allow expansion    
    fields_frame = ctk.CTkFrame(manage_frame, fg_color="#f0f4f8")
    fields_frame.grid(row=3, column=0, columnspan=2)
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


    # Load staff into the dropdown
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

        staff_combo.configure(values=staff_options) 
            
    def check_staff_input(*args):
        global staff_options

        value = staff_search_var.get()  # Get current user input
        if value == staff_placeholder:  # Ignore placeholder
            staff_combo.configure(values=staff_options)
            return
        filtered_options = [option for option in staff_options if value.lower() in option.lower()]
        staff_combo.configure(values=filtered_options)  # Add placeholder back

    # Staff Dropdown with Placeholder
    staff_name_label = ctk.CTkLabel(fields_frame, text="Staff Name:", font=ctk.CTkFont(size=12), text_color="black")
    staff_name_label.grid(row=0, column=0, sticky="w", padx=25, pady=(10,0))
    staff_search_var = tk.StringVar()
    staff_search_var.trace_add("write", check_staff_input)
    staff_combo = ctk.CTkComboBox(fields_frame, variable=staff_search_var, values=[staff_placeholder] + staff_options,  width=300, height=25)
    staff_combo.grid(row=1, column=0, padx=25, pady=(0,20), sticky="w")
    load_staff()
    staff_combo.set(staff_placeholder)
    staff_combo.bind("<FocusIn>", lambda e: reset_staff_dropdown())
    staff_combo.bind("<FocusOut>", lambda e: reset_staff_dropdown())

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

    time_slot_label = ctk.CTkLabel(fields_frame, text="Time Slot:", font=ctk.CTkFont(size=12), text_color="black")
    time_slot_label.grid(row=2, column=0, sticky="w", padx=25, pady=(10,0))
    time_slot_search_var = tk.StringVar()
    time_slot_search_var.trace_add("write", check_time_slot_input)
    time_slot_combo = ctk.CTkComboBox(fields_frame, values=time_slots, variable=time_slot_search_var, width=300, height=25)
    time_slot_combo.grid(row=3, column=0,  padx=25, pady=(0,20), sticky="w")
    time_slot_combo.set(time_slot_placeholder)
    time_slot_combo.bind("<FocusIn>", lambda e: reset_time_slot_dropdown())
    time_slot_combo.bind("<FocusOut>", lambda e: reset_time_slot_dropdown())

    # Appointment Date Field
    appointment_date_label = ctk.CTkLabel(fields_frame, text="Appointment Date:", font=ctk.CTkFont(size=12), text_color="black")
    appointment_date_label.grid(row=4, column=0, sticky="w", padx=25, pady=(10,0))
    appt_date_frame = ctk.CTkFrame(fields_frame, fg_color="#f0f4f8", width=600)
    appt_date_frame.grid(row=5, column=0, pady=(0,20), padx=25, sticky="w")
    appt_date_frame.grid_rowconfigure(0, weight=1)
    appt_date_frame.grid_columnconfigure(0, weight=1)
    appt_date_frame.grid_columnconfigure(1, weight=1)
    appointment_date = ctk.CTkEntry(appt_date_frame, placeholder_text="YYYY-MM-DD")
    appointment_date.grid(row=0, column=0, pady=(0,20), sticky="w")
    open_calendar_button = ctk.CTkButton(appt_date_frame, text="Pick a Date", command=lambda: open_calendar(appointment_date))
    open_calendar_button.grid(row=0, column=1, padx=20, pady=(0,20))
    error_labels["appt_date"] = ctk.CTkLabel(appt_date_frame, text="", text_color="red", font=("Arial", 10))
    error_labels["appt_date"].grid(row=0, column=0, pady=(40,0), sticky="w")
    
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
    upload_button = ctk.CTkButton(prescription_frame, text="Upload File", command= lambda:upload_prescription)
    upload_button.grid(row=0, column=1, padx=(70,0), pady=(10,20), sticky="w")

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
        
    # Appointment Type Dropdown
    at_type_label = ctk.CTkLabel(fields_frame, text="Appointment Type:", font=ctk.CTkFont(size=12), text_color="black")
    at_type_label.grid(row=0, column=1, padx=25, pady=(10,0), sticky="w")
    appointment_type_search_var = tk.StringVar()
    appointment_type_search_var.trace_add("write", check_appt_type_input)
    appt_type_combo = ctk.CTkComboBox(fields_frame, values=[appt_type_placeholder] + appointment_types, variable=appointment_type_search_var, width=300, height=25)
    appt_type_combo.grid(row=1, column=1, padx=25, pady=(0,20), sticky="w")
    appt_type_combo.set(appt_type_placeholder)
    appt_type_combo.bind("<FocusIn>", lambda e: reset_appt_type_dropdown())
    appt_type_combo.bind("<FocusOut>", lambda e: reset_appt_type_dropdown())

    def reset_appt_status_dropdown():
        # Restore the placeholder when the field is empty
        if not status_combo.get() :
            status_combo.set(appt_status_placeholder)
        elif status_combo.get() == appt_status_placeholder:
            status_combo.set("")

        status_combo.configure(values=appointment_statuses)  # Ensure placeholder is the first value

    def check_appt_status_input(*args):
        # global time_slots
        value = appointment_status_search_var.get()  # Get current user input
        if value == appt_status_placeholder:  # Ignore placeholder
            status_combo.configure(values=appointment_statuses)
            return
        
    # Status Dropdown
    status_label = ctk.CTkLabel(fields_frame, text="Appointment Status:", font=ctk.CTkFont(size=12), text_color="black")
    status_label.grid(row=2, column=1, padx=25, pady=(10,0), sticky="w")
    appointment_status_search_var = tk.StringVar()
    appointment_status_search_var.trace_add("write", check_appt_status_input)
    status_combo = ctk.CTkComboBox(fields_frame, values=[appt_status_placeholder] + appointment_statuses, variable=appointment_status_search_var, width=300, height=25)
    status_combo.grid(row=3, column=1, padx=25, pady=(0,20), sticky="w")
    status_combo.set(appt_status_placeholder)
    status_combo.bind("<FocusIn>", lambda e: reset_appt_status_dropdown)
    status_combo.bind("<FocusOut>", lambda e: reset_appt_status_dropdown)

    # Case Details Text Area
    case_details_label = ctk.CTkLabel(fields_frame, text="Case Details:")
    case_details_label.grid(row=4, column=1, padx=25, pady=(10,0), sticky="w")
    case_details_frame = ctk.CTkFrame(fields_frame, fg_color="grey", corner_radius=5)
    case_details_frame.grid(row=5, column=1, rowspan=3, columnspan=2, padx=25, pady=(0,20), sticky="w")
    case_details_frame.grid_columnconfigure(0, weight=1)
    case_details_frame.grid_rowconfigure(0, weight=1)
    case_details = ctk.CTkTextbox(case_details_frame, width=300, height=100, font=ctk.CTkFont(size=12))
    case_details.grid(row=0, column=0, pady=2, padx=2, sticky="w")  # Padding to create the inner spacing

    # Clear all fields
    def clear_fields():
        global appointment_details
        global staff_options
        # Reset CTkComboBox widgets to their placeholder
        staff_combo.set(staff_placeholder)
        staff_combo.configure(values=staff_options)
        time_slot_combo.set(time_slot_placeholder)
        time_slot_combo.configure(values=time_slots)
        appt_type_combo.set(appt_type_placeholder)
        appt_type_combo.configure(values=appointment_types)
        status_combo.set(appt_status_placeholder)
        status_combo.configure(values=appointment_statuses)
        appointment_date.delete(0, ctk.END)
        case_details.delete("1.0", ctk.END)
        entry_search.delete(0, ctk.END)
        appointment_details = None
        after_clear_field_save_btn_status = "normal" if appointment_details else "disabled"
        after_clear_field_save_btn_color = "#3b8ed0" if appointment_details else "grey"
        submit_btn.configure(state=after_clear_field_save_btn_status, fg_color=after_clear_field_save_btn_color)
        
        # Clear all previous error messages
        for error_label in error_labels.values():
            error_label.configure(text="")

    # Save appointment changes
    def save_appointment():
        global appointment_details, appt_searched
        # Clear all previous error messages
        for error_label in error_labels.values():
            error_label.configure(text="")

        appt_date = appointment_date.get()
        if appt_date:
            appt_date = datetime.strptime(appt_date, "%Y-%m-%d").date()
            today = datetime.today().date() # Get today's date without the time part
            if appt_date < today:
                error_labels["appt_date"].configure(text="The selected date cannot be in the past.")
                return
            
        # if appointment_details is None:  # Explicitly check if None
        #     messagebox.showinfo("Warning", "Please select an appointment to update the details.")
        #     return

        try:
            appt_id = appointment_details[0]
            appt_date = appointment_date.get()
            appt_time = time_slot_combo.get()
            appt_type = appt_type_combo.get()
            details = case_details.get("1.0", tk.END).strip()
            status = status_combo.get()
            staff_var = staff_combo.get().split(" - ")[0]
            prescription_file_path = prescription_field["file_path"]
            prescription_document_data = None

            # Assuming 'prescription_document' is a file (e.g., PDF or image)
            if prescription_file_path:
                with open(prescription_file_path, 'rb') as file:
                    prescription_document_data = file.read()  # Read the file as binary

            conn = connect_db()
            if conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                    UPDATE appointments
                    SET staff_id = %s, appointment_date = %s, appointment_time = %s, appt_type = %s, case_details = %s, status = %s, prescription_document = %s
                    WHERE appointment_id = %s
                """, (staff_var, appt_date, appt_time, appt_type, details, status, prescription_document_data, appt_id))
                    conn.commit()
                    clear_fields()
                    
                    messagebox.showinfo("Success", "Appointment updated successfully!")
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
        finally:
            if conn:
                conn.close()
        
    def go_back():
        manage_frame.destroy()
        create_home_page(frame, staff_id)

    # Button Actions and Frame
    button_frame = ctk.CTkFrame(manage_frame, fg_color="#f0f4f8")
    button_frame.grid(row=4, column=0, columnspan=2, pady=50, padx=15)
    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)
    button_frame.grid_columnconfigure(2, weight=1)
    button_frame.grid_rowconfigure(0, weight=1)
    
    save_btn_status = "normal" if appointment_details else "disabled"
    save_btn_color = "#3b8ed0" if appointment_details else "grey"
    submit_btn = ctk.CTkButton(button_frame, text="Save", command=save_appointment, fg_color=save_btn_color, state=save_btn_status)
    submit_btn.grid(row=0, column=0, padx=10)

    reset_btn = ctk.CTkButton(button_frame, text="Clear", command=clear_fields)
    reset_btn.grid(row=0, column=1, padx=10)

    back_btn = ctk.CTkButton(button_frame, text="Back", command=go_back)
    back_btn.grid(row=0, column=2, padx=10)
