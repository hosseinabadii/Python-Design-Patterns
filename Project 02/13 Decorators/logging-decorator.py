import logging
from functools import wraps

# define logger
def create_logger():

    logger = logging.getLogger("exc_logger")
    logger.setLevel(logging.INFO)

    logfile = logging.FileHandler("exc_logger.log")
    logger.addHandler(logfile)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logfile.setFormatter(formatter)

    return logger

# Define decorator
def log_exception(logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                msg = f"exception in {func.__name__} \n {'='*40}"
                logger.exception(msg)
                raise
        return wrapper
    return decorator

# Example:
@log_exception(create_logger())
def calculate():
    return 10/0


if __name__ == "__main__":
    calculate()
