import streamlit as st
import pdfkit

def calculate_price(item_price, quantity, hours):
    total_price = item_price * quantity * hours
    return total_price

# Streamlit alkalmazás felépítése
st.title('Árajánlat Készítő App')

# Adatbeviteli mezők
name = st.text_input('Név', '')
address = st.text_input('Cím', '')
interest = st.text_input('Érdeklődés tárgya', '')

# Legördülő menük az ajánlati tételekhez
item = st.selectbox('Ajánlati tétel', ['Tétel 1', 'Tétel 2', 'Tétel 3'])
quantity = st.number_input('Mennyiség', min_value=1, value=1)
hours = st.number_input('Óraszám', min_value=1, value=1)

# Árak számítása
item_price = st.number_input('Egységár', min_value=1, value=1000)
total_price = calculate_price(item_price, quantity, hours)

# Ajánlat generálása
st.markdown(f'### Ajánlat')
st.write(f'Név: {name}')
st.write(f'Cím: {address}')
st.write(f'Érdeklődés tárgya: {interest}')
st.write(f'Ajánlati tétel: {item}')
st.write(f'Mennyiség: {quantity}')
st.write(f'Óraszám: {hours}')
st.write(f'Összár: {total_price} Ft')

# Szablon generálása
template = f"""
**Ajánlat**

Név: {name}
Cím: {address}
Érdeklődés tárgya: {interest}

Ajánlati tétel: {item}
Mennyiség: {quantity}
Óraszám: {hours}
Összár: {total_price} Ft
"""

st.markdown(f'### Ajánlat Sablon')
st.code(template)

if st.button('PDF Letöltése'):
    generate_pdf(template, 'ajanlat.pdf')
    st.success('PDF sikeresen létrehozva! Kattints a linkre a letöltéshez.')
    st.markdown('[ajanlat.pdf letöltése](./ajanlat.pdf)', unsafe_allow_html=True)
