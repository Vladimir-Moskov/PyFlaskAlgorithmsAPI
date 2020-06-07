from flask_restful import Resource, reqparse, abort
from algorithms import timeit

parser = reqparse.RequestParser(bundle_errors=True)
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
        abort_if_arg_is_not_valid(count, "count")
    abort_if_arg_is_not_valid(n, "n")
    return n, count


class FactorialAPI(Resource):
    def __init__(self, **kwargs):
        self.strategy = kwargs["strategy"]

    def get(self):
        n, count = validate_args()
        result, execution_time = timeit.timed(self.strategy, count, n)
        return {
                    'status': 'success',
                    'data': result,
                    'execution_time': f"Execution time {execution_time} ms (millisecond)"
                }, \
            200, \
            {'Access-Control-Allow-Origin': '*'}
