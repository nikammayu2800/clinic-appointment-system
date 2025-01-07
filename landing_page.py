# import tkinter as tk
# import customtkinter as ctk
# from tkinter import ttk
# from PIL import Image, ImageTk, ImageOps # For adding logos
# from db_connection import connect_db 
# from login_screen import show_login


# def landing_page(root):
#     from signup_screen import show_signup_page
#     # Set the appearance mode and color theme
#     ctk.set_appearance_mode("light")
#     ctk.set_default_color_theme("blue")

#     # Clear existing widgets
#     for widget in root.winfo_children():
#         widget.destroy()

#     # Set up the main frame and configure the layout weights
#     root.columnconfigure(0, weight=1)
#     root.rowconfigure(0, weight=1)

#     # Create the main frame
#     main_frame = ctk.CTkFrame(root, fg_color="#f0f4f8")
#     main_frame.pack(fill="both", expand=True)
#     main_frame.grid_columnconfigure(0, weight=1) 
#     main_frame.grid_columnconfigure(1, weight=0)
#     main_frame.grid_columnconfigure(2, weight=0)
#     main_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)  # Make rows flexible

#     # Welcome Title
#     title_label = ctk.CTkLabel(main_frame, text="Welcome to Lakeside Health Clinic", 
#                             font=ctk.CTkFont("Helvetica", 40, "bold"), text_color="#2C3E50")
#     title_label.grid(row=0, column=0, columnspan=2, padx=(30,20), pady=(20, 10), sticky="nsew")
    
#     # Load the illustration
#     illustration_img = Image.open("logos/medicine.png")  # Update with your illustration path
#     illustration_img = ctk.CTkImage(illustration_img, size=(400, 350))

#     # Illustration Label
#     illustration_label = ctk.CTkLabel(main_frame, image=illustration_img, text="")
#     illustration_label.grid(row=1, column=1, rowspan=4, padx=(20,30), pady=20, sticky="nsew")

#     subtitle_label_frame = ctk.CTkFrame(main_frame, fg_color="#f0f4f8", width=500)
#     subtitle_label_frame.grid(row=2, column=0, columnspan=2, padx=20, sticky="w")

#     # Subtitle
#     subtitle_label = ctk.CTkLabel(subtitle_label_frame, text="Lakeside Health Clinic is a caring neighborhood clinic providing essential healthcare services. "
#             "Known for its personal touch, the clinic supports families and individuals with a range of services, "
#             "focusing on patient health and comfort. As the community grows, Lakeside remains committed to "
#             "meeting everyone’s needs with quality care.",
#                                 font=ctk.CTkFont("Helvetica", 16), text_color="#2C3E50", justify="center", wraplength=480)
#     subtitle_label.grid(row=0, column=0, padx=2, pady=2, sticky="n")

#     # Buttons Frame
#     buttons_frame = ctk.CTkFrame(main_frame, fg_color="#f0f4f8")
#     buttons_frame.grid(row=3, column=0, padx=20, pady=5, sticky="")

#     def navigate_to(screen_func):
#         for widget in root.winfo_children():
#             widget.destroy()
#         screen_func(root)

#     # Login Button
#     login_btn = ctk.CTkButton(buttons_frame, text="Login", width=150, height=50, 
#                             font=ctk.CTkFont("Helvetica", 16, "bold"), corner_radius=20, command=lambda: navigate_to(show_login))
#     login_btn.grid(row=0, column=0, padx=10)

#     # Signup Button
#     signup_btn = ctk.CTkButton(buttons_frame, text="Signup", width=150, height=50, 
#                             font=ctk.CTkFont("Helvetica", 16, "bold"), corner_radius=20, command=lambda: navigate_to(show_signup_page))
#     signup_btn.grid(row=0, column=1, padx=10)

#     # # Disclaimer Label
#     # disclaimer_label = ctk.CTkLabel(main_frame, text="Disclaimer: This is a sample application created for academic purposes only.",
#     #                                 font=ctk.CTkFont("Helvetica", 10), text_color="#e74c3c", anchor="w")
#     # disclaimer_label.grid(row=3, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="ew")

#     # # Footer Information
#     # footer_label = ctk.CTkLabel(main_frame, text="© 2024 Central Michigan University, CBA BIS598, Fall 2024", 
#     #                             font=ctk.CTkFont("Helvetica", 10), text_color="#bdc3c7")
#     # footer_label.grid(row=4, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="ew")



import tkinter as tk
import customtkinter as ctk
from customtkinter import CTkImage
from tkinter import ttk
from PIL import Image, ImageTk  # For adding logos
from db_connection import connect_db
from login_screen import show_login

def landing_page(root):
    from signup_screen import show_signup_page

    # Set the appearance mode and color theme
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    # Clear existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Configure root layout for responsiveness
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Create the main frame
    main_frame = ctk.CTkFrame(root, fg_color="#f0f4f8")
    main_frame.grid(row=0, column=0, sticky="nsew")
    main_frame.grid_columnconfigure(0, weight=2)  # Column for text
    main_frame.grid_columnconfigure(1, weight=1)  # Column for image
    main_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

    # Welcome Title
    title_label = ctk.CTkLabel(main_frame, text="Welcome to Lakeside Health Clinic",
                               font=ctk.CTkFont("Helvetica", 40, "bold"), text_color="#2C3E50")
    title_label.grid(row=0, column=0, columnspan=2, padx=(30, 20), pady=(20, 10), sticky="n")

    # Inside the landing_page function, replace this section
    try:
        illustration_img = Image.open("logos/medicine.png")  # Update with your illustration path
        illustration_img = CTkImage(light_image=illustration_img, size=(400, 350))  # Use CTkImage with size
        illustration_label = ctk.CTkLabel(main_frame, image=illustration_img, text="")
        illustration_label.grid(row=1, column=1, rowspan=4, padx=(20, 30), pady=20, sticky="nsew")
    except FileNotFoundError:
        illustration_label = ctk.CTkLabel(main_frame, text="Image Not Found", text_color="red")
        illustration_label.grid(row=1, column=1, rowspan=4, padx=(20, 30), pady=20, sticky="nsew")

    # Subtitle Frame
    subtitle_label_frame = ctk.CTkFrame(main_frame, fg_color="#f0f4f8")
    subtitle_label_frame.grid(row=2, column=0, padx=20, sticky="nsew")

    # Subtitle Text
    subtitle_label = ctk.CTkLabel(subtitle_label_frame,
                                  text=("Lakeside Health Clinic is a caring neighborhood clinic providing essential healthcare services. "
                                        "Known for its personal touch, the clinic supports families and individuals with a range of services, "
                                        "focusing on patient health and comfort. As the community grows, Lakeside remains committed to "
                                        "meeting everyone’s needs with quality care."),
                                  font=ctk.CTkFont("Helvetica", 16), text_color="#2C3E50", justify="center", wraplength=480)
    subtitle_label.pack(fill="both", expand=True, padx=10, pady=10)

    # Buttons Frame
    buttons_frame = ctk.CTkFrame(main_frame, fg_color="#f0f4f8")
    buttons_frame.grid(row=3, column=0, padx=20, pady=5, sticky="ew")
    buttons_frame.grid_columnconfigure((0, 1), weight=1)  # Equal spacing for buttons

    def navigate_to(screen_func):
        for widget in root.winfo_children():
            widget.destroy()
        screen_func(root)

    # Login Button
    login_btn = ctk.CTkButton(buttons_frame, text="Login", width=150, height=50,
                               font=ctk.CTkFont("Helvetica", 16, "bold"), corner_radius=20,
                               command=lambda: navigate_to(show_login))
    login_btn.grid(row=0, column=0, padx=10, pady=10)

    # Signup Button
    signup_btn = ctk.CTkButton(buttons_frame, text="Signup", width=150, height=50,
                                font=ctk.CTkFont("Helvetica", 16, "bold"), corner_radius=20,
                                command=lambda: navigate_to(show_signup_page))
    signup_btn.grid(row=0, column=1, padx=10, pady=10)

    # Disclaimer Label (Optional)
    disclaimer_label = ctk.CTkLabel(main_frame,
                                    text="Disclaimer: This is a sample application created for academic purposes only.",
                                    font=ctk.CTkFont("Helvetica", 10), text_color="#e74c3c")
    disclaimer_label.grid(row=4, column=0, columnspan=2, padx=20, pady=(10, 5), sticky="ew")

    # Footer Information (Optional)
    footer_label = ctk.CTkLabel(main_frame,
                                text="© 2024 Central Michigan University, CBA BIS598, Fall 2024",
                                font=ctk.CTkFont("Helvetica", 10), text_color="#bdc3c7")
    footer_label.grid(row=5, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="ew")

if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Lakeside Health Clinic")
    root.geometry("1024x768")  # Default size
    root.minsize(800, 600)  # Prevent the window from being too small
    landing_page(root)
    root.mainloop()
