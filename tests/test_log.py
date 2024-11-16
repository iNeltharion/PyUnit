import unittest
from parameterized import parameterized
from app.main import Calculator
from app.error import InvalidInputException


class TestCalculatorLog(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Фикстура для создания калькулятора
        cls.calc = Calculator()

    @parameterized.expand([
        # Тестируем корректные значения
        (2, 10, 0.30102999566398114),  # log(2, 10) ≈ 0.3010
        (8, 2, 3),  # log(8, 2) = 3
        (16, 4, 2),  # log(16, 4) = 2
        (27, 3, 3),  # log(27, 3) = 3
    ])
    def test_log_valid_input(self, a, base, expected_result):
        # Тест на правильные данные
        result = self.calc.log(a, base)
        self.assertAlmostEqual(result, expected_result, places=7)  # Сравниваем с точностью до 7 знаков

    @parameterized.expand([
        # Тестируем неправильные типы данных
        ('a', 2),  # строка вместо числа
        (2, 'b'),  # строка вместо числа
        ('string', 'b'),  # обе строки
        (None, 10),  # None вместо числа
    ])
    def test_log_invalid_type(self, a, base):
        # Тест на неправильный тип данных
        with self.assertRaises(TypeError):
            self.calc.log(a, base)

    @parameterized.expand([
        # Тестируем некорректные данные для логарифма
        (0, 10),  # log(0, 10) — a должно быть больше 0
        (1, 10),  # log(1, 10) — a не может быть равно 1
        (2, 0),  # log(2, 0) — основание не может быть 0
        (2, -3),  # log(2, -3) — основание не может быть отрицательным
        (-5, 10),  # log(-5, 10) — a должно быть больше 0
    ])
    def test_log_invalid_input(self, a, base):
        # Тест на ошибку InvalidInputException
        with self.assertRaises(InvalidInputException):
            self.calc.log(a, base)

    @parameterized.expand([
        # Тестируем другие крайние случаи
        (0.0001, 10),  # log(0.0001, 10) — очень маленькое значение для a
        (1000, 1000),  # log(1000, 1000) — равные значения a и base
    ])
    def test_log_edge_cases(self, a, base):
        # Тестируем пограничные случаи
        result = self.calc.log(a, base)
        self.assertIsInstance(result, float)  # Проверяем, что результат — это число с плавающей точкой


if __name__ == '__main__':
    unittest.main()
