import Lab2

print("Test_Lab2")


def test_find_min_max():
    result = []
    input_arr = [5, 67, 32]
    test_arr = [5, 67]

    result = Lab2.calc_min_max_temperature(input_arr)
    
    assert (result == test_arr)

def test_calc_average():
    result = []
    input_arr = [5, 67, 32]
    test_arr = 34.67

    result = Lab2.calc_average_temperature(input_arr)
    result = round(result,2)  

    assert (result == test_arr)

def test_calc_median_temperature():
    result = []
    input_arr = [5, 67, 32]
    test_arr = 32

    result = Lab2.calc_median_temperature(input_arr)
    
    assert (result == test_arr)