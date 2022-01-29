# from pytube import Youtube
#
# link = input("Enter URL of the video")
# video = Youtube(link)
# stream = video.streams.get_highest_resolution()
# stream.download()

# friends = ["Jim", "Karen", "Kevin"]
# for index in range(len(friends)):
#     print(friends[index])
# for index in range(5):
#     if index == 0:
#         print("first iteration")
#     else:
#         print("Not first")

# exponent function
# print(2**3)
# def raise_to_power(base_num, power_num):
#     result = 1
#     for index in range(power_num):
#         result = result * base_num
#     return result
#
# print(raise_to_power(3, 49))

# 2d lists
# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
# # print(number_grid[2][1])
#
# for row in number_grid:
#     for col in row:
#         print(col)

# # translator
# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#                 translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation
# print(translate(input("Enter a phrase: ")))

# try:
#     number = int(input("enter a num"))
#     print(number)
# except:
#     print("invalid8")

# person = input("Enter your name here: ")
# age = input("Enter your age here: ")
# output = "{a} is {b} years old".format(a=person, b=age)
# print(output)

# employee_file = open("employee.txt", "r")
# for employee in employee_file.readlines():
#     print(employee)
# # print(employee_file.readlines()[0])
# employee_file.close()

# employee_file = open("index.html", "w")
# # print(employee_file.read())
# employee_file.write("<h1>welcome</h1>")
# employee_file.close()

# def countdown():
#     i = 5
#     while i > 0:
#         yield i
#         i = -1
# for i in countdown():
#     print(i)

# num_1 = int(input("Enter your first nmuber here: "));
# num_2 = int(input("Enter your second number here:   "));
# operator = input("Enter your operator: ");
# if(operator == "+"):
#     print(num_1 + num_2);
# elif(operator == "-"):
#     print(num_1 - num_2);
# else:
#     print("Invalid op");
import percentage as percentage
from instapy import InstaPy

session = InstaPy(username="creed_d_programmer", password="temidayo4")
session.login()
session.like_by_tags(["bmw", "mercedes"], amount=5)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True,percentage=50)
session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
session.end()

