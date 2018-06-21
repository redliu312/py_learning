import retrying



def retry_if_not_keyboard_interrupt(exception):
    return not isinstance(exception, KeyboardInterrupt)

def retry_some(func,retry=3):
    _runner = retrying.retry(stop_max_attempt_number=retry, retry_on_exception=retry_if_not_keyboard_interrupt
                             )(func)

    return _runner()





