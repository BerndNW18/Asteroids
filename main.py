# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            collided = asteroid.collision(player)
            if collided:
                print("Collision! Game over!")
                running = False

            for shot in shots:
                if asteroid.collision(shot):
                    print("Asteroid hit!")
                    asteroid.split()
                    shot.kill()

        for draw_item in drawable:
            draw_item.draw(screen)  

        
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()




if __name__ == "__main__":
    main()
