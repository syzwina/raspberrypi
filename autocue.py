"""
Here is the News
A Raspberry Pi Auto Cue Test 1
"""

import time     # for delays
import os, pygame, sys

pygame.init() # initialise graphics interface
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption("Auto Cue Test 1")
screenWidth = 980
screenHeight = 610
screen = pygame.display.set_mode([screenWidth, screenHeight])
background = pygame.Surface((screenWidth, screenHeight))
segments = 4
segment = 0 # initial start place
textHeight = screenHeight / segments
textSurface = [pygame.Surface((screenWidth, textHeight)) for s in range(0, segments+1)]

# define the colours to use for the usre interface
cBackground = (0, 0, 0)
cText = (255, 255, 255)
background.fill(cBackground) # make background colour
font = pygame.font.Font(None, int(textHeight))

def main():
    lines = 5
    while True:
        for i in range(0, 5):
            setWords("This is line " + str(lines-1), i)
            lines += 1
            for offset in range(0, int(textHeight), 4):
                checkForEvent()
                # time.sleep(0.1)
                drawScreen(offset)

def drawScreen(offset): # draw to the screen
    global segment
    screen.blit(background, [0,0]) # set background colour
    for index in range(0, segments+1):
        segment+=1
        if (segment > segments): # wrap around segment number
            segment = 0
        drawWords(segment, offset)
    pygame.display.update()

def setWords(words, index):
    textSurface[index] = font.render(words, True, cText, cBackground)

def drawWords(index, offset):
    textRect = textSurface[index].get_rect()
    textRect.centerx = screenWidth / 2
    textRect.top = screenHeight - (textHeight * index) - offset
    screen.blit(textSurface[index], textRect)

def terminate(): # close down the program
    print ("Closing down, please wait.")
    pygame.quit() # close pygame
    sys.exit()

def checkForEvent(): # see if you need to quit
    event = pygame.event.poll()
    if event.type == pygame.QUIT :
        terminate()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        terminate()

if __name__ == '__main__':
    main()
