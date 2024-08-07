# Overview

Hi everyone, Here is group 13 with our group members: Haopeng Zhu(a1901635) and Zeyu Liu(a1903617). This project provides a secure and real-time chat application that supports both public and private messaging. It is built using Python with the websockets library, incorporating advanced security features and encryption for data protection. chat_server.py is the backdoor-free server code, and chat_server1.py is the server code containing the ethical backdoor.

## Table of Contents
- **Features**
- **Technologies Used**
- **Prerequisites**
- **Installation**
- **Usage**
- **Configuration**
- **Security and Encryption**
- **License**
- **Contact**


## Features
Real-time messaging: Users can send and receive messages instantly.
Encryption: Secure client-to-client communication using RSA encryption.
File Transfer: Point-to-point encrypted file sharing.
Presence Updates: Real-time updates on user availability.
Rate Limiting: To prevent abuse and ensure service quality.

## Technologies Used
1. Python 3.8+
2. WebSockets
3. RSA cryptography
4. JSON
5. Git

## Prerequisites
Python 3.8 or later
websockets and cryptography libraries
A modern web browser

## Installation
To set up the chat system on your local machine:

Clone the repository: git clone URL_TO_REPOSITORY
Navigate to the project directory: cd path_to_project
Install required Python packages: pip install websockets cryptography
Start the server: python chat_server.py
Open the client script in your browser or run: python chat_client.py

## Usage

1. Starting the Application
**Server**: Run python chat_server.py to start the server.
**Client**: Execute python chat_client.py to launch the client interface.

2. Logging In
Open the client application.
Enter your desired username to connect to the chat server.

3. Sending Messages
Private Message: Select a user from the active user list to initiate a private conversation. Messages are encrypted using RSA encryption.
Public Message: Type your message in the chat input field and press send. It will be visible to all connected users.

4. File Transfer
Choose a file under the size limit of 10KB.
Send directly to another user, ensuring that the file is encrypted before transmission.

## Configuration

**Server**
The server is set up to listen on `0.0.0.0` at port `5555`.
Modify chat_server.py to change settings.

**Client**
Clients connect to the server using the specified server IP address and port `5555`.
Client configuration can be adjusted in chat_client.py.

## Encryption
**RSA Encryption**
Implement RSA encryption to securely transmit messages and files between clients.
Keys are generated dynamically upon client and server start.

**Secure WebSocket (WSS)**
The application uses WSS to ensure that all communications between the client and server are encrypted.

**Authentication**
Simple username entry point; consider integrating more robust authentication methods for enhanced security.

**Input Validation**
Inputs from users are validated and sanitized to prevent injection attacks and ensure secure communication.

**Rate Limiting**
Implement rate limiting to prevent denial-of-service attacks and manage the load on the server effectively

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). 

**Contact**
Group 13
For more information or to report issues, please contact: a1901635@adelaide.edu.au

GitHublink: https://github.com/HaopengZhu/CHATAPP.git
