
"""
Physics simulation.  Circle objects move according to physics laws, colliding
with screen walls and each other.  Program runs various physics simulations
including:
    - vectors
    - object detection
    - collision detection
    - object movement
    - elasticity
    - density
"""

import pygame as game
import random, math



# CONSTANTS:

BACKGROUND_COLOR = (255, 255, 255)
# Width and Height of game window.
(W, H) = (800, 500)
# Density of air.  Factor that controls the rate of speed reduction.
AIR_MASS = 0.2
# How much bounce is in objects.  Factor that controls the increae or decrease
# in speed when collision is detected.
ELASTICITY = 0.75
GRAVITY = (math.pi, 0.002)

# Create "screen" reference for gameplay window.
screen = game.display.set_mode((W, H))
game.display.set_caption('physics_test')




def addVectors(angle1, length1, angle2, length2):
    """
    Input:
        - angle1, length1 = Floats of first particle to add.
        - angle2, length2 = Floats of second particle to add.
    Output:
        - Tuple of angle and length of combined vectors of 2 particles from
        input.
    """
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2

    angle = 0.5 * math.pi - math.atan2(y, x)
    length  = math.hypot(x, y)

    return (angle, length)




def findParticle(particles, x, y):
    """
    Input:
        - particles = List of objects to test proximity to.
        - x, y = Coordinates (mouse coord) to test proximity of objects to.
    Output:
        - Return particle from list that is within proximity to coordinates.
    """

    for p in particles:
        # Takes distance from coordinates of iterated particle (p) to
        # coordinates from argument, and compares it to size of (p).  If
        # distance between coordinates is less than size, the "return" is (p).
        if math.hypot(p.x - x, p.y - y) <= p.size:
            return p

    return None




def collide(p1, p2):
    """
    Input:
        - p1, p2 = The two particles being tested for collision.
    Output:
        - p1.x, p1.y, p2.x, p2.y = Updated coordinates of argued particles if
        particles come within tested collision range.
    """

    # Create "dist" reference.  "dist" is the calculated distance between the
    # coordinates of the two argued particles.
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.hypot(dx, dy)

    # If statement passes True if "dist" reference is smaller then the sum of
    # the radiuses of the particles.  i.e.  Calculates a particle collision.
    if dist < p1.size + p2.size:
        angle = math.atan2(dy, dx) + 0.5 * math.pi
        total_mass = p1.mass + p2.mass

        (p1.angle, p1.speed) = addVectors(p1.angle, (p1.speed * (p1.mass - \
        p2.mass) / total_mass), angle, (2 * p2.speed * p2.mass / total_mass))
        (p2.angle, p2.speed) = addVectors(p2.angle, (p2.speed * (p2.mass - \
        p1.mass) / total_mass), angle + math.pi, (2 * p1.speed * p1.mass / \
        total_mass))
        p1.speed *= ELASTICITY
        p2.speed *= ELASTICITY

        overlap = 0.5 * (p1.size + p2.size - dist + 1)
        p1.x += math.sin(angle) * overlap
        p1.y -= math.cos(angle) * overlap
        p2.x -= math.sin(angle) * overlap
        p2.y += math.cos(angle) * overlap




class Particle():
    """
    Create Particle class for all particle instances.  Initiates attributes and defines functions display, move, and bounce.
    """

    def __init__(self, position, size, mass=1):
        """
        Input:
            - position = A tuple of X and Y coordinates.
            - size = Length of radius of circle.
            - mass = (default = 1)
        """

        self.x, self.y = position
        # Length of radius of circle.
        self.size = size
        self.color = (0, 0, 255)
        # Pixel width of border color of circle.
        self.thickness = 0
        self.speed = 0
        self.angle = 0
        # Circle's density; compares mass from particle to particle to
        # calculate mass influence.
        self.mass = mass
        # Air density; rate of speed decrease without acceleration.
        self.drag = (self.mass / (self.mass + AIR_MASS)) ** self.size




    def display(self):
        """
        Output:
            - Draws circle for each in particle class.
        """

        game.draw.circle(screen, self.color, (int(self.x), int(self.y)), \
        self.size, self.thickness)




    def move(self):
        """
        Output:
            - self.x, self.y = Positional adjustments.
            - self.speed = Rate of positional adjustments.
        """

        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.speed *= self.drag





    def bounce(self):
        """
        Output:
            - Makes particles bounce off walls of screen when collision is
            detected.
        """

        # If statement passes True if particle collides with Right wall.
        if self.x > W - self.size:
            # Adjust particle's vectors if collision is detected.
            self.x = 2 * (W - self.size) - self.x
            self.angle = - self.angle
            self.speed *= ELASTICITY

        # If statement passes True if particle collides with Left wall.
        elif self.x < self.size:
            # Adjust particle's vectors if collision is detected.
            self.x = 2 * self.size - self.x
            self.angle = - self.angle
            self.speed *= ELASTICITY

        # If statement passes True if particle collides with Bottom wall.
        if self.y > H - self.size:
            # Adjust particle's vectors if collision is detected.
            self.y = 2 * (H - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= ELASTICITY

        # If statement passes True if particle collides with Top wall.
        elif self.y < self.size:
            # Adjust particle's vectors if collision is detected.
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= ELASTICITY




number_of_particles = 20
my_particles = []

for n in range(number_of_particles):
    """
    Iteration randomly creates particles.  Creates random size, density, and
    position.
    """

    # Random generation of particle attributes.
    size = random.randint(10, 50)
    density = random.randint(1, 20)
    x = random.randint(size, W-size)
    y = random.randint(size, H-size)

    # Creates temporary particle reference.
    particle = Particle((x, y), size, density * size ** 2)
    # Sets particle color based on particle density.
    particle.color = (200 - density * 10, 200 - density * 10, 255)
    particle.speed = random.random()
    particle.angle = random.uniform(0, math.pi * 2)

    # Append iterated particle into "my_particles" list.
    my_particles.append(particle)




# Create reference for object in player control.
selected_particle = None

# Game Loop variable.
in_loop = True
while in_loop:
    """
    Gameplay loop.
    """

    # Set background color.
    screen.fill(BACKGROUND_COLOR)




    # Event iterations.
    for event in game.event.get():
        # Quit game detection.
        if event.type == game.QUIT:
            in_loop = False
        # Mouse button detection.  When True the object selected remains
        # "grabbed" by mouse cursor.
        elif event.type == game.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = game.mouse.get_pos()
            selected_particle = findParticle(my_particles, mouseX, mouseY)
        # Mouse button inactivate detection.  When mouse button is disengaged
        # the mouse cursor "releases" the selected object.
        elif event.type == game.MOUSEBUTTONUP:
            selected_particle = None



    # If statement to check for mouse-over selection.  If so, movement of
    # particle is controlled by mouse-movement.
    if selected_particle:
        # Create references to mouse position.
        (mouseX, mouseY) = game.mouse.get_pos()
        dx = mouseX - selected_particle.x
        dy = mouseY - selected_particle.y
        # Adjust particle angle and speed based on mouse movement.
        selected_particle.angle = 0.5 * math.pi + math.atan2(dy, dx)
        selected_particle.speed = math.hypot(dx, dy) * 0.1




    # Iteration of particles within gameplay.  Dictates particle movement with
    # consideration for collision.
    for i, particle in enumerate(my_particles):
        particle.move()
        particle.bounce()
        # Internal iteration for collision detection.
        for particle2 in my_particles[i + 1:]:
            collide(particle, particle2)
        particle.display()




    # Continuously refreshes screen while "in_loop" is True.
    game.display.flip()
