import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from kyber_kem import MockKyberKEM
from file_encryption import FileEncryptor, FileDecryptor

class SecureFileStorageGUI:
    def __init__(self, root):
        self.kem = MockKyberKEM()
        self.encryptor = FileEncryptor()
        self.decryptor = FileDecryptor()
        
        self.root = root
        self.root.title("Secure File Storage with Mock Kyber")
        
        # Create heading
        heading = tk.Label(root, text="Kyber Encryption", font=("Helvetica", 16, "bold"))
        heading.pack(pady=10)
        
        # Create description
        description = tk.Label(root, text="A simple demonstration of post-quantum cryptographic encryption and decryption using a mock Kyber KEM.", wraplength=500)
        description.pack(pady=5)
        
        # Create a frame for the buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        
        # Load and resize images
        self.generate_keys_img = ImageTk.PhotoImage(Image.open("generate_keys.png").resize((100, 100)))
        self.encapsulate_key_img = ImageTk.PhotoImage(Image.open("encapsulate_key.png").resize((100, 100)))
        self.encrypt_file_img = ImageTk.PhotoImage(Image.open("encrypt_file.png").resize((100, 100)))
        self.decrypt_file_img = ImageTk.PhotoImage(Image.open("decrypt_file.png").resize((100, 100)))
        
        # Create buttons with images and text below
        self.generate_keys_button = tk.Button(button_frame, image=self.generate_keys_img, text="Generate Keys", compound="top", command=self.generate_keys)
        self.generate_keys_button.grid(row=0, column=0, padx=5)
        
        self.encapsulate_key_button = tk.Button(button_frame, image=self.encapsulate_key_img, text="Encapsulate Key", compound="top", command=self.encapsulate_key)
        self.encapsulate_key_button.grid(row=0, column=1, padx=5)
        
        self.encrypt_file_button = tk.Button(button_frame, image=self.encrypt_file_img, text="Encrypt File", compound="top", command=self.encrypt_file)
        self.encrypt_file_button.grid(row=0, column=2, padx=5)
        
        self.decrypt_file_button = tk.Button(button_frame, image=self.decrypt_file_img, text="Decrypt File", compound="top", command=self.decrypt_file)
        self.decrypt_file_button.grid(row=0, column=3, padx=5)
        
        # Create text widgets for displaying file contents
        self.encrypted_text = tk.Text(root, height=6, width=60)
        self.encrypted_text.pack(pady=8)
        
        self.decrypted_text = tk.Text(root, height=6, width=60)
        self.decrypted_text.pack(pady=8)
        
        self.status_label = tk.Label(root, text="", fg="green")
        self.status_label.pack(pady=5)
        
        # Add exit button
        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack(pady=5)
        
        # Add refresh button
        self.refresh_button = tk.Button(root, text="Refresh", command=self.refresh)
        self.refresh_button.pack(pady=5)
    
    def generate_keys(self):
        self.kem.generate_keys()
        messagebox.showinfo("Success", "Keys Generated Successfully")

    def encapsulate_key(self):
        self.ciphertext, self.shared_secret = self.kem.encapsulate_key()
        messagebox.showinfo("Success", f"Key Encapsulated\nCiphertext: {self.ciphertext}\nShared Secret: {self.shared_secret}")

    def encrypt_file(self):
        input_file = filedialog.askopenfilename(title="Select file to encrypt")
        if input_file:
            output_file = filedialog.asksaveasfilename(title="Save encrypted file as")
            if output_file:
                self.encryptor.encrypt_file(input_file, output_file, self.shared_secret)
                self.status_label.config(text="File encrypted successfully.")
                with open(output_file, 'rb') as f:
                    encrypted_content = f.read()
                self.encrypted_text.delete('1.0', tk.END)
                self.encrypted_text.insert(tk.END, encrypted_content)
    
    def decrypt_file(self):
        input_file = filedialog.askopenfilename(title="Select file to decrypt")
        if input_file:
            output_file = filedialog.asksaveasfilename(title="Save decrypted file as")
            if output_file:
                decapsulated_secret = self.kem.decapsulate_key(self.ciphertext)
                self.decryptor.decrypt_file(input_file, output_file, decapsulated_secret)
                self.status_label.config(text="File decrypted successfully.")
                with open(output_file, 'r') as f:
                    decrypted_content = f.read()
                self.decrypted_text.delete('1.0', tk.END)
                self.decrypted_text.insert(tk.END, decrypted_content)
    
    def refresh(self):
        self.encrypted_text.delete('1.0', tk.END)
        self.decrypted_text.delete('1.0', tk.END)
        self.status_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = SecureFileStorageGUI(root)
    root.mainloop()
