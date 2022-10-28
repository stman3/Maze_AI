import pygame
from random import choice, randrange

resl = WIDTH,HIGHT =1352,832
TILE = 104

cols,rows = WIDTH//TILE,HIGHT//TILE


pygame.init()
screen = pygame.display.set_mode(resl)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 60)






class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.walls = {'top':True,'right':True,'bottom':True,'left':True}
        self.visited = False
        self.map = False
        self.goal = False

    def draw_currtent_cell(self):
        x,y = self.x*TILE,self.y*TILE
        pygame.draw.rect(screen, pygame.Color('green'), (x+2,y+2,TILE-2,TILE-2))

    def draw(self):
        x,y = self.x*TILE,self.y*TILE
        
        if self.map:
            pygame.draw.rect(screen, pygame.Color((100,100,100)), (x,y,TILE,TILE))
        
        if self.goal:
             pygame.draw.rect(screen, pygame.Color('red'), (x,y,TILE,TILE))
        if self.visited:
            pygame.draw.rect(screen, pygame.Color('black'), (x,y,TILE,TILE))
        if self.walls['top']:
            pygame.draw.line(screen, pygame.Color('black'), (x, y), (x + TILE, y),2)
        if self.walls['right']:
            pygame.draw.line(screen, pygame.Color('black'), (x + TILE, y), (x + TILE, y + TILE),2)
        if self.walls['bottom']:
            pygame.draw.line(screen, pygame.Color('black'), (x + TILE, y + TILE), (x , y + TILE),2)
        if self.walls['left']:
            pygame.draw.line(screen, pygame.Color('black'), (x, y + TILE), (x, y),2)


    def check_cell(self, x, y):
        find_index = lambda x, y: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return grid_cells[find_index(x, y)]

    def check_neighborsDFS(self):
        neighbors = []
        top = self.check_cell(self.x, self.y - 1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)
        if top and not top.visited and not top.map:
            neighbors.append(top)
        if right and not right.visited and not right.map:
            neighbors.append(right)
        if bottom and not bottom.visited and not bottom.map:
            neighbors.append(bottom)
        if left and not left.visited and not left.map:
            neighbors.append(left)
        return choice(neighbors) if neighbors else False

    def check_neighborsA(self,goalx,goaly):
        top = self.check_cell(self.x, self.y - 1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)


        topH = abs(top.x - goalx)+abs(top.y-goaly)
        rightH = abs(right.x - goalx)+abs(right.y-goaly)
        bottomH = abs(bottom.x - goalx)+abs(bottom.y-goaly)
        leftH = abs(left.x - goalx)+abs(left.y-goaly)
        if not top or  top.visited or  top.map:
            topH = 1000
        if not right or  right.visited or  right.map:
            rightH = 1000
        if not bottom or  bottom.visited or  bottom.map:
            bottomH = 1000
        if not left or  left.visited or  left.map:
            leftH = 1000
        print("toph= ",topH," rightH= ",rightH," bottomH= ",bottomH," leftH= ",leftH)
        if top and not top.visited and not top.map:
            if topH<=rightH and topH<=bottomH and topH<=leftH:
                return top if top else False
        if right and not right.visited and not right.map:
            if rightH<=topH and rightH<=bottomH and rightH<=leftH:
                return right if right else False
        if bottom and not bottom.visited and not bottom.map:
            if bottomH<=rightH and bottomH<=topH and bottomH<=leftH:
                return bottom if bottom else False
        if left and not left.visited and not left.map:
            if leftH<=rightH and leftH<=bottomH and leftH<=topH:
                return left if left else False
        


        


class Button:
	def __init__(self,text,width,height,pos,elevation):
		#Core attributes 
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]
		# top rectangle 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#475F77'

		# bottom rectangle 
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#354B5E'
		#text
		self.text_surf = font.render(text, True, (0,0,255))
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

	def draw(self):
		# elevation logic 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#D74B4B'
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = '#475F77'
  


button1 = Button('DFS',200,40,(376,416),5)
button2 = Button('A*',200,40,(776,416),5)
grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
current_cell = grid_cells[67]
map = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,17,25,26,31,33,38,39,42,47,49,51,52,56,61,64,65,70,72,76,77,78,81,86,90,91,92,93,94,95,96,97,98,99,100,101,102,103]
goal = 35
player = 67
stack = []


#draw map and goal

for i in map:
    grid_cells[i].map = True
    grid_cells[i].draw()

grid_cells[goal].goal = True
grid_cells[goal].draw()


speed = 30
while True:
    screen.fill(pygame.Color('white'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if button1.pressed or button2.pressed:
        speed = 1
        if button1.pressed:
            if not current_cell.goal:
                [cell.draw() for cell in grid_cells]
                current_cell.visited = True
                current_cell.draw_currtent_cell()

                next_cell = current_cell.check_neighborsDFS()
                if next_cell:
                    next_cell.visited = True
                    stack.append(next_cell)
                    current_cell = next_cell
                else:
                    current_cell =stack.pop()
            else:
                font = pygame.font.SysFont(None, 60)
                img = font.render('win', True, (0,0,255))
                screen.blit(img, (676, 416))
        else:
            if not current_cell.goal:
                [cell.draw() for cell in grid_cells]
                current_cell.visited = True
                current_cell.draw_currtent_cell()

                next_cell = current_cell.check_neighborsA(grid_cells[goal].x,grid_cells[goal].y)
                if next_cell:
                    next_cell.visited = True
                    stack.append(next_cell)
                    current_cell = next_cell
                else:
                    current_cell =stack.pop()
            else:
                font = pygame.font.SysFont(None, 60)
                img = font.render('win', True, (0,0,255))
                screen.blit(img, (676, 416))
    else:
        button1.draw()
        button2.draw()
    pygame.display.flip()
    clock.tick(speed)