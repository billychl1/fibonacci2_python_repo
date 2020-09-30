A RESTful service in Python that features the following endpoints. Try to apply general python best practices where applicable (i.e. imagine this will be a larger application later). 

• GET /fib/: Given a number, find all combinations of fibonacci number that add up to that particular number.

The fibonacci sequence is being calculated as follows: fn=fn−1+fn−2∀n>2;withthefirst two numbers being f1 = f2 = 1 are excluded from the sequence, hence your f1 = 2.

Example for »/fib/11« the response will be a list of all possible combinations with a status code 200. [ [2, 2, 2, 2, 3], [2, 2, 2, 5], [2, 3, 3, 3], [3, 3, 5], [8, 3] ] 

• GET/health: Return health information about the service. Definition of »healtcheck« is up to you.

How to start the service:
host@~/fibonacci2_python$ python3 main.py

How to invoke the fib service:
$ curl -i http://localhost:5000/fib/11

How to invoke the healthcheck service:
$ curl -i http://localhost:5000/health

Unit test:
host@~/fibonacci2_python$ python3 -m unittest tests.test

Tox:
host@~/fibonacci2_python$ tox