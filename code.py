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
name = st.text_input('Név', key='name_input')
address = st.text_input('Cím', key='address_input')
interest = st.text_input('Érdeklődés tárgya', key='interest_input')

# Rendelés tételek
items = []
counter = 0

# Tétel hozzáadása
if st.button(f'Új tétel hozzáadása {counter + 1}', key=f'add_button_{counter}'):
    item_name = st.text_input('Tétel neve', key=f'item_name_{counter}')
    quantity_or_hours = st.number_input('Mennyiség vagy óraszám', min_value=1, value=1, key=f'quantity_or_hours_{counter}')
    unit_type = st.selectbox('Mérték', ['Darab', 'Óra'], key=f'unit_type_{counter}')
    
    # Elrejtjük az egységárat és használjuk a programban meghatározott értéket
    item_price = 1000  # Állítsd be az árat, amit szeretnél
    
    items.append({
        'name': item_name,
        'quantity_or_hours': quantity_or_hours,
        'unit_type': unit_type,
        'price': calculate_price(item_price, quantity_or_hours) if unit_type == 'Darab' else calculate_price(item_price, hours=quantity_or_hours)
    })
    counter += 1

# Tétel törlése
if st.button('Tétel törlése') and items:
    del items[-1]

# Tételek listája
st.markdown('### Tételek')
for idx, item in enumerate(items):
    template = f"""
    **{item['name']}**
    Mennyiség/Óraszám: {item['quantity_or_hours']} {item['unit_type']}
    Ár: {item['price']} Ft
    """
    st.write(template)

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

for idx, item in enumerate(items):
    template += f"""
Ajánlati tétel {idx + 1}: {item['name']}
Mennyiség/Óraszám: {item['quantity_or_hours']} {item['unit_type']}
Összár: {item['price']} Ft
"""

# Ajánlat sablon megjelenítése
st.markdown(f'### Ajánlat Sablon')
st.code(template)
