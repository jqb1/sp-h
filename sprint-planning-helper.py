import argparse
from file_handler import FileHandler
from task_handler import TaskHandler


# here is where we start
def main():
    # parsing arguments passed when calling script
    parser = argparse.ArgumentParser(description="Choosing task file and max velocity")
    parser.add_argument('file', help="type filename with tasks", type=str)
    parser.add_argument('velocity', help="type velocity points of your team", type=int)

    arg = parser.parse_args()

    # pass a filename to TaskHandler class constructor
    file = FileHandler()
    task_list = file.read_file(arg.file)

    task_handler = TaskHandler()
    # provide every task with KSP/storypoints ratio
    task_list = task_handler.update_tasks_ratio(task_list)

    best_tasks = task_handler.choose_best_tasks(task_list, arg.velocity, best_tasks=[])
    best_task_ids = [task['task_id'] for task in best_tasks]

    print("Best tasks available for you:")
    task_str = ', '.join(best_task_ids)
    print(task_str)


if __name__ == '__main__':
    main()
