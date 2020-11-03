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
        self.player_turn = True

    ## Create a single button
    def create_button(self):
        b = Button(self.board, command=lambda:self.button_click(b))

        ## TODO: Change the font, size, color of the button to your liking
        ## https://www.tutorialspoint.com/python/tk_button.htm

        b['bg'] = 'CadetBlue1'
        b['activebackground'] = 'green2'
        b['font'] = 'Helvetica'
        b['fg'] = 'deep pink'
        b['bd'] = 10
        b['height'] = 4
        b['width'] = 10
        b['relief'] = RAISED
        
        return b

    ## Create 9 buttons and arrange them in a 3x3 grid
    def create_buttons(self):
        buttons = list()

        ## TODO: Create 9 buttons, arrange them in a 3x3 grid, and add them to the list

        but1 = self.create_button()
        buttons.append(but1)
        but1.grid(row=0, column=0)
 
        but2 = self.create_button()
        buttons.append(but2)
        but2.grid(row=1, column=0)

        but3 = self.create_button()
        buttons.append(but3)
        but3.grid(row=2, column=0)

        but4 = self.create_button()
        buttons.append(but4)
        but4.grid(row=0, column=1)

        but5 = self.create_button()
        buttons.append(but5)
        but5.grid(row=1, column=1)

        but6 = self.create_button()
        buttons.append(but6)
        but6.grid(row=2, column=1)

        but7 = self.create_button()
        buttons.append(but7)
        but7.grid(row=0, column=2)

        but8 = self.create_button()
        buttons.append(but8)
        but8.grid(row=1, column=2)

        but9 = self.create_button()
        buttons.append(but9)
        but9.grid(row=2, column=2)
                    
        return buttons

    ## Do this when a button is clicked
    def button_click(self, button):
        ## Add text to button based on whose turn it is
        if self.player_turn:
            ## TODO: Change button text to 'X' and button state to disabled
            button['text'] = 'X'
            button['state'] = DISABLED
        else:
            ## TODO: Change button text to 'O' and button state to disabled
            button['text'] = 'O'
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
        self.buttons['state'] = DISABLED
        
    def check_winner(self):
        char = ''
        
        ## TODO: Check which player's turn it is and make sure char is correct
        ## Player 1 is always 'X'
        ## Player 2 is always 'O'
        if self.player_turn:
            char = 'X'
        else:
            char = 'O'

        hasWon = False
        
        ## TODO: Check if the text of three buttons in a row equals char

        ## TODO: Check if the text of three buttons in a column equals char
        
        ## TODO: Chech if the text of the diagonal buttons equals char
        
        
        if hasWon:
            ## Disable all buttons
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
    
