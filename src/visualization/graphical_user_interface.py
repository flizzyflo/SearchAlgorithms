import pygame
import sys

islands = [["W", "W", "W", "W", "W", "W", "W", "W"],
           ["W", "L", "W", "L", "L", "L", "W", "W"],
           ["W", "L", "W", "W", "W", "W", "W", "W"],
           ["W", "L", "L", "W", "W", "L", "W", "W"],
           ["W", "W", "W", "W", "W", "L", "W", "W"],
           ["W", "L", "W", "L", "W", "L", "W", "W"],
           ["W", "W", "W", "W", "W", "W", "W", "W"],
           ["W", "W", "W", "W", "W", "W", "W", "W"]]

WINDOW_WIDTH = len(islands) * 100
WINDOW_HEIGHT = len(islands[0]) * 100
GRID_WIDTH = WINDOW_WIDTH // len(islands)
GRID_HEIGHT = WINDOW_HEIGHT // len(islands)
def main():
    pygame.init()

    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))    

    while True:
        keys = pygame.key.get_pressed()
        draw_grid(screen= SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_w]:
                    print("w")
                    SCREEN.fill("white")
                if keys[pygame.K_s]:
                    SCREEN.fill("black")
            

        pygame.display.update()
        

def draw_grid(screen: pygame.Surface):
    x, y = 0, 0

    for row in range(0, WINDOW_WIDTH, GRID_WIDTH):
        
        y = 0
        
        for column in range(0, WINDOW_HEIGHT, GRID_WIDTH):
            
            if islands[y][x] == "W":
                rect = pygame.Rect(row, column, GRID_WIDTH, GRID_HEIGHT)
                pygame.draw.rect(screen,"darkblue", rect, 20)
            
            elif islands[y][x] == "L":
                rect = pygame.Rect(row, column, GRID_WIDTH, GRID_HEIGHT)
                pygame.draw.rect(screen,"lightgreen", rect, 20)
            
            if y + 1 > len(islands[0]):
                pass

            else:
                y += 1
        
        if x + 1 > len(islands):
                pass
        else:
            x += 1

if __name__ == '__main__':

    main()