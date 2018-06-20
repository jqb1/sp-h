class TaskHandler:

    # method which provide every task with its ratio (helps to choose which task is the best to take)
    def update_tasks_ratio(self, task_list):
        for task in task_list:
            ratio = self.count_ratio(task['story_points'], task['KSP'])
            task.update({'ratio': ratio})
        return task_list

    @staticmethod
    def count_ratio(story_points, ksp):
        ratio = float(int(ksp) / int(story_points))
        # setting precision to 3 decimal points
        ratio = round(ratio, 3)
        return ratio

    def choose_best_tasks(self, task_list, velocity_left, best_tasks):

        best_task = None

        best_ratio = 0
        for task in task_list:

            if int(task['story_points']) <= velocity_left and float(task['ratio']) > best_ratio:
                best_ratio = float(task['ratio'])
                best_task = task

        # if we used all points or didn't find any more matching tasks, we have nothing to do here
        if velocity_left == 0 or best_ratio == 0:
            # if there is some velocity points left
            # check if last element can be replaced by better-score task
            if velocity_left != 0:
                best_tasks = self.find_last_element(task_list, best_tasks, velocity_left)

            return best_tasks

        else:
            velocity_left -= int(best_task['story_points'])
            best_tasks.append(best_task)

            task_list = self.delete_task(task_list, int(best_task['task_id']))

            if self.is_empty(task_list):
                return best_tasks

            # run again recursively
            return self.choose_best_tasks(task_list, velocity_left, best_tasks)

    # this method is crucial if we want our KSP to be the highest possible
    @staticmethod
    def find_last_element(task_list, best_tasks_list, velocity_left):
        last_task = best_tasks_list[-1]
        last_task_velocity = int(last_task['story_points'])

        velocity_left -= last_task_velocity

        # we have available velocity, check if there is better task to take
        # for now, the best task is the last one added
        best_ksp = int(last_task['KSP'])
        best_task = last_task
        for task in task_list:
            if int(task['story_points']) == velocity_left and int(task['story_points']) > best_ksp:
                best_ksp = int(task['story_points'])
                best_task = task

        # if better task was found, change last one added and return
        if best_task != last_task:
            # change last element
            best_tasks_list[-1] = best_task
            return best_tasks_list
        else:
            return best_tasks_list

    @staticmethod
    def is_empty(task_list):
        if len(task_list) == 0:
            return True
        else:
            return False

    @staticmethod
    def delete_task(task_list, task_id):

        for task in task_list:
            if int(task['task_id']) == task_id:
                task_list.remove(task)

                return task_list

    @staticmethod
    def print_chosen_tasks(chosen_tasks):
        print("Best tasks you can choose:")
        out_str = ', '.join(chosen_tasks)
        print(out_str, end='\n')
