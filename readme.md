# 🔥 FAHZ-TOOLS - Blackhat Toolkit (Educational)

**Dibuat oleh FahzDev**  
*Open-source untuk pembelajaran keamanan siber*

---

## ⚠️ PERINGATAN PENTING ⚠️

Tools ini **HANYA** untuk tujuan edukasi dan penelitian keamanan.  
Gunakan hanya di lingkungan testing milik sendiri atau dengan izin tertulis.

**Penyalahgunaan tools ini dapat berakibat pidana!**

---

## 📦 INSTALLASI DI TERMUX

```bash
# Update paket Termux
pkg update && pkg upgrade -y

# Install Python dan dependencies
pkg install python git -y

# Clone repository
git clone https://github.com/fahzdev/fahz-tools
cd fahz-tools

# Install library Python yang dibutuhkan
pip install requests cryptography

# Jalankan tools
python main.py
