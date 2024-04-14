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
items = st.session_state.get('items', [{'name': '', 'quantity_or_hours': 1}])
for idx, item in enumerate(items):
    item['name'] = st.selectbox(f'Tétel {idx + 1}', list(items_data.keys()), index=0 if item['name'] == '' else list(items_data.keys()).index(item['name']))
    item['quantity_or_hours'] = st.number_input(f'Mennyiség vagy óraszám {idx + 1}', min_value=1, value=item['quantity_or_hours'])

if st.button('+'):
    items.append({'name': '', 'quantity_or_hours': 1})

st.session_state['items'] = items

# Ajánlat generálása
total_price = sum(calculate_price(items_data[item['name']]['price'], item['quantity_or_hours']) for item in items)

st.markdown(f'### Ajánlat')
st.write(f'Név: {name}')
st.write(f'Cím: {address}')
st.write(f'Érdeklődés tárgya: {interest}')
st.write(f'Összár: {total_price} Ft')

# Szablon generálása
template = f"""
**Ajánlat**

Név: {name}
Cím: {address}
Érdeklődés tárgya: {interest}
"""

for idx, item in enumerate(items):
    price = calculate_price(items_data[item['name']]['price'], item['quantity_or_hours'])
    template += f"""
Ajánlati tétel {idx + 1}: {item['name']}
Mennyiség/Óraszám: {item['quantity_or_hours']}
Összár: {price} Ft
"""

# Ajánlat sablon megjelenítése
st.markdown(f'### Ajánlat Sablon')
st.code(template)
