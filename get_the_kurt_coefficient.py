# Shin Yamagami
# Nov 9th, 2015
# This program prompt users to enter a file including home prices, and
# calculate its Kurt Coefficient of single family home prices.

def description():
    # display the description
    print('This program prompts users to enter a file lists home prices in\n' +
          'it, and calculate the Kurt Coefficient of single family home\n'
          'prices.')
def get_file():
    # get a file to be read from users and return it
    return input('Please enter the file name with extension: ')
def read_file(home_prices):
    # open a 'home_prices' file in read mode and return it
    return open(home_prices, 'r')
def get_number(price_list):
    # get the number of how many prices are listed in price_list
    return int(len(price_list))
def get_total(price_list):
    # get the sum of prices in price_list
    total = 0
    for i in price_list:
        total += float(i)
    return total
def get_average(number, total):
    # get the average of prices listed in a file from number and total
    return total / number
def get_pop_stand_dev(number, price_list, average):
    # calculate the population standard deviation of prices from number,
    # price_list and average
    pop_stand_dev = 0
    numerator_of_stand = 0
    for i in price_list:
        numerator_of_stand += (float(i) - average) ** 2
    return (numerator_of_stand / number) ** (1/2)    
def get_kurt_coefficient(number, price_list, average, pop_stand_dev):
    # calculate the kurt coefficient from number, price_lsit, average
    # and pop_stand_dev
    numerator_of_kurt = 0
    for i in price_list:
        numerator_of_kurt += ((float(i) - average) / pop_stand_dev) ** 4
    return numerator_of_kurt / number 
def main():
    description()
    home_prices = get_file()
    prices = read_file(home_prices)
    price_list = prices.readlines()
    number = get_number(price_list)
    total = get_total(price_list)
    average = get_average(number, total)
    pop_stand_dev = get_pop_stand_dev(number, price_list, average)
    kurt_coefficient = get_kurt_coefficient(number, price_list, average, pop_stand_dev)
    prices.close()
    print('The number of prices listed in your file is ', number)
    print('The total of prices listed in your file is ', total)
    print('The average of prices listed in your file is ', average)
    print('The population standard deviation of prices is ', pop_stand_dev)
    print('The kurt_coefficient of single family home prices is ', kurt_coefficient)
    # first, this program display the description of it, prompt users to 
    # enter a file with its extension, open it in a read mode, make a list of
    # prices with a 'readlines' method, get the number of prices in it, get the
    # total of prices, calculate the average of them, calculate the population
    # standard deviation of them and finally calculate the kurt coefficient of
    # them.
main()
