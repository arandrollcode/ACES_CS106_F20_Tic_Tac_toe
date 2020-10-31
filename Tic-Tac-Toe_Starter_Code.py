from tkinter import *
import tkinter.messagebox
import random

class TTTGame:
    def __init__(self):
        self.board = Tk()

        ## Set the title of the board
        self.board.title('Tic Tac Toe')

        ## List of 9 buttons for our game
        self.buttons = self.create_buttons()
        
        self.moves_made = 0
        self.player_turn = 1

    ## Create a single button
    def create_button(self):
        b = Button(self.board, command=lambda:self.button_click(b))

        ## TODO: Change the font, size, color of the button to your liking
        ## https://www.tutorialspoint.com/python/tk_button.htm
        ## b['bg'] =
        
        return b

    ## Create 9 buttons and arrange them in a 3x3 grid
    def create_buttons(self):
        buttons = list()

        ## TODO: Create 9 buttons, arrange them in a 3x3 grid, and add them to the list

        return buttons

    ## Do this when a button is clicked
    def button_click(self, button):
        ## Add text to button based on whose turn it is
        if self.player_turn == 1:
            ## TODO: Change button text to 'X' and button state to disabled
        else:
            ## TODO: Change button text to 'O' and button state to disabled

        ## TODO: Add 1 to self.moves_made
            
        ## TODO: Check for winner
    
        ## TODO: Change player turn to other player
        ## If player_turn was 1, change it to 2
        ## If player_turn was 2, change it to 1

    def disable_all_buttons(self):
        ## TODO: Disable all of the buttons

    def check_winner(self):
        char = 'X'
        
        ## TODO: Check which player's turn it is and make sure char is correct
        ## Player 1 is always 'X'
        ## Player 2 is always 'O'

        hasWon = False
        
        ## TODO: Check if the text of three buttons in a row equals char
        
        ## TODO: Check if the text of three buttons in a column equals char

        ## TODO: Chech if the text of the diagonal buttons equals char

        
        if hasWon == True:
            ## Disable all buttons
            tkinter.messagebox.showinfo("Tic-Tac-Toe", 'Player {} Wins'.format(player))

        ## TODO: Check if all moves have been made
        ## If all moves have been made and there is no winner, it is a tie
        elif _________________:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a tie")

    def run(self):
        self.board.mainloop()

        
if __name__ == '__main__':
    game = TTTGame()
    game.run()


