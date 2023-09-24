class MockConnectionManager():
    def __init__(self):
        print('Mock Connection Manager is getting Initialized')

    def __enter__(self):
        return self

    def connect(self):
        return "I am connected from test"

    def __exit__(self, type, value, traceback):
        pass