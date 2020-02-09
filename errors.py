class ArgumentError(Exception):
    def __init__(self):
        super(*args, **kwargs)


class HandFullError(Exception):
    def __init__(self, *args, **kwargs):
        super(*args, **kwargs)

