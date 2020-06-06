from flask_restful import Resource, reqparse, abort
import factorial
import timeit

parser = reqparse.RequestParser()
parser.add_argument('n', type=int, help='m is mandatory argument (n >= 0)', required=True, location='args')
parser.add_argument('count', type=int, help='count is optional argument (count > 0, default count=1)', required=False, location='args')


def abort_if_arg_is_not_valid(arg_value: int, arg_name: str):
    if arg_value < 0:
        abort(404, message=f"The value of {arg_name} = {arg_value} is not valid. It should be NOT less then zero")


def validate_args():
    args = parser.parse_args()
    n = args["n"]
    count = 1
    if args["count"]:
        count = args["count"]
    abort_if_arg_is_not_valid(n, "n")
    return n, count


class FactorialMathAPI(Resource):

    def get(self):
        n, count = validate_args()
        result, execution_time = timeit.timed(factorial.factorial_math, count, m)
        return {
                    'status': 'success',
                    'data': result,
                    'execution_time': f"Execution time {execution_time} ms (millisecond)"
                }, \
            200, \
            {'Access-Control-Allow-Origin': '*'}


class FactorialRecursiveAPI(Resource):

    def get(self):
        n, count = validate_args()
        result, execution_time = timeit.timed(factorial.factorial_recursive, count, m)
        return {
                    'status': 'success',
                    'data': result,
                    'execution_time': f"Execution time {execution_time} ms (millisecond)"
                }, \
            200, \
            {'Access-Control-Allow-Origin': '*'}


class FactorialSequenceAPI(Resource):

    def get(self):
        n, count = validate_args()
        result, execution_time = timeit.timed(factorial.factorial_sequence, count, m)
        return {
                    'status': 'success',
                    'data': result,
                    'execution_time': f"Execution time {execution_time} ms (millisecond)"
                }, \
            200, \
            {'Access-Control-Allow-Origin': '*'}


class FactorialDivAndConqAPI(Resource):

    def get(self):
        n, count = validate_args()
        result, execution_time = timeit.timed(factorial.factorial_div_and_conq, count, m)
        return {
                    'status': 'success',
                    'data': result,
                    'execution_time': f"Execution time {execution_time} ms (millisecond)"
                }, \
            200, \
            {'Access-Control-Allow-Origin': '*'}