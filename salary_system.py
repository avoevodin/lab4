"""Model of system with central gravity.

"""


import graphics as gr
SIZE_X = 800
SIZE_Y = 800
G = 1200

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)


def move_object(object, cur_coords, target_coords):
    """Move object to new coords.

        Keyword Args:
            object -- object that should be moved (object from gr)
            cur_coords -- current coords of object (Point from gr)
            target_coords -- target coords (Point from gr)

    """
    diff_x = target_coords.x - cur_coords.x
    diff_y = target_coords.y - cur_coords.y
    object.move(diff_x, diff_y)


def add(point_1, point_2):
    """Sum two vectors.

        Keyword arguments:
            point_1 -- coords of first point (Point from gr)
            point_2 -- coords of second point (Point from gr)

    """
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point


def sub(point_1, point_2):
    """Subtract vectors.

        Keyword Args:
            point_1 -- coords of first point (Point from gr)
            point_2 -- coords of second point(Point from gr)

    """
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)
    return new_point


def update_acceleration(ball_coords, center_coords):
    """Change acceleration for gravity moving.

        Keyword Args:
        ball_coords -- current coords of ball (Point from gr)
        center_coords -- coords of center (Point from gr)

    """
    diff = sub(ball_coords, center_coords)
    distance = (diff.x ** 2 + diff.y ** 2) ** (3/2)

    return gr.Point(-diff.x * G / distance, -diff.y * G / distance)


def draw_circle(coords):
    """Draw circle in selected coords

        Keyword arguments:
            coords - coords of circle's center (Point from gr)

    """
    circle = gr.Circle(coords, 10)
    circle.setFill('red')

    circle.draw(window)

    return circle


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


def draw_central_gravity_system():
    """Draw central gravity system.

    """
    coords = gr.Point(400, 700)
    velocity = gr.Point(2, 0)
    circle = draw_circle(coords)

    for i in range(10000):
        new_coords = add(coords, velocity)
        move_object(circle, coords, new_coords)
        acceleration = update_acceleration(coords, gr.Point(SIZE_X / 2, SIZE_Y / 2))
        coords = new_coords
        velocity = add(velocity, acceleration)
        check_coords(coords, velocity)


if __name__ == "__main__":
    draw_central_gravity_system()
