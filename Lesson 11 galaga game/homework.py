import pgzrun

WIDTH = 1200
HEIGHT = 600

TITLE = "Galaga Fruit game"

gun = Actor("banana")
enemy = Actor("apple")

gun.pos = (600,550)

speed = 5

bullets = []
enemies = []

score = 0
direction = -1

gun.dead = False
gun.countdown  = 90

for x in range(8):
    for y in range(4):
        enemies.append (Actor("apple"))

        enemies[-1].x = 100 + 50 * x
        enemies[-1].y = 80 + 50 * y

def on_key_down(key):
    if gun.dead == False:
        if key == keys.SPACE:
            bullets.append(Actor("grape"))
            
            bullets[-1].x = gun.x
            bullets[-1].y = gun.y - 100

def draw():
    screen.clear()
    screen.fill("blue")

    screen.draw.text("Score:" + str(score), (50, 30))

    if gun.dead == False:
        gun.draw()

    for enemy in enemies:
        enemy.draw()

    for bullet in bullets:
        bullet.draw()

def update():
    pass


pgzrun.go()