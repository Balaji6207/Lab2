def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def get_user_input():
    num=input()
    num=num.split(",")
    num= [float(i) for i in num]
    return num
def calc_average_temperature(num):
    avg = 0
    for i in num:
        avg += i/len(num)     
    return avg
def calc_min_max_temperature(num):
    min = num[0]
    max = num[0]
    for i in num:
        if min > i:  
            min = i
        if max < i:
            max = i
    return [min,max] 
display_main_menu()
num = get_user_input()
print("Average temperature is " + str(calc_average_temperature(num)))
print("Minimum temperature is " + str(calc_min_max_temperature(num)[0]))       
print("Maximum temperature is " + str(calc_min_max_temperature(num)[1]))  