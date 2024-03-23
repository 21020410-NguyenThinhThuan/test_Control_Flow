import unittest
from unittest.mock import patch
from io import StringIO
import coverage

# Bắt đầu đo lường độ bao phủ
cov = coverage.Coverage()
cov.start()

from login import login

class LoginTestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_successful_login(self, mock_stdout):
        user_input = ['admin', '12345']
        with patch('builtins.input', side_effect=user_input):
            result = login()
            self.assertEqual(result, "Đăng nhập thành công!")

    @patch('sys.stdout', new_callable=StringIO)
    def test_failed_login(self, mock_stdout):
        user_input = ['admin', 'wrong_password']
        with patch('builtins.input', side_effect=user_input):
            result = login()
            self.assertEqual(result, "Đăng nhập thất bại. Vui lòng đăng nhập lại.")

    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_username(self, mock_stdout):
        user_input = ['wrong_username', '12345']
        with patch('builtins.input', side_effect=user_input):
            result = login()
            self.assertEqual(result, "Đăng nhập thất bại. Vui lòng đăng nhập lại.")

    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_password(self, mock_stdout):
        user_input = ['wrong_username', 'wrong_password']
        with patch('builtins.input', side_effect=user_input):
            result = login()
            self.assertEqual(result, "Đăng nhập thất bại. Vui lòng đăng nhập lại.")

if __name__ == '__main__':
    # Chạy các test case
    unittest.main()

    # Dừng đo lường độ bao phủ và in kết quả
    cov.stop()
    cov.save()
    cov.report()


