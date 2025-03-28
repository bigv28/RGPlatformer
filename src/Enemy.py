import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def normalised(self):
        length = math.sqrt(self.x**2 + self.y**2)
        return Vector(self.x/length, self.y/length) if length > 0 else Vector(0, 0)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

class Entity:
    def __init__(self, position, size, hp):
        self.position = position
        self.size = size
        self.hp = hp
        self.max_hp = hp
        self.velocity = Vector(0, 0)
        self.direction = 1
    
    def move(self, velocity):
        self.position.x += velocity.x
        self.position.y += velocity.y
    
    def collides_with(self, other):
        return (abs(self.position.x - other.position.x) < (self.size.x + other.size.x)/2 and
                abs(self.position.y - other.position.y) < (self.size.y + other.size.y)/2)

class Enemy(Entity):
    def __init__(self, position, size, hp=100, damage=10, speed=2):
        super().__init__(position, size, hp)
        self.damage = damage
        self.speed = speed
        self.attack_range = 50
        self.target = None
    
    def update(self, target_position, obstacles):
        self.target = target_position
        direction = (self.target - self.position).normalised()
        self.velocity = direction * self.speed
        
        for obstacle in obstacles:
            if self.collides_with(obstacle):
                avoidance = (self.position - obstacle.position).normalised()
                self.velocity += avoidance * self.speed * 0.5
        
        self.move(self.velocity)
        
        if self.velocity.x > 0:
            self.direction = 1
        elif self.velocity.x < 0:
            self.direction = -1
