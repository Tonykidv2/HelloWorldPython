import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)

# Ball properties
ball_radius = 10
ball_pos = [WIDTH // 2, HEIGHT // 3]
ball_velocity = [2, 1]
gravity = 0.2
friction = 0.99

# Hexagon properties
hex_radius = 200
hex_center = (WIDTH // 2, HEIGHT // 2)
rotation_speed = 0.02
hex_angle = 0

# Helper functions
def rotate_point(point, angle, center):
    """
    Rotate a point around a center by a given angle.
    """
    ox, oy = center
    px, py = point
    
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)

    qx = ox + cos_theta * (px - ox) - sin_theta * (py - oy)
    qy = oy + sin_theta * (px - ox) + cos_theta * (py - oy)
    return [qx, qy]


def get_hexagon_vertices(center, radius, angle):
    """
    Return the vertices of a hexagon given the center, radius, and rotation angle.
    """
    cx, cy = center
    vertices = []
    for i in range(6):
        theta = angle + math.radians(60 * i)
        x = cx + radius * math.cos(theta)
        y = cy + radius * math.sin(theta)
        vertices.append([x, y])
    return vertices


def reflect_ball(normal, velocity):
    """
    Reflect the ball's velocity vector off a wall with a given normal.
    """
    dot_product = velocity[0] * normal[0] + velocity[1] * normal[1]
    reflected_velocity = [
        velocity[0] - 2 * dot_product * normal[0],
        velocity[1] - 2 * dot_product * normal[1]
    ]
    return reflected_velocity


# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Apply gravity to ball
    ball_velocity[1] += gravity

    # Update ball position
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Apply friction
    ball_velocity[0] *= friction
    ball_velocity[1] *= friction

    # Rotate hexagon
    hex_angle += rotation_speed
    hex_vertices = get_hexagon_vertices(hex_center, hex_radius, hex_angle)

    # Draw hexagon
    pygame.draw.polygon(screen, WHITE, hex_vertices, 2)

    # Collision detection with hexagon walls
    for i in range(6):
        p1 = hex_vertices[i]
        p2 = hex_vertices[(i + 1) % 6]

        # Vector from p1 to p2
        wall_vector = [p2[0] - p1[0], p2[1] - p1[1]]
        wall_length = math.hypot(wall_vector[0], wall_vector[1])
        wall_normal = [-wall_vector[1] / wall_length, wall_vector[0] / wall_length]

        # Check distance from ball to wall
        edge_to_ball = [ball_pos[0] - p1[0], ball_pos[1] - p1[1]]
        projection = edge_to_ball[0] * wall_normal[0] + edge_to_ball[1] * wall_normal[1]

        if abs(projection) < ball_radius:
            # Project the ball position onto the wall   # nudge it a bit more
            ball_pos[0] -= projection * wall_normal[0] * -2
            ball_pos[1] -= projection * wall_normal[1] * -2

            # Reflect ball velocity
            ball_velocity = reflect_ball(wall_normal, ball_velocity)

    # Draw ball
    pygame.draw.circle(screen, RED, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
