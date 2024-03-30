import pygame,sys
from pygame import Vector2
from Level import level

class Game:
    def __init__(self):
        # essentials ------
        pygame.init()
        self.level = level
        self.height = 1280
        self.weight = 720
        self.screen = pygame.display.set_mode((self.height,self.weight))
        self.fbs = pygame.time.Clock()
        self.player_attirbutes(6,300)
        self.monester_carrot(100,100,1,200)
        self.images()
        self.fonts()
        self.Settings()
        self.game_active = True
        self.stop = True
        self.main = False
        self.mouse_pos = pygame.mouse.get_pos()

    def Settings(self):
        self.volume = 100
        self.gamma = 100
        self.graphics = 'high'
        self.frames = 60

    def lose_screen(self):
        self.screen.fill((210, 40, 40))
        lose_text = self.font_6.render('You Lost', True, (20, 20, 20))
        self.screen.blit(lose_text, (580, 340))

    def images(self):
        self.bg_1 = pygame.image.load('Assets/ui/pattern_stop.png').convert()
        self.Button_1 = pygame.image.load('Assets/ui/resume_button.png').convert()
        self.Button_2 = pygame.image.load('Assets/ui/settings_button.png')
        self.Button_3 = pygame.image.load('Assets/ui/quit_button.png')
        self.game_paused_title = pygame.image.load('Assets/ui/game_paused_title.png').convert_alpha()

    def fonts(self):
        self.font_1 = pygame.font.Font(None, 16)
        self.font_2 = pygame.font.Font(None, 32)
        self.font_3 = pygame.font.Font(None, 64)
        self.font_4 = pygame.font.Font(None, 72)
        self.font_5 = pygame.font.Font(None, 120)
        self.font_6 = pygame.font.Font('Assets/dpcomic.ttf', 64)

        # sprites---------

    def player_attirbutes(self, step, health):
        self.Player_w1 = pygame.image.load('Assets/player/player_walk/Player_w_1.png')
        self.Player_w2 = pygame.image.load('Assets/player/player_walk/Player_w_2.png')
        self.Player_w3 = pygame.image.load('Assets/player/player_walk/Player_w_3.png')
        self.Player_w4 = pygame.image.load('Assets/player/player_walk/Player_w_4.png')

        self.Player_walk_list = [self.Player_w1, self.Player_w2, self.Player_w3, self.Player_w4]
        self.Player_index = 0
        self.Player_walk = self.Player_walk_list[self.Player_index]
        self.Player_pos = (self.height / 2, self.weight / 2)
        self.Player_rect = self.Player_walk.get_rect(center=(500,500))
        self.movement = [False, False, False, False]
        self.flip = False
        self.move = False
        self.speed = step
        self.c_speed = step / 1.2
        self.health = health
        self.player_health()

    def player_health(self):
        self.fonts()
        health_length = self.health * 1.5
        health_bar_rect = pygame.Rect(1100, 90, health_length, 50)
        health_bar = pygame.draw.rect(self.screen, (10, 190, 40), health_bar_rect)
        health_display = self.font_1.render(str(self.health), True, (100, 20, 20))
        self.screen.blit(health_display, (1100, 90))

    def Player_walk_anim(self, anim_speed):
        self.Player_index += anim_speed
        self.Player_walk = self.Player_walk_list[int(self.Player_index)]
        if self.Player_index >= 3:
            self.Player_index = 0
        if self.Player_index <= -3.5:
            self.Player_index = 0




    def monester_carrot(self,x,y,speed,health ):
        carrot_walk_1 = pygame.image.load('Assets/enemies/carrot/carrot_w_1.png')
        carrot_walk_2 = pygame.image.load('Assets/enemies/carrot/carrot_w_2.png')
        carrot_walk_3 = pygame.image.load('Assets/enemies/carrot/carrot_w_3.png')
        carrot_walk_4 = pygame.image.load('Assets/enemies/carrot/carrot_w_4.png')
        carrot_walk_5 = pygame.image.load('Assets/enemies/carrot/carrot_w_5.png')
        carrot_walk_6 = pygame.image.load('Assets/enemies/carrot/carrot_w_6.png')
        carrot_walk_7 = pygame.image.load('Assets/enemies/carrot/carrot_w_7.png')
        self.carrot_walk_list = [carrot_walk_1, carrot_walk_2, carrot_walk_3, carrot_walk_4, carrot_walk_5,
                                 carrot_walk_6, carrot_walk_7]
        self.carrot_index = 0
        self.moneste_health = health

        self.carrot_pos = Vector2(x,y)
        self.carrot_speed = speed


    def monester_carrot_anim(self, anim_speed):
        self.carrot_index += anim_speed
        self.carrot_walks = self.carrot_walk_list[int(self.carrot_index)]

        if self.carrot_index >= 6:
            self.carrot_index = 0



    def follow_player(self,player_pos):
        direction = player_pos - self.carrot_pos

        direction.normalize_ip()

        c_velocity = direction * self.speed / 1.5

        self.carrot_pos += c_velocity





    def run(self):
        while True:
            self.level().run()

            self.follow_player(self.Player_rect.topleft)
            print(self.carrot_pos,self.Player_rect.center)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.game_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.game_active = False
                            self.stop = True
                        if event.key == pygame.K_w:
                            self.movement[0] = True
                            self.move = True
                        if event.key == pygame.K_s:
                            self.movement[2] = True
                            self.move = True
                        if event.key == pygame.K_a:
                            self.movement[1] = True
                            self.flip = True
                            self.move = True
                        if event.key == pygame.K_d:
                            self.movement[3] = True
                            self.flip = False
                            self.move = True

                    if event.type == pygame.KEYUP:
                        self.Player_index = 0
                        if event.key == pygame.K_w:
                            self.movement[0] = False
                            self.move = False
                        if event.key == pygame.K_s:
                            self.movement[2] = False
                            self.move = False
                        if event.key == pygame.K_a:
                            self.movement[1] = False
                            self.move = False
                        if event.key == pygame.K_d:
                            self.movement[3] = False
                            self.move = False


            if self.game_active:

                if self.health <= 0:
                    self.game_active = False
                    self.stop = False
                    self.lose_screen()

                if self.Player_rect.y <= 0:
                    self.Player_rect.y = 0

                
                self.screen.fill((200, 200, 200))
                self.monester_carrot_anim(0.13)
                self.screen.blit(pygame.transform.scale(self.carrot_walks,(200,200)),self.carrot_pos)
                self.player_health()
                square_1 = pygame.Rect(20,20,100,50)
                #pygame.draw.rect(self.screen, (30, 30, 30), self.Player_rect)
                if self.Player_rect.colliderect(square_1):
                    self.health -= 1
                    pygame.draw.rect(self.screen,(30,30,30),square_1)
                else:
                    pygame.draw.rect(self.screen, (70, 70, 70), square_1)

                self.Player_rect.y -= (self.movement[0] - self.movement[2]) * self.speed
                self.Player_rect.x -= (self.movement[1] - self.movement[3]) * self.speed



                if self.move:
                    if self.flip:
                        self.screen.blit(pygame.transform.flip(self.Player_walk, True, False), self.Player_rect)
                    else:
                        self.screen.blit(self.Player_walk, self.Player_rect)
                    self.Player_walk_anim(0.1)
                else:
                    self.screen.blit(self.Player_walk,self.Player_rect)
                    self.move = False



            if self.game_active== False and self.stop == True:
                mouse_pos1 = pygame.mouse.get_pos()
                self.screen.blit(self.bg_1,(0,0))
                
                button_1_rect = pygame.Rect(515,315,250,73)
                button_2_rect = pygame.Rect(515, 408, 250, 73)
                button_3_rect = pygame.Rect(515, 501, 250, 73)
                self.screen.blit(self.Button_1,button_1_rect)
                self.screen.blit(self.Button_2,button_2_rect)
                self.screen.blit(self.Button_3, button_3_rect)
                self.screen.blit(self.game_paused_title,(487, 110))
                if button_1_rect.collidepoint(mouse_pos1):
                    self.Button_1.set_alpha(150)
                    if pygame.mouse.get_pressed()[0]:
                        self.game_active = True
                else:
                    self.Button_1.set_alpha(255)
                if button_2_rect.collidepoint(mouse_pos1):
                    self.Button_2.set_alpha(150)
                    if pygame.mouse.get_pressed()[0]:
                        self.game_active = True
                else:
                    self.Button_2.set_alpha(255)
                if button_3_rect.collidepoint(mouse_pos1):
                    self.Button_3.set_alpha(150)
                    if pygame.mouse.get_pressed()[0]:
                        pygame.quit()
                        sys.exit()
                else:
                    self.Button_3.set_alpha(255)
            if self.game_active == False and self.stop == False:
                self.lose_screen()


                    #487 - 110
            pygame.display.flip()
            self.fbs.tick(self.frames)

Game().run()