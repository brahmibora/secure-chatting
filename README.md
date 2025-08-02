# secure-chatting

# 🔐 Secure TCP Chat Application with GUI

A secure, encrypted LAN chat system with a beautiful Tkinter GUI, built using Python. This project demonstrates core networking, encryption, multi-threading, and GUI concepts — ideal for showcasing system-level skills for internships at companies like **Cisco**.

---

## 📌 Features

- ✅ Real-time chat using **TCP sockets**
- ✅ **AES-encrypted** end-to-end messaging
- ✅ Beautiful **Tkinter GUI**
- ✅ Supports multiple clients
- ✅ **Logs all chat messages** with timestamps
- ✅ Easy to extend with file sharing or login features

---

## 🧰 Tech Stack

- **Python 3**
- `socket`, `threading` – for networking and concurrency
- `tkinter`, `scrolledtext` – for GUI
- `pycryptodome` – for AES encryption
- `datetime` – for logging messages

---

## 🗂️ Project Structure

secure_chat/
├── client.py # GUI client with encryption
├── server.py # TCP server with message broadcasting & logging
├── encryption.py # AES encrypt/decrypt utilities
├── chat.log # Auto-generated log file



---

## 🔐 Encryption Logic

- **AES (CBC mode)** with a 16-byte secret key
- Messages are padded and encrypted before sending
- IV is randomly generated for each message and attached with ciphertext
- On the server side, each message is decrypted before broadcasting

---

## 💬 How It Works

1. **Server (`server.py`)**:
   - Accepts incoming client connections
   - Receives encrypted messages, decrypts, and logs them
   - Broadcasts encrypted messages to all other clients

2. **Client (`client.py`)**:
   - GUI lets user send and view messages
   - Messages are encrypted before sending and decrypted after receiving

---

## 🖥️ GUI Preview

+-----------------------------------------+
| [Secure TCP Chat] ×|
| |
| Alice: Hi Bob! |
| Bob: Hey Alice! |
| |
| [Type message here...] [Send Button] |
+-----------------------------------------+

yaml
Copy
Edit

---


🤝 Credits
Built with ❤️ by Brahmi Bora
Inspired by secure messaging apps and Cisco's focus on network-level engineering.

