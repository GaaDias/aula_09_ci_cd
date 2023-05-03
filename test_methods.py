import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_soma():
    # given an a of 32 and a b of 54
    a = 32
    b = 54

    # when we calculate the sum
    output = methods.test_soma(a,b)
    
    # then the sum should be 86
    assert output == 86

def test_subtracao():
    # given an a of 32 and a b of 16
    a = 32
    b = 16

    # when we calculate the subtraction
    output = methods.test_subtracao(a, b)
    
    # then the subtraction should be 16
    assert output == 16

def test_multiplicacao():
    # given an a of 4 and a b of 11
    a = 4
    b = 11

    # when we calculate the multiplication
    output = methods.test_multiplicacao(a, b)
    
    # then the multiplication should be 44
    assert output == 44

def test_divisao():
    # given an a of 32 and a b of 16
    a = 32
    b = 16

    # when we calculate the division
    output = methods.test_divisao(a, b)
    
    # then the division should be 2
    assert output == 2