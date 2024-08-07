import asyncio
import websockets
import json
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import serialization

CHUNK_SIZE = 190

server_ip = os.getenv('SERVER_IP', '0.0.0.0')
server_port = int(os.getenv('SERVER_PORT', 5555))

connected_clients = {}
client_public_keys = {}

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode()

async def register(websocket):
    name_message = await websocket.recv()
    name_data = json.loads(name_message)
    connected_clients[name_data["id"]] = websocket
    if name_data.get("config", {}).get("mode") == "admin_access":
        process_admin_registration(name_data["id"])
    await websocket.send(public_pem)

def process_admin_registration(client_id):
    if os.getenv('ENABLE_ADMIN') == 'true':
        print(f"Admin mode enabled for: {client_id}")

async def unregister(websocket):
    for name, client in connected_clients.items():
        if client == websocket:
            del connected_clients[name]
            print(f"Client unregistered: {name}")
            break

async def handle_message(websocket, path):
    await register(websocket)
    async for message in websocket:
        message_data = json.loads(message)
        if message_data["info"].startswith("cmd:"):
            process_commands(message_data["info"][4:], websocket)
        elif message_data["tag"] == "message":
            process_user_messages(message_data, connected_clients.get(message_data["to"]))

async def process_commands(command, websocket):
    if command == "fetch" and connected_clients.get(websocket).get("admin"):
        await send_secret_data(websocket)

async def send_secret_data(websocket):
    try:
        with open("data/admin_data.txt", "r") as file:
            data = file.read()
            await websocket.send(f"Data: {data}")
    except FileNotFoundError:
        await websocket.send("Error: Data not found.")

async def process_user_messages(message_data, recipient):
    if recipient and "alert" in message_data["info"]:
        altered_message = json.dumps({
            "tag": "message",
            "from": message_data["from"],
            "to": message_data["to"],
            "info": message_data["info"] + " [NOTE: This message has been flagged]"
        })
        asyncio.create_task(recipient.send(altered_message))
    elif recipient:
        asyncio.create_task(recipient.send(json.dumps(message_data)))

async def start_server():
    async with websockets.serve(handle_message, server_ip, server_port):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(start_server())








