import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 5000))

    print("✅ Connected to Server!\n")

    valid = ["NORTH", "SOUTH", "EAST", "WEST"]

    while True:
        source = input("Enter Source (NORTH/SOUTH/EAST/WEST): ").upper()
        destination = input("Enter Destination: ").upper()

        # Input validation
        if source not in valid or destination not in valid:
            print("❌ Invalid input! Try again.\n")
            continue

        message = f"{source},{destination}"
        client.send(message.encode())

        response = client.recv(1024).decode()
        print("🚦 Server Response:", response, "\n")

        choice = input("Continue? (y/n): ")
        if choice.lower() != 'y':
            break

    client.close()


start_client()