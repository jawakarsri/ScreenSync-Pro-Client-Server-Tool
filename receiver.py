from vidstream import StreamingServer
import threading

# Update the IP address to your machine's active IP (192.168.1.4)
receiver = StreamingServer('192.168.1.4', 9999)

# Start the server in a separate thread
t = threading.Thread(target=receiver.start_server)
t.start()

# Wait for user input to stop the server
while input("") != 'STOP':
    continue

receiver.stop_server()