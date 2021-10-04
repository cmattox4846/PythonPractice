# day_of_week = 'Monday'
# print(day_of_week)
# day_of_week = 'Friday'
# print(f"I can't wait until {day_of_week}!")


# animal_input = input('What is your favorite animal?')
# color_input = input('What is your favorite color?')
# print(f"I've never seen a {color_input} {animal_input}")


#**** time of day 
# time_of_day = 1100
# meal_choice = ""
# if time_of_day < 1200: meal_choice = 'Breakfast'

# elif time_of_day > 1200 and time_of_day < 1700: meal_choice = 'Lunch'

# elif time_of_day > 1700: meal_choice = 'Dinner'


# print(meal_choice)


# random Number 
# import random

# number = random.randrange(0,10 +1)

# print(number)
# if number >= 0 and  number < 3:
#     print('Beatles')

# elif number > 2 and  number < 6:
#     print('Stones')

# elif number > 5 and  number < 9:
#     print('Floyd')

# elif number > 8 and  number <= 10:
#     print('Hendrix')

# msg = 'Python is cool!'

# for number in range(7):
#     print(msg)

# for number2 in range(11):
#     print(number2)

# msg_hello = 'Hello'
# msg_goodbye = 'GoodBye'

# for count in range(5):
#     print(msg_hello)
#     print(msg_goodbye)

# height= 40
# while height < 48:
#     print('Cannot Ride!')
#     height += 1

# Magic Number Game 
#import random


# magic_numbers = random.randrange(0,100,+1)
# guess =  0

# print(magic_numbers)
# while guess != magic_numbers:
#     guess = int(input('Please enter your guess!'))
#     if guess > magic_numbers:
#             if guess > (magic_numbers - 10) or guess < magic_numbers: 
#                 print('Getting Warmer') 
#             print('Too Low!')
#     elif guess < magic_numbers:
#         if guess < (magic_numbers + 10) or guess > magic_numbers:
#             print('Getting Warmer!')
#         print('Too High!')
#     elif guess == magic_numbers:
#         print(f'{guess} is the correct number!')  



# def print_movie_name():
#     Fav_movie = 'Casino'
#     print(Fav_movie)

# print_movie_name()


# def favorite_band ():
#     band_name_input = input('Please enter your favorite band name')
#     return band_name_input

# band_results = favorite_band()

# print(band_results)

# def concert_display(musical_act):
#     my_street = input("Please enter the street you live on")
#     print(f'It would be great if {musical_act} played a show on {my_street}')

# concert_display("Zac Brown Band")

desktop_items = ['desk', 'lamp', 'pencil']
#print(desktop_items[1])

desktop_items.append('Infinity Gauntlet')

#print(desktop_items[3])

for items in desktop_items:
    print(items)