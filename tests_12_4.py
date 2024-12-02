import logging
from rt_with_exceptions import Runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:

            test = Runner('walk_test', -33)
            for i in range(10):
                test.walk()
            self.assertEqual(test.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            test = Runner(asd)
            for i in range(10):
                test.run()
            self.assertEqual(test.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)




logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w',
                    encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')
if __name__ == '__main__':
    unittest.main()