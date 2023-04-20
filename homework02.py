ice_cream_assortment = {'Сливочное', 'Бурёнка', 'Вафелька', 'Сладкоежка'}
ice_cream_stock = {'Сливочное', 'Вафелька', 'Сладкоежка'}
result = ice_cream_assortment.difference(ice_cream_stock)
print(f'Закончилось: {result}')