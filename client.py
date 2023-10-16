import xmlrpc.client
import threading
import time

proxy = xmlrpc.client.ServerProxy('http://10.0.2.15:8000/RPC2')  # Replace <VM_IP> with the VM's IP address.

def upload_file(filename):
    try:
        time.sleep(5)
        with open(filename, 'rb') as f:
            file_data = f.read()
        result = proxy.upload(filename, xmlrpc.client.Binary(file_data))
        print(result)
    except Exception as e:
        print("Error uploading file:", e)

def download_file(filename):
    try:
        time.sleep(5)
        file_info = proxy.download(filename)
        with open(file_info['filename'], 'wb') as f:
            f.write(file_info['data'].data)
        print("File downloaded successfully.")
    except Exception as e:
        print("Error downloading file:", e)

upload_thread = threading.Thread(target=upload_file, args=("example.txt",)) #make custom input
download_thread = threading.Thread(target=download_file, args=("example.txt",)) #make custom input

upload_thread.start()
download_thread.start()

upload_thread.join()
download_thread.join()
