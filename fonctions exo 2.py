def storage (quantity_storage):
    monthly_price = 0
    if quantity_storage == 50:
        monthly_price = 1.30
    elif quantity_storage == 200:
        monthly_price = 4
    elif quantity_storage == 2000:
        monthly_price = 13
    else:
        print ("Erreur, prix non défini.")
        return 0
    return monthly_price

print ("Choisissez la quantité de stockage que vous souhaitez :")
value = int(input())
print(storage(value))