"""
   Web API - PyFlaskAlgorithmsAPI,
     applications configuration variables / global constants
"""


class Config:
    """
       applications general settings/variables
    """
    DEBUG_GLOBAL = True

    # default host ip
    HOST_API_APP = "0.0.0.0"

    # wep app port
    PORT_API_APP = "5000"

    # api root url
    SERVER_NAME_API_APP = "/algorithms/api/v1"

    # log location
    LOG_DIRRECTORY = "logs/AlgorithmsAPILog.log"
    LOG_SIZE = 10240
    LOG_BACKUP_COUNT = 10




