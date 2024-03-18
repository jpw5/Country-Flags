import customtkinter as ctk
import tkinter
from tkinter import PhotoImage
from PIL import Image, ImageTk  # Import Pillow's Image and ImageTk modules
import random
from countries import countries  # Assuming this now contains paths, not PhotoImage objects

ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.title('Country Flags')
root.geometry('460x420')  # Adjust the window size as needed
root.resizable(False, False)

# Initialize rand with a valid index
rand = random.randint(1, len(countries) - 1)


def update_flag_image():
    global rand, flag_image
    root.geometry('460x420')
    # flags_name.delete(0, tkinter.END)
    rand = random.randint(1, len(countries) - 1)
    flag_path = countries[rand]["Flag"]
    # Use Pillow to open and resize the image
    image = Image.open(flag_path)
    image_resized = image.resize((452, 302), Image.Resampling.LANCZOS)  # Updated resize line
    flag_image = ImageTk.PhotoImage(image_resized)
    flags.configure(image=flag_image)
    flags.image = flag_image  # Keep a reference


def submit():
    user_input = flags_name.get()
    if user_input.lower() == countries[rand]["Name"].lower():
        root.geometry('460x480')
        answer_label.configure(text='Correct!', text_color='green')
    else:
        root.geometry('460x480')
        answer_label.configure(text="Wrong. Try again!", text_color='red')


flags = ctk.CTkLabel(root, text='')  # Initialize without setting an image
flags.pack()

# Load and display the initial flag image after the GUI has started
update_flag_image()

flags_name = ctk.CTkEntry(root, placeholder_text='Enter name of country', font=ctk.CTkFont(size=20), width=400)
flags_name.pack(pady=(5, 5))

flags_button = ctk.CTkButton(root, text='Next', command=update_flag_image, font=ctk.CTkFont(size=20), width=400)
flags_button.pack()

flags_submit = ctk.CTkButton(root, text='Submit', command=submit, font=ctk.CTkFont(size=20), width=400)
flags_submit.pack(pady=(5, 10))

answer_label = ctk.CTkLabel(root, text='', font=ctk.CTkFont(size=30))
answer_label.pack(pady=(10, 0))

root.mainloop()
