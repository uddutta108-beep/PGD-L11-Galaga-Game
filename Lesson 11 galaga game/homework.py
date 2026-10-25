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


    if len(enemies) == 0:
        game_over()

def game_over():
    screen.draw.text("GAME OVER", (550, 300))

def update():
    global score, direction

    move_down = False

    if gun.dead == False:
        if keyboard.left:
            gun.x -= speed
            if gun.x >=WIDTH:
                gun.x = WIDTH

        elif keyboard.right:
            gun.x += speed
            if gun.x >= WIDTH:
                gun.x = WIDTH

    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove (bullet)

        else:
            bullet.y -= 10

    if len(enemies) > 0 and (enemies[-1].x > WIDTH-80 or enemies[0].x <80):

        move_down = True
        direction = direction * -1

    for enemy in enemies:
        enemy.x += 5*direction

        if move_down == True:
            enemy.y += 100

        if enemy.y > HEIGHT:
            enemies.remove (enemy)

        for bullet in bullets:
            if enemy.colliderect(bullet):
                score = score + 100

                bullets.remove(bullet)
                enemies.remove(enemy)

                if len(enemies) == 0:
                    game_over()

        if enemy.colliderect(gun):
            gun.dead = True

    if gun.dead:
        gun.countdown -= 1

    if gun.countdown == 0:
        gun.dead = False
        gun.countdown = 90

pgzrun.go()