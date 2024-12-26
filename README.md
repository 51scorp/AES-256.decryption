# SSH File Decryption Script  

This script retrieves an encrypted file from a remote Linux server via SSH and decrypts its content using AES encryption.  

## Features  
- Connects to a remote Linux server securely using SSH (`paramiko` library).  
- Fetches the specified encrypted file from the server.  
- Decrypts the file using AES in CFB mode with a predefined key.  

---

## Prerequisites  

Ensure the following Python libraries are installed:  
- `paramiko`  
- `pycryptodome` (provides AES encryption tools)  

To install these dependencies, run:  
```bash  
pip install paramiko pycryptodome  
```  

---

## Usage  

1. **Update Configuration**  
   Modify the following variables in the script to match your setup:  
   - `LINUX_IP`: IP address of the remote Linux server.  
   - `USERNAME`: SSH username.  
   - `PASSWORD`: SSH password.  
   - `FILE_PATH`: Path to the encrypted file on the server.  
   - `key_str`: Encryption key (replace with the actual key used for decryption).  

2. **Run the Script**  
   Execute the script by running:  
   ```bash  
   python script_name.py  
   ```  

3. **Output**  
   If the operation succeeds, the script prints the decrypted content (e.g., a root password). If it fails, error messages will help you debug issues.  

---

## Example  

For the following configuration:  
```python  
LINUX_IP = "10.10.10.10"  
USERNAME = "root"  
PASSWORD = "password"  
FILE_PATH = "/your/path/file.txt"  
key_str = "key_AES"  
```  

The script fetches the file `/your/path/file.txt` from the server at `10.10.10.10`, decrypts it using the provided key, and prints the result.  

---

## Security Warning  

- Ensure the encryption key (`key_str`) and SSH credentials (`PASSWORD`) are stored securely and not hard-coded in production environments.  
- Use environment variables or a secure key management system to handle sensitive information.  

---

## License  

This script is provided "as-is" under the [MIT License](LICENSE). Use it at your own risk.  
