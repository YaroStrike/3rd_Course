import pygame
import math
import random
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Инициализация Pygame
pygame.init()

# Настройка дисплея
WIDTH, HEIGHT = 1366, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
backgrounds = ['vostochny.jpg', 'tropo.jpg', 'strato.jpg', 'ISS.jpg']
current_bg_index = 0
background_image = pygame.image.load(backgrounds[current_bg_index])
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Свойства ракеты
rocket_pos = [(WIDTH // 2)-20, HEIGHT - 245]
thrust = 0.9
gravity = 9.81
game_started = False
rocket_image = pygame.image.load('angara1.png')
rocket_image = pygame.transform.scale(rocket_image, (40, 240))
initial_rocket_pos = rocket_pos[1]

# Функция для отображения стартового меню
def show_start_menu():
    font = pygame.font.Font(None, 74)
    text = font.render("Нажми SPACE для начала", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()

# Функция для отображения мощности и гравитации
def display_interface(thrust, gravity):
    font = pygame.font.Font(None, 36)
    thrust_text = font.render(f"Мощь: {thrust:.2f}", True, (255, 255, 255))
    gravity_text = font.render(f"Гравитация: {gravity:.2f} м/c²", True, (255, 255, 255))
    screen.blit(thrust_text, (10, HEIGHT - 65))
    screen.blit(gravity_text, (10, HEIGHT - 40))

# Выхлоп
particles = []

def create_exhaust():
    for _ in range(20):  # Create (n) particles
        angle = random.uniform(math.pi / 4, 3 * math.pi / 4) # 45, 135 градусов
        speed = random.uniform(3, 5)  # Random speed
        color = (255, 255, 255)  # Particle color
        size = random.randint(2, 5)  # Random size for each particle
        particles.append([rocket_pos[0] + 20, rocket_pos[1] + 240, speed * math.cos(angle), speed * math.sin(angle), color, size])

# Функция для обновления частиц
def update_exhaust():
    for particle in particles:
        particle[0] += particle[2]  # Update x position
        particle[1] += particle[3]  # Update y position
        particle[3] += 0.1  # Simulate gravity effect
        
        # Decrease particle size over time
        particle[5] = max(0, particle[5] - 0.075)  # Reduce size, ensuring it doesn't go below 0

    # Remove particles that are too small or have gone off-screen
    particles[:] = [p for p in particles if p[1] < HEIGHT and p[5] > 0]

# Игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            game_started = True

    if not game_started:
        show_start_menu()
    else:
        # Apply gravity
        rocket_pos[1] += gravity * 0.4
        if rocket_pos[1] > initial_rocket_pos:
            rocket_pos[1] = initial_rocket_pos
        # Обновление позиции ракеты
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            rocket_pos[1] -= thrust * 8  # Движение ракеты вверх
            create_exhaust()
        if keys[pygame.K_DOWN]:
            rocket_pos[1] -= thrust * 2.5  # Движение ракеты вниз
            create_exhaust()

        # Change background if rocket exits
        if rocket_pos[1] < -250: # следующий фон
            particles.clear()
            current_bg_index = (current_bg_index + 1) % len(backgrounds)
            background_image = pygame.image.load(backgrounds[current_bg_index])
            background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
            rocket_pos[1] = (HEIGHT)  # Reset rocket position to the bottom
        elif rocket_pos[1] > 452.6: # предыдущий фон
            particles.clear()
            if current_bg_index != 0: 
                current_bg_index = (current_bg_index - 1) % len(backgrounds)
                background_image = pygame.image.load(backgrounds[current_bg_index])
                background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
                rocket_pos[1] = -250
        # Отрисовка всего
        update_exhaust()
        screen.blit(background_image, (0, 0))
        screen.blit(rocket_image, (rocket_pos[0], rocket_pos[1]))  # Отрисовка ракеты
        for particle in particles:
            square_size = particle[5]  # Use the random size
            square_rect = (int(particle[0]), int(particle[1]), square_size, square_size)
            pygame.draw.rect(screen, (255, 90, 0), square_rect)
        display_interface(thrust, gravity)  # Отображение мощности и гравитации
        pygame.display.flip()

pygame.quit()