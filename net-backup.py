from netmiko import ConnectHandler
import datetime
import os

device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.10",    # GANTI dengan IP Perangkat Cisco
    "username": "admin",      # GANTI dengan Username SSH 
    "password": "cisco_ssh_pass",      # GANTI dengan Password SSH 
    "secret": "yayaya"  # GANTI dengan Enable Secret (note nek ada)
}

BACKUP_DIR = "network_backups"
if not os.path.exists(BACKUP_DIR):
    os.mkdir(BACKUP_DIR)
    print(f"Direktori '{BACKUP_DIR}' dibuat.")


try:
    print(f"Sedang mencoba koneksi ke {device['host']}...")

    net_connect = ConnectHandler(**device)
    
    net_connect.enable() 
  
    print("Mengambil running-config...")
    output = net_connect.send_command("show running-config")
   
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{BACKUP_DIR}/{device['host']}_backup_{timestamp}.txt"
    
    with open(filename, "w") as f:
        f.write(output)
        
    print(f"[SUCCESS] Konfigurasi berhasil disimpan ke: {filename}")
    
except Exception as e:
    print(f"[ERROR] Gagal melakukan backup untuk {device['host']}: {e}")
    
finally:
    if 'net_connect' in locals():
        net_connect.disconnect()
        print("Koneksi ditutup.")