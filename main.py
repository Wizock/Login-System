from api import *
from admin import *
import sqlite3

def main():
    while True:
        pygame.event.pump()
        if keyPressed('space'):
            break
    endWait()
if __name__=="__main__":
    main()



