from vidstream import ScreenShareClient
import threading 

# Update the IP address to the receiver's active IP (192.168.1.4)
sender = ScreenShareClient('192.168.1.4', 9999)  # Adjust IP if receiver is on another device

# Start the screen sharing in a separate thread
t = threading.Thread(target=sender.start_stream)
t.start()

# Wait for user input to stop the screen sharing
while input("") != 'STOP':
    continue

sender.stop_stream()