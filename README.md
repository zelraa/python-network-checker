# Python Network Status Checker (Ping Sweeper)

## 💻 Deskripsi Proyek

Skrip Python sederhana ini dirancang untuk melakukan ping sweep otomatis pada daftar alamat IP yang ditentukan. Proyek ini dibuat untuk mendemonstrasikan kemampuan dasar dalam Otomasi Jaringan dan pengujian konektivitas menggunakan Python.

## 🛠️ Teknologi yang Digunakan

- **Bahasa Pemrograman:** Python 3
- **Library:** `os` dan `platform` (Library standar)
- **Konsep Jaringan:** Protokol ICMP (Ping)
- **Sistem Operasi:** Kompatibel dengan Windows, Linux, dan macOS.

## ✨ Fitur Utama

1.  **Multi-Platform:** Otomatis menyesuaikan perintah `ping` (-n 1 atau -c 1) berdasarkan sistem operasi.
2.  **Report Status:** Memberikan status yang jelas ([SUCCESS] UP atau [FAIL] DOWN) untuk setiap IP.
3.  **Error Handling:** Menggunakan blok `try-except` untuk menangani interupsi keyboard (Ctrl+C).

## 🚀 Cara Menjalankan

1.  **Kloning Repositori:**
    ```bash
    git clone [https://github.com/zelraa/py-networkchecker.git](https://github.com/zelraa/py-networkchecker.git)
    cd python-ping-sweeper
    ```
2.  **Jalankan Skrip:**
    ```bash
    python network_checker.py
    ```

## 📄 Contoh Output
