import socket, hashlib, os

def create_file():
    data = os.urandom(1024)  # 1KB random binary
    with open("file.txt", "wb") as f:
        f.write(data)
    checksum = hashlib.md5(data).hexdigest()
    return data, checksum

def main():
    s = socket.socket()
    s.bind(("0.0.0.0", 5000))
    s.listen(1)
    print("Server is waiting for connection...")
    conn, addr = s.accept()
    print(f"Connected to {addr}")

    data, checksum = create_file()
    conn.sendall(data + b"::" + checksum.encode())
    conn.close()
    print("File and checksum sent.")

if __name__ == "__main__":
    main()
