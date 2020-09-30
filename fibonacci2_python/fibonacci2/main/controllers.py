from flask import Blueprint, current_app, render_template, jsonify, abort, make_response
import math
import itertools
import time
from fibonacci2.cache import cache

main = Blueprint("main", __name__, template_folder="templates")

class Calculator:
    def __init__(self):
        pass

    def fibonacci2(self, input_int):
        x = [1,1]
        for i in range(1, int(math.ceil(input_int/2)+1)):  
            x.append(x[-1] + x[-2]) 
    
        x = [y for y in x if y <= input_int and y != 1]
    
        for i in range(len(x)):
                for j in range(int(math.floor(input_int/x[i])-1)):
                    x.append(x[i])

        retVal = [seq for i in range(len(x), 0, -1) for seq in itertools.combinations(x, i) if sum(seq) == input_int]
        for i in range(len(retVal)):    
            retVal[i] = sorted(retVal[i])
        retVal = [list(y) for y in set(tuple(y) for y in retVal)]
        
        return retVal
       

@main.route('/fib/<int:input_int>', methods=['GET'])
def get_fib(input_int):
    t0 = time.time()
    result = cache.get('fibonacci' + str(input_int)) #Caching layer to avoid recalculating
    if result is None:
        calc = Calculator()
        result = calc.fibonacci2(input_int)
        cache.set('fibonacci' + str(input_int), result)
    t1 = time.time() #Basic benchmark of the program
    return jsonify({'result': str(result), 'benchmark(in seconds)': "{:.20f}".format(t1-t0)}) 
