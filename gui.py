import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from image_script import generate_image  # Assuming the function is in image_script.py

class ImageGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Generator")

        # Creating the notebook (tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        # Tab for Images
        self.image_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.image_tab, text="Images")

        # Tab for Files (empty for now)
        self.file_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.file_tab, text="Files")

        # Tab for Settings
        self.settings_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.settings_tab, text="Settings")

        # Widgets for the Image tab
        self.width_label = ttk.Label(self.image_tab, text="Width:")
        self.width_label.grid(row=0, column=0, padx=5, pady=5)

        self.width_entry = ttk.Entry(self.image_tab)
        self.width_entry.grid(row=0, column=1, padx=5, pady=5)

        self.height_label = ttk.Label(self.image_tab, text="Height:")
        self.height_label.grid(row=1, column=0, padx=5, pady=5)

        self.height_entry = ttk.Entry(self.image_tab)
        self.height_entry.grid(row=1, column=1, padx=5, pady=5)

        self.format_label = ttk.Label(self.image_tab, text="Format:")
        self.format_label.grid(row=2, column=0, padx=5, pady=5)

        # Make the combobox read-only to restrict input to dropdown options only
        self.format_combobox = ttk.Combobox(self.image_tab, values=["jpg", "jpeg", "png"], state="readonly")
        self.format_combobox.grid(row=2, column=1, padx=5, pady=5)

        self.generate_button = ttk.Button(self.image_tab, text="Generate Image", command=self.generate_image)
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=5)

        # Output section with a Text widget for error messages
        self.error_text = tk.Text(self.image_tab, width=50, height=10, wrap="word", state="disabled")
        self.error_text.grid(row=5, column=0, columnspan=2, pady=5)

        # Widgets for the Settings tab
        self.save_label = ttk.Label(self.settings_tab, text="Save Location:")
        self.save_label.grid(row=0, column=0, padx=5, pady=5)

        self.save_location_text = ttk.Label(self.settings_tab, text="No location selected")
        self.save_location_text.grid(row=0, column=1, padx=5, pady=5)

        self.choose_save_button = ttk.Button(self.settings_tab, text="Choose Save Location", command=self.choose_save_location)
        self.choose_save_button.grid(row=1, column=0, columnspan=2, pady=5)

        self.save_path = ""  # To store the chosen save path

    def choose_save_location(self):
        # Open file explorer to choose a save location
        self.save_path = filedialog.askdirectory()
        if self.save_path:
            self.save_location_text.config(text=self.save_path)  # Update the GUI to show the selected location
            self.show_message(f"Selected save path: {self.save_path}")

    def generate_image(self):
        try:
            # Check if a save location is selected
            if not self.save_path:
                self.show_message("Please select a save location in the Settings tab.", error=True)
                return

            # Get values from the entry fields
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())
            file_format = self.format_combobox.get()

            # Get current date and time
            from datetime import datetime
            current_time = datetime.now().strftime("%d.%m.%Y_%H:%M")

            # Call the function to generate the image
            filename = f"{self.save_path}/{current_time}_{width}x{height}_{file_format}.png"
            generate_image(width, height, file_format, filename)
            self.show_message(f"Image generated and saved as {filename}")

        except ValueError:
            self.show_message("Please enter valid numeric values for width and height.", error=True)
        except Exception as e:
            self.show_message(f"Error: {str(e)}", error=True)

    def show_message(self, message, error=False):
        # Enable the Text widget to insert the message
        self.error_text.config(state="normal")
        if error:
            self.error_text.insert(tk.END, f"ERROR: {message}\n")
        else:
            self.error_text.insert(tk.END, f"{message}\n")
        # Disable the Text widget to prevent user editing
        self.error_text.config(state="disabled")
        self.error_text.yview(tk.END)  # Scroll to the bottom


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGeneratorApp(root)
    root.mainloop()
