#  Money example
#
#  Demonstrates overriding inherited DisplayText and InputText methods

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import pygwidgets
from DisplayMoney import *
from InputNumber import *

# 2 - Define constants
BLACK = (0, 0, 0)
BLACKISH = (10, 10, 10)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
title = pygwidgets.DisplayText(window, (0, 40),
                'Demo of InputNumber and DisplayMoney fields',
                fontSize=36, width=WINDOW_WIDTH, justified='center')

inputCaption = pygwidgets.DisplayText(window, (20, 150),
                'Input money amount (dollor):', fontSize=24,
                width=190, justified='right')
inputField = InputNumber(window, (230, 150), '', width=150, initialFocus=True)

inputCaption_euro = pygwidgets.DisplayText(window, (20, 200),
                'Input money amount (euro):', fontSize=24,
                width=190, justified='right')
inputField_euro = InputNumber(window, (230, 200), '', width=150)

okButton = pygwidgets.TextButton(window, (430, 200), 'OK')

outputCaption1 = pygwidgets.DisplayText(window, (20, 300),
                'Output dollars & cents:', fontSize=24,
                width=190, justified='right')
moneyField1 = DisplayMoney(window, (230, 300), '', textColor=BLACK,
                backgroundColor=WHITE, width=150)

outputCaption2 = pygwidgets.DisplayText(window, (20, 350),
                'Output euro & cents:', fontSize=24,
                width=190, justified='right')
moneyField2 = DisplayMoney(window, (230, 350), '', textColor=BLACK,
                backgroundColor=WHITE, width=150)

outputCaption3 = pygwidgets.DisplayText(window, (20, 400),
                'Output dollars only:', fontSize=24,
                width=190, justified='right')
moneyField3 = DisplayMoney(window, (230, 400), '', textColor=BLACK,
                backgroundColor=WHITE, width=150,
                showCents=False)

outputCaption4 = pygwidgets.DisplayText(window, (20, 450),
                'Output euro only:', fontSize=24,
                width=190, justified='right')
moneyField4 = DisplayMoney(window, (230, 450), '', textColor=BLACK,
                backgroundColor=WHITE, width=150,
                showCents=False)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # If the event was a click on the close box, quit pygame and the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pressing Return/Enter or clicking OK triggers action
        if inputField.handleEvent(event) or inputField_euro.handleEvent(event) or okButton.handleEvent(event):
            try:
                dollar_value = inputField.getValue()
                euro_value = inputField_euro.getValue()
            except ValueError:  # any remaining error
                inputField.setValue('(not a number)')
                inputField_euro.setValue('(not a number)')
            else:  # input was OK
                moneyField1.setValue(str(dollar_value))
                moneyField2.setValue(str(euro_value))
                moneyField3.setValue(str(dollar_value))
                moneyField4.setValue(str(euro_value))

    # 8  Do any "per frame" actions

    # 9 - Clear the window
    window.fill(BACKGROUND_COLOR)

    # 10 - Draw all window elements
    title.draw()
    inputCaption.draw()
    inputField.draw()
    inputCaption_euro.draw()
    inputField_euro.draw()
    okButton.draw()
    outputCaption1.draw()
    moneyField1.draw()
    outputCaption2.draw()
    moneyField2.draw()
    outputCaption3.draw()
    moneyField3.draw()
    outputCaption4.draw()
    moneyField4.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
