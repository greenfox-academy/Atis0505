shop_items = ["Cupcake", 2, "Brownie", false]

# Accidentally we added "2" and "false" to the list. 
# Your task is to change from "2" to "Croissant" and change from "false" 
# to "Ice cream"
# No, don't just remove the items :)

for n in shop_items:
    if n is 2:
        shop_items[n] = "Croissant"
    elif str(n) == 'false':
        shop_items[n] = "Ice cream"
print(shop_items)