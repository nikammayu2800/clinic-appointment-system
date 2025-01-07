import tkinter as tk
from login_screen import show_login
from landing_page import landing_page
from patient_registration import show_registration

root = tk.Tk()
root.title("Clinic Appointment System")
root.configure(background='#E4E4E4')
root.geometry("1000x800")
# root.resizable(True, True)

root.withdraw()
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - root.winfo_width()) // 2
y = (screen_height - root.winfo_height()) // 2
root.geometry(f"+{x}+{y}")
root.deiconify()


def navigate_to(screen_func):
    for widget in root.winfo_children():
        widget.destroy()
    screen_func(root)

# Start by showing the login screen
navigate_to(landing_page)


root.mainloop()

