#Feb 2021 - My first attempt at a complete program using PYSimpleGUI - Peter Bowers

import PySimpleGUI as sg
import random

# my favourite theme so far
sg.theme('Kayak')

layout = [[sg.Text('Enter a number between 1 and 100:'), sg.Input(key='-IN-', justification='center', do_not_clear=False)],
          [sg.Text('', text_color= sg.YELLOWS[0], font=20, size=(300,1),justification='center', key='-OUT-')],
          [sg.Button('OK', bind_return_key=True, size=(10,1)), sg.Button('Quit')]]
# do_not_clear=False on a Text element will clear the text box as soon as the button is clicked
# bind_return_key=True on a Button element enables the Enter key on the keyboard

# element_justification='center' will center all elements horizontally in the window
window = sg.Window("Guess My Number!", layout, element_justification='center', size=(400,200))

# count the number of attempts in each turn
count = 0
# get a random number between 1 and 100
secret = random.randrange(1, 101)

while True:
    event, values = window.read()
    # try/except with ValueError will catch letters, etc.(anything that is not a whole number)
    try:
        if event == 'Quit' or event == sg.WIN_CLOSED:        
                break    
        # check for a valid number
        if (int(values['-IN-']) > 100 or int(values['-IN-']) < 1):
            sg.Popup('Enter a number between 1 and 100', auto_close=True, auto_close_duration=2)

        if (int(values['-IN-']))> secret:
            window['-OUT-'].update(values['-IN-'] + ' is too high, try again!')
            count+=1            
        elif (int(values['-IN-'])) < secret:
            window['-OUT-'].update(values['-IN-'] + ' is too low, try again!')
            count+=1           
        else:
            count+=1           
            window['-OUT-'].update(values['-IN-'] + ' is correct, in ' + str(count)+ ' tries, good job!')            
            # assign the popup to a variable so I can read the values returned from the buttons.
            myResult = sg.popup_yes_no("You're a Winner", 'Play again?', location=(2400, 600), no_titlebar=True)
            if myResult == "No":
                sg.popup_no_buttons("Thanks for playing!!", location=(2400, 600), no_titlebar=True, auto_close=True)
                break
            else:
                # we are going to play again
                window['-OUT-'].update('')
                secret = random.randrange(1, 101)                
                count = 0                          
        
    except ValueError:   
        sg.popup_no_buttons('Enter a whole number between 1 and 100', auto_close=True, no_titlebar=True )        

window.close()