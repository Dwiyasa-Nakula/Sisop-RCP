import xmlrpc.client
import threading
import time

proxy = xmlrpc.client.ServerProxy('http://10.0.2.15:8000/RPC2')  # Replace <VM_IP> with the VM's IP address.

print("What do you want to do?")
print("1. Upload a file")
print("2. Download a file")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    upload_file_name = input("Enter the name of the file to upload: ")

    def upload_file(filename):
        try:
            time.sleep(5)
            with open(filename, 'rb') as f:
                file_data = f.read()
            result = proxy.upload(filename, xmlrpc.client.Binary(file_data))
            print(result)
        except Exception as e:
            print("Error uploading file:", e)

    upload_thread = threading.Thread(target=upload_file, args=(upload_file_name,))
    upload_thread.start()
    upload_thread.join()

elif choice == "2":
    download_file_name = input("Enter the name of the file to download: ")

    def download_file(filename):
        try:
            time.sleep(5)
            file_info = proxy.download(filename)
            with open(file_info['filename'], 'wb') as f:
                f.write(file_info['data'].data)
            print("File downloaded successfully.")
        except Exception as e:
            print("Error downloading file:", e)

    download_thread = threading.Thread(target=download_file, args=(download_file_name,))
    download_thread.start()
    download_thread.join()
else:
    print("Invalid choice. Please enter 1 for upload or 2 for download.")
