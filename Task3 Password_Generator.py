import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack()
        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.generated_password_label = tk.Label(root, text="")
        self.generated_password_label.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.accept_button = tk.Button(root, text="Accept Password", state=tk.DISABLED, command=self.accept_password)
        self.accept_button.pack()

        self.submitted_password_label = tk.Label(root, text="")
        self.submitted_password_label.pack()

        self.submit_button = tk.Button(root, text="Submit Password", state=tk.DISABLED, command=self.submit_password)
        self.submit_button.pack()

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_fields)
        self.reset_button.pack()

        self.username = ""
        self.password_length = 0
        self.generated_password = ""
        self.submitted_password = ""

    def generate_password(self):
        self.username = self.username_entry.get()
        self.password_length = int(self.length_entry.get())

        if not self.username:
            self.generated_password_label.config(text="Please enter a username.")
            return

        if self.password_length <= 0:
            self.generated_password_label.config(text="Please enter a valid password length.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password_length = self.password_length - len(self.username)
        if password_length < 1:
            self.generated_password_label.config(text="Password length must be longer than the username.")
            return

        self.generated_password = self.username + ''.join(random.choice(characters) for _ in range(password_length))
        self.generated_password_label.config(text=f"Generated Password: {self.generated_password}")
        self.accept_button.config(state=tk.NORMAL)
        self.submit_button.config(state=tk.DISABLED)
        self.submitted_password_label.config(text="")
        self.submitted_password = ""

    def accept_password(self):
        self.accept_button.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.NORMAL)
        self.submitted_password_label.config(text="")
        self.submitted_password = ""

    def submit_password(self):
        if self.username and self.generated_password:
            self.submitted_password = self.generated_password
            self.submitted_password_label.config(text=f"Submitted Password: {self.submitted_password}")
        else:
            self.submitted_password_label.config(text="Generate a password first.")

    def reset_fields(self):
        self.username_entry.delete(0, tk.END)
        self.length_entry.delete(0, tk.END)
        self.generated_password_label.config(text="")
        self.accept_button.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.DISABLED)
        self.submitted_password_label.config(text="")
        self.username = ""
        self.password_length = 0
        self.generated_password = ""
        self.submitted_password = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
