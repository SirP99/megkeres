import streamlit as st

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
name = st.text_input('Név', '')
address = st.text_input('Cím', '')
interest = st.text_input('Érdeklődés tárgya', '')

# Rendelés tételek
items = []
while st.button('Tétel hozzáadása'):
    item_name = st.text_input('Tétel neve', '')
    quantity = st.number_input('Mennyiség', min_value=1, value=1, key=item_name+'_quantity')
    hours = st.number_input('Óraszám', min_value=1, value=1, key=item_name+'_hours')
    item_price = st.number_input('Egységár', min_value=1, value=1000, key=item_name+'_price')
    items.append({
        'name': item_name,
        'quantity': quantity,
        'hours': hours,
        'price': calculate_price(item_price, quantity, hours)
    })

# Ajánlat generálása
st.markdown(f'### Ajánlat')
st.write(f'Név: {name}')
st.write(f'Cím: {address}')
st.write(f'Érdeklődés tárgya: {interest}')

total_price = sum(item['price'] for item in items)
st.write(f'Összár: {total_price} Ft')

# Szablon generálása
template = f"""
**Ajánlat**

Név: {name}
Cím: {address}
Érdeklődés tárgya: {interest}
"""

for item in items:
    template += f"""
Ajánlati tétel: {item['name']}
Mennyiség: {item['quantity']} db
Óraszám: {item['hours']} óra
Összár: {item['price']} Ft
"""

# Ajánlat sablon megjelenítése
st.markdown(f'### Ajánlat Sablon')
st.code(template)
