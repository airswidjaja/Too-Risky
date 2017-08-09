import sys
import time
from termcolor import colored, cprint

# Last updated Wed 9 Aug 2017 AEST

# Oi! Why you looking at my shoddy programming?
# Yeah. Open-source and licenced under the GNU General Public Licence. Check me out on YouTube: youtube.com/c/AdrianWidjaja.
# Gameplay
def play():
    onedone = "1"
    onedtwo = "2"
    cprint("NARRATOR: One day, someone wanted to go to the beach. This person was you. Your name is...", "grey", "on_white")
    time.sleep(3)
    cprint("NARRATOR: What is your name?", "grey", "on_white")
    personname = raw_input("")
    cprint("NARRATOR: Your name is " + personname + ".", "grey", "on_white")
    time.sleep(1)
    cprint("NARRATOR: " + personname + " was going to the beach. You were going to go swimming.", "grey", "on_white")
    time.sleep(1.5)
    cprint("NARRATOR: " + personname + " arrived at the beach. It was sunny and hot. You really needed a cool swim. However, there was a sign which read that the beach was closed, due to high tides and shark infestation. Should " + personname + " walk another 30 minutes to a different beach, or should " + personname + " swim in the closed beach out of sight from the lifeguards? Type '1' for the first option. Type '2' for the second option.", "grey", "on_white")
    decisionone = raw_input("")
    if decisionone == onedone: # Decision 1 Option 1
        threedone = "1"
        threedtwo = "2"
        print("YOU: I'm going to go walk to the other beach, which is 30 minutes away.")
        cprint("NARRATOR: Then, Amy catches up with you.")
        text = colored("AMY: Hey " + personname + ". You wanna go rock jumping?", "blue")
        print(text)
        time.sleep(2)
        print("YOU: I've never been before. How high is the cliff?")
        text = colored("AMY: Only 3 meters. It's gonna be great. Come on. Type '1' if you wanna have the time of your life and go rock jumping. Type '2' if you're a chicken.", "blue")
        print(text)
        decisionthree = raw_input("")
        if decisionthree == threedone: # Decision 3 Option 1
            fourdone = "1"
            fourdtwo = "2"
            text = colored("AMY: Yeah! That's what I'm talkin' about, my man.", "blue")
            print(text)
            time.sleep(1)
            print("YOU: Is there any equipment involved?")
            time.sleep(1)
            text = colored("AMY: Nup! Let's walk down to the beach, near dat quadrangle, ya know. We'll jump off the cliff and whoa it's gonna be fun!", "blue")
            print(text)
            time.sleep(2)
            cprint("NARRATOR: You near the beach near the quadrangle, and you see the cliff you are jumping off. It looked like that Amy lied to you; that cliff looks more around 10 meters. You decided to keep going, it can't be that bad, right?", "grey", "on_white")
            text = colored("AMY: Let's go!", "blue")
            time.sleep(1)
            print(text)
            print("YOU: Wow, those are some big rocks at the bottom of this cliff. Should I still go? Type '1' to keep jumping. Type '2' if you're Amy's definition of a chicken, which, I strongly disagree with.")
            decisionfour = raw_input("")
            if decisionfour == fourdone: # Decision 4 Option 1
                print("YOU: Let's go Amy.")
                time.sleep(1)
                text = colored("AMY: Yeah mate! This is gonna be so freaky.", "blue")
                print(text)
                time.sleep(1)
                cprint("NARRATOR: You get ready to jump. You do a classic run up and jump of the edge, and you see everything around you for a second. It almost feels like a rollercoaster. You aim your eyes to the ocean, until you realise, you're not gonna make it.", "grey", "on_white")
                time.sleep(3)
                print("YOU: Help! Help me!")
                time.sleep(0.8)
                cprint("NARRATOR: You hit the ground and you are sure you broke a bone. There are people approaching, from all sides, including a lifeguard.", "grey", "on_white")
                print("YOU: Ouch!")
                time.sleep(1)
                text = colored("LIFEGUARD: Okay kid, it's gonna be okay. Just stick with me, and for your information, what you did was TOO RISKY.", "cyan")
                print(text)
                text = colored("Game over. You made 1 good choice and 1 bad choice. To play again, type 'play'.", "red", attrs=["bold"])
                print(text)
                home()
        else: # Decision 3 Option 2
            if decisionthree == threedtwo:
                fivedone = "1"
                fivedtwo = "2"
                text = colored("AMY: Chicken. Maybe Sam will know how fun works.", "blue")
                print(text)
                cprint("NARRATOR: You continue to make your way to the beach. You reach the beach, and after much delay, you finally get there. To your left, there is a surfboard rental shop. You wouldn't mind a good surf? Type '1' to go surfing, and type '2' to just swim.", "grey", "on_white")
                decisionfive = raw_input("")
                if decisionfive == fivedone: # Decision 5 Option 1
                    print("YOU: Hey Sam, can I rent a surfboard? I'm goin' surfing.")
                    time.sleep(1)
                    text = colored("SAM: Yep, that's going to be $15 for the afternoon.", "magenta")
                    print(text)
                    time.sleep(1)
                    print("YOU: Thanks Sam.")
                    time.sleep(1)
                    text = colored("SAM: No problem " + personname + ". Have a good day!", "magenta")
                    print(text)
                    time.sleep(1)
                    cprint("NARRATOR: You're having the time of your life, and wishing that your Maths teacher wouldn't give so much homework so you would have more time for this.", "grey", "on_white")
                    time.sleep(1)
                    print("YOU: You know, I wonder how it's going for Amy. I think she's been TOO RISKY.")
                    text = colored("You have finished the game. You made a lot of good decisions today. To play again, type 'play'.", "red", attrs=["bold"])
                    home()
                else:
                    if decisionfive == fivedtwo: # Decision 5 Option 1
                        fivedone = "1"
                        fivedtwo = "2"
                        print("YOU: Ah, let's go swimming.")
                        cprint("NARRATOR: The sand on your feet, the wind in your hair, you love it all. You can choose to go further down the beach, past the red and yellow flags, or move closer to the lifeguard station. Type '1' to go further down the beach. Type '2' to move closer to the lifeguards.", "grey", "on_white")
                        decisionsix = raw_input("")
                        if decisionsix == fivedone:
                            cprint("NARRATOR: You head further down the beach and you start to swim. You accidentally swim into a riptide and you can't get out! You wave your hand and try to tread water, but, you're drifting away from shore. You sink. You can't breathe, but, after being exhausted from treading water, you have no energy to get up.", "grey", "on_white")
                            time.sleep(3)
                            print("YOU: Huh? What? Where am I?")
                            time.sleep(2)
                            text = colored("LIFEGUARD: You're in the first aid office, and you should always stay between the flags. Good thing another person was sunbathing down there to save you. Going down there was TOO RISKY.", "cyan")
                            print(text)
                            text = colored("Game over. You made 1 bad choice and 1 good choice. To play again, type 'play'", "red", attrs=["bold"])
                            print(text)
                            home()
                        else:
                            if decisionsix == fivedtwo: # Decision 5 Option 1
                                cprint("NARRATOR: And now, your're swimming safely. You made the right choice, and everyone you see out of the lifeguard's vicinity is being TOO RISKY.", "grey", "on_white")
                                text = colored("You have finished the game. You made a lot of good decisions today. To play again, type 'play'.", "red", attrs=["bold"])
                                print(text)
                                home()
                            else:
                                text = colored("Error: Invalid Command (Error Code x000001)", "red")
                                print(text)
                                home()
                                
                    else:
                        text = colored("Error: Invalid Command (Error Code x000001)", "red")
                        print(text)
                        home()
 
                    
            else:
                text = colored("Error: Invalid Command (Error CodeL x000001)", "red")
                print(text)
                home()
 
    else:
         if decisionone == onedtwo: # Decision 1 Option 2
             twodone = "1"
             twodtwo = "2"
             print("YOU: I'm so hot, I'll do anything to get a swim!")
             time.sleep(2)
             cprint("NARRATOR: You go swimming in the ocean, and it's nice and cool, until, you pop up your head and see a grey fin in the distance. It's coming right towards you.", "grey", "on_white")
             time.sleep(2)
             print("YOU: Ah!")
             time.sleep(0.6)
             text = colored("LIFEGUARD: Hey kiddo, jump on quick!", "cyan")
             print(text)
             time.sleep(2)
             print("YOU: *jumps on to boat*")
             time.sleep(2)
             text = colored("LIFEGUARD: You're lucky you made it alive. Did you see the sign that said the beach was closed?", "cyan")
             print(text)
             time.sleep(2)
             cprint("Should " + personname + " be honest and say the truth, or lie to get out of trouble? Type '1' to be honest. Type '2' to lie.", "grey", "on_white")
             decisiontwo = raw_input("")
             if decisiontwo == twodone: # Decision 2 Option 1
                   text = colored("LIFEGUARD: You're very naughty. What you did was TOO RISKY.", "grey", "on_white")
                   print(text)
                   text = colored("Game over. You made 1 bad choice and 1 good choice. To play again, type 'play'", "red", attrs=["bold"])
                   print(text)
                   home()
             else:
                 if decisiontwo == twodtwo: # Decision 2 Option 2
                     text = colored("LIFEGUARD: You should always check the signs before entering the beach. What you did was TOO RISKY.")
                     print(text)
                     text = colored("Game over. You made 2 bad choices and no good choices. To play again, type 'play'.", "red", attrs=["bold"])
                     print(text)
                     home()
                 else: # Invalid command, crash failsafe.
                    text = colored("Error: Invalid Command (Error CodeL x000001)", "red")
                    print(text)
                    home()
 
                
                

# input definitions and stringvars

def home():
    print("")
    homecom = raw_input("")
    commandrun = "play"
    information = "about"
    nerdmylife = "nerdstuff"
    eatmorenachos = "penguins"
    if homecom == commandrun:
        play()
    else:
        if homecom == information:
            print("")
            text = colored("Too Risky is a game about taking smart decisions on risks at the beach. If you make a bad choice, consequences can and will occur. At the end of the day, make the right choices and don't land yourself in trouble. Too Risky is a story-based text role-playing game, where you take the role of someone and are presented with opportunities to make choices. Remember, your decisions will affect your future.", "red")
            print(text)
            print("")
            cprint("Our narrator talks in grey text.", "grey", "on_white")
            print("You talk in standard text.")
            text = colored("Amy speaks in blue text.", "blue")
            print(text)
            text = colored("Sam chats with you in magenta text.", "magenta")
            print(text)
            text = colored("The lifeguard speaks in cyan text.", "cyan")
            print(text)
            home()
        else:
            if homecom == nerdmylife:
                print("")
                text = colored("Too Risky was developed by Adrian Widjaja in the Python Programming Language. Too Risky is released under the GNU General Public Licence. Our source code is online at https://github.com/airswidjaja/TooRisky.py.", "red")
                print(text)
                print("")
                text = colored("This version of Too Risky is 0.1. This is an early access version. Bugs may be present.", "red")
                print(text)
                print("")
                text = colored("List of commands: play (starts the game), nerdstuff (displays commands and about section), about (displays information on how to play the game.", "red")
                home()
            else:
                if homecom == eatmorenachos:
                    cprint("PENGUINS ARE THE BEST!", "white", "on_magenta")
                    home()
                else:
                    print("")
                    text = colored("Error: Invalid Command (Error CodeL x000001)", "red")
                    print(text)
                    print("")
                    home()
def devtool():
            home()
           
                    
# start of boot

print("")
print("")
text = colored("Too Risky 0.1 is provided under the GNU General Public Licence. Our source code is available on GitHub at https://github.com/airswidjaja/TooRisky.py. WARNING: Your terminal client software must support ASCII colour formatting. If not, some characters may not render as intended.", 'red', attrs=["bold"])
print(text)
print("")
text = colored("Welcome to Too Risky! To start the game, type 'play'. To learn more about the game, type 'about'. ", "red", attrs=["bold"])
print(text)
print("")
home()
