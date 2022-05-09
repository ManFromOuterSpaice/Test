def main():
    x, y = 300, 400


    width, height = 200, 300

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
    walls_width = 0.9 * width
    walls_height = 0.5 * height
    roof_height = height - foundation_height - walls_height

    draw_foundation(x, y, width, foundation_height)
    draw_walls(x, y - foundation_height, walls_width, walls_height)
    draw_roof(x, y - foundation_height - walls_height, width, roof_height)


def draw_foundation(x, y, width, height):

  """
    Нарисовать фундамент домика ширины widht и высоты height от опорной точки(x, y),
    которая находится в середине нижней точки фундамента.
    :param x: координата x середины фундамента
    :param y: координата y низа фундамента
    :param width: полная ширина фундамента (фундамент или вылеты крыши включены)
    :param height: полная высота фундамента
    :return: None
    """
  print("Фундамент",x,y,width,height)
  pass  # do nothing

def draw_walls(x, y, width,height):
    print("Стены", x,y,width,height)
    pass


def draw_roof(x,y,widht, height):
    print("Крыша",x,y,widht,height)
    pass


main()
