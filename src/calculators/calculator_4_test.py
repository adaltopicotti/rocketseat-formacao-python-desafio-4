from typing import Dict, List


from src.calculators.calculator_4 import Calculator4
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        pass

    def variance(self, numbers: List[float]) -> float:
        pass

    def mean(self, numbers: List[float]) -> float:
        return 7


def test_calculate():
    mock_request = MockRequest({"numbers": [4, 8, 7, 9]})

    driver = MockDriverHandler()
    calculator_4 = Calculator4(driver)

    response = calculator_4.calculate(mock_request)

    assert isinstance(response, dict)
    assert "data" in response
    assert "calculator" in response["data"]
    assert "result" in response["data"]
    assert response["data"] == {'calculator': 4, 'result': 7.0}