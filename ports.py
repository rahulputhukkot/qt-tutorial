#NOTE: This file was a POC and not to be used


# import time
# import serial

# # Define the virtual serial port names
# port_send = "/dev/tnt4"
# port_receive = "/dev/tnt5"


# ser_send = serial.Serial(
#     port_send,
#     9600,
#     bytesize=serial.EIGHTBITS,
#     stopbits=serial.STOPBITS_ONE,
#     parity=serial.PARITY_NONE,
#     timeout=3
#     )

# ser_receive = serial.Serial(
#     port_receive,
#     9600,
#     bytesize=serial.EIGHTBITS,
#     stopbits=serial.STOPBITS_ONE,
#     parity=serial.PARITY_NONE,
#     timeout=3
#     )

# time.sleep(1)

# try:
#     counter = 0
#     with open("received_data.txt", "a") as file:
#         while True:

#             # Data to send (simulating live data)
#             data_to_send = "Live data: " + str(counter) + "\r\n"
#             counter += 1

#             # Send data to the virtual device
#             ser_send.write(data_to_send.encode())
#             ser_send.flush()  

#             time.sleep(0.1)
#             received_data = ""

#             received_data = ser_receive.readline().decode().strip()

#             print(f"Received data: '{received_data}'")
#             if received_data:
#                 file.write(received_data + "\n")
#             file.flush() 
#             # ser_send.flushOutput()
#             # ser_receive.flushInput()

# except Exception as e:
#     print(f"An Error has occoured: {e}")
#     ser_send.close()
#     ser_receive.close()
