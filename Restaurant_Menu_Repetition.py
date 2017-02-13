print "Welcome to your menu program"

menu = {}

while True:
    dish = raw_input("Enter name of dish: ")
    price = raw_input("Enter price of dish: ")
    menu[dish] = price

    end = raw_input("Do you want to add another dish? (y/n)")

    if end == "n":
        break

print "Our daily menu: "
for item in menu:
    print item + "........" + price

with open("menu.txt", "w+") as menu_file:
    for dish in menu:
        menu_file.write("%s, %s Eur\n" % (dish, menu[dish]))

print "Goodbye!"