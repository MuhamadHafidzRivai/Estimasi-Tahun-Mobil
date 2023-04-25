import pickle
import streamlit as st

model = pickle .load(open('estimasi_mobil.sav','rb'))

st.title('Estimasi Tahun Mobil')

Selling_price = st.number_imput('Input Harga Mobil')
Owner = st.number_input('Input Owner Mobil')
Present_Price = st.number('Input Harga Sekarang')
Kms_Driven = st.number('Input Jarak Tempuh')

predict = ''

if st.button('Estimasi Tahun'):
    predict = model.predict(
        [[Selling_price,Owner,Present_Price,Kms_Driven]]
    )
    st.write ('Estimasi Tahun Mobil dalam Ponds :', predict)
