import apple
import snake
import random

# board holds a snake and an apple and can check for collisions/grow the snake if necessary 
class Board:
    def __init__(self, width, height, snakeCoord, snakeLength, snakeDirection):
        self.width = width
        self.height = height

        # set snake
        self.snake = snake.Snake(snakeCoord[0], snakeCoord[1], snakeLength, snakeDirection)

        # set apple at random location not on snake
        self.apple = apple.Apple(random.randint(0, self.width - 1), random.randint(0, self.height - 1))
        while self.apple.get_coord() in self.snake.get_body():
            self.apple.set_coord(random.randint(0, self.width - 1), random.randint(0, self.height - 1))
        self.score = 0

    def __place_apple(self):
        self.apple.set_coord(random.randint(0, self.width - 1), random.randint(0, self.height - 1))
        while self.apple.get_coord() in self.snake.get_body():
            self.apple.set_coord(random.randint(0, self.width - 1), random.randint(0, self.height - 1))

    def __is_on_apple(self):
        # check if snake is on apple
        if self.snake.get_head() == self.apple.get_coord():
            self.score += 1
            return True
        return False 

    def __is_past_wall(self):
        # check if snake is on wall
        if self.snake.get_head()[0] >= self.width or self.snake.get_head()[0] < 0 or self.snake.get_head()[1] >= self.height or self.snake.get_head()[1] < 0:
            return True
        return False

    def change_direction(self, direction):
        self.snake.change_direction(direction)

    # return true if board is still in a valid state, false if game is over
    def move(self):
        onApple = self.__is_on_apple()
        self.snake.move(onApple)
        if onApple:
            self.__place_apple()

        # check for game over
        if self.__is_past_wall() or self.snake.ate_itself():
            return False
        else:
            return True

    def get_score(self):
        return self.score

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height