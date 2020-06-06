from flask import Flask
from config import Config
from algorithms import ackermann, fibonacci, factorial

from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

from api_resources import ackermann_api, factorial_api, fibonacci_api

app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True
api = Api(app, prefix=Config.SERVER_NAME_API_APP)
# add CORS for frontend cross domain policy
cors = CORS(app)

# http://127.0.0.1:5000//algorithms/api/v1/ackermann
api.add_resource(ackermann_api.AckermannAPI, '/ackermann',  endpoint="ackermann", methods=['GET'],
                 resource_class_kwargs={'strategy': ackermann.ackermann})
api.add_resource(ackermann_api.AckermannAPI, '/ackermann_dp',  endpoint="ackermann_dp", methods=['GET'],
                 resource_class_kwargs={'strategy': ackermann.ackermann_dp})

# http://127.0.0.1:5000//algorithms/api/v1/factorial
api.add_resource(factorial_api.FactorialAPI, '/factorial_math',  endpoint="factorial_math", methods=['GET'],
                 resource_class_kwargs={'strategy': factorial.factorial_math})
api.add_resource(factorial_api.FactorialAPI, '/factorial_recursive',  endpoint="factorial_recursive", methods=['GET'],
                 resource_class_kwargs={'strategy': factorial.factorial_recursive})
api.add_resource(factorial_api.FactorialAPI, '/factorial_sequence',  endpoint="factorial_sequence", methods=['GET'],
                 resource_class_kwargs={'strategy': factorial.factorial_sequence})
api.add_resource(factorial_api.FactorialAPI, '/factorial_div_and_conq',  endpoint="factorial_div_and_conq", methods=['GET'],
                 resource_class_kwargs={'strategy': factorial.factorial_div_and_conq})

# http://127.0.0.1:5000//algorithms/api/v1/fibonacci
api.add_resource(fibonacci_api.FibonacciAPI, '/fibonacci_formula',  endpoint="fibonacci_formula", methods=['GET'],
                 resource_class_kwargs={'strategy': fibonacci.fibonacci_formula})
api.add_resource(fibonacci_api.FibonacciAPI, '/fibonacci_sequence',  endpoint="fibonacci_sequence", methods=['GET'],
                 resource_class_kwargs={'strategy': fibonacci.fibonacci_sequence})
api.add_resource(fibonacci_api.FibonacciAPI, '/fibonacci_recursive',  endpoint="fibonacci_recursive", methods=['GET'],
                 resource_class_kwargs={'strategy': fibonacci.fibonacci_recursive})
api.add_resource(fibonacci_api.FibonacciAPI, '/fibonacci_recursive_dp',  endpoint="fibonacci_recursive_dp", methods=['GET'],
                 resource_class_kwargs={'strategy': fibonacci.fibonacci_recursive_dp})

if __name__ == '__main__':
    app.run(port=Config.PORT_API_APP, debug=Config.DEBUG_GLOBAL)
