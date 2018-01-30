import sys
import pygame
import random
from time import sleep
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

def check_play_button(settings,screen,status,scoreboard,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not status.game_active:
        # 重置
        settings.init_speed()
        pygame.mouse.set_visible(False)
        status.reset_stats()
        status.game_active = True

        # 重置记分牌
        scoreboard.prep_score()
        scoreboard.prep_high_score()
        scoreboard.prep_level()
        scoreboard.prep_ships()

        # 清空数据
        aliens.empty()
        bullets.empty()
        create_fleet(settings,screen,ship,aliens)
        ship.center_ship()

def check_events(settings,screen,status,scoreboard,play_button,ship,aliens,bullets):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x ,mouse_y = pygame.mouse.get_pos()
            check_play_button(settings,screen,status,scoreboard,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def update_screen(settings , screen , status , scoreboard , ship ,aliens ,bullets,play_button):
    # 刷新屏幕
    # screen.fill(settings.bg_color)
    screen.blit(settings.background_image,(0,0))
    # 展示子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 展示飞行物和靶子
    ship.blitme()
    aliens.draw(screen)
    scoreboard.show_score()

    # 如果游戏处于非活跃状态 显示Play按钮
    if not status.game_active:
        play_button.draw_button()
    # 设为可见
    pygame.display.flip()

def fire_bullet(settings , screen ,ship ,bullets):
    # 创建一颗子弹 存入bullets数组中
    new_bullet = Bullet(settings, screen, ship)
    bullets.add(new_bullet)

def del_bullet(settings,screen,status,scordboard,ship,aliens,bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_isBoom(settings,screen,status,scordboard,ship,aliens,bullets)

def check_isBoom(settings,screen,status,scordboard,ship,aliens,bullets):
    # 若有子弹击中外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            status.score += settings.alien_points * len(aliens)
            scordboard.prep_score()
        check_high_score(status,scordboard)
    if len(aliens) == 0:
        bullets.empty()
        settings.increase_speed()
        create_fleet(settings, screen, ship, aliens)
        # 提高等级
        status.level += 1
        scordboard.prep_level()

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


def ship_hit(ai_settings, screen, stats, scoreboard, ship, aliens, bullets):
    # 被撞到
    if stats.ships_left > 0:
        stats.ships_left -= 1
        scoreboard.prep_ships()
        aliens.empty()
        bullets.empty()
        # 创建一堆新的靶子，飞船也重置
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def update_aliens(settings,screen,status,scoreboard,ship,aliens,bullets):
    # 检查是否有外星人碰到边缘
    check_fleet_edges(settings,aliens)
    aliens.update()
    # 如果和飞船发生碰撞则结束
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(settings,screen,status,scoreboard,ship,aliens,bullets)
    # 检查是否有靶子到达底部
    check_aliens_bottom(settings,screen,status,scoreboard,ship,aliens,bullets)

def change_fleet_direction(settings, aliens):
    """Drop the entire fleet, and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1

def check_fleet_edges(settings, aliens):
    # 是否有碰到边缘的靶子
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def check_aliens_bottom(ai_settings, screen, stats,scoreboard, ship, aliens, bullets):
    # 是否有碰到底部的靶子
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen , stats, scoreboard, ship, aliens, bullets)
            break

def check_high_score(stats, scoreboard):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.prep_high_score()