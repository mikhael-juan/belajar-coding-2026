# Pesan selamat datang
print("Selamat datang di Kalkulator UTBK!")
print("Siapkan masa depanmu mulai sekarang! Pastikan skor tryoutmu melampaui passing grade jurusan favorit dari universitas terbaik di Indonesia!")
print("Sebelum mulai rasionalisasi, silakan input nilai 4 tryout terakhir")
print("❗Pastikan yang anda input adalah nilai rata-rata setiap tryout ")
Tryout_1=float(input("Ketik nilai tryout pertama (dalam angka) "))
Tryout_2=float(input("Ketik nilai tryout kedua (dalam angka) "))
Tryout_3=float(input("Ketik nilai tryout ketiga (dalam angka) "))
Tryout_4=float(input("Ketik nilai tryout keempat (dalam angka) "))
rata_rata=round((Tryout_1+Tryout_2+Tryout_3+Tryout_4)/4, 2)
print(f"\nRata rata tryout anda adalah:{rata_rata}")
# ❗❗❗Sebenarnya masih ada bug, yaitu kalau nilai tryout yang user input lebih dari 4 digit, rata-rata otomatis keluar lebih dari 4 digit juga. Tapi karena belum belajar len raw split, jadi biarkan saja dulu (karena sudah ada warning sebelumnya untuk input nilai rata rata Tryout)

# Supaya variabelnya bisa dipakai di bawah
passing_grade=0
nama_prodi=""
valid=True

# Daftar Universitas Terbaik di Indonesia
print("\nSekarang silakan pilih PTN impianmu!")
print("1. Universitas Indonesia (UI)")
print("2. Universitas Gadjah Mada (UGM)")
print("3. Institut Teknologi Bandung (ITB)")
univ=input("Ketik PTN pilihan anda (1-3) ")

# If Universitas Indonesia
if univ=="1":
    print("\nJurusan favorit apa di Universitas Indonesia yang menjadi target anda?")
    print("1. Pendidikan Dokter (FK)")
    print("2. Ilmu Hukum (FH)")
    print("3. Ilmu Komunikasi (FISIP)")
    target=input("Ketik pilihan anda (1-3) ")

# Untuk 1. FK UI
    if target=="1":
        passing_grade=780
        nama_prodi="Pendidikan Dokter - Universitas Indonesia"
        print("Passing grade jurusan anda adalah 780")
        print(f"rata rata tryout anda:{round(rata_rata, 2)}")

        
# Untuk 2. FH UI
    elif target=="2":
        passing_grade=760
        nama_prodi="Ilmu Hukum - Universitas Indonesia"
        print("Passing grade jurusan anda adalah 760")
        print(f"rata rata tryout anda:{round(rata_rata, 2)}")

# Untuk 3. FISIP UI
    elif target=="3":
        passing_grade=750
        nama_prodi="Ilmu Komunikasi - Universitas Indonesia"
        print("Passing grade jurusan anda adalah 750")
        print(f"rata rata tryout anda:{round(rata_rata, 2)}")

    else:
        print("Pilihan tidak valid, silakan ketik angka (1-3)")
        valid=False


# If Universitas Gadjah Mada
elif univ=="2":
    print("Jurusan favorit apa di Universitas Gadjah Mada yang menjadi target anda?")
    print("1. Pendidikan Dokter (FK)")
    print("2. Teknik Sipil (FT)")
    print("3. Hukum (FH)")
    target=input("Ketik pilihan anda (1-3) ")


# Untuk 1. FK UGM
    if target=="1":
        nama_prodi="Pendidikan Dokter - Universitas Gadjah Mada"
        passing_grade=770
        print("Passing grade jurusan anda adalah 770")
        print(f"rata rata tryout anda:{round(rata_rata, 2)}")
        
# Untuk 2. FT UGM
    elif target=="2":
        passing_grade=765
        nama_prodi="Teknik Sipil - Universitas Gadjah Mada"
        print("Passing grade jurusan anda adalah 765")
        print(f"rata rata tryout anda:{round(rata_rata, 2)}")

# Untuk 3. FH UGM
    elif target=="3":
        passing_grade=770
        nama_prodi="Ilmu Hukum - Universitas Gadjah Mada"
        print("Passing grade jurusan anda adalah 770")
        print(f"rata rata tryout anda:{round(rata_rata, 2)}")

    else:
        print("Pilihan tidak valid, silakan ketik angka (1-3)")
        valid=False


# If Institut Teknologi Bandung
elif univ=="3":
    print("Fakultas favorit apa di Institut Teknologi Bandung yang menjadi target anda?")
    print("1. Sekolah Teknik Elektro dan Informatika (STEI-K)")
    print("2. Fakultas Teknik Pertambangan dan Perminyakan (FTTM)")
    print("3. Sekolah Bisnis dan Manajemen (SBM)")
    target=input("Ketik pilihan anda (1-3) ")

# Untuk 1. STEI-K (ITB)
    if target=="1":
        passing_grade=765
        nama_prodi="STEI-K Institut Teknologi Bandung"
        print("Passing grade jurusan anda adalah 765")
        print(f"rata rata tryout anda:{round(rata_rata, 2)}")
        
# Untuk 2. FTTM (ITB)
    elif target=="2":
        passing_grade=767
        nama_prodi="FTTM - Institut Teknologi Bandung"
        print("Passing grade jurusan anda adalah 767")
        print(f"rata rata tryout anda:{round(rata_rata, 2)}")

# Untuk 3. SBM (ITB)
    elif target=="3":
        passing_grade=740
        nama_prodi="SBM - Institut Teknologi Bandung"
        print("Passing grade jurusan anda adalah 740")
        print(f"rata rata tryout anda:{round(rata_rata, 2)}")

    else:
        print("Pilihan tidak valid, silakan ketik angka (1-3)")
        valid=False

# Selesaikan dulu semua univ dan jurusan, baru lanjut ke bawah
if valid:
    lanjut=input("\nApakah anda ingin melihat peluang kelulusan anda? (YA/TIDAK)")

if lanjut.upper()=="YA":
    selisih=rata_rata - passing_grade

    print("\n" + "=" * 50)
    print("HASIL ANALISIS PELUANG ANDA") 
    print(f"Rata-Rata Tryout:{rata_rata}")
    print(f"Passing Grade Jurusan Pilihan: {passing_grade}")
    print(f"Selisih (Rata-Rata - Passing Grade:{selisih:+2f} ")
    if selisih >=30:
         print("✅ PELUANG BESAR")
         print("Nilaimu jauh melampaui passing grade!")
         print("Jaga konsistensi skor hingga UTBK nanti!")

    elif selisih >=10:
         print("✅ PELUANG CUKUP BESAR")
         print(f"Nilaimu {selisih:.2f} poin di atas passing grade!")
         print("Selalu pertahankan dan jangan lengah!") 
         
    elif selisih >=0:
        print("⚠️ PELUANG CENDERUNG TIPIS")
        print(f"Nilaimu hanya {selisih:.2f} poin di atas passing grade!")
        print("Kondisi anda sangat rawan! Terus evaluasi tryout dan terus lakukan peningkatan! ") 

    else:
        print("❌ PELUANG KECIL")
        print("Nilaimu di bawah passing grade!")
        print("Kondisi anda sangat rawan! Terus evaluasi tryout dan segera lakukan peningkatan! ") 

else: 
    print("Baik! Semoga anda mampu mempersiapkan UTBK dengan lancar")
