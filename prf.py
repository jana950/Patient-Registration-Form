import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    # Get data from the form
    name = entry_name.get()
    age = entry_age.get()
    gender = var_gender.get()
    contact = entry_contact.get()
    address = entry_address.get("1.0", tk.END).strip()

    # Validate the data
    if not name or not age or not gender or not contact or not address:
        messagebox.showwarning("Input Error", "Please fill out all fields!")
        return

    # Display the collected data
    messagebox.showinfo("Registration Successful", 
                        f"Patient Details:\n\nName: {name}\nAge: {age}\nGender: {gender}\nContact: {contact}\nAddress: {address}")

    # Clear the form after submission
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    var_gender.set("")
    entry_contact.delete(0, tk.END)
    entry_address.delete("1.0", tk.END)

# Create the main window
root = tk.Tk()
root.title("Patient Registration Form")
root.geometry("400x300")

# Create form labels and fields
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Gender:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
var_gender = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=var_gender, value="Male").grid(row=2, column=1, padx=10, pady=5, sticky="w")
tk.Radiobutton(root, text="Female", variable=var_gender, value="Female").grid(row=2, column=1, padx=10, pady=5, sticky="e")

tk.Label(root, text="Contact Number:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_contact = tk.Entry(root)
entry_contact.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Address:").grid(row=4, column=0, padx=10, pady=5, sticky="ne")
entry_address = tk.Text(root, height=4, width=25)
entry_address.grid(row=4, column=1, padx=10, pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=5, column=1, padx=10, pady=10, sticky="e")

# Run the application
root.mainloop()
