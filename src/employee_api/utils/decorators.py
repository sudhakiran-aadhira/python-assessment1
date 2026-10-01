import logging
import time
from functools import wraps
from typing import Any, Callable


logger = logging.getLogger(__name__)


def log_execution(
    func: Callable[..., Any]
) -> Callable[..., Any]:

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):

        start_time = time.perf_counter()

        try:
            result = func(*args, **kwargs)

            duration = (
                time.perf_counter() - start_time
            )

            logger.info(
                "Function %s completed in %.4f seconds",
                func.__name__,
                duration
            )

            return result

        except Exception:
            duration = (
                time.perf_counter() - start_time
            )

            logger.exception(
                "Function %s failed after %.4f seconds",
                func.__name__,
                duration
            )

            raise

    return wrapper
