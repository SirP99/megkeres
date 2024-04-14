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
while st.button(f'Tétel hozzáadása {counter + 1}', key=f'add_button_{counter}'):
    item_name = st.text_input('Tétel neve', key=f'item_name_{counter}')
    quantity = st.number_input('Mennyiség', min_value=1, value=1, key=f'quantity_{counter}')
    hours = st.number_input('Óraszám', min_value=1, value=1, key=f'hours_{counter}')
    
    # Elrejtjük az egységárat és használjuk a programban meghatározott értéket
    item_price = 1000  # Állítsd be az árat, amit szeretnél
    
    # Hozzáadás gomb
    if st.button(f'Hozzáadás {counter + 1}', key=f'add_item_{counter}'):
        items.append({
            'name': item_name,
            'quantity': quantity,
            'hours': hours,
            'price': calculate_price(item_price, quantity, hours)
        })
        counter += 1

    st.write(f'Egységár: {item_price} Ft')

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
Mennyiség: {item['quantity']} db
Óraszám: {item['hours']} óra
Összár: {item['price']} Ft
"""

# Ajánlat sablon megjelenítése
st.markdown(f'### Ajánlat Sablon')
st.code(template)
