import asyncio
import pygame

async def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    
    while True:
        screen.fill((255, 0, 0))  # Red screen
        pygame.display.flip()
        await asyncio.sleep(0.1)

asyncio.run(main())