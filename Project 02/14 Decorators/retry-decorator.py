import time
import logging
from functools import wraps

def retry(ExceptionToCheck: Exception, tries: int=4, delay: int=2, backoff: int=1, logger=None):
    """"Retry calling the decorated function using as exponential backoff.
    
    :param ExceptionToCheck: the exception to check. maybe a tuple of exceptions
    :param tries: number of times to try before giving up
    :param delay: initial delay between retries in second
    :param backoff: backoff multiplier e.g. value of 2 will double the delay each retry
    :param logger: logger to use. if None, use print
    """
    def retry_decorator(func):

        @wraps(func)
        def retry_wrapper(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 0:
                try:
                    return func(*args, **kwargs)
                except ExceptionToCheck as e:
                    msg = f"{str(e)} Retrying in {mdelay} seconds..."
                    print(msg)
                    if logger:
                        logger.basicConfig(filename='app.log', filemode='w')
                        logger.warning(msg)

                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return func(*args, **kwargs)
        
        return retry_wrapper
    
    return retry_decorator


@retry(ExceptionToCheck=ZeroDivisionError, logger=logging)
def calculate():
    return 10/0

calculate()
