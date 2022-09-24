#!/usr/bin/env python3

import random

NAMES = ["Janice", "Fiona", "Arthur", "Brody", "Connor", "Katie", "Megan", "Laura", "Muhammad", "Paul"]
q_array = ["LIBRARY", "WIFI", "DEADLINE", "HOLIDAY", "CANTEEN", "EXAM"]
a_array = ["The library is closed today.", "WiFi is excellent across the campus.",
           "Your deadline has been extended by two working days.",
           "Campus is next closed for the holiday period on the 17th of December and reopens on the 4th of January.",
           "The canteen serves food from 12pm to 2pm Monday to Friday.",
           "An exam timetable will be sent to your Poppleton email address in the next week."]
responses = ["Hmmm.", "Yes.", "Tell me more.", "Very nice.", "Oh dear.", "That sounds good.", "Indeed."]


def welcome():
    print("Welcome to Pop Chat")
    print("One of our operators will be pleased to help you today.")
    print("")
    email_check()


def email_check():
    user_email = input("Please enter your Poppleton email address: ")
    if user_email == "":
        print("Please enter an email.")
        email_check()
    counter = user_email.count('@')
    if counter != 1 or len(user_email.split('@')[0]) < 2 or user_email.split('@')[1] != "pop.ac.uk":
        print(user_email, "isn't valid at pop.ac.uk. Please try again.")
        email_check()
    else:
        print(f'Hi, {user_email.split("@")[0].capitalize()}! Thank you, and Welcome to PopChat!')
        print(f'My name is {random.choice(NAMES)}, and it will be my pleasure to help you.')
        question()
        print("")
        print(f'Thanks, {user_email.split("@")[0].capitalize()}, for using PopChat. See you again soon!')
        exit()


def question():
    if random.randint(1, 10) == 1:
        print("*** NETWORK ERROR ***")
        return
    query = input("---> ").upper()
    if "EXIT" in query or "BYE" in query or "HELP" in query:
        return
    i = 0
    while i < 6:
        if q_array[i] in query:
            print(a_array[i])
            break
        i = i + 1
    if i == 6:
        print(random.choice(responses))
    question()


if __name__ == '__main__':
    welcome()
