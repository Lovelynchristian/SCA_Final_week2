buffet_restaurant = ('rice', 'beans', 'yam', 'indomie')
print("Buffet-style restaurant offers:")
for i in buffet_restaurant:
    print(i)
    
buffet_restaurant[0] = ('spaghetti')

buffet_restaurant = ('rice', 'beans', 'yam', 'indomie')
print("Original Buffet-style restaurant offers:")
for i in buffet_restaurant:
    print(i)

buffet_restaurant = ('spaghetti', 'Egusi', 'yam', 'indomie')
print("\nModified Buffet-style restaurant offers:")
for i in buffet_restaurant:
    print(i)