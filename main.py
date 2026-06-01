from src.membership import Membership

system = Membership("System")

print("\n--- 1. MENAMPILKAN TABEL BENEFIT ---")
system.show_benefit()

print("\n--- 2. MENAMPILKAN TABEL REQUIREMENTS ---")
system.show_requirements()

print("\n--- 3. MENAMBAHKAN USER BARU ---")
user_baru = [
    {"nama": "Dina", "tier": "Silver"},
    {"nama": "Raka", "tier": "Gold"},
    {"nama": "Ana", "tier": "Platinum"}
]
for data in user_baru:
    system.add_new_user(data["nama"], data["tier"], overwrite=True)
    print(f"Berhasil mendaftarkan {data['nama']} Tier {data['tier']} ke dalam database")

print("\n--- 4. MEMPREDIKSI MEMBERSHIP USER BARU ---")
calon_member = [
    {"nama": "Budi", "expense": 7, "income": 12},
    {"nama": "Adit", "expense": 5, "income": 6}, #Menambahkan user lain
]

for calon in calon_member:
    objek_user = Membership(calon["nama"])
    hasil_prediksi = objek_user.predict_membership(expense=calon["expense"], income=calon["income"])
    print(f" Hasil prediksi untuk {calon['nama']} adalah {hasil_prediksi}")
    print(f" (Data {calon['nama']} otomatis langsung disimpan ke database)")

print("\n--- 5. CEK STATUS MEMBERSHIP DARI DATABASE ---")
daftar_nama_dicek = ["Sumbul", "Dina", "Raka", "Ana", "Budi", "Wati", "Adit"]
for nama in daftar_nama_dicek:
    status_tier = system.show_membership(nama)
    print(f"Status {nama} di database: {status_tier}")

print("\n--- 6. MENGHITUNG HARGA AKHIR (POTONGAN DISKON) ---")
daftar_belanjaan = [200000, 150000]
pelanggan_belanja = ["Dina", "Budi", "Raka"]
    
for nama_pembeli in pelanggan_belanja:
        total_bayar = system.calculate_price(nama_pembeli, daftar_belanjaan)
        tier_pembeli = system.show_membership(nama_pembeli)
        
        print(f"Total Belanja {nama_pembeli} ({tier_pembeli}) : Rp {total_bayar:.0f}")