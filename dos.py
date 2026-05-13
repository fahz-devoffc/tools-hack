#!/usr/bin/env python3
import subprocess
import time
import sys

def dos_attack(target_url):
    print(f"\n[!] TARGET: {target_url}")
    print("[!] Memulai DoS Attack - Jaringan akan terganggu selama 10 menit")
    print("[!] Tekan Ctrl+C untuk membatalkan\n")
    
    # Perintah iptables untuk memblokir koneksi ke target (Linux)
    if sys.platform.startswith('linux'):
        print("[*] Menggunakan iptables untuk blokir...")
        subprocess.run(['sudo', 'iptables', '-A', 'OUTPUT', '-d', target_url, '-j', 'DROP'])
        
        print("[*] Serangan aktif selama 10 menit...")
        for i in range(10, 0, -1):
            print(f"[*] {i} menit tersisa...", end='\r')
            time.sleep(60)
            
        print("\n[*] Menghentikan serangan...")
        subprocess.run(['sudo', 'iptables', '-D', 'OUTPUT', '-d', target_url, '-j', 'DROP'])
        print("[✓] Serangan selesai! Jaringan pulih.")
        
    else:
        print("[!] Tool ini hanya berfungsi di Linux dengan iptables")

if __name__ == "__main__":
    print("="*50)
    print("💀 DOS ATTACK TOOL - FAHZ-TOOLS 💀")
    print("⚠️  MEMBLOKIR JARINGAN SENDIRI KE TARGET")
    print("="*50)
    
    target = input("\nMasukkan target URL (contoh: example.com): ")
    dos_attack(target)
