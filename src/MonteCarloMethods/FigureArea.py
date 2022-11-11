import numpy as np
from functools import reduce


def calculate(basic_square: np.ndarray, figure_borders: list, n_points: int) -> float:
    """
    Вычисление площади произвольной фигуры, вписанной в прямоугольник

    Args:
        basic_square – координаты верхней левой и нижней правой точек описанного прямоугольника
        figure_borders – список функций, принимающих координаты точек и возвращающих bool
        n_points – число точек, брошенных на прямоугольник

    Returns:
        Площадь вписанной в прямоугольник фигуры
    """
    
    basic_square_left_top_point, basic_square_right_bottom_point = basic_square
    basic_square_area = __get_basic_square_area(basic_square_left_top_point, basic_square_right_bottom_point)

    points = [ __generate_point(basic_square_left_top_point, basic_square_right_bottom_point) for _ in range(n_points) ]
    points_in_borders = list(filter(lambda point: __point_satisfies_borders(point, figure_borders), points))
    n_points_in_borders = len(points_in_borders)

    figure_area = basic_square_area * n_points_in_borders / n_points
    return figure_area


def __get_basic_square_area(basic_square_left_top_point: float, basic_square_right_bottom_point: float) -> float:
    basic_square_width = basic_square_right_bottom_point[0] - basic_square_left_top_point[0]
    basic_square_height = basic_square_left_top_point[1] - basic_square_right_bottom_point[1]
    basic_square_area = basic_square_width * basic_square_height
    return basic_square_area

def __generate_point(basic_square_left_top_point: float, basic_square_right_bottom_point: float) -> np.ndarray:
    min_x = basic_square_left_top_point[0]
    max_x = basic_square_right_bottom_point[0]
    min_y = basic_square_right_bottom_point[1]
    max_y = basic_square_left_top_point[1]

    point_x = min_x + np.random.random() * (max_x - min_x)
    point_y = min_y + np.random.random() * (max_y - min_y)

    return np.array([point_x, point_y])

def __point_satisfies_borders(point: np.ndarray, figure_borders: list) -> bool:
    return reduce(lambda result, function: result * function(point), figure_borders, 1)




        