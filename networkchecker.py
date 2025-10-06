import os
import platform

# 1. Tentukan Daftar IP Target (Diletakkan di luar fungsi agar mudah diakses)
ip_list = [
    '192.168.1.1',     # Gateway Router Lokal (Contoh: Harusnya UP)
    '8.8.8.8',         # Google DNS (Contoh: Harusnya UP)
    '192.168.1.254',   # IP yang tidak ada (Contoh: Harusnya DOWN)
    '10.10.10.10'      # IP yang tidak ada (Contoh: Harusnya DOWN)
]

def check_network_status():
    """
    Melakukan ping sweep ke daftar IP yang ditentukan dan melaporkan status.
    """
    
    # 2. Tentukan Perintah Ping Berdasarkan OS
    # -n 1 untuk Windows, -c 1 untuk Linux/macOS
    if platform.system() == "Windows":
        ping_command = "ping -n 1"
    else:
        ping_command = "ping -c 1"
    
    # Tambahkan Try-Except Block untuk Error Handling
    try:
        print("--- Memulai Pengecekan Status Jaringan ---")
        print(f"Menggunakan OS: {platform.system()}")
        
        # 3. Lakukan Iterasi (Loop) untuk Mengecek Setiap IP
        for ip in ip_list:
            full_command = f"{ping_command} {ip}"
            
            # os.system menjalankan perintah dan mengembalikan return code (0 = Sukses)
            response = os.system(full_command)
            
            # 4. Tampilkan Hasil
            if response == 0:
                print(f"[SUCCESS] {ip} is UP.")
            else:
                print(f"[FAIL] {ip} is DOWN or Unreachable.")
                
    except KeyboardInterrupt:
        # Menangani jika pengguna menekan Ctrl+C
        print("\n\n[WARNING] Pengecekan dihentikan oleh pengguna.")
    except Exception as e:
        # Menangani error tak terduga lainnya
        print(f"\n[ERROR] Terjadi kesalahan tak terduga: {e}")
        
    finally:
        print("--- Pengecekan Selesai ---")

# Panggil Fungsi Utama hanya jika script dijalankan secara langsung
if __name__ == "__main__":
    check_network_status()