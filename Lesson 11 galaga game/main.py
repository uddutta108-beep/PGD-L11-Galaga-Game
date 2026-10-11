import pgzrun

WIDTH = 1200
HEIGHT = 600

TITLE = "Galaga Game"

ship = Actor("spaceship")
bug = Actor("bug")

ship.pos = (600,550)

speed = 5

bullets = []
enemies = []

score = 0
direction = 1

ship.dead  = False
ship.countdown = 90

for x in range(8):
    for y in range(4):
        enemies.append (Actor("bug"))

        enemies[-1].x = 100 + 50 * x
        enemies[-1].y = 80 + 50 * y

def on_key_down(key):
    if ship.dead == False:
        if key == keys.SPACE:
            bullets.append(Actor("bullet"))

            bullets[-1].x = ship.x
            bullets[-1].y = ship.y - 100

def draw():
    screen.clear()
    screen.fill("blue")

    screen.draw.text("Score:" + str(score), (50, 30))

    if ship.dead == False:
        ship.draw()

    for enemy in enemies:
        enemy.draw()

    for bullet in bullets:
        bullet.draw()





























pgzrun.go()