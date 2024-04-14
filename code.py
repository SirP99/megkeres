import streamlit as st

# Tétel adatok
items_data = {
    'Tétel 1': {'price': 1000},
    'Tétel 2': {'price': 1500},
    'Tétel 3': {'price': 2000}
}

def calculate_price(item_price, quantity=None, hours=None):
    if quantity is not None and hours is not None:
        total_price = item_price * quantity * hours
    elif quantity is not None:
        total_price = item_price * quantity
    elif hours is not None:
        total_price = item_price * hours
    else:
        total_price = item_price
    return total_price

# Streamlit alkalmazás felépítése
st.title('Árajánlat Készítő App')

# Adatbeviteli mezők
name = st.text_input('Név', key='name_input')
address = st.text_input('Cím', key='address_input')
interest = st.text_input('Érdeklődés tárgya', key='interest_input')

# Tétel választó legördülő menü
selected_item = st.selectbox('Válassz egy tételt', list(items_data.keys()))

# Mennyiség/Óraszám mező
quantity_or_hours = st.number_input('Mennyiség vagy óraszám', min_value=1, value=1)

# Ár kiszámítása a kiválasztott tételhez
item_price = items_data[selected_item]['price']
price = calculate_price(item_price, quantity_or_hours)

# Ajánlat generálása
st.markdown(f'### Ajánlat')
st.write(f'Név: {name}')
st.write(f'Cím: {address}')
st.write(f'Érdeklődés tárgya: {interest}')
st.write(f'Összár: {price} Ft')

# Szablon generálása
template = f"""
**Ajánlat**

Név: {name}
Cím: {address}
Érdeklődés tárgya: {interest}
Ajánlati tétel: {selected_item}
Mennyiség/Óraszám: {quantity_or_hours} {items_data[selected_item]['unit']}
Összár: {price} Ft
"""

# Ajánlat sablon megjelenítése
st.markdown(f'### Ajánlat Sablon')
st.code(template)
