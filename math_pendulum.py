"""Model of math pendulum with gravity.

"""


import graphics as gr
import math

SIZE_X = 800
SIZE_Y = 800
ARM_LENGTH = 300
G_ACCELERATION = 0.01
BALL_MASS = 10

window = gr.GraphWin("Pendulum", SIZE_X, SIZE_Y)
G = 0.01


def update_coords(coords, angle):
    """Update coords with new angle value.

        Keyword Args:
            coords -- current coords of ball (Point from gr)

    """
    koeff_y = 1 if coords.x <= SIZE_X / 2 else -1
    new_point = gr.Point(coords.x + ARM_LENGTH * math.sin(angle / 2) * 2 * (2 ** (1/2) / 2),
                         coords.y + koeff_y * ARM_LENGTH * math.sin(angle / 2) * 2 * (2 ** (1/2) / 2))
    velocity = gr.Point(new_point.x - coords.x,
                        new_point.y - coords.y)
    return velocity

def get_angle(angle, angle_velocity):
    """Get updated angle, angle_acceleration and angle_velocity.

        Keyword Args:
        angle -- current angle (Point from gr)
        angle_acceleration -- current angle acceleration (Point from gr)
        angle_velocity -- current angle velocity (Point from gr)

    """
    angle_acceleration = -G_ACCELERATION * math.sin(angle)
    angle += angle_velocity
    angle_velocity += angle_acceleration
    angle_velocity *= 0.99
    return angle, angle_velocity


def swing_pendulum():
    """Pendulum swinging.

    """
    angle = 6
    angle_velocity = 0
    center_point = gr.Point(SIZE_X / 2, SIZE_Y * 0.2)
    coords = gr.Point(center_point.x - ARM_LENGTH * math.sin(angle / 2) * 2 * (2 ** (1/2) / 2),
                      center_point.y + ARM_LENGTH * math.sin(angle / 2) * 2 * (2 ** (1/2) / 2))
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('white')
    rectangle.draw(window)

    center = gr.Circle(center_point, 20)
    center.setFill('black')
    center.draw(window)

    ball = gr.Circle(gr.Point(coords.x, coords.y), BALL_MASS * 5)
    ball.setFill('green')
    ball.draw(window)

    while 1 == 1:
        new_angle, angle_velocity = get_angle(angle, angle_velocity)
        velocity = update_coords(ball.getCenter(), new_angle - angle)
        angle = new_angle
        ball.move(velocity.x, velocity.y)
        line = gr.Line(center_point, ball.getCenter())
        line.draw(window)
        gr.time.sleep(0.03)
        line.undraw()
        if window.checkMouse():
            break
    window.close()


if __name__ == "__main__":
    swing_pendulum()
