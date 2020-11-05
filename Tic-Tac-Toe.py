from tkinter import *
import tkinter.messagebox
import tkinter.font as font
import random

class TTTGame:
    def __init__(self):
        self.board = Tk()

        ## Set the title of the board
        self.board.title('Tic Tac Toe')

        ## List of 9 buttons for our game
        self.buttons = self.create_buttons()
        
        self.moves_made = 0
        self.player_turn = True

    ## Create a single button
    def create_button(self):
        b = Button(self.board, command=lambda:self.button_click(b))
        m = 1.5
                
        ## TODO: Change the font, size, color of the button to your liking
        ## https://www.tutorialspoint.com/python/tk_button.htm
        my_font = font.Font(size=int(25*m), weight='bold')

        b['bg'] = 'CadetBlue1'
        b['activebackground'] = 'green2'
        b['font'] = my_font
        b['bd'] = int(12*m)
        b['height'] = int(1.5*m)
        b['width'] = int(4*m)
        b['relief'] = RAISED

        return b


    ## Create 9 buttons and arrange them in a 3x3 grid
    def create_buttons(self):
        buttons = list()

        ## TODO: Create 9 buttons, arrange them in a 3x3 grid, and add them to the list
        for i in range(3):
            for j in range(3):
                but = self.create_button()
                but.grid(row=i, column=j)
                buttons.append(but)
        return buttons


    ## Do this when a button is clicked
    def button_click(self, button):
        ## Add text to button based on whose turn it is
        if self.player_turn:
            ## TODO: Change button text to 'X' and button state to disabled
            button['text'] = 'X'
            button['disabledforeground'] = 'blue2'
            button['state'] = DISABLED
        else:
            ## TODO: Change button text to 'O' and button state to disabled
            button['text'] = 'O'
            button['disabledforeground'] = 'red2'
            button['state'] = DISABLED
            
        ## TODO: Add 1 to self.moves_made
        self.moves_made += 1
        ## TODO: Check for winner
        self.check_winner()
        ## TODO: Change player turn to other player
        ## If player_turn was True, change it to False
        ## If player_turn was False, change it to True
        self.player_turn = not self.player_turn


    def disable_all_buttons(self):
        ## TODO: Disable all of the buttons
        for button in self.buttons:        
            button['state'] = DISABLED

        
    def check_winner(self):
        char = 'X'
        
        ## TODO: Check which player's turn it is and make sure char is correct
        ## Player 1 is always 'X'
        ## Player 2 is always 'O'
        if not self.player_turn:
            char = 'O'

        hasWon = False
        
        ## TODO: Check if the text of three buttons in a row equals char

        if ((self.buttons[0]['text'] == self.buttons[1]['text'] == self.buttons[2]['text'] == char) or
            (self.buttons[3]['text'] == self.buttons[4]['text'] == self.buttons[5]['text'] == char) or
            (self.buttons[6]['text'] == self.buttons[7]['text'] == self.buttons[8]['text'] == char)):
            hasWon = True

        ## TODO: Check if the text of three buttons in a column equals char

        if ((self.buttons[0]['text'] == self.buttons[3]['text'] == self.buttons[6]['text'] == char) or
            (self.buttons[1]['text'] == self.buttons[4]['text'] == self.buttons[7]['text'] == char) or
            (self.buttons[2]['text'] == self.buttons[5]['text'] == self.buttons[8]['text'] == char)):
            hasWon = True
            
        ## TODO: Chech if the text of the diagonal buttons equals char

        if ((self.buttons[0]['text'] == self.buttons[4]['text'] == self.buttons[8]['text'] == char) or
            (self.buttons[2]['text'] == self.buttons[4]['text'] == self.buttons[6]['text'] == char)):
            hasWon = True


        if hasWon:
            ## Disable all buttons
            player='1'
            if not self.player_turn:
                player='2'
            self.disable_all_buttons()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", 'Player {} Wins'.format(player))

        ## TODO: Check if all moves have been made
        ## If all moves have been made and there is no winner, it is a tie
        elif self.moves_made == 9:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a tie")


    def run(self):
        self.board.mainloop()



if __name__ == '__main__':
    game = TTTGame()
    game.run()
