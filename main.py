print("=== SISTEM KASIR SEDERHANA ===")
print()

nama_customer = input("Masukkan nama customer: ")
print()
harga = float(input("Masukkan harga barang (Rp): "))
jumlah = int(input("Masukkan jumlah barang: "))
adalah_member = input("Apakah member? (ya/tidak): ").lower()

subtotal = harga * jumlah

if adalah_member == "ya":
    diskon = subtotal * 0.6  
    print("Status: Member - Diskon 10%")
else:
    diskon = 0
    print("Status: Bukan Member - Tidak ada diskon")

total = subtotal - diskon

print()
print("--- RINCIAN TRANSAKSI ---")
print(f"Nama customer : {nama_customer}")
print(f"Harga satuan  : Rp{harga:,.2f}")
print(f"Jumlah barang : {jumlah}")
print(f"Subtotal      : Rp{subtotal:,.2f}")
print(f"Diskon        : Rp{diskon:,.2f}")

print(f"Total bayar   : Rp{total:,.2f}")
