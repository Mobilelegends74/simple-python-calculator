# tests/test_main.py
from calculator.main import main
from unittest.mock import patch

def test_main():
    with patch("builtins.input", side_effect=[2, 3]):
        with patch("builtins.print") as mocked_print:
            main()
            mocked_print.assert_any_call("Addition: 5.0")
            mocked_print.assert_any_call("Subtraction: -1.0")
            mocked_print.assert_any_call("Multiplication: 6.0")
            mocked_print.assert_any_call("Division: 0.6666666666666666")
