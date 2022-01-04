class Snake:
    def __init__(self, x, y, length, direction):
        self.x = x
        self.y = y
        self.length = length
        self.direction = direction
        self.body = []
        for i in range(length):
            self.body.append((x, y))
            # grow snake body in the opposite direction of the head
            if direction == 'right':
                x -= 1
            elif direction == 'left':
                x += 1
            elif direction == 'up':
                y += 1
            elif direction == 'down':
                y -= 1
    
    def move(self, grow):
        # move head in the snake's current direction
        if self.direction == 'right':
            self.x += 1
        elif self.direction == 'left':
            self.x -= 1
        elif self.direction == 'up':
            self.y -= 1
        elif self.direction == 'down':
            self.y += 1
        self.body.insert(0, (self.x, self.y))

        # if snake is growing, don't remove tail
        if not grow:
            self.body.pop()
        else:
            self.length += 1

    def change_direction(self, direction):
        self.direction = direction

    def ate_itself(self):
        # check for duplicates in the snake's body from 1 to the end
        for i in range(1, len(self.body)):
            if self.body[0] == self.body[i]:
                return True
        return False

    def get_body(self):
        return self.body

    def get_head(self):
        return self.body[0]

    def get_direction(self):
        return self.direction