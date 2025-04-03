import math

# Vector class to handle 2D coordinates and basic operations like subtraction and scaling
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Subtraction of two vectors
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    # Normalize vector (make it unit length)
    def normalised(self):
        length = math.sqrt(self.x**2 + self.y**2)
        return Vector(self.x/length, self.y/length) if length > 0 else Vector(0, 0)
    
    # Multiply vector by scalar value
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    # Return magnitude (length) of the vector
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

# Entity class represents objects in the game, such as the player or enemies
class Entity:
    def __init__(self, position, size, hp):
        self.position = position  # Position of the entity
        self.size = size          # Size (dimensions) of the entity
        self.hp = hp              # Health points of the entity
        self.max_hp = hp          # Maximum health points for reference
        self.velocity = Vector(0, 0)  # Initial velocity is zero
        self.direction = 1        # Direction of movement (1 for right, -1 for left)
    
    # Move the entity by the velocity vector
    def move(self, velocity):
        self.position.x += velocity.x
        self.position.y += velocity.y
    
    # Check if this entity collides with another entity
    def collides_with(self, other):
        # Check if the entities' bounding boxes overlap
        return (abs(self.position.x - other.position.x) < (self.size.x + other.size.x)/2 and
                abs(self.position.y - other.position.y) < (self.size.y + other.size.y)/2)

# Enemy class, inheriting from Entity, adds specific behavior for enemies
class Enemy(Entity):
    def __init__(self, position, size, hp=100, damage=10, speed=2):
        super().__init__(position, size, hp)  # Initialize parent class (Entity)
        self.damage = damage    # How much damage the enemy deals
        self.speed = speed      # How fast the enemy moves
        self.attack_range = 50  # Attack range for when the enemy can attack
        self.target = None      # Target to follow (usually the player)
    
    # Update the enemy’s behavior each frame
    def update(self, target_position, obstacles):
        self.target = target_position  # Update target position (e.g., player position)
        
        # Calculate direction towards the target and normalize it
        direction = (self.target - self.position).normalised()
        
        # Update velocity based on target direction and speed
        self.velocity = direction * self.speed
        
        # Check for collisions with obstacles
        for obstacle in obstacles:
            if self.collides_with(obstacle):
                # If collision occurs, avoid the obstacle by pushing the enemy away
                avoidance = (self.position - obstacle.position).normalised()
                self.velocity += avoidance * self.speed * 0.5  # Apply avoidance force
        
        # Move the enemy based on the updated velocity
        self.move(self.velocity)
        
        # Adjust enemy's direction based on movement (for sprite facing)
        if self.velocity.x > 0:
            self.direction = 1  # Moving right
        elif self.velocity.x < 0:
            self.direction = -1  # Moving left


