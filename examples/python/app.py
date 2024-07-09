from random import randint
from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/liveness")
def liveness():
    return "OK"

@app.route("/readiness")
def readiness():
    return "OK"

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

@app.route('/fib')
def stress_cpu():
    n = randint(1, 30)
    result = fib(n)
    return f"Fibonacci number at position {n} is {result}"

@app.route('/fibby/<int:n>')
def stress_cpu_int(n):
    result = fib(n)
    return f"Fibonacci number at position {n} is {result}"


@app.route('/')
def hello():
    return "Hello, World!"