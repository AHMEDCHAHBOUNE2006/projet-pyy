import tkinter as tk

def change_text():
    name = entry.get()
    label.config(text=f"Hello {name}")

root = tk.Tk()
root.title("Simple App")
root.geometry("250x150")

label = tk.Label(root, text="Enter your name:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Say Hello", command=change_text)
button.pack(pady=5)

root.mainloop()