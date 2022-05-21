#This code is intended  to make the game hilo, objective is to 
import random
def main():
    card_list = [1]
    total = createtotal("Z")
    #welcome (show test game to get 1st card number)
    while total > 0:
    
        card = random.randint(1,13)
        print(card)
        card_list.append(card)
        print(card_list)  
        guess = input("Will the next card be higher or lower? [h/l] ")
        if guess == "h":
            if card > card_list[-1]:
                createtotal("Y")
            elif card == card_list[-1]:
                print("No correct guess. Points are pushed")
            else:
                createtotal("N")  

        if guess == "l":
            if card > card_list[-1]:
                createtotal("N")
            elif card == card_list[-1]:
                print("No correct guess. Points are pushed")
            else:
                createtotal("Y")          




def createtotal(correct):
    total = 300
    if correct == "Y":
        total + 100
        return total
    elif correct == "N":
        total - 75
        return total   
    else:
        return total



if __name__ == "__main__":
    main()             