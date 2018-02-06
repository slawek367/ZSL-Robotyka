#!/usr/bin/env python

import RPi.GPIO as GPIO
from SimpleMFRC522 import SimpleMFRC522 as RFID
from time import sleep

GPIO.setwarnings(False)
rfid = RFID()

class User():

    def __init__(self, username, userSurrname, money):
        self.username = username
        self.userSurrname = userSurrname
        self.money = money
        self.id = ""
    
    def updateUserCard(self):
        print("Please use your card:")
        rfid.write(self.username + " " + self.userSurrname)
        cardId, cardText = rfid.read()
        self.id = cardId
        print("Dear " + cardText + " Card was updated in your account!")
    
    def showUserInfo(self):
        print("Name: " + self.username)
        print("Surrname: " + self.userSurrname)
        print("Money: " + str(self.money))
        print("Id: " + str(self.id))

class Users():

    def __init__(self):
        self.userList = []
    
    def addUser(self, username, userSurrname, money):
        user = User(username, userSurrname, money)
        user.updateUserCard()
        self.userList.append(user)
    
    def showUsers(self):
        for user in self.userList:
            user.showUserInfo
    
    def getUserByCard(self):
        cardId, cardText = rfid.read()
        user = next((user for user in self.userList if user.id == cardId), None)
        return user

users = Users()

users.addUser("Tomasz", "Kowalski", 2000)
sleep(1)
users.addUser("Wojciech", "Kowal", 5000)
sleep(1)

while True:
    print("Przyloz karte by zidentyfikowac uzytkownika:")
    users.getUserByCard().showUserInfo()
    sleep(1)