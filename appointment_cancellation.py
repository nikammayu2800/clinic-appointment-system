import tkinter as tk
from tkinter import messagebox, ttk
from db_connection import connect_db

def show_appointment_cancellation(frame):
    # Clear existing widgets
    for widget in frame.winfo_children():
        widget.destroy()

    # Colors and Fonts for consistency
    BG_COLOR = '#f5f5f5'  # Background color for the main frame
    LABEL_BG = '#f5f5f5'  # Background for label containers
    BUTTON_COLOR = '#f5f5f5'  # Button color
    FONT_TITLE = ("Helvetica", 18, "bold")
    FONT_LABEL = ("Helvetica", 12)

    # Main frame for the cancellation form
    cancel_frame = tk.Frame(frame, bg=BG_COLOR, padx=20, pady=20, relief=tk.RIDGE, bd=2)
    cancel_frame.pack(pady= 10, padx=10, fill=tk.BOTH, expand=True)

    # Title section
    title_frame = tk.Frame(cancel_frame, bg=LABEL_BG, pady=10)
    title_frame.grid(row=0, column=0, columnspan=3, sticky='ew', pady=10)
    
    # Title label
    title_label = tk.Label(title_frame, text="Cancel Appointment", font=FONT_TITLE, bg=LABEL_BG)
    title_label.grid(row=0, column=1, padx=10)

    # Logo
    try:
        logo = tk.PhotoImage(file='logos/cancle_appointment.png')  # Update with the correct logo path
        logo_label = tk.Label(title_frame, image=logo, bg=LABEL_BG)
        logo_label.image = logo  # Keep reference to avoid garbage collection
        logo_label.grid(row=0, column=0, padx=10)
    except:
        logo_label = tk.Label(title_frame, text="No Logo", bg=LABEL_BG)  # Fallback if logo not found
        logo_label.grid(row=0, column=0, padx=10)

    # Search bar
    tk.Label(cancel_frame, text="Search by Patient Name or Appointment ID:", font=FONT_LABEL, bg=BG_COLOR)\
        .grid(row=1, column=0, padx=10, pady=5, sticky='e')
    entry_search = tk.Entry(cancel_frame, width=30, font=("Helvetica", 11))
    entry_search.grid(row=1, column=1, padx=10, pady=5)

    # Patient Details
    tk.Label(cancel_frame, text="Patient Name/ID:", font=FONT_LABEL, bg=BG_COLOR)\
        .grid(row=2, column=0, padx=10, pady=5, sticky='e')
    patient_label = tk.Label(cancel_frame, text="", width=30, anchor="w", bg="white", relief="sunken")
    patient_label.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(cancel_frame, text="Appointment Date:", font=FONT_LABEL, bg=BG_COLOR)\
        .grid(row=3, column=0, padx=10, pady=5, sticky='e')
    appointment_date_label = tk.Label(cancel_frame, text="", width=30, anchor="w", bg="white", relief="sunken")
    appointment_date_label.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(cancel_frame, text="Appointment Time:", font=FONT_LABEL, bg=BG_COLOR)\
        .grid(row=4, column=0, padx=10, pady=5, sticky='e')
    appointment_time_label = tk.Label(cancel_frame, text="", width=30, anchor="w", bg="white", relief="sunken")
    appointment_time_label.grid(row=4, column=1, padx=10, pady=5)

    # Clear fields function
    def clear_fields():
        entry_search.delete(0, tk.END)
        patient_label.config(text="")
        appointment_date_label.config(text="")
        appointment_time_label.config(text="")

    # Load appointment details into the labels
    def load_appointment_details(appointment):
        patient_label.config(text=appointment[1])
        appointment_date_label.config(text=appointment[2])
        appointment_time_label.config(text=appointment[3])

    # Search for an appointment
    def search_appointment():
        search_value = entry_search.get()
        if not search_value:
            messagebox.showerror("Error", "Please enter a value to search.")
            return

        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            if search_value.isdigit():
                query = """
                    SELECT a.appointment_id, CONCAT(p.first_name, ' ', p.last_name), 
                           a.appointment_date, a.appointment_time
                    FROM appointments a
                    JOIN patients p ON a.patient_id = p.patient_id
                    WHERE a.appointment_id = %s
                """
                cursor.execute(query, (int(search_value),))
            else:
                query = """
                    SELECT a.appointment_id, CONCAT(p.first_name, ' ', p.last_name), 
                           a.appointment_date, a.appointment_time
                    FROM appointments a
                    JOIN patients p ON a.patient_id = p.patient_id
                    WHERE CONCAT(p.first_name, ' ', p.last_name) LIKE %s
                """
                cursor.execute(query, (f"%{search_value}%",))

            result = cursor.fetchone()
            conn.close()

            if result:
                load_appointment_details(result)
            else:
                messagebox.showinfo("No Results", "No appointment found.")
                clear_fields()

    # Cancel appointment
    def confirm_cancellation():
        appointment_time = appointment_time_label.cget("text")
        if not appointment_time:
            messagebox.showerror("Error", "No appointment selected to cancel.")
            return

        if messagebox.askyesno("Confirm Cancellation", "Are you sure you want to cancel this appointment?"):
            conn = connect_db()
            if conn:
                cursor = conn.cursor()
                try:
                    appointment_id = int(entry_search.get())
                    cursor.execute("DELETE FROM appointments WHERE appointment_id = %s", (appointment_id,))
                except ValueError:
                    cursor.execute("""
                        SELECT a.appointment_id
                        FROM appointments a
                        JOIN patients p ON a.patient_id = p.patient_id
                        WHERE CONCAT(p.first_name, ' ', p.last_name) = %s
                    """, (patient_label.cget("text"),))
                    appointment_id = cursor.fetchone()
                    cursor.execute("DELETE FROM appointments WHERE appointment_id = %s", (appointment_id[0],))

                conn.commit()
                conn.close()
                messagebox.showinfo("Cancelled", "Appointment cancelled successfully.")
                clear_fields()

    # Buttons
    btn_search = tk.Button(cancel_frame, text="Search", command=search_appointment, 
                           bg=BUTTON_COLOR, width=12)
    btn_search.grid(row=1, column=2, padx=5)

    btn_cancel = tk.Button(cancel_frame, text="Confirm Cancellation", command=confirm_cancellation,
                           bg=BUTTON_COLOR, width=20)
    btn_cancel.grid(row=5, column=0, pady=15)

    btn_clear = tk.Button(cancel_frame, text="Clear", command=clear_fields, 
                          bg='#6C757D', width=12)
    btn_clear.grid(row=5, column=1, pady=15)
