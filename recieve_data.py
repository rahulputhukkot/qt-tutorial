import asyncio
import serial

# Define the virtual serial port names
port_receive = "/dev/tnt1"

async def read_serial():
    try:

        ser_receive = serial.Serial(port_receive, 9600, timeout=0)

        while True:
            data = ser_receive.readline()

            if data:
                received_data = data.decode().strip()
                print(f"Received data: '{received_data}'")
                with open("received_data.txt", "a") as file:
                    file.write(received_data + "\n")
                    file.flush() 

            await asyncio.sleep(0.1)

    except Exception as e:
        print(f"An Error has occoured: {e}")

async def main():

    await asyncio.gather(read_serial())

if __name__ == "__main__":
    asyncio.run(main())
