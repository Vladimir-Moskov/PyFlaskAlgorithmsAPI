
# PyFlaskAlgorithmsAPI
# Here is solution ()
  0. Please, see Task statement in TaskRequarments.md
  1. Flask framework with Flask-Restfull has been used to implement task web api.
  2. Web api source code in app/ directory
  3. Implementation of algorithms in app/algorithms directory
  4. Unit tests for algorithms in tests/algorithms directory.
  5. simple flask-monitoringdashboard library has been used as "monitoring of my choice"
     (for mo details see https://flask-monitoringdashboard.readthedocs.io/en/latest/index.html
                         https://github.com/flask-dashboard/Flask-MonitoringDashboard)
  6. No any cash has been implemented to store previously calculated data, web API is stateless
     (according to requirement - "The results per function should be calculated separately")

## From point of view MVP (Minimum Valuable Product)

1. For simplicity - logging has not been added

2. For simplicity - unit tests and integration tests has not been implemented on 100%

3. For simplicity - there is no any authorization/security
> TODO: implement it

4. Error handling have not been done properly
> TODO: implement it

## Project setup steps (with Docker)

    1. Be sure your system has docker installed and your user has all required permissions to perform
    followed action

    2. Go to project root

        >  cd   your_local_directory/PyFlaskAlgorithmsAPI

    3. Build docker image, by default it take Dockerfile from current directory for build

        > sudo docker build -t algorithms-api-image .

    4. Run docker image with web api application running on it
        > sudo docker run --init --rm --publish 5000:5000 algorithms-api-image

    5. In case permission issue - your user not in sudo group, run previous commands without sudo


## Project setup steps (on OS directly / development Environment)

 1. download / unzip project into your local disc, be sure project in PyFlaskAlgorithmsAPI directory

 2. Install latest Python 3.7 if you do not have [https://realpython.com/installing-python/]
    and run cmd / terminal console

 3. Install pip  use command
   > python get-pip.py
   or follow step by step [https://www.liquidweb.com/kb/install-pip-windows/]

 4. Install Python virtualenv with command
   > pip install virtualenv

 5. set project folder as you current folder
    > cd   your_local_directory/PyFlaskAlgorithmsAPI

 6. Run next command in order to create virtualenv for project
   > virtualenv venv

 7. Activate virtual environment
   > ./venv/Scripts/activate

 8. install project dependencies
    return to project root
   > cd your_local_directory/PyFlaskAlgorithmsAPI

   > pip install -r requirements.txt

    and use

    > pip freeze > requirements.txt

    in order to update list of project libraries
    and use

    > pip install <package-name>

    in case you miss some


 ### Start web api application

    1.  Here is where application located -
        > PyFlaskAlgorithmsAPI/app

    2. Run it with
       >  python PyFlaskAlgorithmsAPI/app/algorithms_api.py

    3. application will be started on default HOST and PORT

        > http://localhost:5000/


    4. The flowing API endpoints will be exposed to execute corespondent algorithms:


       http://192.168.2.21:5000/algorithms/api/v1/ackermann?m=3&n=4&count=100
       http://192.168.2.21:5000/algorithms/api/v1/ackermann_dp?m=3&n=4&count=100

        http://192.168.2.21:5000/algorithms/api/v1/factorial_math?n=40&count=100
        http://192.168.2.21:5000/algorithms/api/v1/factorial_recursive?n=40&count=100
        http://192.168.2.21:5000/algorithms/api/v1/factorial_sequence?n=40&count=100
        http://192.168.2.21:5000/algorithms/api/v1/factorial_div_and_conq?n=40&count=100

        http://192.168.2.21:5000/algorithms/api/v1/fibonacci_formula?n=40&count=100
        http://192.168.2.21:5000/algorithms/api/v1/fibonacci_sequence?n=40&count=100
        http://192.168.2.21:5000/algorithms/api/v1/fibonacci_recursive?n=40&count=100
        http://192.168.2.21:5000/algorithms/api/v1/fibonacci_recursive_dp?n=40&count=100

    5. Web API monitoring will be available (Use the credentials u:admin, p:admin to log in.)
          - Log into the Dashboard at: http://localhost:5000/dashboard/login
          - Go to the Overview tab in the left menu: http://localhost:5000/dashboard/overview


