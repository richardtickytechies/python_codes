import random
import time
rock=1
paper=2
scissors=3
names={rock: "Rock",paper:"Paper",scissors:"Scissors"}
rules={rock:scissors,paper:rock,scissors:paper}
player_score=0
computer_score=0
def start():
    print("Let's play a game of Rock Paper Scissors!")
    while game():
        pass
    scores()
def game():
    player=move()
    computer=random.randint(1,3)
    result(player,computer)
    return play_again()
def move():
    while True:
        print("")
        player=input("Rock = 1\nPaper = 2\nScissors = 3\nMake a Move: ")
        try:
            player=int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print("Oh! You mis-typed! You should only type in 1, 2, or 3!")
def result(player,computer):
    print("3!")
    time.sleep(1)
    print("2!")
    time.sleep(1)
    print("1!")
    time.sleep(0.5)
    print("Computer threw {0}".format(names[computer]))
    global player_score,computer_score
    if player==computer:
        print("Oh my! It's a Tie!")
    else:
        if rules[player]==computer:
            print("You have destroyed the computer in this battle!")
            player_score+=1
        else:
            print("The computer has annihilated your teensy-tiny-brain.")
            computer_score+=1
def play_again():
    answer=input("Would you like to play again? (Y/N): ")
    if answer in ("Y","y"):
        return answer
    else:
        print("Thanks for playing, the scores are a shown below.")                                                                      
def scores():
    global player_score, computer_score
    print("SCORES")
    print("Player: ",player_score)
    print("Computer: ",computer_score)
if __name__=='__main__':
    start()