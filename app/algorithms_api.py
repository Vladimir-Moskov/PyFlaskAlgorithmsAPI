from flask import Flask
from config import Config

from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

from api_resources import ackermann_api, factorial_api, fibonacci_api

app = Flask(__name__)
api = Api(app, prefix=Config.SERVER_NAME_API_APP)
# add CORS for frontend cross domain policy
cors = CORS(app)

# http://127.0.0.1:5000//algorithms/api/v1/ackermann
api.add_resource(ackermann_api.AckermannAPI, '/ackermann',  endpoint="ackermann", methods=['GET'])
api.add_resource(ackermann_api.AckermannDPAPI, '/ackermann_dp',  endpoint="ackermann_dp", methods=['GET'])

# http://127.0.0.1:5000//algorithms/api/v1/factorial
api.add_resource(factorial_api.FactorialMathAPI, '/factorial_math',  endpoint="factorial_math", methods=['GET'])
api.add_resource(factorial_api.FactorialRecursiveAPI, '/factorial_recursive',  endpoint="factorial_recursive", methods=['GET'])
api.add_resource(factorial_api.FactorialSequenceAPI, '/factorial_sequence',  endpoint="factorial_sequence", methods=['GET'])
api.add_resource(factorial_api.FactorialDivAndConqAPI, '/factorial_div_and_conq',  endpoint="factorial_div_and_conq", methods=['GET'])

# http://127.0.0.1:5000//algorithms/api/v1/fibonacci
api.add_resource(fibonacci_api.FibonacciFormulaAPI, '/fibonacci_formula',  endpoint="fibonacci_formula", methods=['GET'])
api.add_resource(fibonacci_api.FibonacciSequenceAPI, '/fibonacci_sequence',  endpoint="fibonacci_sequence", methods=['GET'])
api.add_resource(fibonacci_api.FibonacciRecursiveAPI, '/fibonacci_recursive',  endpoint="fibonacci_recursive", methods=['GET'])
api.add_resource(fibonacci_api.FibonacciRecursiveDpAPI, '/fibonacci_recursive_dp',  endpoint="fibonacci_recursive_dp", methods=['GET'])

if __name__ == '__main__':
    app.run(port=Config.PORT_API_APP, debug=Config.DEBUG_GLOBAL)
