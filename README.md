# 🔒 Secure Authentication Module for Operating Systems

## 🏗️ Overview
The **Secure Authentication Module for Operating Systems** is a robust security framework designed to enhance system security through multi-factor authentication (MFA). It provides multiple layers of protection by integrating password hashing, OTP verification, and biometric recognition to safeguard user accounts against vulnerabilities such as buffer overflows and trapdoors.

## ✨ Features
- 🔑 **Password Hashing**: Securely stores user credentials using SHA-256 hashing.
- 🔢 **One-Time Password (OTP)**: Generates and verifies dynamic 6-digit OTPs.
- 🧑‍💻 **Face Recognition**: Utilizes OpenCV to authenticate users through facial recognition.
- 🛡️ **Biometric Authentication (Upcoming)**: Aims to incorporate biometric data for enhanced security.

## 🛠️ Technology Stack
- 🐍 **Python**: Core programming language.
- 🖼️ **Tkinter**: GUI for user interaction.
- 📷 **OpenCV**: Face recognition and verification.
- 🔏 **Hashlib**: SHA-256 hashing for password security.

## ⚙️ How It Works
1. 📝 **User Registration**: Hashes and securely stores the username and password.
2. 🔐 **Login with OTP**: Verifies user credentials and generates an OTP for two-factor authentication.
3. 🧑‍🦱 **Login with Face Recognition**: Uses the system's webcam to authenticate users biometrically.
4. 🛡️ **Biometric Authentication (Upcoming)**: Will include additional biometric methods.

## 📥 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AbhishekKumar-77/Secure-Authentication-Module.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Secure-Authentication-Module
   ```
3. Install required dependencies:
   ```bash
   pip install opencv-python
   ```

## 🚀 Usage
1. **Run the Application:**
   ```bash
   python Secure_Auth_Module.py
   ```
2. 📝 **Register** a new user by providing a username and password.
3. 🔑 **Login** using either OTP or Face Recognition.

## 🗂️ Project Structure
```
Secure-Authentication-Module/
├── Secure_Auth_Module.py
├── users.txt
├── README.md
```

## 🔮 Future Enhancements
- 🏷️ Implementing biometric authentication for fingerprint or iris recognition.
- 🔒 Secure storage of OTPs and user data.
- 🧾 Logging and audit trails for security events.

## 🤝 Contributing
Contributions are welcome! Feel free to submit issues or pull requests to enhance the module.

## 📜 License
This project is licensed under the **MIT License**.

## 📬 Contact
For any inquiries or feedback, please contact [Abhishek kumar,abhishekkumar776505@gmail.com].

