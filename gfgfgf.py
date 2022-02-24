import pygame as py
import lvl_setter as lvl

from sys import exit
import math
from math import *
#classes
class Player(py.sprite.Sprite):
    def __init__(self, bullet_count):
        super().__init__()
        self.image = py.transform.rotozoom(py.image.load('placeholder.png').convert_alpha(),0,0.33)
        self.rect = self.image.get_rect(midbottom = (512,384))
        self.gun = py.transform.rotozoom(py.image.load('gunlmao.png').convert_alpha(),0,0.33)
        self.grnd_im = py.transform.rotozoom(py.image.load('grndplc.png').convert_alpha(),0,0.33)
        self.gravy=0
        self.gravx=0
        self.ang=0
        self.flip_left = True
        self.flip_right = False
        self.gun_copy = self.gun
        self.isgunrot = True
        self.bullet_count = bullet_count
        self.remove_ = True
        self.allowed = True
        self.obst_list = 0
        self.coll_with = 0
        self.the_y = 0
        self.can_tp = True
    def movement(self):
        self.mouse_button = py.mouse.get_pressed()
        self.keys = py.key.get_pressed()
        if self.isgunrot:
            if self.keys[py.K_a]:self.rect.x-=5
            elif self.keys[py.K_d]:self.rect.x+=5
        self.rect.x+=self.gravx
        self.rect.y+=self.gravy
        self.obst_count = len(obst_group.sprites())
    def gun_spin(self):
        try:
            self.mouse_pos = py.mouse.get_pos()
            if self.mouse_pos[1] < self.rect.centery:
                if self.mouse_pos[0]>self.rect.centerx:
                    if self.flip_right:
                        self.gun = py.transform.flip(self.gun,False,True)
                    self.flip_right = False
                    self.flip_left = True
                    self.hipot = sqrt((self.mouse_pos[0]-self.rect.centerx)**2+(self.mouse_pos[1]-self.rect.centery)**2)
                    self.other = sqrt((self.mouse_pos[0]-self.rect.centerx)**2)
                    self.cosinus = self.other/self.hipot
                    self.degree = math.acos(self.cosinus) * (180/math.pi)
                    self.gun_copy = py.transform.rotate(self.gun,self.degree) 
                    display.blit(self.gun_copy,(self.rect.centerx - int(self.gun_copy.get_width()/2), self.rect.centery - int(self.gun_copy.get_height()/2)))
                else:
                    if self.flip_left:
                        self.gun = py.transform.flip(self.gun,False,True)
                    self.flip_right = True
                    self.flip_left = False
                    self.hipot = -1*(sqrt((self.mouse_pos[0]-self.rect.centerx)**2+(self.mouse_pos[1]-self.rect.centery)**2))
                    self.other = -1*(sqrt((self.mouse_pos[0]-self.rect.centerx)**2))
                    self.cosinus = -1*(self.other/self.hipot)
                    self.degree = (math.acos(self.cosinus) * (180/math.pi))
                    self.gun_copy = py.transform.rotate(self.gun,self.degree)
                    display.blit(self.gun_copy,(self.rect.centerx - int(self.gun_copy.get_width()/2), self.rect.centery - int(self.gun_copy.get_height()/2)))
                self.other2 = sqrt((self.mouse_pos[1]-self.rect.centery)**2)

            else:
                if self.mouse_pos[0]>self.rect.centerx:
                    if self.flip_right:
                        self.gun = py.transform.flip(self.gun,False,True)
                    self.flip_right = False
                    self.flip_left = True

                    self.hipot = (sqrt((self.mouse_pos[0]-self.rect.centerx)**2+(self.mouse_pos[1]-self.rect.centery)**2))
                    self.other = (sqrt((self.mouse_pos[0]-self.rect.centerx)**2))
                    self.cosinus = self.other/self.hipot
                    self.degree = -1*(math.acos(self.cosinus) * (180/math.pi))
                    self.gun_copy = py.transform.rotate(self.gun,self.degree) 
                    display.blit(self.gun_copy,(self.rect.centerx - int(self.gun_copy.get_width()/2), self.rect.centery - int(self.gun_copy.get_height()/2)))

                else:
                    if self.flip_left:
                        self.gun = py.transform.flip(self.gun,False,True)
                    self.flip_right = True
                    self.flip_left = False
                    self.hipot = -1*(sqrt((self.mouse_pos[0]-self.rect.centerx)**2+(self.mouse_pos[1]-self.rect.centery)**2))
                    self.other = -1*(sqrt((self.mouse_pos[0]-self.rect.centerx)**2))
                    self.cosinus = -1*(self.other/self.hipot)
                    self.degree = -1*(math.acos(self.cosinus) * (180/math.pi))
                    self.gun_copy = py.transform.rotate(self.gun,self.degree)
                    display.blit(self.gun_copy,(self.rect.centerx - int(self.gun_copy.get_width()/2), self.rect.centery - int(self.gun_copy.get_height()/2)))
                self.other2 = -1*(sqrt((self.mouse_pos[1]-self.rect.centery)**2))
        except ZeroDivisionError:
            print('lmaooooooooooo')
    def gun_mob(self):
        if self.mouse_button[0] and self.bullet_count !=0 and self.remove_:
            self.rect.y-=5
            self.allowed,self.isgunrot = True,False
            self.gravx = -1*(self.other / 40)
            if self.other2 <0:
                if self.degree<-60 and self.degree > - 130:
                    self.gravy = -11 + (self.other2 / 100)
                else:
                    self.gravy = -6 + (self.other2 / 100)
            else:
                self.gravy = 15 - (self.other2 / 100)
            if self.other < 0:
                self.gravx+=6
            else:
                self.gravx-=6
            self.bullet_count -=1
            self.remove_=False
        if not self.mouse_button[0]:
            self.remove_=True
        if self.gravx<0:
            self.gravx+=0.2
        else:
            self.gravx-=0.2
        if self.gravx > -1 and self.gravx <1:
            self.gravx = 0

        
    def coll_handle(self):
        if self.allowed:
            if self.gravy <7:
                self.gravy +=0.4
            if self.gravy>2:
                self.isgunrot = False
        self.coll_with = py.sprite.spritecollide(player.sprite,obst_group,False)
        if self.coll_with:
            self.isgunrot = True
            self.the_y = self.coll_with[0].rect[1]
            self.allowed = False
            if self.rect.bottom - self.the_y<=16:
                self.gravy = 0
                self.rect.bottom = self.the_y
            else:
                self.gravx = 0
                self.gravy = 0
                self.isgunrot = False
                self.allowed = True
                if self.rect.bottom >= self.coll_with[0].rect.bottom:
                    self.can_tp = False
                    self.gravy = 0
                    self.rect.top = self.coll_with[0].rect.bottom
                if self.can_tp:
                    if self.rect.x > self.coll_with[0].rect.x:
                        self.rect.left = self.coll_with[0].rect.right
                        self.gravx = 0
                    elif self.rect.x < self.coll_with[0].rect.x:
                        self.rect.right = self.coll_with[0].rect.left
                        self.gravx = 0

        else:
            self.can_tp = True
            self.allowed = True
        


    def float_text(self,name,rgb,xy):
        self.rand_text=font.render(str(name),True,rgb)
        self.rand_text_rect = self.rand_text.get_rect(center = xy)
        display.blit(self.rand_text,self.rand_text_rect)
    def update(self):
        self.movement()
        self.gun_spin()
        self.gun_mob()
        self.coll_handle()
        self.float_text(f'Bullets: {self.bullet_count}',(0,0,0),(660,50))
class Platform(py.sprite.Sprite):
    def __init__ (self,name,pos):
        super().__init__()
        self.image = py.transform.rotozoom(py.image.load(name).convert_alpha(),0,0.33)
        self.rect = self.image.get_rect(topleft = pos)
        self.obst_list = []
    def update(self):
        pass
class Editor_obj(py.sprite.Sprite):
    def __init__(self,parametr,pos):
        super().__init__()
        self.pos2 = pos
        self.pos = (0,0) 
        self.image = py.image.load('editor.png').convert_alpha()
        self.rect = self.image.get_rect(center = (0,0))
        self.parametr = parametr

    def update(self):
        if self.parametr == 0:
            self.pos = ((py.mouse.get_pos()[0]//8)*8,(py.mouse.get_pos()[1]//8)*8)
            self.rect = self.image.get_rect(center = self.pos)
        else:
            self.rect = self.image.get_rect(center = self.pos2)

#misc
game_state = 0
clock = py.time.Clock()
py.init()
display = py.display.set_mode((1024,768))
py.display.set_caption('Shot Jumper')
font = py.font.Font('BAUHS93.TTF',50)
index = 1

#functions

def placeholder(limit):
    global index
    levol = lvl.spr_list('bruhsmth.txt')
    useful_stuff = lvl.make_coord(levol)
    if index < len(useful_stuff):
        print(index)
        if useful_stuff[index-1] == 100:
            name = 'grndplc.png'
        obst_group.add(Platform(name, useful_stuff[index]))
        index+=2
    if py.key.get_pressed()[py.K_e]:
        index = 1
def editor():
    global game_state
    index = 1
    one_way = True
    two_way = True
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                exit()
            if event.type == py.KEYDOWN and event.key == py.K_e:
                if game_state == 0: game_state =1
                else:
                    obst_group.empty()
                    lvl.close_out('bruhsmth.txt')
                    game_state = 0
        if game_state ==0:
            break
        display.fill((255,255,255))
        coords = ((py.mouse.get_pos()[0]//8)*8,(py.mouse.get_pos()[1]//8)*8)
        if py.mouse.get_pressed()[0] and two_way:
            editor_group.add(Editor_obj(1,coords))
            lvl.write_to_file(100,coords, 'bruhsmth.txt')
            two_way = False
        if not py.mouse.get_pressed()[0]:
            two_way = True
        if one_way:
            thee_edit_block.add(Editor_obj(0,coords))
            one_way = False
        editor_group.draw(display)
        editor_group.update()
        thee_edit_block.draw(display)
        thee_edit_block.update()
        py.display.update()
        clock.tick(60)
def main(bullet):
    global game_state
    player.add(Player(bullet))
    if game_state == 0:
        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    exit()
                if event.type == py.KEYDOWN and event.key == py.K_e:
                    if game_state == 0:
                        index = 1
                        lvl.start_out('bruhsmth.txt')
                        editor_group.empty()
                        game_state =1
                    else:
                        game_state = 0
            display.fill((255,255,255))
            player.draw(display)
            placeholder(100)
            obst_group.draw(display)
            player.update()
            obst_group.update()
            if game_state ==1:
                break
            py.display.update()
            clock.tick(60)

            
#surfaces
grnd = py.transform.rotozoom(py.image.load('grndplc.png').convert_alpha(),0,0.32)
player = py.sprite.GroupSingle()
obst_group = py.sprite.Group()
thee_edit_block = py.sprite.GroupSingle() 
editor_group = py.sprite.Group()
editor_block_outline = py.image.load('editor.png').convert_alpha()


while True:
    if game_state == 0:
        main(50)
    else:
        editor()

