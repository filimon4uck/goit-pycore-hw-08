from custom_errors import NotFound


def input_error(function):
    def inner(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except ValueError as e:
            return e
        except KeyError as e:
            return e
        except IndexError:
            return e
        except NotFound as e:
            return e

    return inner
