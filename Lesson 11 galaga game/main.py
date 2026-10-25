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

    if len(enemies) == 0:
        game_over()

def game_over():
    screen.draw.text("GAME OVER", (550, 300))

def update():
    global score, direction

    move_down = False

    if ship.dead == False:
        if keyboard.left:
            ship.x -= speed
            if ship.x <= 0:
                ship.x = 0

        elif keyboard.right:
            ship.x += speed
            if ship.x >= WIDTH:
                ship.x = WIDTH

    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove (bullet)

        else:
            bullet.y -= 10

    if len(enemies)>0 and (enemies[-1].x > WIDTH-80 or enemies[0].x < 80):

        move_down = True
        direction = direction*-1

    for enemy in enemies:
        enemy.x += 5*direction

        if move_down == True:
            enemy.y += 100

        if enemy.y >HEIGHT:
            enemies.remove(enemy)

        for bullet in bullets:
            if enemy.colliderect(bullet):
                score = score + 100

                bullets.remove(bullet)
                enemies.remove(enemy)

                if len(enemies) == 0:
                    game_over()

        if enemy.colliderect(ship):
            ship.dead = True

    if ship.dead:
        ship.countdown -= 1

    if ship.countdown == 0:
        ship.dead = False
        ship.countdown = 90

pgzrun.go()