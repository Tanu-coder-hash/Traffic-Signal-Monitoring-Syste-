import socket
import threading
from datetime import datetime

# Initial traffic data
traffic_data = {
    ("NORTH", "SOUTH"): 10,
    ("EAST", "WEST"): 30,
    ("NORTH", "EAST"): 5,
    ("SOUTH", "WEST"): 25,
    ("NORTH", "WEST"): 35,
    ("EAST", "SOUTH"): 28
}

# Alternate routes
alternate_routes = {
    ("NORTH", "WEST"): "NORTH -> EAST -> WEST",
    ("EAST", "SOUTH"): "EAST -> NORTH -> SOUTH",
    ("SOUTH", "WEST"): "SOUTH -> EAST -> WEST",
    ("EAST", "WEST"): "EAST -> SOUTH -> WEST"
}

THRESHOLD = 20


def handle_client(conn, addr):
    print(f"[CONNECTED] {addr}")

    try:
        while True:
            data = conn.recv(1024).decode()

            if not data:
                break

            source, destination = data.split(",")

            time_now = datetime.now().strftime("%H:%M:%S")
            print(f"[{time_now}] {addr} → {source} to {destination}")

            vehicles = traffic_data.get((source, destination), 0)

            # Decision logic
            if vehicles > THRESHOLD:
                alt = alternate_routes.get(
                    (source, destination),
                    f"{source} -> EAST -> {destination}"
                )
                response = f"❌ Heavy Traffic ({vehicles} vehicles)! Suggested Route: {alt}"
            else:
                response = f"✅ Clear Route ({vehicles} vehicles): {source} -> {destination}"

            # Update traffic dynamically
            traffic_data[(source, destination)] = vehicles + 5

            conn.send(response.encode())

    except:
        print(f"[DISCONNECTED] {addr}")

    conn.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 5000))
    server.listen(10)

    print("🚦 Server Started... Waiting for clients...\n")

    while True:
        conn, addr = server.accept()

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        print(f"[ACTIVE CLIENTS]: {threading.active_count() - 1}")


start_server()