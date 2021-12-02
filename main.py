# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:46:41 2020

@author: abdil
"""
import random,time,smtplib
global total_score

username = input("What is Your Name:\t")
greet = print("Hello {}, Enjoy the game ".format(username))
print()
def main():
    total_score = 0
    seconds = 3
    print("Guess a Number and win points... You Can Add up all points\n If You reach 100 points You will win your favorite Candy Bar")
    print("\t You Have 9 Guesses each time")
    candy = input("What is your Favourite Candy Bar?: ")
    print("---Game Scores---")
    print("Right Guess in 1 Time = 10 Points\n","Right Guess in 2 Times = 9 Pionts\n","Right Guess in 3 Times = 8 Pionts\n",
          "Right Guess in 4 Times = 7 Pionts\n","Right Guess in 5 Times = 6 Pionts\n","Right Guess in 6 Times = 5 Pionts\n",
          "Right Guess in 7 Times = 4 Points\n","Right Guess in 8 Times = 3 Points\n","Right Guess in 9 Times = 2  Points\n","Wrong Guess = 0\n")
    for second in range(seconds):
        print("Game Begining in ...")
        print(str(seconds-second))
        print()
        time.sleep(1)
    print("-----Start-----")
    while True: 
        game_score = 0
        mynum = random.randint(1,1000)
        num = random.randint(1,100)
        try:
            for n in range(1):
            
                for guesses in range(1,10):
                    user_num = int(input("{}, Take a guess of a number between {} and {}:\t".format(username,(mynum+num),(mynum+num))))
                    
                    if user_num < mynum:
                        print("Your Guess is too low\n")
                    elif user_num > mynum:
                        print("Your Guess is too high\n")
                    else:
                        break
                    
                if user_num == mynum:
                    print("Great Job {} !! you guessed the number in {} times\n".format(username,guesses))
                    if guesses == 1:
                        game_score = 10
                        print("Game Score = {}".format(game_score))
                    elif guesses == 2:
                        game_score = 9
                        print("Game Score = {}".format(game_score))
                    elif guesses == 3:
                        game_score = 8
                        print("Game Score = {}".format(game_score))
                    elif guesses == 4:
                        game_score = 7
                        print("Game Score = {}".format(game_score))
                    elif guesses == 5:
                        game_score = 6
                        print("Game Score = {}".format(game_score))
                    elif guesses == 6:
                        game_score = 5
                        print("Game Score = {}".format(game_score))
                    elif guesses == 7:
                        game_score = 4
                        print("Game Score = {}".format(game_score))
                    elif guesses == 8:
                        game_score = 3
                        print("Game Score = {}".format(game_score))
                    elif guesses == 9:
                        game_score = 2
                        print("Game Score = {}".format(game_score))
                    else:
                        game_score = 0
                        print("Game Score = {}".format(game_score)) 
                        print()
                else:
                    print("Sorry {} !! You didn't guess the number the number was {}\n".format(username,mynum))
                total_score+= game_score
                print("Total Score = {}".format(total_score))
                print()
                if total_score >= 100:
                    total_score = 0
                    seconds = 3
                    for second in range(seconds):
                        print("Wait for it...")
                        print(str(seconds-second)+" Seconds")
                        print()
                        time.sleep(1)
                    print("Congratulations {} !!!  You Have 100 points Now!!!!\n You Won a {} Bar!".format(username,candy))
                    print()
                    sender = "abdillahi.isse@hotmail.com"
                    receiver = "abdillahi.isse@hotmail.com"
                    passwrd = "Abdi1998"
                    subject = (f"Subject: {username} Won a {candy} Candy Bar")
                    body = (f"\r\n\r\n{username} reach a game score of 100 points, and he/she should get his/her {candy} Candy Bar\r\n\r\n")
                    msg = subject+body
                    smtpObj = smtplib.SMTP(host='smtp-mail.outlook.com',port=587)
#                    smtpObj.ehlo()
                    smtpObj.starttls()
                    smtpObj.login(sender,passwrd)
                    smtpObj.sendmail(sender,receiver,msg)
                    smtpObj.quit()
                elif total_score >= 50:
                    print("Go On!!! You're  halfway there!!!")
                    print()
        except ValueError:
                print("You Didn't Enter a number ,Please try again.\n")
                break
        except Exception as e:
                print("Error: %s" %e)
                break
            
            
    
        try:
            choice = input("Play Again:\t 1.Yes\t 2.No:\t")
            print()
            if choice == "1":
                continue
            elif choice == "2":
                print("Bye {} ... See You Next Time".format(username))
                break
            else:
                print("You Didn't enter any choice!!!")
                break
            
        except ValueError:
                print("You Didn't Enter a number ,Please try again.\n")
                break
        except Exception as e:
                print("Error: %s" %e)
                break

if __name__ =="__main__":
    main()
    