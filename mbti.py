# Ask users for their name
nama = input("What is your name? ").strip().title()
print(f" Selamat datang {nama}, silakan jawab pertanyaan dengan jujur untuk mengetahui tipe MBTI anda! \n Klik enter untuk melanjutkan!")
# Menyiapkan skor awal untuk 4 dimensi
skor_EI=0
skor_SN=0
skor_TF=0
skor_JP=0

def tanya(pertanyaan):
    while True:
        jawaban=input(f"\n{pertanyaan} (ya/tidak): ").strip().lower()

        if jawaban in ["ya", "y","benar", "betul"]:
            return "ya"
        elif jawaban in ["tidak", "enggak", "gak"]:
            return "tidak"
        else:
            print("Jawaban hanya diperbolehkan 'ya' atau 'tidak'.")

# Pertanyaan dimensi Ekstrovert/Introvert
# Ekstrovert seringkali mendapat energi setelah beraktivitas dengan banyak orang, introvert seringkali mendapat energi setelah menyendiri/me-time
#Pertanyaan E/I ke-1
jawaban=tanya ("Kamu merasa lebih berenergi setelah hangout ramai-ramai daripada me-time sendirian?")
if jawaban=="ya":
    skor_EI+=1
elif jawaban=="tidak":
    skor_EI-=1

#Pertanyaan E/I ke-2
jawaban=tanya ("Kamu cenderung bicara dulu baru berpikir, bukan sebaliknya?")
if jawaban=="ya":
    skor_EI+=1
elif jawaban=="tidak":
    skor_EI-=1

#Pertanyaan E/I ke-3
jawaban=tanya ("Kamu lebih suka kerja kelompok daripada kerja sendiri?")
if jawaban=="ya":
    skor_EI+=1
elif jawaban=="tidak":
    skor_EI-=1

#Pertanyaan E/I ke-4
jawaban=tanya ("Saat memiliki masalah, kamu lebih nyaman untuk bercerita dengan orang lain daripada merenungkannya sendiri?")
if jawaban=="ya":
    skor_EI+=1
elif jawaban=="tidak":
    skor_EI-=1

#Pertanyaan E/I ke-5
jawaban=tanya ("Saat acara kumpul keluarga, kamu lebih sering membuka topik obrolan?")
if jawaban=="ya":
    skor_EI+=1
elif jawaban=="tidak":
    skor_EI-=1

# Pertanyaan dimensi Sensing/Intuition
# Sensing (S) mempercayai informasi berdasarkan apa yang dilihat dan dialami langsung. Intuition(N)Lebih suka melihat pola dan kemungkinan dari fakta
#Pertanyaan S/N ke-1
jawaban=tanya ("Saat belajar hal baru, kamu lebih suka contoh nyata dan langkah konkret daripada teori dan konsep abstrak?")
if jawaban=="ya":
    skor_SN+=1
elif jawaban=="tidak":
    skor_SN-=1

#Pertanyaan S/N ke-2
jawaban=tanya ("Kamu lebih sering membayangkan bagaimana sesuatu bisa menjadi berbeda di masa depan, daripada fokus pada apa yang terjadi sekarang?")
if jawaban=="ya":
    skor_SN-=1
elif jawaban=="tidak":
    skor_SN+=1

#Pertanyaan S/N ke-3
jawaban=tanya ("Saat mengikuti instruksi, kamu seringkali mencari jalan pintas sendiri, serta tidak mengikuti instruksi tertulis yang ada?")
if jawaban=="ya":
    skor_SN-=1
elif jawaban=="tidak":
    skor_SN+=1

#Pertanyaan S/N ke-4
jawaban=tanya ("Kamu sering mendasari argumenmu berdasarkan data statistik yang valid, bukan berdasarkan asumsi pribadimu?")
if jawaban=="ya":
    skor_SN+=1
elif jawaban=="tidak":
    skor_SN-=1

#Pertanyaan S/N ke-5
jawaban=tanya ("Kamu langsung menyebarkan berita yang baru saja diterima, tanpa memastikan keakuratannya?")
if jawaban=="ya":
    skor_SN-=1
elif jawaban=="tidak":
    skor_SN+=1

# Pertanyaan dimensi Thinking/Feeling
# Thinking (T) Mengutamakan logika dan objektivitas. Feeling (F) mengutamakan perasaan, harmoni, dan dampak emosional
#Pertanyaan T/F ke-1
jawaban=tanya ("Saat mengkritik pekerjaan teman, kamu cenderung memikirkan cara paling halus untuk menyampaikan tanpa menyinggungnya? ")
if jawaban=="ya":
    skor_TF-=1
elif jawaban=="tidak":
    skor_TF+=1

#Pertanyaan T/F ke-2
jawaban=tanya ("Saat berdebat, kamu berusaha mempertahankan argumen logis dan mengabaikan perasaan lawan debat? ")
if jawaban=="ya":
    skor_TF+=1
elif jawaban=="tidak":
    skor_TF-=1

#Pertanyaan T/F ke 3
jawaban=tanya ("Dalam mengambil keputusan, kamu cenderung mengabaikan fakta dan memilih mengikuti perasaanmu?")
if jawaban=="ya":
    skor_TF-=1
elif jawaban=="tidak":
    skor_TF+=1

#Pertanyaan T/F ke 4
jawaban=tanya ("Segera mengungkapkan kepada sahabat tentang fakta yang menyakitkan lebih baik daripada terus menutupinya?")
if jawaban=="ya":
    skor_TF+=1
elif jawaban=="tidak":
    skor_TF-=1

#Pertanyaan T/F ke 5
jawaban=tanya ("Saya memilih untuk menagih uang pinjaman teman, walaupun akan memicu keributan?")
if jawaban=="ya":
    skor_TF+=1
elif jawaban=="tidak":
    skor_TF-=1

# Pertanyaan dimensi Judging/Perceiving
# Judging (J) Merasa lebih nyaman ketika sesuatu sudah diputuskan dan terencana. P (Perceiving) merasa lebih nyaman membiarkan opsi tetap terbuka.
#Pertanyaan J/P ke-1
jawaban=tanya ("Kamu memilih menjalani akhir pekan secara fleksibel tanpa perencanaan?")
if jawaban=="ya":
    skor_JP-=1
elif jawaban=="tidak":
    skor_JP+=1

#Pertanyaan J/P ke-2
jawaban=tanya ("Kamu biasanya menyelesaikan tugas atau pekerjaan jauh sebelum batas waktu, bukan di menit-menit terakhir?")
if jawaban=="ya":
    skor_JP+=1
elif jawaban=="tidak":
    skor_JP-=1

#Pertanyaan J/P ke-3
jawaban=tanya ("Kamu merasa kesal jika ada seseorang yang mengganggu rutinitas harianmu?")
if jawaban=="ya":
    skor_JP+=1
elif jawaban=="tidak":
    skor_JP-=1

#Pertanyaan J/P ke-4
jawaban=tanya ("Kamu bersedia membatalkan aktivitas yang sudah direncanakan, dan menerima ajakan untuk melakukan aktivitas lain?")
if jawaban=="ya":
    skor_JP-=1
elif jawaban=="tidak":
    skor_JP+=1

#Pertanyaan J/P ke-5
jawaban=tanya ("Saat berlibur ke luar kota, kamu sudah merencanakan destinasi wisata yang akan dikunjungi, transportasi yang digunakan, bahkan kuliner yang akan dicoba?")
if jawaban=="ya":
    skor_JP+=1
elif jawaban=="tidak":
    skor_JP-=1
# Menghitung hasil
print("Menghitung hasil, klik enter untuk melanjutkan)")


# Menentukan kriteria Ekstrovert/Introvert
if skor_EI>=0:
    huruf_EI="E"
elif skor_EI<0:
    huruf_EI="I"
else:
    huruf_EI="?"

# Menentukan kriteria Sensing/Intuition
if skor_SN>=0:
    huruf_SN="S"
elif skor_SN<0:
    huruf_SN="N"
else:
    huruf_SN="?"

# Menentukan kriteria Thinking/Feeling
if skor_TF>=0:
    huruf_TF="T"
elif skor_TF<0:
    huruf_TF="F"
else:
    huruf_TF="?"

# Menentukan kriteria Judging/Perceiving
if skor_JP>=0:
    huruf_JP="J"
elif skor_JP<0:
    huruf_JP="P"
else:
    huruf_JP="?"

# Gabungkan huruf akhir untuk tipe MBTI pengguna
tipe_mbti=huruf_EI+huruf_SN+huruf_TF+huruf_JP

# Tampilkan hasil
def tampilkan_hasil(tipe, nama):
    print("\n"+"-"*50)
    print(f"Hasil MBTI: {nama} adalah tipe {tipe}")
    print("-"*50)

    match tipe:
        case"ISTJ":
            print("Nama: Ahli Logistik")
            print("Karakter: Disiplin, bertanggung jawab, praktis, teratur ")
            print("Kekuatan: Dapat dipercaya, teliti, konsisten, pekerja keras")
            print("Tantangan: Sulit beradaptasi dengan perubahan, cenderung kaku")
            print("Persentase Populasi: 11–14%")
    
        case"ISFJ":
            print("Nama: Pelindung")
            print("Karakter: Peduli, setia, rendah hati, sabar ")
            print("Kekuatan: Empatik, perhatian, dapat diandalkan, suka membantu")
            print("Tantangan: Sulit menolak permintaan, sering mengutamakan orang lain")
            print("Persentase Populasi: 13–14%")

        case"INFJ":
            print("Nama: Advokat")
            print("Karakter: Idealis, bijaksana, intuitif, penuh empati")
            print("Kekuatan: Visioner, memahami orang lain, berprinsip")
            print("Tantangan: Perfeksionis, mudah lelah secara emosional, tertutup")
            print("Persentase Populasi: 1–2%")

        case"INTJ":
            print("Nama: Arsitek")
            print("Karakter: Strategis, mandiri, analitis, visioner")
            print("Kekuatan: Perencana yang baik, logis, inovatif")
            print("Tantangan: Terkesan dingin, kurang sabar terhadap orang")
            print("Persentase Populasi: 2–3%")

        case"ISTP":
            print("Nama: Virtuoso")
            print("Karakter:  Tenang, logis, mandiri, suka praktik")
            print("Kekuatan: Cepat memecahkan masalah, adaptif, terampil")
            print("Tantangan: Sulit mengungkapkan perasaan, mudah bosan")
            print("Persentase Populasi: 4–6%")

        case"ISFP":
            print("Nama: Petualang")
            print("Karakter: Kreatif, lembut, fleksibel, menghargai kebebasan")
            print("Kekuatan: Artistik, empatik, mudah beradaptasi")
            print("Tantangan: Kurang suka perencanaan, menghindari konflik")
            print("Persentase Populasi: 8–9%")

        case"INFP":
            print("Nama: Mediator")
            print("Karakter: Idealis, imajinatif, penyayang, reflektif")
            print("Kekuatan: Kreatif, setia pada nilai, pendengar yang baik")
            print("Tantangan: Terlalu sensitif, sering ragu mengambil keputusan")
            print("Persentase Populasi: 4–5%")

        case"INTP":
            print("Nama: Ahli Logika")
            print("Karakter: Analitis, ingin tahu, objektif, inovatif")
            print("Kekuatan: Berpikir kritis, kreatif, cepat memahami konsep")
            print("Tantangan: Terlalu banyak berpikir (overthinking), kurang fokus pada tindakan")
            print("Persentase Populasi: 3–5%")

        case"ESTP":
            print("Nama: Pengusaha")
            print("Karakter: Berani, aktif, spontan, percaya diri")
            print("Kekuatan: Cepat bertindak, pandai melihat peluang")
            print("Tantangan: Impulsif, kurang mempertimbangkan risiko jangka panjang")
            print("Persentase Populasi: 4–5%")

        case"ESFP":
            print("Nama: Penghibur")
            print("Karakter: Ramah, ceria, energik, suka bersosialisasi")
            print("Kekuatan: Mudah bergaul, optimis, menghibur orang lain")
            print("Tantangan: Mudah terdistraksi, kurang suka rutinitas")
            print("Persentase Populasi: 8–9%")

        case"ENFP":
            print("Nama: Juru Kampanye")
            print("Karakter: Antusias, kreatif, penuh semangat, komunikatif")
            print("Kekuatan: Menginspirasi, inovatif, mudah membangun hubungan")
            print("Tantangan: Sulit konsisten, mudah bosan dengan rutinitas")
            print("Persentase Populasi: 7–8%")

        case"ENTP":
            print("Nama: Pendebat")
            print("Karakter: Cerdas, kreatif, kritis, suka tantangan")
            print("Kekuatan: Cepat menemukan ide, pandai berdiskusi")
            print("Tantangan: Sering berdebat, kurang memperhatikan detail")
            print("Persentase Populasi: 3–4%")
    
        case"ESTJ":
            print("Nama: Eksekutif")
            print("Karakter: Tegas, terorganisir, realistis, disiplin")
            print("Kekuatan: Pemimpin yang baik, efisien, bertanggung jawab")
            print("Tantangan: Cenderung keras kepala, kurang peka terhadap perasaan orang lain")
            print("Persentase Populasi: 8–9%")

        case"ESFJ":
            print("Nama:  Konsul")
            print("Karakter: Ramah, hangat, peduli, kooperatif")
            print("Kekuatan: Membangun hubungan baik, suka membantu, setia")
            print("Tantangan: Terlalu mencari pengakuan, sensitif terhadap kritik")
            print("Persentase Populasi: 9–12%")

        case"ENFJ":
            print("Nama: Protagonist")
            print("Karakter: Karismatik, peduli, memotivas")
            print("Kekuatan: Pemimpin inspiratif, komunikatif, empatik")
            print("Tantangan: Terlalu mengutamakan orang lain, mudah stres")
            print("Persentase Populasi: 2–3%")

        case"ENTJ":
            print("Nama: Komandan")
            print("Karakter: Ambisius, percaya diri, strategis, tegas")
            print("Kekuatan: Pemimpin visioner, pengambil keputusan yang baik")
            print("Tantangan: Dominan, kurang sabar, sulit menerima kelemahan orang lain")
            print("Persentase populasi: 2–3%")

        case"?":
            print("Hasil tidak bisa ditentukan (skor seimbang di beberapa dimensi).\n Coba mengetik jawaban dengan lebih spontan dan tanpa terlalu lama mempertimbangkan!")

        case _:
            print(f" Tipe '{tipe}' tidak dikenali. Cek apakah ada huruf '?' di hasilmu.")
tampilkan_hasil(tipe_mbti, nama)

