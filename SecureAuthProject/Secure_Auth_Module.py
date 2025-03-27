import hashlib
import random
import time
import tkinter as tk
from tkinter import messagebox
import cv2

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def generate_otp():
    random.seed(time.time())
    return str(random.randint(100000, 999999))

def save_user(username, hashed_password):
    try:
        with open("users.txt", "a") as file:
            file.write(f"{username} {hashed_password}\n")
        return True
    except:
        return False

def validate_user(username, password):
    hashed_password = hash_password(password)
    try:
        with open("users.txt", "r") as file:
            for line in file:
                if not line.strip():  # Skip empty lines
                    continue
                parts = line.strip().split()
                if len(parts) != 2:  # Skip malformed lines
                    continue
                stored_user, stored_hash = parts
                if stored_user == username and stored_hash == hashed_password:
                    return True
    except FileNotFoundError:
        return False
    return False

def face_recognition():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    recognized = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) > 0:
            recognized = True
            break

        cv2.imshow('Face Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return recognized

def register_user():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        hashed_password = hash_password(password)
        if save_user(username, hashed_password):
            messagebox.showinfo("Success", "Registration Successful.")
        else:
            messagebox.showerror("Error", "Registration Failed.")
    else:
        messagebox.showwarning("Warning", "Please fill in all fields.")

def login_user_with_otp():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    if username and password:
        if validate_user(username, password):
            otp = generate_otp()
            messagebox.showinfo("OTP", f"Your OTP is: {otp}")
            otp_window = tk.Toplevel(root)
            otp_window.title("Enter OTP")
            tk.Label(otp_window, text="Enter OTP").pack()
            otp_entry = tk.Entry(otp_window)
            otp_entry.pack()

            def verify_otp():
                if otp_entry.get().strip() == otp:
                    messagebox.showinfo("Success", "Login Successful!")
                    otp_window.destroy()
                    root.destroy()
                else:
                    messagebox.showerror("Error", "Authentication Failed.")

            tk.Button(otp_window, text="Verify", command=verify_otp).pack()
        else:
            messagebox.showerror("Error", "Invalid Credentials.")
    else:
        messagebox.showwarning("Warning", "Please fill in all fields.")

def face_recognition():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Cannot open webcam.")
        return False

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    if face_cascade.empty():
        messagebox.showerror("Error", "Face cascade not found.")
        return False

    recognized = False
    start_time = time.time()

    while time.time() - start_time < 10:  # Run for 10 seconds
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) > 0:
            recognized = True
            break

        cv2.imshow('Face Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return recognized

def biometric_auth():
    messagebox.showinfo("Info", "Biometric Authentication not yet implemented.")

root = tk.Tk()
root.title("Secure Authentication Module")

username_label = tk.Label(root, text="Username")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Register", command=register_user).pack()
tk.Button(root, text="Login with OTP", command=login_user_with_otp).pack()
tk.Button(root, text="Login with Face", command=face_recognition).pack()
tk.Button(root, text="Login with Biometric", command=biometric_auth).pack()

root.mainloop() 