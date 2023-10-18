import xmlrpc.client
import threading
import time
import os

proxy = xmlrpc.client.ServerProxy('http://10.4.67.52:8000/RPC2')
directory = "."
save_path = "."

def download_file_from_server(host_ip, file_name, save_path="."):
    try:
        file_info = proxy.download(file_name)
        if 'data' in file_info and 'filename' in file_info:
            file_data = file_info['data'].data
            full_save_path = os.path.join(save_path, file_info['filename'])

            with open(full_save_path, 'wb') as f:
                f.write(file_data)
            print(f"File '{file_name}' downloaded and saved to '{full_save_path}'.")
        else:
            print(f"Error downloading file '{file_name}' from the server.")
    except Exception as e:
        print(f"Error downloading file '{file_name}': {str(e)}")

print("What do you want to do?")
print("1. Send a file")
print("2. Download a file")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    upload_file_name = input("Enter the name of the file to send: ")

    def upload_file(filename):
        try:
            time.sleep(5)
            with open(filename, 'rb') as f:
                file_data = f.read()
            result = proxy.upload(filename, xmlrpc.client.Binary(file_data))
        except Exception as e:
            print("Error uploading file:", e)

    upload_thread = threading.Thread(target=upload_file, args=(upload_file_name,))
    upload_thread.start()
    upload_thread.join()


elif choice == "2":
    download_file_name = input("Enter the name of the file to download: ")
    download_file_from_server("10.4.67.52", download_file_name, directory)

else:
    print("Invalid choice. Please enter 1 for upload or 2 for download.")
