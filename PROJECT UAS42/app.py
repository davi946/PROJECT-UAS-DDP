import streamlit as st
from PIL import Image

# Data Soal Quiz
questions = [
    {
        "question": "Apa fungsi utama dari statement 'print' dalam Python?",
        "options": ["Menghapus file", "Menampilkan teks atau output", "Membuat variabel baru", "Menyusun data menjadi list"],
        "answer": "Menampilkan teks atau output"
    },
    {
        "question": "Apa hasil dari operasi len(['Python', 'HTML', 'Math'])?",
        "options": ["2", "3", "4", "Error"],
        "answer": "3"
    },
    {
        "question": "Apa kepanjangan dari HTML?",
        "options": ["Hyperlink Text Language", "Hypertext Markup Language", "Hypermedia Text Layer", "High Text Management Language"],
        "answer": "Hypertext Markup Language"
    },
    {
        "question": "Tag apa yang digunakan untuk membuat heading terbesar di HTML?",
        "options": ["<h1>", "<h6>", "<header>", "<head>"],
        "answer": "<h1>"
    },
    {
        "question": "Berapa hasil dari 25 x 4?",
        "options": ["100", "90", "80", "110"],
        "answer": "100"
    },
]

# Data Dictionary
dictionary_data = {
    "apel": "Apple.",
    "alpukat": "Avocado.",
    "anggur": "Grape.",
    "belimbing": "Star Fruit.",
    "bengkoang": "Jicama.",
    "cermai": "Cherry Blossom.",
    "cokelat": "Chocolate.",
    "ceri": "Cherry.",
    "cranberi": "Cranberry",
    "buah naga": "Dragon Fruit.",
    "duku": "Duku.",
    "durian": "Durian.",
    "delima": "Pomegranate.",
    "elderberry": "Elderberries.",
    "frambos": "Raspberry.",
    "feijoa": "Feijoa.",
    "flamboyan": "Flamboyant.",
    "gandum": "Wheat.",
    "gandaria": "Gandaria.",
    "jambu biji": "Guava.",
    "jambu air": "Water Apple.",
    "jeruk": "Orange.",
    "jagung": "Corn.",
    "kelapa": "Coconut.",
    "kacang": "Peanut.",
    "kelengkeng": "Longan.",
    "kenari": "Canary.",
    "kesemek": "Persimmon.",
    "kentang": "Potato.",
    "kiwi": "Kiwi.",
    "kismis": "Raisins.",
    "kopi": "Coffee.",
    "kolang kaling": "Sugar Palm",
    "kurma": "Date.",
    "labu": "Pumpkin.",
    "lemon": "Lemon.",
    "leci": "Lychee.",
    "limau": "Lime.",
    "mangga": "Mango.",
    "manggis": "Mangosteen.",
    "markisa": "Passion Fruit.",
    "melon": "Honey Dew.",
    "nanas": "Pineapple.",
    "nangka": "Jackfruit.",
    "naga": "Dragon Fruit.",
    "pepaya": "Papaya.",
    "pir": "Pear.",
    "pisang": "Banana.",
    "rambutan": "Rambutan.",
    "salak": "Snakefruit.",
    "sawo": "Sapodilla.",
    "semangka": "Watermelon.",
    "stroberi": "Strawberry.",
    "terong": "Eggplant.",
    "timun": "Cucumber",
    "ubi": "Sweet Potato.",
    "vanili": "Vanilla.",
    "zaitun": "Olive.",
}

# Konfigurasi halaman
st.set_page_config(
    page_title="Aplikasi Pendidikan Kelompok 4",
    page_icon="✨",
    layout="wide"
)

# Tambahkan CSS untuk styling tambahan
st.markdown("""
    <style>
    .main {background-color: #f9f9f9; color: #333;}
    .stSidebar {background-color: rgb(0, 0, 0);}
    .stSidebarContent {color: #000000;} /* Mengubah warna font sidebar menjadi hitam */
    .stButton>button {background-color: #4CAF50; color: white; border: none; padding: 10px 20px; cursor: pointer; transition: 0.3s;}
    .stButton>button:hover {background-color: #45a049;}
    .stTextInput>div>input {border: 2px solid #4CAF50; border-radius: 5px;}
            
    </style>
""", unsafe_allow_html=True)


# Header dengan gambar (opsional)
header_image = Image.open("header.jpg")  # Ganti dengan file gambar yang sesuai
st.image(header_image, use_container_width=True, caption="Aplikasi Sederhana kelompok 4 poenya 🔥")


# Sidebar untuk navigasi
st.sidebar.title("🌟 Menu Navigasi")
menu = st.sidebar.radio(
    "Pilih Halaman:",
    ["🏠 Home", "📝 Quiz", "🧮 Kalkulator", "📚 English Dictionary"],
)

# Tampilan Home
if menu == "🏠 Home":
    st.title("✨ Selamat Datang di Aplikasi Pendidikan")
    st.write("""
    Aplikasi ini dirancang untuk memberikan pengalaman interaktif dengan berbagai fitur menarik:
    - **Quiz** untuk menguji pengetahuan Anda.
    - **Kalkulator** untuk perhitungan sederhana.
    - **English Dictionary** untuk mengetahui nama-nama buah dalam bahasa Inggris.
    
    Gunakan menu di sidebar untuk eksplorasi lebih lanjut yaa! 💡
    """)
    st.image("welcome.jpg", caption="Mari Jelajahi Bersama!", use_container_width=True)
    
#  untuk manggil gambar ya teman teman

# Tampilan Quiz
elif menu == "📝 Quiz":
    st.title("📝 Quiz Interaktif")
    st.write("Uji pengetahuanmu dengan menjawab soal-soal berikut!")

    # Tempat untuk menyimpan jawaban pengguna
    user_answers = {}
    
    # Menampilkan soal-soal quiz
    for i, question in enumerate(questions):
        st.write(f"**{i + 1}. {question['question']}**")
        user_answers[f"q{i}"] = st.radio(
            f"Pilih jawaban untuk soal {i + 1}:", 
            question['options'], 
            key=f"q{i}"
        )

    # Tombol untuk submit jawaban
    if st.button("Kirim Jawaban"):
        score = 0
        lives = 3

        # Mengevaluasi jawaban pengguna
        for i, question in enumerate(questions):
            if user_answers[f"q{i}"] == question["answer"]:
                score += 20
                st.write(f"**Soal {i + 1}: ✅ Jawaban benar!**")
            else:
                lives -= 1
                st.write(f"**Soal {i + 1}: ❌ Jawaban salah.** Jawaban yang benar adalah: **{question['answer']}**")

        # Menampilkan hasil akhir
        st.write(f"**Skor Akhir: {score}**")
        if lives > 0:
            st.success(f"**Sisa Nyawa: {lives}**")
            st.success("Selamat! Kamu telah menyelesaikan quiz 🎉")
        else:
            st.warning("⚠️ Kamu kehabisan nyawa! Tetap semangat belajar!")

            
        


# Tampilan Kalkulator
elif menu == "🧮 Kalkulator":
    st.title("🧮 Kalkulator Sederhana")

    num1 = st.number_input("Masukkan angka pertama:", value=0.0)
    num2 = st.number_input("Masukkan angka kedua:", value=0.0)
    operation = st.selectbox("Pilih operasi matematika:", ["Tambah", "Kurang", "Kali", "Bagi"])

    result = None
    if st.button("Hitung"):
        try:
            if operation == "Tambah":
                result = num1 + num2
            elif operation == "Kurang":
                result = num1 - num2
            elif operation == "Kali":
                result = num1 * num2
            elif operation == "Bagi":
                if num2 == 0:
                    raise ZeroDivisionError("Tidak bisa membagi dengan nol.")
                result = num1 / num2
            st.success(f"Hasil: **{result}**")
        except Exception as e:
            st.error(str(e))

# Tampilan Dictionary
elif menu == "📚 English Dictionary":
    st.title("📚 Kamus Buah Bahasa Inggris Sederhana")

    # Menampilkan daftar buah dalam dropdown
    fruit_list = list(dictionary_data.keys())  # Daftar nama buah
    selected_fruit = st.selectbox("Pilih nama buah dari daftar:", fruit_list)

    # Menampilkan definisi buah yang dipilih
    if st.button("Cari Definisi"):
        definition = dictionary_data.get(selected_fruit.lower(), None)
        if definition:
            st.success(f"**{selected_fruit.capitalize()}**: {definition}")
        else:
            st.error(f"Kata **'{selected_fruit}'** tidak ditemukan dalam kamus.")

