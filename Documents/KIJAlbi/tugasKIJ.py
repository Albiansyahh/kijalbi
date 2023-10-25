def vigenere_cipher(text, key, encrypt=True):
    result = ""
    key_length = len(key)
    
    for i, char in enumerate(text):
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            key_char = key[i % key_length].lower()
            shift_amount = ord(key_char) - ord('a')
            
            if not encrypt:
                shift_amount = -shift_amount
            
            encrypted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            
            if is_upper:
                encrypted_char = encrypted_char.upper()
            
            result += encrypted_char
        else:
            result += char
    
    return result

def encrypt_vigenere(text, key):
    return vigenere_cipher(text, key)

def decrypt_vigenere(text, key):
    return vigenere_cipher(text, key, encrypt=False)

def main():
    choice = input("Pilih operasi (1: Enkripsi, 2: Dekripsi): ")
    
    if choice == "1":
        plaintext = input("Masukkan pesan yang ingin Anda enkripsi: ")
        key = input("Masukkan kunci: ")
        encrypted_text = encrypt_vigenere(plaintext, key)
        print(f"Pesan Terenkripsi: {encrypted_text}")
    elif choice == "2":
        ciphertext = input("Masukkan pesan yang ingin Anda dekripsi: ")
        key = input("Masukkan kunci: ")
        decrypted_text = decrypt_vigenere(ciphertext, key)
        print(f"Pesan Terdekripsi: {decrypted_text}")
    else:
        print("Pilihan tidak valid. Silakan pilih 1 (Enkripsi) atau 2 (Dekripsi).")

if __name__ == "__main__":
    main()