"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2,
                        y=self.window.height-self.paddle.height-paddle_offset)
        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)
        # self.bricks = GRect(width=brick_width, height=brick_height)
        self.label_1 = GLabel('You Lose')
        self.label_1.font = '-50'
        self.label_2 = GLabel('You Win!')
        self.label_2.font = '-50'
        # Draw bricks.
        for y in range(brick_rows):
            for x in range(brick_cols):
                self.bricks = GRect(width=brick_width, height=brick_height)
                position_x = x * (self.bricks.width+brick_spacing)
                position_y = brick_offset + y*(self.bricks.height+brick_spacing)
                self.bricks.filled = True
                if y % 10 < 2:
                    self.bricks.color = "red"
                    self.bricks.fill_color = "red"
                elif y % 10 < 4:
                    self.bricks.fill_color = "orange"
                    self.bricks.color = "orange"
                elif y % 10 < 6:
                    self.bricks.color = "yellow"
                    self.bricks.fill_color = "yellow"
                elif y % 10 < 8:
                    self.bricks.color = "green"
                    self.bricks.fill_color = "green"
                else:
                    self.bricks.color = "blue"
                    self.bricks.fill_color = "blue"
                self.window.add(self.bricks, x=position_x, y=position_y)

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED
        self.set_ball_velocity()

        # Initialize our mouse listeners.
        onmousemoved(self.mouse_move)
        self.is_start = False
        self.has_click = False # for the user to determine whether they click the start button
        onmouseclicked(self.check)

        self.collision = 0

        self.collision_times = 0
        self.win_points = brick_cols*brick_rows

    def reset_ball(self):  # After ball collide to the bottom of the window, we need to reset the ball
        self.window.remove(self.ball)
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)

    def check_for_collision(self):   # use four corners of the ball to detect whether the ball collide anything
        for x in range(int(self.ball.x), int(self.ball.x+self.ball.width+1), self.ball.width):
            for y in range(int(self.ball.y), int(self.ball.y + self.ball.height + 1), self.ball.height):
                point = self.window.get_object_at(x, y)
                if point is not None:
                    if point != self.paddle:
                        self.collision = 1   # when ball collide  bricks
                        self.window.remove(point)
                        self.collision_times += 1
                    else:
                        self.collision = 2   # when ball collide paddle
                    return self.collision

    def check(self, mouse):
        self.has_click = True
        # if self.is_start is False:
        #     self.is_start = True
        # else:
        #     pass

    def mouse_move(self, mouse):
        if mouse.x > self.window.width - self.paddle.width/2:
            self.paddle.x = self.window.width - self.paddle.width
        if mouse.x < 0 + self.paddle.width/2:
            self.paddle.x = 0
        if 0 + self.paddle.width/2 <= mouse.x <= self.window.width - self.paddle.width/2:
            self.paddle.x = mouse.x - self.paddle.width/2

    def get_x_velocity(self):
        velocity_x = self.__dx
        return velocity_x

    def get_y_velocity(self):
        velocity_y = self.__dy
        return velocity_y

    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        if random.random() > 0.5:
            self.__dy = -self.__dy


