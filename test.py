import streamlit as st
import requests
import pandas as pd
import time

#membuat pilihan menggunakan st.sidebar
option = st.sidebar.selectbox("Menu Utama",["Beranda","Perhitungan Kerapatan Curah","Perhitungan Kerapatan Absolut","Perhitungan Kerapatan Relatif","Tabel Kerapatan Air"])

#jika yang dipilih option beranda
if option == "Beranda":

#tentang kelompok
    st.markdown("<h1 style='text-align: center; color: red;'>APLIKASI PERHITUNGAN KERAPATAN</h1>", unsafe_allow_html=True)
    st.markdown('**---------------------------------------------------------------------------------------------------------------------------------------**')
    st.write('Hallo semua, selamat datang di aplikasi perhitungan kerapatan.')
    st.write('sebelum membahas tentang perhitungan kerapatann, kenalan dulu yu sama pembuat aplikasi nya')
    st.image("photo.jpeg",caption="kenalin kami dari kelompok 1 kelas 1C Analisis Kimia.")

#penjelasan mengenai kerapatan
    st.write("Sebelum mengetahui aplikasi perhitungan kerapatan, perlu diketahui terlebih dahulu apa itu massa jenis. Penting dipahami sebelumnya terkait pengertian dari massa jenis. Nama lain dari massa jenis yaitu densitas atau kerapatan.")
    st.write("Adapun yang dimaksud kerapatan adalah pengukuran massa setiap satuan volume dari suatu objek atau benda. Pengukuran setiap objek ini memiliki massa jenis yang berbeda-beda dan tergantung dari temperatur yang ada.")
    st.write("Penting diketahui bahwa semakin tinggi massa jenis dari benda tersebut maka volume benda juga semakin besar atau dapat dikatakan berbanding lurus dengan volume. Dari konsep massa jenis tersebut dapat disimpulkan jika posisi benda di air akan mempengaruhi massa jenisnya.")
    st.write("Apabila benda tersebut berada di atas permukaan air baik itu dalam keadaan terdorong, terapung, atau terlempar, maka itu menunjukkan bahwa massa jenisnya rendah. Begitu juga sebaliknya apabila benda tersebut berada di dasar, maka massa jenisnya besar.")
    st.write("Lalu bagaimana dengan perhitungan kerapatan?dan bagaimana dengan jenis jenis kerapatan? Mari kita bahas satu per satu.")
    st.write("Kerapatan terbagi menjadi 3 jenis yaitu: kerapatan curah, kerapatan absolut, dan kerapatan relatif berikut penjelasan dari jenis jenis kerapatan serta perhitungannya.")

#penjelasan mengenai jenis kerapatan curah
    st.markdown('<h3 style="color:red;">1. KERAPATAN CURAH</h3>', unsafe_allow_html=True)
    st.write("Kerapatan Curah adalah perbandingan berat bahan terhadap volume yang ditempatinya, termasuk ruang kosong diantaranya butiran bahan. Gelas ukur atau wadah disiapkan kemudian berat wadah ditimbang (W1) dan volume wadah (v).")
    st.image("Screenshot (2).png", caption='rumus kerapatan curah')

#penjelasan mengenai jenis kerapatan absolut
    st.markdown('<h3 style="color:red;">2. KERAPATAN ABSOLUT</h3>', unsafe_allow_html=True)
    st.write("Kerapatan absolut adalah ukuran seberapa padat atau rapat suatu benda atau zat. Ini mengacu pada jumlah massa atau materi yang terkandung dalam suatu volume tertentu.")
    st.image("Screenshot (1).png", caption= 'rumus kerapatan absolut')

#penjelasan mengenai jenis kerapatan rerlatif 
    st.markdown('<h3 style="color:red;">3. KERAPATAN RELATIF</h3>', unsafe_allow_html=True)
    st.write("Kerapatan relatif mengacu pada perbandingan kerapatan suatu zat atau benda terhadap kerapatan zat referensi yang umum digunakan.")
    st.image("Screenshot (3).png", caption= 'rumus kerapatan relatif')
    
#jika yang dipilih option perhitungan kerapatan curah
if option == "Perhitungan Kerapatan Curah":
    st.title("Perhitungan Kerapatan Curah")

#pengguna memasukkan data yang dibutuhkan
    Berat_Wadah_Kosong = st.number_input("Masukkan Berat Wadah Kosong (g)")
    st.write(f"[Berat Wadah Kosong adalah] {Berat_Wadah_Kosong} g")
    Volume_Sampel = st.number_input("Masukkan Volume Sampel (mL)")
    st.write(f"[Volume Sampel adalah] {Volume_Sampel} mL")
    Bobot_gelas_Wadah_Sampel = st.number_input("Masukkan Bobot Wadah dan Sampel(g)",step=1e-6,format="%.4f")
    st.write(f"[Bobot gelas Wadah dan Sampel adalah]{Bobot_gelas_Wadah_Sampel} gram:")
    tombol = st.button("Lihat hasil perhitungan")
    with st.spinner("Memproses hasil..."):
        time.sleep(2)

#perhitungan dimulai bila data sudah di isi
    if tombol:
        nilai_Kerapatan = (Bobot_gelas_air_Sampel) / ((Volume_air_akhir) - (Volume_air_awal)); nilai_Kerapatan = (Bobot_gelas_air_Sampel) / ((Volume_air_akhir) - (Volume_air_awal))
        st.success(f"Nilai Kerapatan Curah adalah {nilai_Kerapatan}g/mL")

#jika yang dipilih option perhitungan kerapatan Absolut
if option == "Perhitungan Kerapatan Absolut":
    st.title("Perhitungan Kerapatan Absolut")

#pengguna memasukkan data yang dibutuhkan
    Volume_air_awal = st.number_input("Masukkan volume awal air (mL)")
    st.write(f"[Volume Awal Air adalah]{Volume_air_awal} mL ")
    Bobot_gelas_air = st.number_input("Masukkan bobot gelas yang berisi air (g)", format="%.4f") 
    st.write(f"[Bobot gelas yang berisi Air adalah]{ Bobot_gelas_air} gram")
    Volume_air_akhir = st.number_input("Masukkan Volume Akhir Air (mL)")
    st.write(f"[Volume Akhir Air adalah]{Volume_air_akhir} mL")
    Bobot_gelas_air_Sampel = st.number_input("Masukkan bobot gelas yang berisi air dan Sampel (g)", format="%.4f")
    st.write(f"[Bobot gelas yang berisi Air dan Sampel adalah] {Bobot_gelas_air_Sampel} gram")
    tombol = st.button("Lihat hasil perhitungan")
    with st.spinner("Memproses hasil..."):
        time.sleep(2)

#perhitungan dimulai bila data sudah di isi
    if tombol:
        nilai_Kerapatan = ((Bobot_gelas_air_Sampel) - (Bobot_gelas_air))/ ((Volume_air_akhir) - (Volume_air_awal))
        st.success(f"Nilai Kerapatan Absolut adalah {nilai_Kerapatan}g/mL")

#jika yang dipilih option perhitungan kerapatan Relatif
if option == "Perhitungan Kerapatan Relatif":
    st.title("Perhitungan Kerapatan Relatif")

#pengguna memasukkan data yang dibutuhkan
    Kerapatan_absolut = st.number_input("Masukkan Kerapatan Absolut (g/mL)")
    st.write(f"[Kerapatan absolut adalah]{Kerapatan_absolut} g/mL")

    Kerapatan_air = st.number_input("Masukkan Kerapatan air pada temperatur dan tekanan yang sama (g/mL)")
    st.info("Kerapatan bisa dilihat pada pilihan menu ** tabel kerapatan air**")
    st.write(f":[Kerapatan air pada temperatur dan tekanan yang sama adalah]{Kerapatan_air} g/mL")
    
    tombol = st.button("Lihat hasil perhitungan")
    with st.spinner("Memproses hasil..."):
        time.sleep(2)

#perhitungan dimulai bila data sudah di isi
    if tombol:
         nilai_Kerapatan = Kerapatan_absolut/Kerapatan_air
         st.success(f"Nilai Kerapatan Absolut adalah {nilai_Kerapatan} g/mL")
    
#jika yang dipilih option tabel kerapatan air
if option == "Tabel Kerapatan Air":

#membuat data frame
    data = {
    "Temperatur": [20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 27.5, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0],
    "Kerapatan air": [0.9982, 0.9980, 0.9978, 0.9976, 0.9973, 0.9971, 0.9968, 0.9965, 0.9964, 0.9963, 0.9960, 0.9957, 0.9954, 0.9951, 0.9947, 0.9944, 0.9941, 0.9937, 0.9934, 0.9930, 0.9026, 0.9922],}
    df = pd.DataFrame(data)

#pembuatan tampilan tabel pada web
    st.write("Tabel Kerapatan Air (g/mL):")
    st.table(df)