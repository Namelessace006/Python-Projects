# # # username = futwk03856
# # # password = cpdrn7
# import re
#
# intro = "I am Eniiyi Bishop Ajala, a 300 level Computer Science student of Landmark University"
# name = "Eniiyi Bishop Ajala"
# print(name.split())
#
# print(name.replace("Bishop", "Oluwadamilola"))
# search = re.search(name, intro)
# print(search)
# if search:
#     print("Match Found")
#     print(intro.find(name))
#     print(intro[5:24])
# else:
#     print("No Matches Found")
#
# # Consider the variable d use slicing to print out the first three elements:
# d = "ABCDEFG"
# print(d[0:3])
#
# # Use a stride value of 2 to print out every second character of the string e:
# e = 'clocrkr1e1c1t'
# print(e[::2])
#
# # Print out a backslash:
# print("This is a backlash \\ ")
#
# # Convert the variable f to uppercase:
# f = "You are wrong"
# print(f.upper())
#
# # Convert the variable f2 to lowercase:
# f2 = "YOU ARE RIGHT"
# print(f2.lower())
#
# # Consider the variable g, and find the first index of the sub-string snow:
# g = """Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
# Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
# Everywhere that Mary went The lamb was sure to go"""
# print(g.find("snow"))
#
# # In the variable g, replace the sub-string Mary with Bob:
# print(g.replace("Mary", "Bob"))
#
# # In the variable g, replace the sub-string , with .:
# print(g.replace(",", "."))
#
# # In the variable g, split the substring to list:
# print(g.split())
#
# # In the string s3, find whether the digit is present or not using the \d and search() function:
# s3 = "House number- 1105"
# ss3 = re.search("\d", s3)
# if ss3:
#     print("Match Found!")
# else:
#     print("No Matches Found.")
#
# # In the string str1, replace the sub-string fox with bear using sub() function:
# str1 = "The quick brown fox jumps over the lazy dog."
# print(str1.replace("fox", "bear"))
#
# # In the string str2 find all the occurrences of woo using findall() function:
# str2 = "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
# string2 = re.findall("woo", str2)
# print(string2)
#
# genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
#                 "R&B", "progressive rock", "disco")
#
# # Find the length of the tuple, genres_tuple:
# print(len(genres_tuple))
#
# # Access the element, with respect to index 3:
# print(genres_tuple[0:3])
#
# # Use slicing to obtain indexes 3, 4 and 5:
# print(genres_tuple[3:6])
#
# # Find the first two elements of the tuple genres_tuple:
# print(genres_tuple[0:2])
#
# # Find the index of 's' in "disco":
# print(genres_tuple)
# print(f"The Indexing of 's' in disco is {genres_tuple[-1][2]}")
#
# # Generate a sorted List from the Tuple C_tuple=(-5, 1, -3):
# C_tuple = (-5, 1, -3)
# print(sorted(C_tuple))
#
# Dictionary = {"I": 1, "Am": 2, "A": 3, "Boy": 4}
# print(Dictionary["I"])
#
# release_year_dict = {"Thriller": "1982", "Back in Black": "1980",
#                      "The Dark Side of the Moon": "1973",
#                      "The Bodyguard": "1992",
#                      "Bat Out of Hell": "1977",
#                      "Their Greatest Hits (1971-1975)": "1976",
#                      "Saturday Night Fever": "1977",
#                      "Rumours": "1977"}
# print(release_year_dict["The Dark Side of the Moon"])
# print(release_year_dict.keys())
# print(release_year_dict.values())
# release_year_dict["Graduation"] = 2019
# print(release_year_dict)
# print(release_year_dict.values())
# del (release_year_dict["The Dark Side of the Moon"])
# del (release_year_dict["Graduation"])
# del (release_year_dict["The Bodyguard"])
# print(release_year_dict.values())
# print(release_year_dict.keys())
# print("Graduation" in release_year_dict)
#
# soundtrack_dic = {"The Bodyguard": "1992", "Saturday Night Fever": "1977"}
# print(soundtrack_dic)
#
# # a) In the dictionary soundtrack_dic what are the keys ?
# print(f"The Keys are: {soundtrack_dic.keys()}")
#
# # b) In the dictionary soundtrack_dic what are the values ?
# print(f"The Values are: {soundtrack_dic.values()}")
#
# # The Albums Back in Black, The Bodyguard and Thriller have the following
# # music recording sales in millions 50, 50 and 65 respectively:
# # a) Create a dictionary album_sales_dict where the keys are the album
# # name and the sales in millions are the values.
# album_sales_dict = {"The Albums Back in Black": 50, "The Bodyguard": 50, "Thriller": 65}
#
# # b) Use the dictionary to find the total sales of Thriller:
# print(f"The total sales of Thriller: {album_sales_dict["Thriller"]}")
#
# # c) Find the names of the albums from the dictionary using the method keys():
# print(f"The name of the albums are: {album_sales_dict.keys()}")
#
# # d) Find the values of the recording sales from the dictionary using the method values:
# print(f"The values of the recordings are: {album_sales_dict.values()}")
#
# # Scenario:Inventory Store
# # The inventory store scenario project utilizes a dictionary-based
# # approach to develop a robust system for managing and tracking
# # inventory in a retail store.
# # Note:- You will be working with two product details.
#
# # Task-1 Create an empty dictionary
# # First you need to create an empty dictionary, where you will be storing the product details.
# Store = {}
#
# # Task-2 Store the first product details in variable
# # Product Name= Mobile phone
# # Product Quantity= 5
# # Product price= 20000
# # Product Release Year= 2020
# Product1_Name = "Mobile Phone"
# Product1_Quantity = 5
# Product1_Price = 20000
# Product1_ReleaseYear = 2020
#
# # Task-3 Add the details in inventory
# Store["Product1_Name"] = Product1_Name
# Store["Product1_Quantity"] = Product1_Quantity
# Store["Product1_Price"] = Product1_Price
# Store["Product1_ReleaseYear"] = Product1_ReleaseYear
# print(Store)
#
# # Task-4 Store the second product details in a variable.
# # Product Name= "Laptop"
# # Product Quantity= 10
# # Product price = 50000
# # Product Release Year= 2023
# Product2_Name = "Laptop"
# Product2_Quantity = 10
# Product2_Price = 50000
# Product2_ReleaseYear = 2023
#
# # Task-5 Add the item detail into the inventory.
# Store["Product2_Name"] = Product2_Name
# Store["Product2_Quantity"] = Product2_Quantity
# Store["Product2_Price"] = Product2_Price
# Store["Product2_ReleaseYear"] = Product2_ReleaseYear
# print(Store)
#
# # Task-6 Display the Products present in the inventory
# # Use print statement for displaying the products
# print(Store)
#
# # Task-7 Check if ProductNo1_releaseYear and ProductNo2_releaseYear is in the inventory
# print("Product1_ReleaseYear" and "Product2_ReleaseYear" in Store)
#
# # Task-8 Delete release year of both the products from the inventory
# del (Store["Product1_ReleaseYear"])
# del (Store["Product2_ReleaseYear"])
#
# print(Store)
#
# # Convert the list ['rap','house','electronic music', 'rap'] to a set:
# list = ['rap','house','electronic music', 'rap']
# list_set = set(list)
# print(list_set)
#
# # Consider the list A = [1, 2, 2, 1] and set B = set([1, 2, 2, 1]), does sum(A) == sum(B)?
# A = [1, 2, 2, 1]
# B = set([1, 2, 2, 1])
# print(sum(A) == sum(B))
#
#
# # Create a new set album_set3 that is the union of album_set1 and album_set2:
# album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
# album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
# album_set3 = album_set1.union(album_set2)
# print(album_set3)
#
# # Find out if album_set1 is a subset of album_set3:
# print(album_set1.issubset(album_set3))
#
#
# # Write an if statement to determine if an album had a rating greater than 8.
# # Test it using the rating for the album “Back in Black” that had a rating of 8.5.
# # If the statement is true print "This album is Amazing!"
# rating = 8.5
# print("Checking...0%")
# if rating > 8:
#     print("This Album is Amazing")
#
# print("Check Complete...100%")
#
#
# # Write an if-else statement that performs the following. If the rating is
# # larger than eight print “this album is amazing”. If the rating is less
# # than or equal to 8 print “this album is ok”.
# print("Checking...0%")
# if rating > 8:
#     print("This Album is Amazing")
# else:
#     print("This Album is Ok")
#
# print("Check Complete...100%")
#
#
# # Write an if statement to determine if an album came out before 1980 or
# # in the years: 1991 or 1993. If the condition is true print out the year
# # the album came out.
#
# AlbumRelease = 2023
# print("Checking...0%")
# if AlbumRelease < 1980 or AlbumRelease == 1991 or AlbumRelease == 1993:
#     print(AlbumRelease)
# else:
#     print("Not in range")
#
# print("Checking Complete...100%")
#
#
# # Write a for loop that prints out all the elements between -5 and 5
# # using the range function.
# for i in range(-5, 5):
#     print(i)
#
# # Print the elements of the following list:
# # Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'].
# # Make sure you follow Python conventions.
# Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
# print(Genres)
# for i in Genres:
#     print(i)
#
# # Write a for loop that prints out the following list:
# # squares=['red', 'yellow', 'green', 'purple', 'blue']
# squares=['red', 'yellow', 'green', 'purple', 'blue']
# for i in squares:
#     print(squares)
#
# # Write a while loop to display the values of the Rating of an album
# # playlist stored in the PlayListRatings list. If the score is less than 6,
# # exit the loop. The list PlayListRatings is given by:
# # PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
# PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
# i = 0
# Rating_ = PlayListRatings[i]
# P = i < len(PlayListRatings)
#
# while Rating_ >= 6 and P:
#     print(Rating_)
#     i += 1
#     Rating_ = PlayListRatings[i]
#     i += 1
#
#
# # Write a while loop to copy the strings 'orange' of the list squares to
# # the list new_squares. Stop and exit the loop if the value on the list
# # is not 'orange':
# squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
# new_squares = []
# i = 0
# S = len(squares)
#
# while i < S and squares[i] == "orange":
#     new_squares.append(squares[i])
# print(new_squares)
# exit()


# i = 0
# while i < 10:
#     i += 1
#     print(i)
#
# print("\n")
#
# nest = 5
# for i in range(1, nest + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print("")
#
# print("\n")
#
# num = 10
# n = 0
# for i in range(1, num + 1):
#     n += i
#     print(n)
# print(f"The Sum of all numbers within range {num} is {n}")
#
# print("\n")
#
# num = 2
# n = 0
# for i in range(1, 11):
#     n += 1
#     num = num * i
#     print(num)
#     num = 2
#
# print("\n")
#
# numbers_ = [12, 75, 150, 180, 145, 525, 50]
# new_numbers = []
#
# for i in numbers_:
#     if i % 5 == 0:
#         if i > 150:
#             if i > 500:
#                 break
#             else:
#                 continue
#         print(i)
#
# print("\n")
#
# counter = 12345
# count = 0
#
# while counter != 0:
#     counter //= 10
#     count += 1
#     print(counter)
# print(count)
#
#
# list = [10, 20, 30, 40, 50]
# List = len(list) - 1

# num1 = int(input("Number1: "))
# num2 = int(input("Number2: "))
# if num1 * num2 < 1000:
#     prod = num1 * num2
#     print(f"{num1} x {num2} = {prod}")
# else:
#     print("The product of these two numbers is greater than 1000.")
#
# string = "pynative"
# print(string[::2])


def digit_check(n):
    if len(n) >= 2:
        return n[0] == n[-1]

    else:
        return False


num_x = [10, 20, 30, 40, 10]
num_y = [75, 65, 35, 75, 30]

print(digit_check(num_x))
print(digit_check(num_y))