import logging

# Konfigurasi logging untuk debug
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def login(username, password):
    # Simulasi database user (ganti dengan database nyata jika diperlukan)
    user_data = {"user1": "password123", "user2": "pass456"}

    if username in user_data and user_data[username] == password:
        logging.info(f"Login berhasil untuk user: {username}")
        return True
    else:
        logging.warning("Login gagal. Periksa username/password.")
        return False

# Input username dan password dari user
if __name__ == "__main__":
    input_username = input("Masukkan username: ")
    input_password = input("Masukkan password: ")

    # Cek login
    login(input_username, input_password)
