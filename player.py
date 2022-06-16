from game.cards import Cards


class Player:
 

    def __init__(self):
        
        self.currentCard = Cards()
        self.is_playing = True
        self.score = 300

    def start_game(self):
        
        while self.is_playing:
            self.get_inputs()
            self.do_outputs()

    def get_inputs(self):
        
        val = self.currentCard.value
        print("The card is: %d" %val)

        
        playerIn = ""
        while playerIn != "h" or playerIn != "l":
            playerIn = input("Higher or lower? [h/l]: ")
            oldCard = self.currentCard
            newCard = Cards()
            if(playerIn == "h"):
                self.get_high(oldCard, newCard)
                break

            elif(playerIn == "l"):
                self.get_low(oldCard, newCard)
                break
            else:
                print("Invalid input")
                print()

    def do_updates(self, guess, newCard):
        
        
        #updates score
        self.score += guess
        if (self.score <= 0):
            self.is_playing = False
        #update card
        self.currentCard.value = newCard

        
    def do_outputs(self):
        
        print(f"Your score is: {self.score}")
        print(f"The card was: {self.currentCard.value}")

        if(self.score <= 0):
            self.is_playing = False
            return

        #loop until y/n
        v = ""
        while v != "n" or v != "y":
            v = input("Play again [y/n]: ")
            if(v == "n"):
                self.is_playing = False
                break
            elif(v == "y"):
                print("")
                break
            else:
                print("Invalid input")


    def get_high(self, c1, c2):
        
        
        if c2.value > c1.value:
            self.do_updates(100, c2.value)
            
        elif c2.value < c1.value:
            self.do_updates(-75, c2.value)


    def get_low(self, c1, c2):
        
        if c2.value < c1.value:
            self.do_updates(100, c2.value)
        elif c2.value > c1.value:
            self.do_updates(-75, c2.value)
        else:
            print("")
            return
