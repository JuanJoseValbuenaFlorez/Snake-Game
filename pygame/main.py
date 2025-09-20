import pygame, sys, random
from pygame.math import Vector2

pygame.init()

BG_COLOR = (173,204,96)
SNAKE_COLOR = (43,52,24)

cell_size = 30
numbre_of_cells = 25


class Food:
    def __init__(self, snake_body):
        self.position = self.generate_random_pos(snake_body)
        
    def draw(self):
        Food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size,cell_size, cell_size)
        screen.blit(food_surface, Food_rect)
        
    def generate_random_cell(self):
        x=random.randint(0,numbre_of_cells - 1)
        y  = random.randint(0,numbre_of_cells - 1)
        return Vector2(x, y)
        
    def generate_random_pos(self,snake_body):
        
        position = self.generate_random_cell()
    
        while position in snake_body:
            position = self.generate_random_cell()
    
        return position
    
class snake:
    def __init__(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1,0)
        self.add_segment = False
        
    def draw(self):
        for segment in self.body:
            segment_rect = pygame.Rect(segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, SNAKE_COLOR, segment_rect,0,7)
            
    def update(self):
        self.body.insert(0, self.body[0] + self.direction)
        if self.add_segment == False:
            self.body.pop()
        else:
            self.add_segment = False
     
class Game:
    def __init__(self):
     self.snake = snake()
     self.food = Food(self.snake.body)
     
    def draw(self):
         self.snake.draw()
         self.food.draw()
         
    def update(self):
        self.snake.update()
        self.check_collision_with_food_()
        
    def check_collision_with_food_(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.generate_random_pos(self.snake.body)   
            self.snake.add_segment = True 
    
         
       
screen = pygame.display.set_mode((cell_size * numbre_of_cells, cell_size *  numbre_of_cells,))

food_surface = pygame.image.load("descarga (1).png")


pygame.display.set_caption("retro snake")

clock = pygame.time.Clock()

game = Game()

Snake_update = pygame.USEREVENT

pygame.time.set_timer(Snake_update,150)


while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
            
      if event.type == Snake_update:
        game.update()
            
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP and game.snake.direction != Vector2(0,1):
              game.snake.direction = Vector2(0,-1)
          if event.key == pygame.K_DOWN and game.snake.direction != Vector2(0,-1):
              game.snake.direction = Vector2(0,1)
          if event.key == pygame.K_RIGHT and game.snake.direction != Vector2(-1,0):
              game.snake.direction = Vector2(1,0)
          if event.key == pygame.K_LEFT and game.snake.direction != Vector2(1,0):
              game.snake.direction = Vector2(-1,0)
              
            
            
    screen.fill(BG_COLOR)
    game.draw()
    game.draw()
    
    pygame.display.update()
    clock.tick(60)
    