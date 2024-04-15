import streamlit as st

# Tétel adatok
items_data = {
    'Mosogatás': {'price': 1000},
    'Asztal': {'price': 1500},
    'Szemétszedés': {'price': 2000}
}

def calculate_price(item_name, quantity=None):
    if item_name not in items_data:
        raise ValueError(f'Invalid item name: {item_name}')

    item_price = items_data[item_name]['price']
    if quantity is not None:
        total_price = item_price * quantity
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
items = st.session_state.get('items', [{'name': 'Mosogatás', 'quantity_or_hours': 1}])

deleted_indices = [False] * len(items)

for idx, item in enumerate(items):
    st.write(f'Tárgy {idx + 1}')
    item['name'] = st.selectbox(f'Válassz egy tárgyat', list(items_data.keys()), index=0 if item['name'] == '' else list(items_data.keys()).index(item['name']), key=f'item_name_{idx}')
    item['quantity_or_hours'] = st.number_input(f'Mennyiség vagy óraszám', min_value=1, value=item['quantity_or_hours'], key=f'quantity_or_hours_{idx}')
    if st.button(f'Törlés {idx + 1}', key=f'delete_button_{idx}'):
        deleted_indices[idx] = True

items = [item for idx, item in enumerate(items) if not deleted_indices[idx]]

if st.button('Hozzáadás'):
    items.append({'name': 'Mosogatás', 'quantity_or_hours': 1})

# Tárgyak frissítése változó
update_items = st.session_state.get('update_items', False)

# Tárgyak frissítése gomb
if st.button('Tárgyak frissítése'):
    st.session_state['update_items'] = True

if update_items:
    st.experimental_rerun()  # Az alkalmazás újraindítása

st.session_state['items'] = items
st.session_state['update_items'] = False

# Ajánlat generálása
total_price = sum(calculate_price(item['name'], item['quantity_or_hours']) for item in items)

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
    price = calculate_price(item['name'], item['quantity_or_hours'])
    template += f"""
Ajánlati tétel {idx + 1}: {item['name']}
Mennyiség/Óraszám: {item['quantity_or_hours']}
Összár: {price} Ft
"""

template += f"""
Végösszeg: {total_price} Ft
"""

# Ajánlat sablon megjelenítése
st.markdown(f'### Ajánlat Sablon')
st.code(template)

st.session_state['update_items'] = True
