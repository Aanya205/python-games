import pygame


screen = pygame.display.set_mode((800,800))

pygame.display.set_caption("Rock Paper Siccors Game")

background = pygame.image.load("rock paper siccors/backround image for rps game.webp")
screen.blit(background,(800,800))

paper = pygame.image.load("rock paper siccors/Paper For the RPS GAME.png")
screen.blit(paper,(400,250))

rock = pygame.image.load("Rock for the RPS Game.png")
screen.blit(rock,(400,500))

siccors= pygame.image.load("rock paper siccors/Siccors for the RPS Game.png")
screen.blit(siccors,(400,750))

kid= pygame.image.load("rock paper siccors/kid image for rps.jpg")
screen.blit(kid,(100,100))

robot= pygame.image.load("rock paper siccors/robot image for rps.jpg")
screen.blit(kid,(200,100))


# blit all images>
#gameover function>
# Another score function for the computer>
# create 2 shaps one on the left and one on the right(for ex right side robot image and left side human image)
#when the mouse if pressed on any of the images (3 if conditions) then a text should come on the screen saying stone has been selected elif if mouse is pressed on the siccors then siccor is selected and same for paper
score1 = 0
def score():
    score_font = pygame.font.Font("Arial", 20)
    score_surface = score.font.render("Score: "+ str(score1), True, "black")
    screen.blit(score_surface, (200,200)) 

score2 = 0
def score3():
    score_font2 = pygame.font.Font("Arial", 20)
    score_surface2 = score.font.render("Score: "+ str(score2), True, "black")
    screen.blit(score_surface2, (400,400)) 




def game_over():
    game_over_font = pygame.font.Font("Arial, 100")
    score_surface = game_over_font.render("Gameover", True, "brown")
    screen.blit(score_surface, (500,500))

# should i use mousebutton down? to check if the photos r being clicked


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()


# create a tkinter page sign up page
#apply sqlite database on top of it and store the detils in this database