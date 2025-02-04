import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle properties
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 5

# Ball properties
BALL_SIZE = 10
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_velocity = [4, 4]

# Paddle positions
left_paddle_pos = [20, HEIGHT // 2 - PADDLE_HEIGHT // 2]
right_paddle_pos = [WIDTH - 30, HEIGHT // 2 - PADDLE_HEIGHT // 2]

# Score
left_score = 0
right_score = 0

# Font for score display
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()

    # Left paddle controls (W and S)
    if keys[pygame.K_w] and left_paddle_pos[1] > 0:
        left_paddle_pos[1] -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle_pos[1] < HEIGHT - PADDLE_HEIGHT:
        left_paddle_pos[1] += PADDLE_SPEED

    # Right paddle controls (Up and Down arrows)
    if keys[pygame.K_UP] and right_paddle_pos[1] > 0:
        right_paddle_pos[1] -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle_pos[1] < HEIGHT - PADDLE_HEIGHT:
        right_paddle_pos[1] += PADDLE_SPEED

    # Update ball position
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Ball collision with top and bottom walls
    if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT - BALL_SIZE:
        ball_velocity[1] = -ball_velocity[1]

    # Ball collision with paddles
    if (ball_pos[0] <= left_paddle_pos[0] + PADDLE_WIDTH and
        left_paddle_pos[1] < ball_pos[1] < left_paddle_pos[1] + PADDLE_HEIGHT):
        ball_velocity[0] = -ball_velocity[0]

    if (ball_pos[0] >= right_paddle_pos[0] - BALL_SIZE and
        right_paddle_pos[1] < ball_pos[1] < right_paddle_pos[1] + PADDLE_HEIGHT):
        ball_velocity[0] = -ball_velocity[0]

    # Scoring
    if ball_pos[0] <= 0:
        right_score += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_velocity = [4, 4]

    if ball_pos[0] >= WIDTH:
        left_score += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_velocity = [-4, 4]

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, (*left_paddle_pos, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (*right_paddle_pos, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_pos[0], ball_pos[1], BALL_SIZE, BALL_SIZE))

    # Draw scores
    left_score_text = font.render(str(left_score), True, WHITE)
    right_score_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_score_text, (WIDTH // 4, 20))
    screen.blit(right_score_text, (3 * WIDTH // 4, 20))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
