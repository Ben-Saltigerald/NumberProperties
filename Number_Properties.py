
def getFactors(x):

    
    factors_list = []

    for i in range(1, x + 1):
        if (x % i  == 0):
            factors_list.append(i)

    return factors_list

print(getFactors)


def isPrime(x):
    if(x == 1):
        return False

    factors_list = []
    
    for i in range(2, x + 1):
        
        if(x % i == 0):
            factors_list.append(i)

    if len(factors_list)>= 2:
            return False    
    else:
        return True
    
    
print(isPrime)

       
def isComposite(x):

    factors_list = []
    
    for i in range(1, x + 1):

        if(x % i == 0):
            factors_list.append(i)
    

    if len(factors_list)>= 3:
            return True
    else:
        return False

print(isComposite)


def isPerfect(x):

    factors_list = []
    
    for i in range(1, x + 1):
        if(x % i == 0):
            factors_list.append(i)
        

    if sum(factors_list)- x == x:
            return True

    else:
        return False
   

    
def isAbundant(x):


    factors_list = []
    
    for i in range(1, x + 1):
        if(x % i == 0):
            factors_list.append(i)
        

    if sum(factors_list)- x > x:
        return True
    else:

        return False


def isTriangular(x):

    for i in range(1, x + 1):
        if i*(i + 1)/2 == x:
            return True
    else:
        return False
             
def isNarcissistic(x):
    x_string = str(x)
    string_length = len(x_string)
    summation = 0
    

    for i in x_string:
        summation += (int(i)** string_length)        


    if(summation == x):
        return True
    else:
        return False

    

def main():

    playing = True
    while playing == True:

        num_input = input('Give me a number from 1 to 10000.  Type -1 to exit. ')

        try:
            num = int(num_input)

            if (num == -1):
                playing = False
                continue

            if (num <= 0 or num > 10000):
                continue

            factors = getFactors(num)
            print("The factors of", num, "are", factors)

            if isPrime(num):
                print(str(num) + ' is prime')
            if isComposite(num):
                print(str(num) + ' is composite')
            if isPerfect(num):
                print(str(num) + ' is perfect')
            if isAbundant(num):
                print(str(num) + ' is abundant')
            if isTriangular(num):
                print(str(num) + ' is triangular')
            if isNarcissistic(num):
                print(str(num) + ' is narcissistic')

        except ValueError:
            print('Sorry, the input is not an int.  Please try again.')
            

if __name__ == '__main__':
    main()
