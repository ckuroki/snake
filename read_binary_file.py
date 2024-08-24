import os
import time

def read_appending_binary_file(file_path, chunk_size=1024, poll_interval=1):
    """
    Reads from a binary file that is being appended by another process.

    :param file_path: Path to the binary file.
    :param chunk_size: Number of bytes to read at a time.
    :param poll_interval: Time interval (in seconds) to wait before checking for new data.
    """
    with open(file_path, 'rb') as file:
        while True:
            current_position = file.tell()
            data = file.read(chunk_size)
            if data:
                # Process the data
                print(f"Read {len(data)} bytes")
                # Example of processing: printing as hexadecimal
                print(data.hex())
            else:
                # No new data, wait and try again
                time.sleep(poll_interval)
                # Check if file size has increased (file was appended)
                file.seek(current_position, os.SEEK_SET)

if __name__ == "__main__":
    # Example usage
    read_appending_binary_file('state.out')

