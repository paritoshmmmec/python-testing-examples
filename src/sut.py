import requests

from src.context_manager_deps import ContextManagerDeps
from src.external_call_func import external_call_func
from src.nested_deps import NestedDependency


class Sut:
    def __init__(self):
        print("init")
        self.nested_deps = NestedDependency()

    def calculate(self):
        nested_dep_return_value = self.nested_deps.play()
        external_api_value = external_call_func(nested_dep_return_value)
        with ContextManagerDeps() as a:
            context_manager_value = a.connect()

        semi_complex_method_value = self.semi_complex_method()

        return (
            nested_dep_return_value,
            external_api_value,
            context_manager_value,
            semi_complex_method_value,
        )

    def call_api(self):
        return requests.get("https://httpbin.org/ip").json()

    def semi_complex_method(self):
        return "I am doing a lot of processing here"
