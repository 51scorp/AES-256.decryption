import paramiko
from Crypto.Cipher import AES

# SSH connection settings for accessing the Linux server
LINUX_IP = "10.10.10.10"  # IP address of the target Linux server
USERNAME = "root"  # SSH username
PASSWORD = "password"  # SSH password
FILE_PATH = "/your/path/file.txt"  # Path to the encrypted file on the server

# Encryption key (as a string) used for decrypting the file
key_str = "key_AES"


def fetch_file_via_ssh(ip, username, password, file_path):
    """
    Connects to a Linux server via SSH and retrieves a file.
    
    Args:
        ip (str): IP address of the Linux server.
        username (str): SSH username for authentication.
        password (str): SSH password for authentication.
        file_path (str): Path to the file to be retrieved on the server.

    Returns:
        bytes: The content of the file as bytes if successful.
        None: If an error occurs during the SSH or file retrieval process.
    """
    try:
        # Create an SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Auto-accept unknown host keys
        ssh.connect(ip, username=username, password=password)  # Connect to the server

        # Open an SFTP session and read the file
        sftp = ssh.open_sftp()
        with sftp.open(file_path, "rb") as remote_file:
            content = remote_file.read()

        # Close SFTP and SSH sessions
        sftp.close()
        ssh.close()
        return content
    except Exception as e:
        print(f"Error connecting to Linux: {e}")  # Print error details
        return None


def decrypt_root_password(encrypted_data: bytes, key: bytes) -> str:
    """
    Decrypts an encrypted file to retrieve the root password.

    Args:
        encrypted_data (bytes): The encrypted file content.
        key (bytes): The encryption key used for AES decryption.

    Returns:
        str: The decrypted password as a string.
    """
    # Extract the initialization vector (IV) from the first 16 bytes of the encrypted data
    iv = encrypted_data[:16]
    # Extract the ciphertext (remaining bytes)
    ciphertext = encrypted_data[16:]

    # Create a new AES cipher in CFB mode with the provided IV and key
    cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=128)
    # Decrypt the ciphertext and decode to a UTF-8 string
    decrypted_bytes = cipher.decrypt(ciphertext)
    return decrypted_bytes.decode('utf-8')


def main():
    """
    Main function to fetch the encrypted file from the server,
    decrypt it, and print the root password.
    """
    # Fetch the encrypted file from the Linux server
    encrypted_content = fetch_file_via_ssh(LINUX_IP, USERNAME, PASSWORD, FILE_PATH)
    if not encrypted_content:
        print("Failed to retrieve the file.")  # Print an error message if file retrieval fails
        return

    # Convert the encryption key string to bytes
    key = key_str.encode('utf-8')

    # Decrypt the encrypted file content and retrieve the root password
    root_password = decrypt_root_password(encrypted_content, key)
    print(f"Root password: {root_password}")  # Output the decrypted root password


if __name__ == "__main__":
    main()
