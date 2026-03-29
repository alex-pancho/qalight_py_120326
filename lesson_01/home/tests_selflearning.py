"""
Тести для перевірки правильності виконання завдань із _selflearning.py
"""
import unittest
import sys
from io import StringIO
import importlib.util
from pathlib import Path

class TestHomeSelfLearning(unittest.TestCase):
    
    def setUp(self):
        """Підготовка до тестів - перехоплення виводу"""
        self.dir = Path(__file__).parent
        self.held, sys.stdout = sys.stdout, StringIO()
    
    def tearDown(self):
        """Відновлення stdout після тестів"""
        sys.stdout = self.held
    
    def load_student_code(self, file_path):
        """Завантаження коду студента для тестування"""
        path = self.dir / file_path
        try:
            spec = importlib.util.spec_from_file_location("student_code", path)
            student_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(student_module)
            return student_module
        except Exception as e:
            self.fail(f"Не вдалося завантажити файл {path}: {e}")
    
    def file_open(self, file_path):
        """Відкриття файлу з правильним кодуванням"""
        path = self.dir / file_path
        try:
            with open(path, 'r', encoding='utf-8') as f:
                code = f.read()
                return code
        except FileNotFoundError:
            self.fail(f"Файл {file_path} не знайдено")
        except Exception as e:
            self.fail(f"Помилка при читанні файлу {file_path}: {e}")
    
    def test_subtraction_output(self):
        """Тест 1: Перевірка виводу віднімання 5 - 5"""
        # Виконуємо код і перехоплюємо вивід
        try:
            code = self.file_open('_selflearning01.py')
            exec(compile(code, '_selflearning01.py', 'exec'))
            output = sys.stdout.getvalue()
            
            # Перевіряємо чи є результат віднімання у виводі
            self.assertIn('0', output, "Результат віднімання 5 - 5 = 0 повинен бути у виводі")
            
        except Exception as e:
            self.fail ("Помилка при виконанні коду віднімання: {e}")
    
    def test_multiplication_output(self):
        """Тест 2: Перевірка виводу множення 3 * 5"""
        try:
            code = self.file_open('_selflearning01.py')
            exec(compile(code, '_selflearning01.py', 'exec'))
            output = sys.stdout.getvalue()
            
            # Перевіряємо чи є результат множення у виводі
            self.assertIn ("15", output, "Результат множення 3 * 5 = 15 повинен бути у виводі")
            
        except Exception as e:
            self.fail (f"Помилка при виконанні коду множення: {e}")
    
    def test_savings_variable_creation(self):
        """Тест 3: Перевірка створення змінної savings = 100"""
        try:
            # Виконуємо код і перевіряємо змінні
            namespace = {}
            code = self.file_open('_selflearning02.py')
            exec(compile(code, '_selflearning02.py', 'exec'), namespace)
            
            self.assertIn('savings', namespace, "Змінна 'savings' повинна бути створена")
            self.assertEqual(namespace['savings'], 100, "Змінна 'savings' повинна дорівнювати 100")
            
        except Exception as e:
            self.fail(f"Помилка при перевірці змінної savings: {e}")
    
    def test_savings_print_output(self):
        """Тест 4: Перевірка виводу змінної savings"""
        try:
            code = self.file_open('_selflearning02.py')
            exec(compile(code, '_selflearning02.py', 'exec'))
            output = sys.stdout.getvalue()
            
            # Перевіряємо чи виводиться значення 100 (savings)
            self.assertIn('100', output, "Значення змінної savings (100) повинно виводитися")
            
        except Exception as e:
            self.fail(f"Помилка при перевірці виводу savings: {e}")
    
    def test_monthly_savings_variable(self):
        """Тест 5: Перевірка створення змінної monthly_savings = 10"""
        try:
            namespace = {}
            code = self.file_open('_selflearning03.py')
            exec(compile(code, '_selflearning03.py', 'exec'), namespace)
            
            self.assertIn('monthly_savings', namespace, "Змінна 'monthly_savings' повинна бути створена")
            self.assertEqual(namespace['monthly_savings'], 10, "Змінна 'monthly_savings' повинна дорівнювати 10")
            
        except Exception as e:
            self.fail(f"Помилка при перевірці змінної monthly_savings: {e}")
    
    def test_num_months_variable(self):
        """Тест 6: Перевірка створення змінної num_months = 4"""
        try:
            namespace = {}
            code = self.file_open('_selflearning03.py')
            exec(compile(code, '_selflearning03.py', 'exec'), namespace)
            
            self.assertIn('num_months', namespace, "Змінна 'num_months' повинна бути створена")
            self.assertEqual(namespace['num_months'], 4, "Змінна 'num_months' повинна дорівнювати 4")
            
        except Exception as e:
            self.fail(f"Помилка при перевірці змінної num_months: {e}")
    
    def test_new_savings_calculation(self):
        """Тест 7: Перевірка правильного обчислення new_savings"""
        try:
            namespace = {}
            code = self.file_open('_selflearning03.py')
            exec(compile(code, '_selflearning03.py', 'exec'), namespace)
            
            self.assertIn('new_savings', namespace, "Змінна 'new_savings' повинна існувати")
            
            # Перевіряємо чи new_savings містить правильний результат
            expected_value = 40  # 10 * 4 = 40
            self.assertEqual(namespace['new_savings'], expected_value, 
                           f"Змінна 'new_savings' повинна дорівнювати {expected_value} (monthly_savings * num_months)")
            
        except Exception as e:
            self.fail(f"Помилка при перевірці обчислення new_savings: {e}")
    
    def test_new_savings_output(self):
        """Тест 8: Перевірка виводу new_savings"""
        try:
            code = self.file_open('_selflearning03.py')
            exec(compile(code, '_selflearning03.py', 'exec'))
            output = sys.stdout.getvalue()
            
            # Перевіряємо чи виводиться значення 40 (new_savings)
            self.assertIn('40', output, "Значення змінної new_savings (40) повинно виводитися")
            
        except Exception as e:
            self.fail(f"Помилка при перевірці виводу new_savings: {e}")

class TestCodeStructure(unittest.TestCase):
    """Додаткові тести структури коду"""
    
    def setUp(self):
        """Підготовка до тестів структури"""
        self.dir = Path(__file__).parent
    
    def test_file_exists(self):
        """Перевірка існування файлів"""
        files_list = ['_selflearning01.py', '_selflearning02.py', '_selflearning03.py']
        for file in files_list:
            file_path = self.dir / file
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.assertIsNotNone(content, f"Файл {file} повинен існувати")
            except FileNotFoundError:
                self.fail(f"Файл {file} не знайдено")
    
    def test_no_syntax_errors(self):
        """Перевірка відсутності синтаксичних помилок"""
        files_list = ['_selflearning01.py', '_selflearning02.py', '_selflearning03.py']
        for file in files_list:
            file_path = self.dir / file
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    code = f.read()
                compile(code, file, 'exec')
            except FileNotFoundError:
                # Пропускаємо файли, які не існують (вони будуть перевірені в test_file_exists)
                continue
            except SyntaxError as e:
                self.fail(f"Синтаксична помилка у файлі {file}: {e}")
            except Exception as e:
                self.fail(f"Помилка при перевірці файлу {file}: {e}")

def run_tests_with_detailed_output():
    """Запуск тестів з детальним виводом результатів"""
    print("=" * 60)
    print("ЗАПУСК ТЕСТІВ ДЛЯ файлів самостійної роботи")
    print("=" * 60)
    
    # Створюємо test suite
    suite = unittest.TestSuite()
    
    # Додаємо всі тести
    suite.addTest(TestHomeSelfLearning('test_subtraction_output'))
    suite.addTest(TestHomeSelfLearning('test_multiplication_output'))
    suite.addTest(TestHomeSelfLearning('test_savings_variable_creation'))
    suite.addTest(TestHomeSelfLearning('test_savings_print_output'))
    suite.addTest(TestHomeSelfLearning('test_monthly_savings_variable'))
    suite.addTest(TestHomeSelfLearning('test_num_months_variable'))
    suite.addTest(TestHomeSelfLearning('test_new_savings_calculation'))
    suite.addTest(TestHomeSelfLearning('test_new_savings_output'))
    suite.addTest(TestCodeStructure('test_file_exists'))
    suite.addTest(TestCodeStructure('test_no_syntax_errors'))
    
    # Запускаємо тести з детальним виводом
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Виводимо підсумок
    print("\n" + "=" * 60)
    print("ПІДСУМОК ТЕСТУВАННЯ:")
    print(f"Всього тестів: {result.testsRun}")
    print(f"Успішних: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Невдалих: {len(result.failures)}")
    print(f"Помилок: {len(result.errors)}")
    
    if result.failures:
        print("\nНЕВДАЛІ ТЕСТИ:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback.split('AssertionError: ')[-1][:500].strip()}")
    
    if result.errors:
        print("\nПОМИЛКИ:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback[:500]}")
    
    success_rate = ((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun) * 100
    print(f"\nВідсоток успішності: {success_rate:.1f}%")
    print("=" * 60)
    
    return result.wasSuccessful()

if __name__ == "__main__":
    # Запуск тестів
    success = run_tests_with_detailed_output()
    
    if success:
        print("🎉 Всі тести пройдено успішно!")
    else:
        print("❌ Деякі тести не пройдено. Перевірте код і спробуйте знову.")
    
        # Додаткова інформація для студента
        print("\n" + "=" * 60)
        print("ІНСТРУКЦІЇ ДЛЯ СТУДЕНТА:")
        print("1. Зробіть роботу за вказівками у файлах _selflearning*")
        print("2. Запустіть цей файл тестів: python tests_selflearning.py")
        print("3. Виправте помилки згідно з повідомленнями тестів")
        print("4. Повторюйте кроки 2-3 до успішного проходження всіх тестів")
    print("=" * 60)