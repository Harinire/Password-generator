import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

# ---------------- PASSWORD GENERATOR ---------------- #

def generate_password():
    characters = ""

    if upper_var.get():
        characters += string.ascii_uppercase

    if lower_var.get():
        characters += string.ascii_lowercase

    if number_var.get():
        characters += string.digits

    if symbol_var.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showwarning("Warning", "Select at least one option!")
        return

    length = int(length_scale.get())

    password = ''.join(random.choice(characters) for _ in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    check_strength(password)


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        strength_label.config(text="Strength: Weak", fg="red")
    elif score == 3 or score == 4:
        strength_label.config(text="Strength: Medium", fg="orange")
    else:
        strength_label.config(text="Strength: Strong", fg="green")


def copy_password():
    password = password_entry.get()

    if password == "":
        return

    root.clipboard_clear()
    root.clipboard_append(password)

    messagebox.showinfo("Copied", "Password copied successfully!")


def save_password():
    password = password_entry.get()

    if password == "":
        return

    with open("saved_passwords.txt", "a") as file:
        file.write(password + "\n")

    messagebox.showinfo("Saved", "Password saved successfully!")


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x550")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Secure Password Generator",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

password_entry = tk.Entry(
    root,
    font=("Arial", 16),
    justify="center",
    width=30
)
password_entry.pack(pady=10)

strength_label = tk.Label(
    root,
    text="Strength:",
    font=("Arial", 12, "bold")
)
strength_label.pack()

length_label = tk.Label(
    root,
    text="Password Length",
    font=("Arial", 12)
)
length_label.pack(pady=5)

length_scale = tk.Scale(
    root,
    from_=4,
    to=32,
    orient=tk.HORIZONTAL,
    length=300
)
length_scale.set(12)
length_scale.pack()

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

ttk.Checkbutton(
    root,
    text="Uppercase",
    variable=upper_var
).pack(anchor="w", padx=90)

ttk.Checkbutton(
    root,
    text="Lowercase",
    variable=lower_var
).pack(anchor="w", padx=90)

ttk.Checkbutton(
    root,
    text="Numbers",
    variable=number_var
).pack(anchor="w", padx=90)

ttk.Checkbutton(
    root,
    text="Symbols",
    variable=symbol_var
).pack(anchor="w", padx=90)

generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=20
)
generate_btn.pack(pady=15)

copy_btn = tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    font=("Arial", 12),
    bg="#2196F3",
    fg="white",
    width=20
)
copy_btn.pack(pady=5)

save_btn = tk.Button(
    root,
    text="Save Password",
    command=save_password,
    font=("Arial", 12),
    bg="#9C27B0",
    fg="white",
    width=20
)
save_btn.pack(pady=5)

root.mainloop()