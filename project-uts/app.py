import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(menu_title=None, options=["Beranda", 'Prediksi', "Prediksi File"], 
        icons=['house-door-fill', 'plus-circle', "file-earmark-plus"], default_index=0)

if(selected == "Beranda"):
    st.write("""
    # :blue[Prediksi] Penyakit Obesitas
    Aplikasi Berbasis Web Untuk Memprediksi Penyakit **Obesitas**. \n
    Data Yang Digunakan Merupakan Data Publik Yang Di Dapat Dari [Kaggle](https://www.kaggle.com/datasets/suleymansulak/obesity-dataset).
    """)
    st.image("obesity2.jpg")

if(selected == "Prediksi"):
    st.title("Kalkulasi :blue[Prediksi]",)
    st.image("calculate.jpg")
    st.radio(
        "Apa jenis kelamin anda?",
        ["laki - laki", "perempuan"],
        index=None
    )
    st.number_input("Berapa usia anda?", min_value=0)
    st.number_input("Berapa tinggi badan anda? (cm)", min_value=0)
    st.radio(
        "Apakah keluarga anda ada yang kelebihan berat badan (obesitas)?",
        ["iya", "tidak"],
        index=None
    )
    st.radio(
        "Apakah anda mengkonsumsi makanan cepat saji?",
        ["iya", "tidak"],
        index=None
    )
    st.radio(
        "Apakah anda mengkonsumsi sayuran?",
        ["jarang", "kadang - kadang", "selalu"],
        index=None
    )
    st.number_input("Berapa kali anda makan dalam sehari?", min_value=0)
    st.radio(
        "Asupan cemilan di antara waktu makan",
        ["jarang", "kadang - kadang", "hampir setiap waktu", "selalu"],
        index=None
    )
    st.radio(
        "Apakah anda merokok?",
        ["iya", "tidak"], 
        index=None
    )
    st.number_input("Berapa liter cairan yang anda konsumsi dalam sehari?", min_value=0.0, value=1.0, step=0.01)
    st.radio(
        "Apakah anda memperhitungkan asupan kalori?",
        ["iya", "tidak"], 
        index=None,
    )
    st.slider(
        "Berapa frekuensi aktivitas fisik anda dalam sehari? (0 = tidak banyak bergerak / 3 = aktivitas tingkat tinggi )", 
        min_value=0.0, 
        max_value=3.0,
         step=0.01
    )
    st.radio(
        "Seberapa sering anda menggunakan gadget?",
        ["antara 0 - 2 jam", "antara 3 - 5 jam", "lebih dari 5 jam"],
        index=None    
    )
    st.radio(
        "Apa alat transportasi yang anda gunakan?",
        ["mobil", "motor", "sepeda", "transportasi umum", "berjalan"],
        index=None    
    )

    if 'clicked' not in st.session_state:
        st.session_state.clicked = False

    def click_button():
        st.session_state.clicked = True

    st.button("Prediksi", on_click=click_button)

    if st.session_state.clicked:
        st.error('Anda Obesitas! Perbaiki Pola Makan Anda Dan Mulailah Untuk Berolahraga')


    

if(selected == "Prediksi File" ):
    st.title("Kalkulasi :blue[Prediksi] Menggunakan File CSV Atau XLSX")
    st.image("calculate.jpg")
    st.file_uploader("Upload File CSV Anda", type=["csv", "xlsx"])


