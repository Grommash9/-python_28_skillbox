

class MyMath:

    @staticmethod
    def circle_len(radius):
        if radius <= 0:
            raise ValueError('Радиус должен быть больше нуля и не равен ему')
        else:
            return 2 * 3.14 * radius

    @staticmethod
    def circle_sq(radius):
        if radius <= 0:
            raise ValueError('Радиус должен быть больше нуля и не равен ему')
        else:
            return 3.14 * (radius ** 2)

    @staticmethod
    def cube_volume(side_len):
        if side_len <= 0:
            raise ValueError('Сторона куба должна быть больше нуля и не равна ему')
        else:
            return side_len ** 3

    @staticmethod
    def surface_of_a_sphere(radius):
        if radius <= 0:
            raise ValueError('Радиус должен быть больше нуля и не равен ему')
        else:
            return 4 * 3.14 * (radius ** 2)
