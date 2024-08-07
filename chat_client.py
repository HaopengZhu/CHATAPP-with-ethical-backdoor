import asyncio
import websockets
import json
import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import serialization

CHUNK_SIZE = 190

client_id = os.getenv('CLIENT_ID', 'Client1')
recipient_id = os.getenv('RECIPIENT_ID', 'Client2')

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

def encrypt_chunk(chunk, public_key):
    return public_key.encrypt(
        chunk,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

def decrypt_chunk(chunk, private_key):
    return private_key.decrypt(
        chunk,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

async def send_message(websocket, public_key):
    while True:
        message = input("Enter message: ")
        encrypted_message = encrypt_chunk(message.encode(), public_key)
        message_data = json.dumps({"tag": "message", "from": client_id, "to": recipient_id, "info": base64.b64encode(encrypted_message).decode()})
        await websocket.send(message_data)
        print("Message sent.")

async def send_file(websocket, file_path, public_key):
    if os.path.getsize(file_path) > 10240:
        print("Error: File size exceeds the limit.")
        return
    with open(file_path, 'rb') as file:
        file_data = file.read()
        encrypted_data = encrypt_chunk(file_data, public_key)
        file_message = json.dumps({
            "tag": "file",
            "from": client_id,
            "to": recipient_id,
            "filename": os.path.basename(file_path),
            "info": base64.b64encode(encrypted_data).decode('utf-8')
        })
        await websocket.send(file_message)
        print("File sent.")

async def receive_message(websocket, private_key):
    while True:
        message = await websocket.recv()
        message_data = json.loads(message)
        if message_data["tag"] == "message":
            encrypted_message = base64.b64decode(message_data["info"])
            decrypted_message = decrypt_chunk(encrypted_message, private_key)
            print("Received message:", decrypted_message.decode())
        elif message_data["tag"] == "file":
            print("File received.")

async def main():
    server_ip = input("Enter server IP address: ")
    server_port = input("Enter server port: ") or 5555
    uri = f"ws://{server_ip}:{server_port}"
    async with websockets.connect(uri) as websocket:
        public_key_pem = await websocket.recv()
        server_public_key = serialization.load_pem_public_key(public_key_pem.encode())
        await asyncio.gather(
            send_message(websocket, server_public_key),
            receive_message(websocket, private_key),
            send_file(websocket, "path_to_file.txt", server_public_key)
        )

if __name__ == "__main__":
    asyncio.run(main())







