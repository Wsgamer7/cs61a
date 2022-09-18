from summation import summation, square, cube


def summation_text():
    assert summation(3, square) == 14
    assert summation(2, cube) ==9
    assert summation(2, square) == 5

summation_text()