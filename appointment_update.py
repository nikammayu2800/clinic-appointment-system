import tkinter as tk
from tkinter import messagebox
from db_connection import connect_db

def show_appointment_update(root, appointment_id):
    update_frame = tk.Frame(root)
    update_frame.pack(pady=20)

    tk.Label(update_frame, text="Update Appointment", font=("Arial", 16)).grid(row=0, columnspan=2, pady=10)

    tk.Label(update_frame, text=f"Updating Appointment ID: {appointment_id}", font=("Arial", 12)).grid(row=1, columnspan=2, pady=5)

    # Fetch appointment details to prefill
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT appointment_date, appointment_time, case_details FROM appointments WHERE appointment_id=%s", (appointment_id,))
        appt = cursor.fetchone()
        conn.close()

    # Update Appointment Date
    tk.Label(update_frame, text="Appointment Date:").grid(row=2, column=0, padx=10, pady=5)
    entry_date = tk.Entry(update_frame)
    entry_date.insert(0, appt[0])
    entry_date.grid(row=2, column=1, padx=10, pady=5)

    # Update Appointment Time
    tk.Label(update_frame, text="Appointment Time:").grid(row=3, column=0, padx=10, pady=5)
    entry_time = tk.Entry(update_frame)
    entry_time.insert(0, appt[1])
    entry_time.grid(row=3, column=1, padx=10, pady=5)

    # Update Case Details
    tk.Label(update_frame, text="Case Details:").grid(row=4, column=0, padx=10, pady=5)
    entry_case_details = tk.Entry(update_frame)
    entry_case_details.insert(0, appt[2])
    entry_case_details.grid(row=4, column=1, padx=10, pady=5)

    def update_appointment():
        from appointment_management import show_appointment_management
        date = entry_date.get()
        time = entry_time.get()
        case_details = entry_case_details.get()

        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE appointments SET appointment_date=%s, appointment_time=%s, case_details=%s WHERE appointment_id=%s", 
                           (date, time, case_details, appointment_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", f"Appointment {appointment_id} updated successfully!")
            show_appointment_management(root)  # Return to the management screen

    tk.Button(update_frame, text="Update", command=update_appointment).grid(row=5, columnspan=2, pady=5)
