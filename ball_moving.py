"""Module for introducing simple physical modeling techniques.

"""
import graphics as gr
SIZE_X = 400
SIZE_Y = 400

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)


def add(point_1, point_2):
    """Sum two vectors

        Keyword arguments:
            point_1 -- coords of first point (Point from gr)
            point_2 -- coords of second point (Point from gr)

    """
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point


def draw_circle(coords):
    """Draw circle in selected coords

        Keyword arguments:
            coords - coords of circle's center (Point from gr)

    """
    circle = gr.Circle(coords, 10)
    circle.setFill('red')

    circle.draw(window)


def clear_window():
    """Clear entire window.

    """
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('green')
    rectangle.draw(window)


def check_coords(coords, velocity):
    """Correct velocity if circle reaches the edge of window

        Keyword arguments:
            coords -- current coords (Point from gr)
            velocity -- current velocity (Point from gr)

    """
    if coords.x < 0 or coords.x > SIZE_X:
        velocity.x = -velocity.x

    if coords.y < 0 or coords.y > SIZE_Y:
        velocity.y = -velocity.y


def move_ball_uniform():
    """Uniform move of a ball.

    """
    coords = gr.Point(200, 200)
    velocity = gr.Point(1, -2)
    acceleration = gr.Point(0, 0.1)

    for i in range(500):
        clear_window()
        draw_circle(coords)

        coords = add(coords, velocity)
        velocity = add(velocity, acceleration)
        check_coords(coords, velocity)

        gr.time.sleep(0.01)

    window.getMouse()
    window.close()


if __name__ == "__main__":
    move_ball_uniform()
