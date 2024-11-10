from typing import Dict, List
from pytest import raises
from src.drivers.numpy_handler import NumpyHandler
from .calculator_3 import Calculator3


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandlerError:
    def variance(self, numbers: List[float]) -> float:
        return 3

class MockDriverHandler:
    def variance(self, numbers: List[float]) -> float:
        return 1000

def test_calculate_with_variance_error():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator3 = Calculator3(MockDriverHandlerError())

    with raises(Exception) as exinfo:
        calculator3.calculate(mock_request)

    assert str(exinfo.value) == 'Falha no processo: Variância menor que multiplicação.'

def test_calculate():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    calculator3 = Calculator3(MockDriverHandler())


    response = calculator3.calculate(mock_request)

    assert isinstance(response, dict)
    assert "data" in response
    assert "calculator" in response["data"]
    assert "success" in response["data"]
    assert "value" in response["data"]
    assert response["data"] == {'calculator': 3, 'success': True, 'value': 1000}
