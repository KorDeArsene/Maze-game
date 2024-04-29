from pygame import  *

window = display.set_mode((1400, 1000))
display.set_caption('Temple Run')
bg = transform.scale(image.load('background.jpg'), (1400, 1000))
player = transform.scale(image.load('hero.png'), (125, 125))
enemy = transform.scale(image.load('cyborg.png'), (125, 125))
treasure = transform.scale(image.load('treasure.png'), (150, 150))
x1 = 75
y1 = 650
x2 = 1200
speed = 10
speed_enemy = 5
player_rect = player.get_rect()
player_rect.topleft = (x1, y1)
enemy_rect = enemy.get_rect()
enemy_rect.topleft = (x2,550)
treasure_rect = treasure.get_rect()
treasure_rect.topleft = (1100, 800)
merah = (255,0,0)
wall1 = Surface((20, 600))
wall1.fill(merah)
wall2 = Surface((20, 175))
wall2.fill(merah)
wall3 = Surface((1100, 20))
wall3.fill(merah)
wall4 = Surface((1100, 20))
wall4.fill(merah)
wall5 = Surface((20, 980))
wall5.fill(merah)
wall6 = Surface((20, 800))
wall6.fill(merah)
wall7 = Surface((20, 450))
wall7.fill(merah)
wall8 = Surface((20, 340))
wall8.fill(merah)
wall9 = Surface((20, 790))
wall9.fill(merah)
wall10 = Surface((20, 150))
wall10.fill(merah)
wall11 = Surface((150, 20))
wall11.fill(merah)
font.init()
font = font.Font(None, 200)
win_text = font.render('YOU WIN!', True, (0, 255, 0))
lose_text = font.render('YOU LOSE!', True, (0, 255, 0))

mixer.init()
bg_sound = mixer.Sound('jungles.ogg')
lose_sound = mixer.Sound('kick.ogg')
win_sound = mixer.Sound('money.ogg')
volume = 0.2
bg_sound.play()
bg_sound.set_volume(volume)

maze_wall = [(250, 15), (250, 800), (250, 15), (250, 975), (1350, 15), (450, 15), (650, 15), (650, 650), (950, 200), (800, 650), (800, 650)]
wall1_rect = wall1.get_rect()
wall1_rect.topleft = maze_wall[0]
wall2_rect = wall2.get_rect()
wall2_rect.topleft = maze_wall[1]
wall3_rect = wall3.get_rect()
wall3_rect.topleft = maze_wall[2]
wall4_rect = wall4.get_rect()
wall4_rect.topleft = maze_wall[3]
wall5_rect = wall5.get_rect()
wall5_rect.topleft = maze_wall[4]
wall6_rect = wall6.get_rect()
wall6_rect.topleft = maze_wall[5]
wall7_rect = wall7.get_rect()
wall7_rect.topleft = maze_wall[6]
wall8_rect = wall8.get_rect()
wall8_rect.topleft = maze_wall[7]
wall9_rect = wall9.get_rect()
wall9_rect.topleft = maze_wall[8]
wall10_rect = wall10.get_rect()
wall10_rect.topleft = maze_wall[9]
wall11_rect = wall11.get_rect()
wall11_rect.topleft = maze_wall[10]
run = True
clock = time.Clock()
FPS = 60
posisi = 'left'
game_over = False
while run:  
   for e in event.get():
      if e.type == QUIT:
         run = False
   if not game_over:
      keys = key.get_pressed()
      if keys[K_a] and player_rect.x > 5:
         player_rect.x -= speed
      if keys[K_d] and player_rect.x < 1245:
         player_rect.x += speed
      if keys[K_w] and player_rect.y > 5:
         player_rect.y -= speed
      if keys[K_s] and player_rect.y < 845:
         player_rect.y += speed
      if enemy_rect.x <= 1000:
         posisi = 'left'
      if enemy_rect.x >= 1200:
         posisi = 'right'
      if posisi == 'left':
         enemy_rect.x += speed_enemy
      if posisi == 'right':
         enemy_rect.x -= speed_enemy
      window.blit(bg, (0, 0))
      window.blit(player, player_rect)
      window.blit(enemy, enemy_rect)
      window.blit(treasure, treasure_rect)
      window.blit(wall1, wall1_rect)
      window.blit(wall2, wall2_rect)
      window.blit(wall3, wall3_rect)
      window.blit(wall4, wall4_rect)
      window.blit(wall5, wall5_rect)
      window.blit(wall6, wall6_rect)
      window.blit(wall7, wall7_rect)
      window.blit(wall8, wall8_rect)
      window.blit(wall9, wall9_rect)
      window.blit(wall10, wall10_rect)
      window.blit(wall11, wall11_rect)
      if player_rect.colliderect(enemy_rect) or player_rect.colliderect(wall1_rect) or player_rect.colliderect(wall2_rect) or player_rect.colliderect(wall3_rect) or player_rect.colliderect(wall4_rect) or player_rect.colliderect(wall5_rect) or player_rect.colliderect(wall6_rect) or player_rect.colliderect(wall7_rect) or player_rect.colliderect(wall8_rect) or player_rect.colliderect(wall9_rect) or player_rect.colliderect(wall10_rect) or player_rect.colliderect(wall11_rect):
         lose_sound.play()
         lose_sound.set_volume(volume)
         game_over = True
         window.blit(lose_text, (350, 500))
      if player_rect.colliderect(treasure_rect):
         win_sound.play()
         win_sound.set_volume(volume)
         game_over = True
         window.blit(win_text, (350, 500))
   display.update()
   clock.tick(FPS)