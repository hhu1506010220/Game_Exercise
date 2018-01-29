import sys
import pygame
from _class.bullet import Bullet

def check_keydown_events(event,settings,screen,ship,bullets):
    # 按下
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings,screen,ship,bullets)

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

def update_screen(settings , screen , ship ,bullets):
    # 刷新屏幕
    screen.fill(settings.bg_color)
    # 展示子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 展示飞行物
    ship.blitme()
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

