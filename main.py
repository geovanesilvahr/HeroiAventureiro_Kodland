# -*- coding: utf-8 -*-
import random

import pgzrun
from pygame import Rect

WIDTH = 600
HEIGHT = 600
TILE_SIZE = 16

MENU = "menu"
GAME = "game"
EXIT = "exit"

game_state = MENU
sound_on = True

start_button = Rect((100, 80), (120, 30))
sound_button = Rect((100, 130), (120, 30))
exit_button = Rect((100, 180), (120, 30))

def generate_map(rows, cols):
    result = []
    for y in range(rows):
        row = []
        for x in range(cols):
            if y == 0 or y == rows - 1 or x == 0 or x == cols - 1:
                row.append(1)
            else:
                row.append(random.choice([0, 0, 0, 2]))
        result.append(row)
    return result

map_data = generate_map(30, 40)

class Character:
    def __init__(self, image_base, pos):
        self.image_base = image_base
        self.image = image_base
        self.x, self.y = pos
        self.frame = 0
        self.hp = 100
        self.attack_range = 40
        self.damage = 10
        self.timer = 0

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if not is_colliding(new_x, new_y):
            self.x = new_x
            self.y = new_y
        self.animate()

    def animate(self):
        self.timer += 1
        if self.timer >= 10:
            self.frame = (self.frame + 1) % 2
            self.image = self.image_base
            self.timer = 0

    def attack(self, enemies):
        for enemy in enemies:
            if distance_to(self, enemy) < self.attack_range:
                enemy.take_damage(self.damage)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Enemy:
    def __init__(self, image, pos, bounds):
        self.image = image
        self.x, self.y = pos
        self.bounds = bounds
        self.hp = 30
        self.wait_time = 0

    def patrol(self):
        if self.hp <= 0:
            return
        self.wait_time += 1
        if self.wait_time >= 30:
            dx = random.choice([-TILE_SIZE, 0, TILE_SIZE])
            dy = random.choice([-TILE_SIZE, 0, TILE_SIZE])
            new_x = self.x + dx
            new_y = self.y + dy
            if self.bounds.collidepoint((new_x, new_y)) and not is_colliding(new_x, new_y):
                self.x = new_x
                self.y = new_y
            self.wait_time = 0

    def take_damage(self, dmg):
        self.hp -= dmg
        print(f"Inimigo recebeu {dmg} de dano! HP restante: {self.hp}")

    def draw(self):
        if self.hp > 0:
            screen.blit(self.image, (self.x, self.y))

def distance_to(a, b):
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5

def draw():
    screen.clear()
    if game_state == MENU:
        screen.draw.text("Heroi Aventureiro", center=(WIDTH//2, 40), fontsize=32, color="white")
        screen.draw.filled_rect(start_button, "blue")
        screen.draw.text("Iniciar Jogo", center=start_button.center, fontsize=24, color="white")

        screen.draw.filled_rect(sound_button, "blue")
        sound_status = "Audio: ON" if sound_on else "Audio: OFF"
        screen.draw.text(sound_status, center=sound_button.center, fontsize=24, color="white")

        screen.draw.filled_rect(exit_button, "blue")
        screen.draw.text("Sair", center=exit_button.center, fontsize=24, color="white")

    elif game_state == GAME:
        draw_map()
        hero.draw()
        for enemy in enemies:
            enemy.draw()
        screen.draw.text(f"HP: {hero.hp}", (10, 10), color="white")

def draw_map():
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            tile_image = f"tile_000{tile}"
            screen.blit(tile_image, (x * TILE_SIZE, y * TILE_SIZE))

def update():
    if game_state == GAME:
        dx = dy = 0
        if keyboard.right: dx = 2
        if keyboard.left: dx = -2
        if keyboard.up: dy = -2
        if keyboard.down: dy = 2
        hero.move(dx, dy)
        for enemy in enemies:
            enemy.patrol()

def on_key_down(key):
    if game_state == GAME and key == keys.SPACE:
        hero.attack(enemies)

def on_mouse_down(pos):
    global game_state, sound_on
    if game_state == MENU:
        if start_button.collidepoint(pos):
            game_state = GAME
        elif sound_button.collidepoint(pos):
            sound_on = not sound_on
        elif exit_button.collidepoint(pos):
            exit()

def is_colliding(x, y):
    col = int(x // TILE_SIZE)
    row = int(y // TILE_SIZE)
    if 0 <= row < len(map_data) and 0 <= col < len(map_data[0]):
        return map_data[row][col] in (1, 2)
    return True

hero = Character("tile_0098", (TILE_SIZE * 6, TILE_SIZE * 6))
enemies = [
    Enemy("tile_0122", (TILE_SIZE * 10, TILE_SIZE * 5), Rect(80, 64, 96, 96)),
    Enemy("tile_0122", (TILE_SIZE * 14, TILE_SIZE * 7), Rect(160, 96, 64, 96))
]

pgzrun.go()
