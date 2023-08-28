import pygame
import random
from sys import exit

# pygame setup
pygame.init()
bottom_right=random.randrange(617, 817, 2)
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("runner ")
clock=pygame.time.Clock()
sky_surface=pygame.image.load('images/Sky.png')
#ground_surface=pygame.image.load('images/ground.png')
snail_surf=pygame.image.load('images/sample.png').convert_alpha()
snail2_surf=pygame.image.load('images/sample2.png').convert_alpha()
snail_rect=snail_surf.get_rect(bottomright=(600,bottom_right))
snail2_rect=snail2_surf.get_rect(topright=(600,-(1040-bottom_right)))
#snail3_rect=snail3_surf.get_rect(bottomright=(600,))
player_surf=pygame.image.load('images/player_walk_2.png').convert_alpha()
player_rect=player_surf.get_rect(midbottom=(80,200))


test_font=pygame.font.Font(None,50)
#score_surf=test_font.render('my game',False,(64,64,64))
font = pygame.font.Font(None, 36)
play_again_text = font.render("Play Again", True, (0, 0, 0))
play_again_rect = play_again_text.get_rect(center=(800 // 2, 400 - 50))
player_gravity=0
count=0
score_updated = False
pygame.mouse.set_visible(False)
while True:
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        game_active=False
        game_started=True

        if(game_started or game_active):
            if event.type==pygame.KEYDOWN: 
                if event.key ==pygame.K_SPACE:
                    player_gravity=-8
            if event.type==pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity=-8 
            else:
                if event.type==pygame.KEYDOWN: 
                    if event.key ==pygame.K_SPACE:
                        game_active=True

    if (game_active or game_started):
        score_surf=test_font.render('score:'+str(count),False,(64,64,64))
        score_rect=score_surf.get_rect(center=(400,50))
        screen.blit(sky_surface,(0,0))
        pygame.draw.rect(screen,'#c0e8ec',score_rect)
        pygame.draw.rect(screen,'#c0e8ec',score_rect,8)
        pygame.draw.line(screen,'blue',(2,0),(2,400))
        screen.blit(score_surf,score_rect)
   # screen.blit(ground_surface,(0,300))
    #player
        player_gravity+=0.8
        player_rect.y+=player_gravity
        screen.blit(player_surf,player_rect)
        snail_rect.left-=4
        snail2_rect.left-=4
        if snail_rect.right<=0: 
            bottom_right=random.randrange(617, 817, 2)
            snail_rect=snail_surf.get_rect(bottomright=(600,bottom_right))
            snail2_rect=snail2_surf.get_rect(topright=(600,-(1040-bottom_right)))
            snail_rect.left=800
            
       
            snail2_rect.left=800
            score_updated = False
        

        mouse_pos=pygame.mouse.get_pos()
        if(player_rect.colliderect(snail_rect)):
            print("collision")
            pygame.quit
        if(player_rect.colliderect(snail2_rect)):
            print("collision")
            pygame.quit
    
        screen.blit(snail2_surf,snail2_rect)   
        screen.blit(snail_surf,snail_rect)
        if snail_rect.right<=80 and not score_updated:
            count+=1
            score_updated = True
            
  
    #if(player_rect.colliderect(snail_rect)):   
     #   print("collision")\


    #if player_rect.collidepoint((mouse_pos)):
        #print("collosion")      
        #print(pygame.mouse.get_pressed())
        if snail_rect.colliderect(player_rect):
            game_active=False
            game_started=False


        if snail2_rect.colliderect(player_rect):
            game_active=False
            game_started=False


        if player_rect.bottom>=400 or  player_rect.top<=0:
            game_active=False
            game_started=False 
            
    else:
        if(count!=0):
            count2=count
        pygame.draw.rect(screen, (200, 200, 200), play_again_rect)
        screen.blit(play_again_text, play_again_rect.topleft)
        score_text = font.render(f"Score: {count2}", True, (0, 0, 0))
        score_rect = score_text.get_rect(center=(800 // 2, 400 // 2))
        screen.blit(score_text, score_rect.topleft)
        snail_rect.left=800       
        snail2_rect.left=800
        player_rect.top=200     
        count=0
        print("count=",count2)
        score_text = font.render(f"Score: {count2}", True, (0, 0, 0))
        

                
         



    pygame.display.update()#updates everything 
    clock.tick(60)