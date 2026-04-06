import socket
import tkinter as tk
from tkinter import messagebox

# Connect to server
def connect_to_server():
    global client
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("localhost", 5000))
        status_label.config(text="Connected to Server", fg="green")
    except:
        status_label.config(text="Connection Failed", fg="red")


# Send request to server
def send_request():
    source = source_var.get()
    destination = dest_var.get()

    if source == "" or destination == "":
        messagebox.showerror("Error", "Please select both source and destination")
        return

    try:
        message = f"{source},{destination}"
        client.send(message.encode())

        response = client.recv(1024).decode()
        result_label.config(text=response)

    except:
        messagebox.showerror("Error", "Server not connected")


# GUI Window
root = tk.Tk()
root.title("🚦 Smart Traffic Monitoring System")
root.geometry("400x350")

# Variables
source_var = tk.StringVar()
dest_var = tk.StringVar()

# Title
tk.Label(root, text="Smart Traffic System", font=("Arial", 16, "bold")).pack(pady=10)

# Source Dropdown
tk.Label(root, text="Select Source").pack()
source_menu = tk.OptionMenu(root, source_var, "NORTH", "SOUTH", "EAST", "WEST")
source_menu.pack(pady=5)

# Destination Dropdown
tk.Label(root, text="Select Destination").pack()
dest_menu = tk.OptionMenu(root, dest_var, "NORTH", "SOUTH", "EAST", "WEST")
dest_menu.pack(pady=5)

# Connect Button
tk.Button(root, text="Connect to Server", command=connect_to_server, bg="blue", fg="white").pack(pady=10)

# Send Button
tk.Button(root, text="Check Traffic", command=send_request, bg="green", fg="white").pack(pady=10)

# Result
result_label = tk.Label(root, text="", wraplength=300, fg="black")
result_label.pack(pady=10)

# Status
status_label = tk.Label(root, text="Not Connected", fg="red")
status_label.pack(pady=5)

root.mainloop()
