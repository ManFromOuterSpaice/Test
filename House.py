def main():
    x, y = 100, 100


    width, height = 200, 200

    draw_house(x, y, width, height)


def draw_house(x, y, width, height):
    """
    Нарисовать домик ширины widht и высоты height от опорной точки(x, y),
    которая находится в середине нижней точки фундамента.
    :param x: координата x середины домика
    :param y: координата y низа фундамента
    :param width: полная ширина домика (фундамент или вылеты крыши включены)
    :param height: полная высота домика
    :return: None
    """
    print('Типа рисую домик...', x, y, width, height)
    foundation_height = 0.05*height
    draw_foundation(x, y, width, height)
    draw_walls()
    draw_roof()
    pass    #do nothing


main()
