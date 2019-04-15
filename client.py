#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import os
import time
import pickle
import json

def receive():
    """Handles receiving of messages."""
    props = []
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            #print(msg)
            if msg == "Greeting from the Monopoly bank! Enter your name and press enter!":
                print(msg)
                send()
            elif msg == "Enter {ready} when ready to play!":
                print(msg)
                input_ready = str(input("Enter: "))
                while input_ready != "{ready}":
                    input_ready = str(input("You can only enter {ready}: "))
                else:
                    client_socket.send(bytes(input_ready, "utf-8"))
            elif msg == "We all are ready!":
                print(msg)
                time.sleep(1)
                os.system('cls')
            elif msg == "What do you want to do?":
                if len(props) != 0:
                    print("Your Properties: " + ', '.join(props))
                print()
                print(msg)
                time.sleep(1)
                print("Type W for Withdraw")
                print("Type P for Pay to Player")
                print("Type A for Pay to All")
                print("Type B for Pay to Bank")
                print("Type C for Collect Money From Everyone")
                print("Type H for Properties options")

                answer = str(input("Enter: ")).lower()

                while answer != "w" and answer != "p" and answer != "b" and answer != "c" and answer != "a" and answer != "h":
                    answer = str(input("Please enter a valid answer: ")).lower()

                client_socket.send(bytes(answer, "utf-8"))

                if answer == "w":
                    asking_amount = client_socket.recv(BUFSIZ).decode("utf8")
                    amount = int(input(asking_amount))
                    client_socket.send(bytes(str(amount), "utf-8"))

                if answer == "p":
                    asking_amount = client_socket.recv(BUFSIZ).decode("utf-8")
                    amount = int(input(asking_amount))
                    client_socket.send(bytes(str(amount), "utf-8"))
                    array_length = client_socket.recv(BUFSIZ).decode("utf-8")
                    print(array_length)
                    ask_code = str(input("Enter Code of Recipient: "))
                    while not(int(ask_code) <= (int(len(array_length)) + 1)) and (int(ask_code) != 0):
                        ask_code = str(input("Code not found! Enter again: "))
                    client_socket.send(bytes(ask_code, "utf-8"))

                if answer == "b":
                    asking_amount = client_socket.recv(BUFSIZ).decode("utf8")
                    amount = int(input(asking_amount))
                    client_socket.send(bytes(str(amount), "utf-8"))

                if answer == "c":
                    asking_amount = client_socket.recv(BUFSIZ).decode("utf-8")
                    amount = int(input(asking_amount))
                    client_socket.send(bytes(str(amount), "utf-8"))
                if answer == "a":
                    asking_amount = client_socket.recv(BUFSIZ).decode("utf-8")
                    amount = int(input(asking_amount))
                    client_socket.send(bytes(str(amount), "utf-8"))
                if answer == "h":
                    properties = client_socket.recv(BUFSIZ).decode("utf-8")
                    properties = json.loads(properties)
                    os.system('cls')
                    print("Which colour/type property are you buying. Type Letter/Letters associated with Colour: ")
                    print("Brown(B)")
                    print("Light Blue(LB)")
                    print("Pink(P)")
                    print("Orange(O)")
                    print("Red(R)")
                    print("Yellow(Y)")
                    print("Green(G)")
                    print("Dark Blue(DB)")
                    print("Stations(S)")
                    print("Utilites(U)")
                    ask_property = str(input("Enter: "))
                    ask_property = ask_property.upper()
                    while ask_property != "B" and ask_property != "LB" and ask_property != "P" and ask_property != "P" and ask_property != "O" and ask_property != "R" and ask_property != "Y" and ask_property != "G" and ask_property != "DB" and ask_property != "S" and ask_property != "U":
                        ask_property = str(input("Enter a valid answer: "))
                        ask_property = ask_property.upper()
                    os.system('cls')
                    if ask_property == "B":
                        print("Which one: ")
                        print("1. Guhawati")
                        print("2. Bhubaneshwar")
                        final_property = int(input("Enter corresponding number with your desired property: "))
                        while final_property != 1 and final_property != 2:
                            final_property = int(input("Enter a correct value(1/2): "))

                        if final_property == 1:
                            amount_to_pay = properties["Guhawati"]
                            chosen_property = "Guhawati"
                        else:
                            amount_to_pay = properties["Bhubaneshwar"]
                            chosen_property = "Bhubaneshwar"

                    if ask_property == "LB":
                        print("Which one: ")
                        print("1. Panaji(Goa)")
                        print("2. Agra")
                        print("3. Vadodara")
                        final_property = int(input("Enter corresponding number with your desired property: "))
                        while final_property != 1 and final_property != 2 and final_property != 3:
                            final_property = int(input("Enter a correct value(1/2/3): "))

                        if final_property == 1:
                            amount_to_pay = properties["Panaji(Goa)"]
                            chosen_property = "Panaji(Goa)"
                        elif final_property == 2:
                            amount_to_pay = properties["Agra"]
                            chosen_property = "Agra"
                        else:
                            amount_to_pay = properties["Vadodara"]
                            chosen_property = "Vadodara"

                    if ask_property == "P":
                        print("Which one: ")
                        print("1. Ludhiana")
                        print("2. Patna")
                        print("3. Bhopal")
                        final_property = int(input("Enter corresponding number with your desired property: "))
                        while final_property != 1 and final_property != 2 and final_property != 3:
                            final_property = int(input("Enter a correct value(1/2/3): "))

                        if final_property == 1:
                            amount_to_pay = properties["Ludhiana"]
                            chosen_property = "Ludhiana"
                        elif final_property == 2:
                            amount_to_pay = properties["Patna"]
                            chosen_property = "Patna"
                        else:
                            amount_to_pay = properties["Bhopal"]
                            chosen_property = "Bhopal"

                    if ask_property == "O":
                        print("Which one: ")
                        print("1. Indore")
                        print("2. Nagpur")
                        print("3. Kochi")
                        final_property = int(input("Enter corresponding number with your desired property: "))
                        while final_property != 1 and final_property != 2 and final_property != 3:
                            final_property = int(input("Enter a correct value(1/2/3): "))

                        if final_property == 1:
                            amount_to_pay = properties["Indore"]
                            chosen_property = "Indore"
                        elif final_property == 2:
                            amount_to_pay = properties["Nagpur"]
                            chosen_property = "Nagpur"
                        else:
                            amount_to_pay = properties["Kochi"]
                            chosen_property = "Kochi"

                    if ask_property == "R":
                        print("Which one: ")
                        print("1. Lucknow")
                        print("2. Chandigarh")
                        print("3. Jaipur")
                        final_property = int(input("Enter corresponding number with your desired property: "))
                        while final_property != 1 and final_property != 2 and final_property != 3:
                            final_property = int(input("Enter a correct value(1/2/3): "))

                        if final_property == 1:
                            amount_to_pay = properties["Lucknow"]
                            chosen_property = "Lucknow"
                        elif final_property == 2:
                            amount_to_pay = properties["Chandigarh"]
                            chosen_property = "Chandigarh"
                        else:
                            amount_to_pay = properties["Jaipur"]
                            chosen_property = "Jaipur"

                    if ask_property == "Y":
                        print("Which one: ")
                        print("1. Pune")
                        print("2. Hyderabad")
                        print("3. Ahmedabad")
                        final_property = int(input("Enter corresponding number with your desired property: "))
                        while final_property != 1 and final_property != 2 and final_property != 3:
                            final_property = int(input("Enter a correct value(1/2/3): "))

                        if final_property == 1:
                            amount_to_pay = properties["Pune"]
                            chosen_property = "Pune"
                        elif final_property == 2:
                            amount_to_pay = properties["Hyderabad"]
                            chosen_property = "Hyderabad"
                        else:
                            amount_to_pay = properties["Ahmedabad"]
                            chosen_property = "Ahmedabad"

                    if ask_property == "G":
                        print("Which one: ")
                        print("1. Kolkata")
                        print("2. Chennai")
                        print("3. Bengaluru")
                        final_property = int(input("Enter corresponding number with your desired property: "))
                        while final_property != 1 and final_property != 2 and final_property != 3:
                            final_property = int(input("Enter a correct value(1/2/3): "))

                        if final_property == 1:
                            amount_to_pay = properties["Kolkata"]
                            chosen_property = "Kolkata"
                        elif final_property == 2:
                            amount_to_pay = properties["Chennai"]
                            chosen_property = "Chennai"
                        else:
                            amount_to_pay = properties["Bengaluru"]
                            chosen_property = "Bengaluru"

                    if ask_property == "DB":
                        print("Which one: ")
                        print("1. Delhi")
                        print("2. Mumbai")
                        final_property = int(input("Enter corresponding number with your desired property: "))
                        while final_property != 1 and final_property != 2:
                            final_property = int(input("Enter a correct value(1/2): "))

                        if final_property == 1:
                            amount_to_pay = properties["Delhi"]
                            chosen_property = "Delhi"
                        else:
                            amount_to_pay = properties["Mumbai"]
                            chosen_property = "Mumbai"

                    if ask_property == "S":
                        print("Which one: ")
                        print("1. Chennai Central Railway Station")
                        print("2. Howrah Railway Station")
                        print("3. New Delhi Railway Station")
                        print("4. Chhatrapati Shivaji Terminus(Victoria Terminus)")
                        final_property = int(input("Enter corresponding number with your desired property: "))
                        while final_property != 1 and final_property != 2 and final_property != 3:
                            final_property = int(input("Enter a correct value(1/2/3/4): "))

                        if final_property == 1:
                            amount_to_pay = properties["Chennai Central Railway Station"]
                            chosen_property = "Chennai Central Railway Station"
                        elif final_property == 2:
                            amount_to_pay = properties["Howrah Railway Station"]
                            chosen_property = "Howrah Railway Station"
                        elif final_property == 3:
                            amount_to_pay = properties["New Delhi Railway Station"]
                            chosen_property = "New Delhi Railway Station"
                        else:
                            amount_to_pay = properties["Chhatrapati Shivaji Terminus(Victoria Terminus)"]
                            chosen_property = "Chhatrapati Shivaji Terminus(Victoria Terminus)"

                    if ask_property == "U":
                        print("Which one: ")
                        print("1. Electric Company")
                        print("2. Water Works")
                        final_property = int(input("Enter corresponding number with your desired property: "))
                        while final_property != 1 and final_property != 2:
                            final_property = int(input("Enter a correct value(1/2): "))
                        try:
                            if final_property == 1:
                                amount_to_pay = properties["Electric Company"]
                                chosen_property = "Electric Company"
                            else:
                                amount_to_pay = properties["Water Works"]
                                chosen_property = "Water Works"
                        except KeyError:
                            print("Property already chosen!")

                    #props.append(chosen_property)
                    client_socket.send(bytes(str(amount_to_pay), "utf-8"))
                    client_socket.send(bytes(chosen_property, "utf-8"))
                    booled = client_socket.recv(BUFSIZ).decode("utf-8")
                    if booled == "Property already bought!":
                        print(booled)
                        time.sleep(3)
                        os.system('cls')
                    else:
                        print(booled)
                        props.append(chosen_property)
                        os.system('cls')
                    time.sleep(1)
                os.system("cls")
            elif msg == "clear screen":
                os.system("cls")
            else:
                print(msg)

        except OSError:  # Possibly client has left the chat.
            break


def send(event=None): # event is passed by binders.
    """Handles sending of messages."""
    msg = str(input(""))
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()


#----Now comes the sockets part----
HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 8000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()