import sys
import pygame
import random
from _class.bullet import Bullet
from _class.alien import Alien

def check_keydown_events(event,settings,screen,ship,bullets):
    # 按下
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # elif event.key == pygame.K_DOWN:
    #     ship.moving_down = True
    # elif event.key == pygame.K_UP:
    #     ship.moving_up = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings,screen,ship,bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def check_keyup_events(event,ship):
    # 松开
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(settings,screen,ship,bullets):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(settings , screen , ship ,aliens ,bullets):
    # 刷新屏幕
    screen.fill(settings.bg_color)
    # 展示子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 展示飞行物和靶子
    ship.blitme()
    aliens.draw(screen)
    # 设为可见
    pygame.display.flip()

def fire_bullet(settings , screen ,ship ,bullets):
    # 创建一颗子弹 存入bullets数组中
    new_bullet = Bullet(settings, screen, ship)
    bullets.add(new_bullet)

def del_bullet(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_fleet(settings,screen,aliens):
    # 创建靶子群
    alien = Alien(settings,screen)
    alien_width = alien.rect.width
    available_x_space = settings.screen_width - 2 * alien_width
    max_alien_num = int(available_x_space / (2 * alien_width))

    for alien_number in range(max_alien_num):
        alien = Alien(settings ,screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        # 随机生成外星人
        random_seed = random.randint(1,10)
        if random_seed<=5:
            aliens.add(alien)