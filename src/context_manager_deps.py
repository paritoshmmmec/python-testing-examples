class ContextManagerDeps:
    def __init__(self):
        print('Initialized')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Sample')

    def connect(self):
        return "I am connected"