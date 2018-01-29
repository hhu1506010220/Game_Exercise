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

def get_aline_num(settings,alien_width):
    available_x_space = settings.screen_width - 2 * alien_width
    max_alien_num = int(available_x_space / (2 * alien_width))
    return max_alien_num

def get_row_num(settings,ship_height,alien_height):
    available_y_space = (settings.screen_height - (3 * alien_height) - ship_height)
    row_num = int(available_y_space / (2 * alien_height))
    return row_num

def create_alien(settings,screen,aliens,alien_num,row_num):
    alien = Alien(settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_num
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2* alien.rect.height * row_num
    # 随机生成外星人
    random_seed = random.randint(1, 10)
    if random_seed <= 5:
        aliens.add(alien)

def create_fleet(settings,screen,ship,aliens):
    # 创建靶子群
    alien = Alien(settings,screen)
    alien_number_x = get_aline_num(settings,alien.rect.width)
    row_number_y = get_row_num(settings,ship.rect.height,alien.rect.height)
    for row_number in range(row_number_y):
        for alien_number in range(alien_number_x):
            create_alien(settings,screen,aliens,alien_number,row_number)

def update_aliens(settings,aliens):
    # 检查是否有外星人碰到边缘
    check_fleet_edges(settings,aliens)
    aliens.update()

def change_fleet_direction(settings, aliens):
    """Drop the entire fleet, and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1

def check_fleet_edges(settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break