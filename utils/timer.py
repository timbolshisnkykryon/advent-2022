def timer(fn):
    from time import perf_counter
    def inner(*args, **kwargs):
        start_time = perf_counter()
        to_execute = fn(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print('{0} took {1:.8f}s to execute'.format(fn.__name__, execution_time))
        return to_execute

    return inner


def dads_timer(fn):
    from datetime import datetime
    def inner(*args, **kwargs):
        start_time = datetime.now()
        to_execute = fn(*args, **kwargs)
        print(f'{fn.__name__} took {datetime.now() - start_time}s to execute')
        return to_execute
    return inner