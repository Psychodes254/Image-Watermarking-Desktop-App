from tkinter import *
from PIL import Image, ImageFont, ImageDraw, ImageTk
from tkinter import messagebox, filedialog

root = Tk()
root.title("Water Mark Your Image")

selected_image = None


def open_image():
    # Define image
    global selected_image, tk_image
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png")])
    if image_path:
        # Open Image Using PIL
        selected_image = Image.open(image_path)
        tk_image = ImageTk.PhotoImage(selected_image)
        my_label.config(image=tk_image)
        my_label.image = tk_image


def add_it():
    # Create Watermark
    if not selected_image:
        messagebox.showerror("Error", "No Image Selected")
        return

    # Define the Font
    try:
        text_font = ImageFont.truetype("arial.ttf", 46)
    except IOError:
        messagebox.showerror("Error", "Font File 'arial.ttf' Not Found")
        return

    # Get Text to Image
    text_to_add = my_entry.get()
    if not text_to_add.strip():
        messagebox.showerror("Error", "No Text Entered")
        return

    # Create a copy to avoid modifying original
    watermarked_image = selected_image.copy()
    edit_image = ImageDraw.Draw(watermarked_image)

    # Calculate text position dynamically
    text_width, text_height = edit_image.textsize(text_to_add, font=text_font)
    image_width, image_height = watermarked_image.size

    # Position watermark (e.g., bottom right with padding)
    position = (
        image_width - text_width - 20,
        image_height - text_height - 20
    )
    edit_image.text(position, text_to_add, font=text_font)

    # Save the Image
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg")])

    if save_path:
        watermarked_image.save(save_path)
        messagebox.showinfo("Success", "Watermark Added Successfully")

    # Clear the Entry Box
    my_entry.delete(0, END)
    my_entry.insert(0, "File Saved")


# Create a Label
my_label = Label(root, text="Select an image to start", font=("Helvetica", 18))
my_label.pack(pady=20)

# Entry box
my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)
my_entry.insert(0, "Enter Watermark Text",)

# Open Image Button
open_img_button = Button(root, text="Add an Image", command=open_image, font=("Helvetica", 24))
open_img_button.pack(pady=20)


# Add Text Button
my_button = Button(root, text="Add Text To Image", command=add_it, font=("Helvetica", 24))
my_button.pack(pady=20)

root.mainloop()
