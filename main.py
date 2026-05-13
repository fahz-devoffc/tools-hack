#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_banner():
    banner = r"""
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║   ███████╗ █████╗ ██╗  ██╗███████╗                     ║
    ║   ██╔════╝██╔══██╗██║  ██║╚══███╔╝                     ║
    ║   █████╗  ███████║███████║  ███╔╝                      ║
    ║   ██╔══╝  ██╔══██║██╔══██║ ███╔╝                       ║
    ║   ██║     ██║  ██║██║  ██║███████╗                     ║
    ║   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝                     ║
    ║                                                          ║
    ║   ████████╗ ██████╗  ██████╗ ██╗     ███████╗           ║
    ║   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝           ║
    ║      ██║   ██║   ██║██║   ██║██║     ███████╗           ║
    ║      ██║   ██║   ██║██║   ██║██║     ╚════██║           ║
    ║      ██║   ╚██████╔╝╚██████╔╝███████╗███████║           ║
    ║      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝           ║
    ║                                                          ║
    ║           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                ║
    ║          FAHZ-TOOLS  |  REDHAT - EDITION                ║
    ║           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """
    print(banner)
    print("\n" + "="*60)
    print("📌 Tools untuk Belajar Hacking disediakan Oleh FahzDev Secara gratis (open-source)")
    print("="*60)
    print("\n⚠️  ALERT: FOR EDUCATIONAL PURPOSE ONLY")
    print("⚠️  Baca tos.txt untuk melihat ketentuan penggunaan")
    print("="*60 + "\n")

def show_menu():
    menu = """
    ╔══════════════════════════════════════════════════════════╗
    ║                    📡 DAFTAR TOOLS 📡                    ║
    ╠══════════════════════════════════════════════════════════╣
    ║                                                          ║
    ║   [1]  DDoS Attack       →  ddos.py                      ║
    ║   [2]  DoS Attack         →  dos.py                       ║
    ║   [3]  Brute Force        →  bruteforce.py                ║
    ║   [4]  SQL Injection      →  sqlinjection.py              ║
    ║   [5]  Build Ransomware   →  ransomwarebuild.py           ║
    ║   [6]  Terms of Service   →  tos.txt                      ║
    ║   [7]  Guide & Tutorial   →  readme.md                    ║
    ║   [0]  Exit               →  Keluar                       ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """
    print(menu)

def main():
    while True:
        clear_screen()
        display_banner()
        show_menu()
        
        try:
            choice = input("\n┌─[Fahz@Tools:~]\n└──╼ Pilih nomor tools: ")
            
            if choice == '1':
                print("\n[+] Menjalankan DDoS Attack...")
                subprocess.run(['python3', 'ddos.py'])
                
            elif choice == '2':
                print("\n[+] Menjalankan DoS Attack...")
                subprocess.run(['python3', 'dos.py'])
                
            elif choice == '3':
                print("\n[+] Menjalankan Brute Force...")
                subprocess.run(['python3', 'bruteforce.py'])
                
            elif choice == '4':
                print("\n[+] Menjalankan SQL Injection Scanner...")
                subprocess.run(['python3', 'sqlinjection.py'])
                
            elif choice == '5':
                print("\n[+] Membangun Ransomware...")
                subprocess.run(['python3', 'ransomwarebuild.py'])
                
            elif choice == '6':
                print("\n[+] Membuka Terms of Service...")
                with open('tos.txt', 'r') as f:
                    print(f.read())
                input("\nTekan Enter untuk kembali...")
                
            elif choice == '7':
                print("\n[+] Membuka Guide...")
                with open('readme.md', 'r') as f:
                    print(f.read())
                input("\nTekan Enter untuk kembali...")
                
            elif choice == '0':
                print("\n[!] Keluar dari FAHZ-TOOLS...")
                sys.exit(0)
                
            else:
                print("\n[!] Pilihan tidak valid! Masukkan angka 0-7")
                input("\nTekan Enter untuk melanjutkan...")
                
        except KeyboardInterrupt:
            print("\n\n[!] Ctrl+C terdeteksi. Keluar...")
            sys.exit(0)
        except Exception as e:
            print(f"\n[!] Error: {e}")
            input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
