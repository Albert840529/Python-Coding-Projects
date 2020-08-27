"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    dx = graphics.get_x_velocity()
    dy = graphics.get_y_velocity()
    life_times = NUM_LIVES
    while True:  # wait for user to click to start the game
        if graphics.has_click is True:
            while True:
                collisions = graphics.check_for_collision()
                if collisions == 1:
                    dy = -dy
                if collisions == 2:
                    if dy > 0:
                        dy = -dy
                    else:
                        dy = dy
                if graphics.collision_times >= graphics.win_points:  # when all bricks removed, stop the game
                    break
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    dx = -dx                            # for the boundary conditions, when ball collide the wall,
                if graphics.ball.y <= 0:                # ball need to bounce back
                    dy = - dy
                if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    life_times -= 1                     # when ball touch the bottom of window, lives minus one,
                    graphics.reset_ball()               # and the game need to be restart
                    break
                graphics.ball.move(dx, dy)
                pause(FRAME_RATE)
            graphics.has_click = False
        elif graphics.collision_times >= graphics.win_points:     # when player remove all bricks
            graphics.window.remove(graphics.ball)
            graphics.window.remove(graphics.paddle)
            graphics.window.add(graphics.label_2, x=(graphics.window.width - graphics.label_2.width) / 2,
                                y=(graphics.window.height - graphics.label_2.height))
            print('You win')
            break
        elif life_times <= 0:
            graphics.window.remove(graphics.ball)
            graphics.window.remove(graphics.paddle)
            graphics.window.add(graphics.label_1, x=(graphics.window.width-graphics.label_1.width)/2,
                                y=(graphics.window.height-graphics.label_1.height))
            print('You lose')
            break
        else:
            pass
        pause(FRAME_RATE)
    # Add animation loop here!


if __name__ == '__main__':
    main()
