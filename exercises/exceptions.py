"""
*************
*           *
*           *
*           *
*************

"""
import traceback

try:
    raise Exception('this is the error message')
except:
    errorFile = open('errorLog.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('the traceback info was written to errorLog.txt')


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1')
    if (width < 2) or (height < 2):
        raise Exception('"width"  and "height" must be greater than 2')
    print(symbol * width)

    for i in range(height - 2):
        space = ' '
        print(f'{symbol}{space * (width - 2)}{symbol}')
    
    print(symbol * width)

boxPrint('6', 20, 7)
boxPrint('X', 3, 45)
boxPrint('*', 20, 7)
boxPrint('*', 3, 3)
