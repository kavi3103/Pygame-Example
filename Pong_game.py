import pygame

# initialise pygame
pygame.init()

dis = pygame.display.set_mode((800,600))

# set caption
pygame.display.set_caption('Pong game')

# paddle x and y points
paddle_x = 200
paddle_y = 520

# ball centre x and y point
ball_x = 400
ball_y = 300

# change ball direction
directionx = 0
directiony = 0

# score
score_value = 0

textX = 10
testY = 10

font = pygame.font.Font('freesansbold.ttf', 32)

missed = 0

# game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

running = True

def show_score(x, y):
    # to show score
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    dis.blit(score, (x, y))


def game_over():
    # to show game over
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    dis.blit(over_text, (200, 200))

def paddle(x,y):
    # draw paddle
    pygame.draw.rect(dis, (255,255,255), pygame.Rect(x, y, 200, 40))

def ball(x,y):
    # draw ball
    pygame.draw.circle(dis,(255,255,255),(x,y),20)

# Game loop

while running:

    # get all events
    for events in pygame.event.get():
        # when quit is pressed
        if events.type == pygame.QUIT:
            running = False

        # when keystroke is pressed
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT:
                paddle_x -= 30
            if events.key == pygame.K_RIGHT:
                paddle_x += 30

    # when boundary conditions change direction
    if ball_x == 0:
        directionx = 1
    if ball_x == 780:
        directionx = 0

    if ball_y == 0:
        directiony = 1
    if ball_y == 580:
        directiony = 0

    if directionx == 0:
         ball_x -= 1
    if directionx == 1:
         ball_x += 1

    if directiony == 0:
        ball_y -= 1
    if directiony == 1:
        ball_y += 1

    # if ball hits paddle
    if paddle_y == ball_y + 20:
        if (ball_x >= paddle_x) and (ball_x <= paddle_x+200):
            directiony = 0
            score_value += 1

    # if the ball is missed
    if ball_y == 550:
        missed += 1

    # end game
    if missed == 10:
        #print ("game over")
        game_over()
        print("score : ", score_value)
        pygame.display.update()
        running = False
        break


    dis.fill((0,0,0))
    ball(ball_x,ball_y)
    paddle(paddle_x,paddle_y)
    show_score(textX, testY)
    pygame.display.update()