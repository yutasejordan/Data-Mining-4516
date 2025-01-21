import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# convert inputan string ke int
gender_mapping = {'Laki-laki': 1, 'Perempuan': 2}
families_obese_mapping = {'Iya': 1, 'Tidak': 2}
consumption_fastfood_mapping = {'Iya': 1, 'Tidak': 2}
consuming_vegetables_mapping = {'Jarang': 1, 'Kadang - Kadang': 2, "Selalu": 3}
meals_daily_mapping = {'1-2 kali': 1, '3 kali': 2, "3 kali lebih": 3}
snack_mapping = {'Jarang': 1, 'Kadang-Kadang': 2,
                 "Hampir Setiap Waktu": 3, "Selalu": 4}
smoking_mapping = {'Iya': 1, 'Tidak': 2}
liquid_intake_mapping = {"Kurang dari 1 liter": 1,
                         "Antara 1-2 liter": 2, "Lebih dari 2 liter": 3}
calculation_calory_mapping = {"Iya": 1, "Tidak": 2}
physical_exercise_mapping = {"Tidak": 1,
                             "1 - 2 hari": 2, "3 - 4 hari": 3, "5 - 6 hari": 4, "lebih dari 6 hari": 5}
gadget_mapping = {"antara 0 - 2 jam": 1,
                  "antara 3 - 5 jam": 2, "lebih dari 5 jam": 3}
transportation_mapping = {"mobil": 1, "motor": 2,
                          "sepeda": 3, "transportasi umum": 4, "berjalan": 5}


# panggil model
obesitas_model = pickle.load(open("./knn_model.sav", "rb"))
scaler = pickle.load(open("./scaler.sav", "rb"))


# sidebar
with st.sidebar:
    selected = option_menu(menu_title=None, options=["Beranda", 'Prediksi'],
                           icons=['house-door-fill', 'plus-circle'], default_index=0)

# halaman beranda
if (selected == "Beranda"):
    st.write("""
        # :blue[Prediksi] Penyakit Obesitas
        Aplikasi Berbasis Web Untuk Memprediksi Penyakit **Obesitas**. \n
        Data Yang Digunakan Merupakan Data Publik Yang Di Dapat Dari [Kaggle](https://www.kaggle.com/datasets/suleymansulak/obesity-dataset).
        """)
    st.image("./img/obesity2.jpg")


# halaman prediksi
if (selected == "Prediksi"):
    st.title("Kalkulasi :blue[Prediksi]",)
    st.image("./img/calculate.jpg")

    sexInput = st.selectbox(
        "Pilih Gender", options=list(gender_mapping.keys()))
    Sex = gender_mapping[sexInput]

    Age = st.slider("Input Umur", 18, 60)

    Height = st.slider("Input Tinggi Badan (cm)", 150, 200)

    Overweight_Obese_Family_Input = st.selectbox(
        "Apakah keluarga anda ada yang kelebihan berat badan (obesitas)?", options=list(families_obese_mapping.keys()))
    Overweight_Obese_Family = families_obese_mapping[Overweight_Obese_Family_Input]

    Consumption_of_Fast_Food_Input = st.selectbox(
        "Apakah anda mengonsumsi makanan cepat saji?", options=list(consumption_fastfood_mapping.keys()))
    Consumption_of_Fast_Food = consumption_fastfood_mapping[Consumption_of_Fast_Food_Input]

    Frequency_of_Consuming_Vegetables_Input = st.selectbox(
        "Apakah anda mengonsumsi sayuran?", options=list(consuming_vegetables_mapping.keys()))
    Frequency_of_Consuming_Vegetables = consuming_vegetables_mapping[
        Frequency_of_Consuming_Vegetables_Input]

    Number_of_Main_Meals_Daily_Input = st.selectbox(
        "Berapa kali anda makan dalam sehari?", options=list(meals_daily_mapping.keys()))
    Number_of_Main_Meals_Daily = meals_daily_mapping[Number_of_Main_Meals_Daily_Input]

    Food_Intake_Between_Meals_Input = st.selectbox(
        "Asupan cemilan?", options=list(snack_mapping.keys()))
    Food_Intake_Between_Meals = snack_mapping[Food_Intake_Between_Meals_Input]

    Smoking_Input = st.selectbox(
        "Apakah anda merokok?", options=list(smoking_mapping.keys()))
    Smoking = smoking_mapping[Smoking_Input]

    Liquid_Intake_Daily_Input = st.selectbox(
        "Berapa liter air yang anda konsumsi? (hari)", options=list(liquid_intake_mapping.keys()))
    Liquid_Intake_Daily = liquid_intake_mapping[Liquid_Intake_Daily_Input]

    Calculation_of_Calorie_Intake_Input = st.selectbox(
        "Apakah anda memperhitungkan asupan kalori?", options=list(calculation_calory_mapping.keys()))
    Calculation_of_Calorie_Intake = calculation_calory_mapping[
        Calculation_of_Calorie_Intake_Input]

    Physical_Excercise_Input = st.selectbox(
        "Latihan fisik per minggu?", options=list(physical_exercise_mapping.keys()))
    Physical_Excercise = physical_exercise_mapping[Physical_Excercise_Input]

    Schedule_Dedicated_to_Technology_Input = st.selectbox(
        "Seberapa sering anda menggunakan gadger dalam sehari?", options=list(gadget_mapping.keys()))
    Schedule_Dedicated_to_Technology = gadget_mapping[Schedule_Dedicated_to_Technology_Input]

    Type_of_Transportation_Used_Input = st.selectbox(
        "Alat transportasi yang anda gunakan?", options=list(transportation_mapping.keys()))
    Type_of_Transportation_Used = transportation_mapping[Type_of_Transportation_Used_Input]

    obes_diagnosis = ""

    if st.button("Tes Prediksi Obesitas"):
        input_data = (Sex, Age, Height, Overweight_Obese_Family,
                      Consumption_of_Fast_Food, Frequency_of_Consuming_Vegetables,
                      Number_of_Main_Meals_Daily, Food_Intake_Between_Meals,
                      Smoking, Liquid_Intake_Daily, Calculation_of_Calorie_Intake,
                      Physical_Excercise, Schedule_Dedicated_to_Technology,
                      Type_of_Transportation_Used)

        input_data_as_array = np.array(input_data)
        input_data_reshape = input_data_as_array.reshape(1, -1)
        std_data = scaler.transform(input_data_reshape)

        obes_prediction = obesitas_model.predict(std_data)

        if (obes_prediction[0] == 1):
            obes_diagnosis = "Berat badan anda kurang!!!"
        elif (obes_prediction[0] == 2):
            obes_diagnosis = "Berat badan anda normal!"
        elif (obes_prediction[0] == 3):
            obes_diagnosis = "Berat badan anda berlebihan!"
        elif (obes_prediction[0] == 4):
            obes_diagnosis = "ANDAA OBESITASS!!!"

        if (obes_prediction[0] == 1):
            st.warning(obes_diagnosis)
        elif (obes_prediction[0] == 2):
            st.success(obes_diagnosis)
        elif (obes_prediction[0] == 3):
            st.warning(obes_diagnosis)
        elif (obes_prediction[0] == 4):
            st.error(obes_diagnosis)
