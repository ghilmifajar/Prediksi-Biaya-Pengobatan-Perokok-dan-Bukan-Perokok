import pickle
import streamlit as st

# load save model
smoker_model = pickle.load(open('insurance_model.sav', 'rb'))

# Judul Untuk Web
st.title('Prediksi Biaya Pengobatan Perokok dan Bukan Perokok')
st.text('Nama : Ghilmi Fajar')
st.text('Nim : 191351151')
st.text('Matkul : Business Intelligence')

# Form Input
age = st.text_input('Masukan Umur')

sex = st.text_input('Masukan Jenis Kelamin')

bmi = st.text_input('Masukan nilai indeks masa tubuh')

children = st.text_input('Masukan Jumlah anak yang ditanggung asuransi kesehatan')

smoker = st.text_input('Masukan status perokok atau tidak perokok')



# kode Prediksi
smoker_analisis =''

#Button Prediksi
if st.button('Prediksi Biaya'):
    smoker_prediction = smoker_model.predict([[age, sex, bmi, children, smoker]])

    if(smoker_prediction[0]==0):
       smoker_analisis = 'Biaya Rendah'
    else:
       smoker_analisis = 'Biaya Tinggi'
st.success(smoker_analisis)