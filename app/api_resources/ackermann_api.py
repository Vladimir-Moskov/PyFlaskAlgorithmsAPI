"""

"""

from flask_restful import Resource, reqparse, abort
from algorithms import timeit
from app import app

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('m', type=int, help='m is mandatory argument (m >= 0)', required=True, location='args')
parser.add_argument('n', type=int, help='n is mandatory argument (n >= 0)', required=True, location='args')
parser.add_argument('count', type=int, help='count is optional argument (count > 0, default count=1)', required=False, location='args')


def abort_if_arg_is_not_valid(arg_value: int, arg_name: str):
    if arg_value < 0:
        message = f"The value of {arg_name} = {arg_value} is not valid. It should be NOT less then zero"
        app.logger.error(message)
        abort(404, message=message)


def validate_args():
    args = parser.parse_args()
    m, n = args["m"], args["n"]
    count = 1
    if args["count"]:
        count = args["count"]
        abort_if_arg_is_not_valid(count, "count")
    abort_if_arg_is_not_valid(m, "m")
    abort_if_arg_is_not_valid(n, "n")
    return m, n, count


class AckermannAPI(Resource):

    def __init__(self, **kwargs):
        self.strategy = kwargs["strategy"]

    def get(self):
        m, n, count = validate_args()
        try:
            result, execution_time = timeit.timed(self.strategy, count, m, n)
        except Exception as error:
            app.logger.error(f'PyFlaskAlgorithmsAPI - {self.__name__} {self.strategy.__name__} {repr(error)}')
            return {
                       'status': 'success',
                       'data': result,
                       'error': f"AckermannAPI - The current request can not be processed because problem in "
                                f"{self.strategy.__name__}"
                   }, \
                   400, \
                   {'Access-Control-Allow-Origin': '*'}

        return {
                    'status': 'success',
                    'data': result,
                    'execution_time': f"Execution time {execution_time} ms (millisecond)"
                }, \
            200, \
            {'Access-Control-Allow-Origin': '*'}
