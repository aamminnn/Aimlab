import logging

def log(message):
    # Configure the logging module
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        handlers=[
                            logging.FileHandler('output.log'),  # Output to a file
                            logging.StreamHandler()  # Output to console
                        ])

    # Log messages
    # logging.debug('This is a debug message')
    logging.debug(message)
