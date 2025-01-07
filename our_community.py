# import tkinter as tk
# import customtkinter as ctk
# from tkinter import messagebox

# def our_community(frame, staff_id):
#     from home_page import create_home_page

#     # Define some fonts and colors
#     font_bold = ("Arial", 12, "bold")
#     font_regular = ("Arial", 12)
#     header_color = "#3b8ed0"

#     # Initialize CustomTkinter appearance
#     ctk.set_appearance_mode("System")
#     ctk.set_appearance_mode("light")  # Change to "dark" for dark mode
#     ctk.set_default_color_theme("blue")  

#     # Clear existing widgets
#     for widget in frame.winfo_children():
#         widget.destroy()

#     # Set up the main frame and configure the layout weights
#     frame.grid_columnconfigure(0, weight=1)
#     frame.grid_rowconfigure(0, weight=1)

#     # Create a frame for the appointment booking form
#     commu_frame = ctk.CTkFrame(frame, fg_color='#f0f4f8', corner_radius=10, width=600)
#     commu_frame.pack(fill="both", expand=True)
#     commu_frame.columnconfigure(0, weight=1)
#     commu_frame.columnconfigure(1, weight=1)

#     # Header Section (Welcome)
#     header_frame = ctk.CTkFrame(commu_frame, corner_radius=0, height=50, bg_color=header_color, fg_color=header_color)
#     header_frame.pack(fill="x")

#     header_label = ctk.CTkLabel(header_frame, text="Welcome to Our Community", font=("Arial", 18, "bold"), text_color="white")
#     header_label.pack(padx=20, pady=10)

#     # Community Guidelines Section
#     guidelines_frame = ctk.CTkFrame(commu_frame, corner_radius=10, bg_color="#f0f4f8", fg_color="#E9ECEF", width=750)
#     guidelines_frame.pack(padx=20, pady=5)

#     guidelines_header = ctk.CTkLabel(guidelines_frame, text="Community Guidelines", font=("Arial", 16, "bold"))
#     guidelines_header.pack(pady=(20, 10))

#     guidelines_text = ctk.CTkLabel(guidelines_frame, text=(
#         "1. Be respectful and kind to everyone.\n"
#         "2. No offensive language or behavior.\n"
#         "3. Share knowledge and help others.\n"
#         "4. Stay on topic and keep discussions relevant.\n"
#         "5. Be patient and understanding with new members."
#     ), font=font_regular, anchor="w", padx=20)
#     guidelines_text.pack(padx=20, pady=(0, 20))

#     # Discussion Section
#     discussion_frame = ctk.CTkFrame(commu_frame, corner_radius=10, bg_color="#f0f4f8", fg_color="#E9ECEF", width=750)
#     discussion_frame.pack(padx=20, pady=5)

#     discussion_header = ctk.CTkLabel(discussion_frame, text="Active Discussions", font=("Arial", 16, "bold"))
#     discussion_header.pack(pady=(20, 10))

#     # Displaying dummy discussion posts
#     discussion_posts = [
#         {"user": "John Doe", "post": "How do I get started with the community?"},
#         {"user": "Jane Smith", "post": "I'm new here, what are the best resources to use?"},
#         {"user": "Chris Lee", "post": "Can anyone recommend some cool projects to collaborate on?"}
#     ]

#     for post in discussion_posts:
#         post_label = ctk.CTkLabel(discussion_frame, text=f"{post['user']} says: {post['post']}", font=font_regular, anchor="w", padx=20, pady=5)
#         post_label.pack(padx=20, pady=(0, 10))

#     # Add Post Section
#     def add_post():
#         new_post = post_entry.get()
#         if new_post:
#             discussion_posts.append({"user": "You", "post": new_post})
#             update_discussion_area()
#             post_entry.delete(0, tk.END)
#         else:
#             messagebox.showwarning("Input Error", "Please enter a post to share.")

#     def update_discussion_area():
#         for widget in discussion_frame.winfo_children():
#             widget.destroy()
#         # Recreate the discussion_header
#         discussion_header = ctk.CTkLabel(
#             discussion_frame,
#             text="Discussion Area",
#             font=("Helvetica", 16, "bold"),
#             text_color="black",
#             anchor="w"
#         )
#         discussion_header.pack(pady=(20, 10))
#         # Add posts dynamically
#         for post in discussion_posts:
#             post_label = ctk.CTkLabel(
#                 discussion_frame,
#                 text=f"{post['user']} says: {post['post']}",
#                 font=("Helvetica", 12),
#                 anchor="w",
#                 padx=20,
#                 pady=5
#             )
#         post_label.pack(padx=20, pady=(0, 10))

#     def go_back():
#         commu_frame.destroy()
#         create_home_page(frame, staff_id)

#     add_post_frame = ctk.CTkFrame(commu_frame, corner_radius=10, bg_color="#f0f4f8", fg_color="#E9ECEF", width=750)
#     add_post_frame.pack(padx=20, pady=5)

#     post_entry_label = ctk.CTkLabel(add_post_frame, text="Share a post with the community:", font=font_bold)
#     post_entry_label.pack(pady=10)

#     post_entry = ctk.CTkEntry(add_post_frame, font=font_regular, width=600)
#     post_entry.pack(padx=20, pady=10)

#     post_button = ctk.CTkButton(add_post_frame, text="Post", font=font_bold, command=add_post)
#     post_button.pack(padx=20, pady=20)
#     # Footer Section (Newsletter and Social Media)
#     footer_frame = ctk.CTkFrame(commu_frame, corner_radius=10, height=50, bg_color="#f0f4f8", fg_color="#E9ECEF")
#     footer_frame.pack(fill="x", padx=10, pady=5)

#     footer_label = ctk.CTkLabel(footer_frame, text="Stay Updated! Subscribe to our newsletter.", font=("Arial", 12, "bold"))
#     footer_label.pack(padx=20, pady=10)

#     newsletter_entry = ctk.CTkEntry(footer_frame, placeholder_text="Enter your email", font=font_regular)
#     newsletter_entry.pack(padx=20, pady=5)

#     subscribe_button = ctk.CTkButton(footer_frame, text="Subscribe", font=font_bold, command=lambda: messagebox.showinfo("Subscribed", "Thank you for subscribing!"))
#     subscribe_button.pack(padx=10, pady=5)

# # Add Back Button to Bottom
#     back_button = ctk.CTkButton(commu_frame, text="Back", font=font_bold, command=go_back)
#     back_button.pack(padx=10, pady=20, side="bottom")


# import tkinter as tk
# import customtkinter as ctk
# from tkinter import messagebox


# def our_community(frame, staff_id):
#     from home_page import create_home_page

#     # Define fonts and colors
#     font_bold = ("Arial", 14, "bold")
#     font_regular = ("Arial", 12)
#     header_color = "#3b8ed0"
#     background_color = "#f8f9fa"
#     section_bg_color = "#e9ecef"

#     # Initialize CustomTkinter appearance
#     ctk.set_appearance_mode("light")
#     ctk.set_default_color_theme("blue")

#     # Clear existing widgets
#     for widget in frame.winfo_children():
#         widget.destroy()

#     # Main frame for layout
#     frame.grid_columnconfigure(0, weight=1)
#     frame.grid_rowconfigure(0, weight=1)

#     # Community frame
#     commu_frame = ctk.CTkFrame(frame, fg_color=background_color, corner_radius=10)
#     commu_frame.pack(fill="both", expand=True)

#     # Header Section
#     header_frame = ctk.CTkFrame(commu_frame, fg_color=header_color, corner_radius=0)
#     header_frame.pack(fill="x", pady=(0, 10))
#     header_label = ctk.CTkLabel(header_frame, text="Welcome to Our Community", font=("Arial", 18, "bold"), text_color="white")
#     header_label.pack(padx=10, pady=10)

#     # Guidelines Section
#     guidelines_frame = ctk.CTkFrame(commu_frame, fg_color=section_bg_color, corner_radius=10)
#     guidelines_frame.pack(fill="x", padx=20, pady=10)
#     guidelines_label = ctk.CTkLabel(guidelines_frame, text="Community Guidelines", font=("Arial", 16, "bold"))
#     guidelines_label.pack(pady=(10, 5))
#     guidelines_text = ctk.CTkLabel(
#         guidelines_frame,
#         text=(
#             "1. Be respectful and kind to everyone.\n"
#             "2. No offensive language or behavior.\n"
#             "3. Share knowledge and help others.\n"
#             "4. Stay on topic and keep discussions relevant.\n"
#             "5. Be patient and understanding with new members."
#         ),
#         font=font_regular,
#         justify="left",
#         anchor="w",
#         text_color="black",
#     )
#     guidelines_text.pack(padx=10, pady=5)

#     # Scrollable Discussion Section
#     discussion_frame = ctk.CTkFrame(commu_frame, fg_color=section_bg_color, corner_radius=10)
#     discussion_frame.pack(padx=20, pady=10)

#     discussion_header = ctk.CTkLabel(discussion_frame, text="Active Discussions", font=("Arial", 16, "bold"), anchor="center")
#     discussion_header.pack(pady=(10, 5), anchor="center")

#     # Canvas for scrollable discussions
#     canvas = tk.Canvas(discussion_frame, bg=section_bg_color, highlightthickness=0)
#     scrollbar = ctk.CTkScrollbar(discussion_frame, command=canvas.yview)
#     scrollable_frame = ctk.CTkFrame(canvas, fg_color=section_bg_color)

#     canvas.create_window((0, 0), window=scrollable_frame, anchor="n")
#     canvas.configure(yscrollcommand=scrollbar.set)

#     scrollbar.pack(side="right", fill="y")
#     canvas.pack(fill="both", padx=5, pady=5)

#     def update_scroll_region(event):
#         canvas.configure(scrollregion=canvas.bbox("all"))

#     scrollable_frame.bind("<Configure>", update_scroll_region)

#     # Initial discussion posts
#     discussion_posts = [
#         {"user": "John Doe", "post": "How do I get started with the community?"},
#         {"user": "Jane Smith", "post": "I'm new here, what are the best resources to use?"},
#         {"user": "Chris Lee", "post": "Can anyone recommend some cool projects to collaborate on?"},
#     ]

#     def display_posts():
#         for widget in scrollable_frame.winfo_children():
#             widget.destroy()  # Clear current posts to avoid duplication

#         for post in discussion_posts:
#             post_label = ctk.CTkLabel(
#                 scrollable_frame,
#                 text=f"{post['user']} says: {post['post']}",
#                 font=font_regular,
#                 anchor="n",
#                 justify="center",
#                 padx=10,
#                 pady=5,
#                 wraplength=500,
#             )
#             post_label.pack(fill="x", pady=(5, 5))

#     display_posts()

#     # Add Post Section
#     add_post_frame = ctk.CTkFrame(commu_frame, fg_color=section_bg_color, corner_radius=10)
#     add_post_frame.pack(fill="x", padx=20, pady=10)

#     post_label = ctk.CTkLabel(add_post_frame, text="Share a post with the community:", font=font_bold)
#     post_label.pack(pady=10)
#     post_entry = ctk.CTkEntry(add_post_frame, font=font_regular, width=400, placeholder_text="Write your post here...")
#     post_entry.pack(pady=10)
#     post_button = ctk.CTkButton(
#         add_post_frame,
#         text="Post",
#         font=font_bold,
#         command=lambda: add_post(post_entry.get()),
#     )
#     post_button.pack(pady=10)

#     def add_post(new_post):
#         if new_post.strip():
#             discussion_posts.append({"user": "You", "post": new_post})
#             post_entry.delete(0, tk.END)
#             display_posts()
#         else:
#             messagebox.showwarning("Input Error", "Please write something to post!")

#     # Footer Section
#     footer_frame = ctk.CTkFrame(commu_frame, fg_color=section_bg_color, corner_radius=10)
#     footer_frame.pack(fill="x", padx=20, pady=10)

#     footer_label = ctk.CTkLabel(footer_frame, text="Stay Updated! Subscribe to our newsletter.", font=font_bold)
#     footer_label.pack(pady=10)
#     email_entry = ctk.CTkEntry(footer_frame, font=font_regular, placeholder_text="Enter your email")
#     email_entry.pack(pady=10)
#     subscribe_button = ctk.CTkButton(
#         footer_frame,
#         text="Subscribe",
#         font=font_bold,
#         command=lambda: messagebox.showinfo("Subscribed", "Thank you for subscribing!"),
#     )
#     subscribe_button.pack(pady=10)

#     # Back Button
#     def go_back():
#         commu_frame.destroy()
#         create_home_page(frame, staff_id)

#     back_button = ctk.CTkButton(commu_frame, text="Back", font=font_bold, command=go_back)
#     back_button.pack(pady=20)


import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox


def our_community(frame, staff_id):
    from home_page import create_home_page

    # Define fonts and colors
    font_bold = ("Arial", 14, "bold")
    font_regular = ("Arial", 12)
    header_color = "#3b8ed0"
    background_color = "#f8f9fa"
    section_bg_color = "#e9ecef"

    # Initialize CustomTkinter appearance
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    # Clear existing widgets
    for widget in frame.winfo_children():
        widget.destroy()

    # Configure grid for main frame
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)

    # Main frame for layout
    commu_frame = ctk.CTkFrame(frame, fg_color=background_color, corner_radius=10)
    commu_frame.grid(row=0, column=0, sticky="nsew")

    # Configure grid for commu_frame
    commu_frame.grid_columnconfigure(0, weight=1)
    commu_frame.grid_rowconfigure(1, weight=1)  # Scrollable content section should expand
    commu_frame.grid_rowconfigure(2, weight=0)  # 

    # Header Section
    header_frame = ctk.CTkFrame(commu_frame, fg_color=header_color, corner_radius=0)
    header_frame.grid(row=0, column=0, sticky="ew")
    header_label = ctk.CTkLabel(header_frame, text="Welcome to Our Community", font=("Arial", 18, "bold"), text_color="white")
    header_label.pack(padx=10, pady=10)

    # Guidelines Section
    guidelines_frame = ctk.CTkFrame(commu_frame, fg_color=section_bg_color, corner_radius=10)
    guidelines_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
    guidelines_frame.grid_columnconfigure(0, weight=1)
    guidelines_frame.grid_propagate(False)
    guidelines_frame.configure(height=150)  # Adjust this value as needed

    guidelines_label = ctk.CTkLabel(guidelines_frame, text="Community Guidelines", font=("Arial", 16, "bold"))
    guidelines_label.grid(row=0, column=0, pady=(10, 5))
    guidelines_text = ctk.CTkLabel(
        guidelines_frame,
        text=(
            "1. Be respectful and kind to everyone.\n"
            "2. No offensive language or behavior.\n"
            "3. Share knowledge and help others.\n"
            "4. Stay on topic and keep discussions relevant.\n"
            "5. Be patient and understanding with new members."
        ),
        font=font_regular,
        justify="left",
        anchor="w",
        text_color="black",
        wraplength=500,
    )
    guidelines_text.grid(row=1, column=0, padx=10, pady=5)


    # Scrollable Discussion Section
    discussion_frame = ctk.CTkFrame(commu_frame, fg_color=section_bg_color, corner_radius=10)
    discussion_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
    discussion_frame.grid_rowconfigure(0, weight=1)
    discussion_frame.grid_columnconfigure(0, weight=1)
    discussion_frame.configure(height=200)

    discussion_header = ctk.CTkLabel(discussion_frame, text="Active Discussions", font=("Arial", 16, "bold"))
    discussion_header.grid(row=0, column=0, pady=(10, 5), sticky="n")

    # Canvas for scrollable discussions
    canvas = tk.Canvas(discussion_frame, bg=section_bg_color, highlightthickness=0)
    canvas.grid(row=1, column=0, sticky="nsew")
    scrollbar = ctk.CTkScrollbar(discussion_frame, command=canvas.yview)
    scrollbar.grid(row=1, column=1, sticky="ns")
    scrollable_frame = ctk.CTkFrame(canvas, fg_color=section_bg_color)
    canvas.create_window((250, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set, height=200)

    def update_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    scrollable_frame.bind("<Configure>", update_scroll_region)

    # Initial discussion posts
    discussion_posts = [
        {"user": "John Doe", "post": "How do I get started with the community?"},
        {"user": "Jane Smith", "post": "I'm new here, what are the best resources to use?"},
        {"user": "Chris Lee", "post": "Can anyone recommend some cool projects to collaborate on?"},
    ]

    def display_posts():
        for widget in scrollable_frame.winfo_children():
            widget.destroy()  # Clear current posts to avoid duplication

        for post in discussion_posts:
            post_label = ctk.CTkLabel(
                scrollable_frame,
                text=f"{post['user']} says: {post['post']}",
                font=font_regular,
                anchor="w",
                justify="left",
                padx=10,
                pady=5,
                wraplength=500,
            )
            post_label.pack(fill="x", pady=(5, 5))

    display_posts()

    # Add Post Section
    add_post_frame = ctk.CTkFrame(commu_frame, fg_color=section_bg_color, corner_radius=10)
    add_post_frame.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")
    add_post_frame.grid_columnconfigure(0, weight=1)

    post_label = ctk.CTkLabel(add_post_frame, text="Share a post with the community:", font=font_bold)
    post_label.grid(row=0, pady=10, sticky="ew")
    post_field_frame = ctk.CTkFrame(add_post_frame, fg_color=section_bg_color)
    post_field_frame.grid(row=1, columnspan=2)
    post_entry = ctk.CTkEntry(post_field_frame, font=font_regular, placeholder_text="Write your post here...", width=200)
    post_entry.grid(row=0, column=0, padx=20, pady=10)
    post_button = ctk.CTkButton(
        post_field_frame,
        text="Post",
        font=font_bold,
        command=lambda: add_post(post_entry.get()),
    )
    post_button.grid(row=0, column=1, padx=20, pady=10)

    def add_post(new_post):
        if new_post.strip():
            discussion_posts.append({"user": "You", "post": new_post})
            post_entry.delete(0, tk.END)
            display_posts()
        else:
            messagebox.showwarning("Input Error", "Please write something to post!")

    # Footer Section
    footer_frame = ctk.CTkFrame(commu_frame, fg_color=section_bg_color, corner_radius=10)
    footer_frame.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
    footer_frame.grid_columnconfigure(0, weight=1)

    footer_label = ctk.CTkLabel(footer_frame, text="Stay Updated! Subscribe to our newsletter.", font=font_bold)
    footer_label.grid(row=0, column=0, pady=10)
    footer_field_frame = ctk.CTkFrame(footer_frame, fg_color=section_bg_color)
    footer_field_frame.grid(row=1, columnspan=2)
    email_entry = ctk.CTkEntry(footer_field_frame, font=font_regular, placeholder_text="Enter your email", width=200)
    email_entry.grid(row=0, column=0, padx=20, pady=10)
    subscribe_button = ctk.CTkButton(
        footer_field_frame,
        text="Subscribe",
        font=font_bold,
        command=lambda: messagebox.showinfo("Subscribed", "Thank you for subscribing!"),
    )
    subscribe_button.grid(row=0, column=1, padx=20, pady=10)

    # Back Button
    def go_back():
        commu_frame.destroy()
        create_home_page(frame, staff_id)

    back_button = ctk.CTkButton(commu_frame, text="Back", font=font_bold, command=go_back)
    back_button.grid(row=5, column=0, pady=20)

