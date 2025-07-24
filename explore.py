
'''first_fav_color = "Blue"
second_fav_color = "Black"
third_fav_color = "Pink"
fourth_fav_color = "Gray"
fifth_fav_color = "Green"

print(first_fav_color)
print(secondv_color)


country1 = "Aus"
country2 = "Malawi"
country3 = "Russia"
country4 = "Nigeria"
country5 = "Usa"
country6 = "Iran"

# A LIST IS A COLLECTION OF ITEMS IN A PARTICULAR ODER
#COUNTRY = []
#COUNTRY = LIST()  IS MOSTLY FOR CONVERTION 

countries = ["Aus", "Malawi","Russia","Nigeria","Usa","Iran"]
print(countries)

fav_movies = ["Home Alone", "JohnWick", "Fast and furious","game of throne","Mufasa","Head of State","Shoot them up"]
print(fav_movies)

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number[:11]
print(number)

mixed_list = ["Victor", 20, False, "Male", 17.2, "Green"]
print(mixed_list)

list_provision = ["Garri", "Sugar", "Cabin", "Milk", "Cornflex"]
print(list_provision)

andriod_phone = ["Samsung", "Techno", "Itel", "Redmi", "Oppo"]

ios = ["11-pro-max", "15-pro", "Xr", "16 Plus", "7-Plus"]
phones = [andriod, ios]

print(phones)
'''
'''
code_letter = ["X", "H", "e", "z", "l", "l", "!", "p", "o", "-", "n", "", "W","r", "@", "d", "o", "#"]
h = code_letter[1]
e = code_letter[2]
l = code_letter[4]
l = code_letter[5]
o = code_letter[8]
print(h+e+l+l+o)

w = code_letter[12]
o = code_letter[8]
r = code_letter[13]
l = code_letter[4]
d = code_letter[15]
print(w+o+r+l+d)
print(code_letter[::-1])
'''
'''
grid = [["The", "sky", "is"],["full", "of", "stars"],["shining", "bright", "tonight"]]
t = grid[0][0]
s = grid[0][1]
print(t,s)

stars = grid[0][0]
sta = grid[1][2]
shin = grid[2][0]
print(stars,sta,shin, "are",sh)

reverse = grid[1][::-1]
print(reverse)
'''
'''
fav_fruits = ["Mango", "Apple", "Orange", "Kiwi", "Banana"]
print("Before update>>>>>")
print(fav_fruits)
fav_fruits[0] = "Coco-nut"
print("New update>>>>>>>>>")
print(fav_fruits)
fav_fruits.append("Mango")
fav_fruits.append("Straw-berry")
print(fav_fruits)

fav_fruits.insert(1


playlist = ["Song A", "Song B", "Song C"]
playlist[1] = "Song D"
print(playlist)
playlist.append("Song E")
print(playlist)
playlist.insert(0, "Intro")
print(playlist)
'''
'''
#PROMPTING STUDENT TO ENTER THERE NAME
desk = []
first_name =input("Enter your name: ")
desk.append(first_name)
print(desk)
second_name = input("Enter your name: ")
desk.append(second_name)
print(desk)
third_name = input("Enter your name: ")
desk.append(third_name)
print(desk)

#PROMPTING STUDENT TO ENTER NAME TO BE REPLACE
replace_name = input("Enter your name: ")
desk[1] = replace_name
print(desk)

#PROMPTING STUDENT THAT WALK IN AND WANT TO BE SITTED BETWEEN FIRST AND SECOND SIT
walk_in = input("Enter your name: ")
desk.insert(1, walk_in)
print(desk)


fav_countries = ["spain", "Malawi", "Iran", "Usa"]
print(fav_countries)
fav_countries.remove("Iran")
print(fav_countries)`
'''

acounts = [["1001", "Joy", "Savings", 1500],["1002", "David","Current", 2000],["1003", "Ruth", "Savings", 1800]]
acounts.remove(acounts[1])
print(acounts)

name, acount_type = acount[1][1:3]
print(name)
print(acount_type)

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList's length:", len(numbers))  # Printing previous list length.

###

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.

###

