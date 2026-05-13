#!/usr/bin/env python3
import os
import sys

def build_ransomware():
    print("\n" + "="*50)
    print("🔧 RANSOMWARE BUILDER - FAHZ-TOOLS 🔧")
    print("="*50)
    
    print("\n[!] PERINGATAN: Ini untuk edukasi!")
    print("[!] Hanya gunakan di sistem milik sendiri!\n")
    
    confirm = input("Apakah Anda yakin? (yes/no): ")
    
    if confirm.lower() == 'yes':
        if os.path.exists('ransomware.py'):
            print("\n[*] Membaca ransomware.py...")
            with open('ransomware.py', 'r') as f:
                code = f.read()
            
            print("\n[✓] SCRIPT RANSOMWARE BERHASIL DIAMBIL:\n")
            print("="*60)
            print(code)
            print("="*60)
            
            # Simpan ke file output
            output_file = "ransomware_build_output.py"
            with open(output_file, 'w') as f:
                f.write(code)
            
            print(f"\n[✓] Script disimpan ke {output_file}")
            print("[*] Jalankan: python3 ransomware_build_output.py")
        else:
            print("[✗] File ransomware.py tidak ditemukan!")
    else:
        print("[!] Dibatalkan.")

if __name__ == "__main__":
    build_ransomware()
