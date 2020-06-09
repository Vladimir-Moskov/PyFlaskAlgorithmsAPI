"""
   Algorithms Wep API application / main file / entry point,
   with configure routing map and application server start up
"""

from config import Config

from algorithms import ackermann
from algorithms import fibonacci
from algorithms import factorial

from app import app
from app import api

from api_resources import ackermann_api, factorial_api, fibonacci_api


# Routing ##############################

# http://127.0.0.1:5000/algorithms/api/v1/ackermann
api.add_resource(ackermann_api.AckermannAPI, '/ackermann',  endpoint="ackermann", methods=['GET'],
                 resource_class_kwargs={'strategy': ackermann.ackermann})
api.add_resource(ackermann_api.AckermannAPI, '/ackermann_dp',  endpoint="ackermann_dp", methods=['GET'],
                 resource_class_kwargs={'strategy': ackermann.ackermann_dp})

# http://127.0.0.1:5000/algorithms/api/v1/factorial
api.add_resource(factorial_api.FactorialAPI, '/factorial_math',  endpoint="factorial_math", methods=['GET'],
                 resource_class_kwargs={'strategy': factorial.factorial_math})
api.add_resource(factorial_api.FactorialAPI, '/factorial_recursive',  endpoint="factorial_recursive", methods=['GET'],
                 resource_class_kwargs={'strategy': factorial.factorial_recursive})
api.add_resource(factorial_api.FactorialAPI, '/factorial_sequence',  endpoint="factorial_sequence", methods=['GET'],
                 resource_class_kwargs={'strategy': factorial.factorial_sequence})
api.add_resource(factorial_api.FactorialAPI, '/factorial_div_and_conq',  endpoint="factorial_div_and_conq", methods=['GET'],
                 resource_class_kwargs={'strategy': factorial.factorial_div_and_conq})

# http://127.0.0.1:5000/algorithms/api/v1/fibonacci
api.add_resource(fibonacci_api.FibonacciAPI, '/fibonacci_formula',  endpoint="fibonacci_formula", methods=['GET'],
                 resource_class_kwargs={'strategy': fibonacci.fibonacci_formula})
api.add_resource(fibonacci_api.FibonacciAPI, '/fibonacci_sequence',  endpoint="fibonacci_sequence", methods=['GET'],
                 resource_class_kwargs={'strategy': fibonacci.fibonacci_sequence})
api.add_resource(fibonacci_api.FibonacciAPI, '/fibonacci_recursive',  endpoint="fibonacci_recursive", methods=['GET'],
                 resource_class_kwargs={'strategy': fibonacci.fibonacci_recursive})
api.add_resource(fibonacci_api.FibonacciAPI, '/fibonacci_recursive_dp',  endpoint="fibonacci_recursive_dp", methods=['GET'],
                 resource_class_kwargs={'strategy': fibonacci.fibonacci_recursive_dp})

#####################################################################3


# run it as server (for development server mod)
if __name__ == '__main__':
    app.logger.info('PyFlaskAlgorithmsAPI - web API startup')
    app.run(port=Config.PORT_API_APP, debug=Config.DEBUG_GLOBAL, host=Config.HOST_API_APP)
