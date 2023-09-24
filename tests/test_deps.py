import json
from unittest.mock import patch

from requests import Response

from src.sut import Sut
from tests.mocks.mock_connection_manager import MockConnectionManager


@patch('src.sut.Sut.semi_complex_method')
@patch('src.sut.ContextManagerDeps')
@patch('src.sut.NestedDependency.play')
@patch('src.sut.external_call_func')
def test_should_demo_correct_demo_value(mock_external_call,
                                        nested_deps,
                                        context_manager_deps,
                                        semi_complex_method):
    nested_deps.return_value = 10
    mock_external_call.return_value = 14
    context_manager_deps.return_value = MockConnectionManager()
    semi_complex_method.return_value = "I am doing no work from mock"

    sut = Sut()
    (nested_dep_return_value,
     external_api_value,
     context_manager_value,
     semi_complex_method_value) = sut.calculate()

    assert nested_dep_return_value == 10
    assert external_api_value == 14
    assert context_manager_value == "I am connected from test"
    assert semi_complex_method_value == "I am doing no work from mock"


@patch('src.sut.requests.get')
def test_request_api_call(mock_request_call):
    mock_request_call.side_effect = mocked_requests_get
    sut = Sut()
    data = sut.call_api()
    assert data


@patch('src.sut.requests.get')
def test_request_api_call_version2(mock_request_call):
    mock_request_call.return_value = MockedResponse()
    sut = Sut()
    data = sut.call_api()
    assert data
    assert data == {"ip": "mocked_ip"}


class MockedResponse:
    def json(self):
        return {
            "ip": 'mocked_ip'
        }


def mocked_requests_get(*args, **kwargs):
    response = Response()
    response.status_code = 200
    response._content = str.encode(json.dumps('Mocked response'))
    return response
