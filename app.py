class shoot:
    def player_fire(self):
        try:
            import pygame

        except:
            import time 
            import os
            print('currently you dont have pygame installed in your PC no need to worry this program will ayrimatically install pygame in your PC')
            time.sleep(2)
            f = open('pygame_install.bat','w')

            f.write('pip install pygame')

            f = open('pygame_install.bat','r')
            os.system('pygame_install.bat')

        finally:
            import pygame
            pygame.init()

            self.game_window = pygame.display.set_mode((1200,600))

            self.run = True
            self.red = (255,0,0)
            self.player_x = 70
            self.player_y = 555
            self.state = False
            self.jump = False
            self.vel_y = 15

            while self.run:
                for event in pygame.event.get():
                    self.key = pygame.key.get_pressed()

                    if event.type == pygame.QUIT:
                        self.run = False

                self.game_window.fill((255,255,255))
                self.player = pygame.draw.rect(self.game_window,self.red,[self.player_x,self.player_y,30,50])

                

                if self.key[pygame.K_RIGHT]:
                    self.player_x+=5

                if self.key[pygame.K_LEFT]:
                    self.player_x-=5

                if self.state == False:
                    if self.key[pygame.K_SPACE]:
                        self.state = True
                        self.bullet_x = self.player_x+20
                        self.bullet_y = self.player_y+20

                if self.state:
                    self.bullet = pygame.draw.rect(self.game_window,self.red,[self.bullet_x,self.bullet_y,30,10])
                    self.bullet_x+=20
                    if self.bullet_x>=1150:
                        self.state = False

                if not self.jump:
                    if self.key[pygame.K_UP]:
                        self.jump = True

                if self.jump:
                    self.player_y -=self.vel_y
                    self.vel_y -=1
                    if self.vel_y<-15:
                        self.vel_y = 15
                        self.jump = False


                
                

                pygame.time.delay(15)
                pygame.display.update()
            

            
                


shoot = shoot()

