import unittest
from task_handler import TaskHandler
from file_handler import FileHandler


class TestOutput(unittest.TestCase):

    def test_output(self):
        task_handler = TaskHandler()

        task_list = FileHandler.read_file('csv_with_tasks.csv')

        task_list = task_handler.update_tasks_ratio(task_list)

        output = task_handler.choose_best_tasks(task_list, 10, best_tasks=[])
        self.assertIsNotNone(output, msg="Output is correct")


if __name__ == '__main__':
    unittest.main()
