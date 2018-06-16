import csv


class TaskHandler:
    def __init__(self, team_velocity):
        self.team_velocity = team_velocity

    def update_tasks_ratio(self, task_list):
        for task in task_list:
            ratio = self.count_ratio(task['story_points'], task['KSP'])
            task.update({'ratio': ratio})
        return task_list

    @staticmethod
    def count_ratio(story_points, KSP):
        ratio = float(int(KSP) / int(story_points))
        # setting precision to 3 decimal points
        ratio = round(ratio, 3)
        return ratio

    def choose_best_tasks(self, task_list):

        count_velocity = 0
        best_tasks_ids = []

        while count_velocity < self.team_velocity and len(task_list) != 0:
            # before we start set best ratio to first task
            best_task = task_list[0]

            # find the best available task to take
            for task in task_list:
                if task['ratio'] > best_task['ratio']:
                    best_task = task

            # when we have best available task,check if not exceeding team velocity
            count_velocity += int(best_task['story_points'])
            if count_velocity > self.team_velocity:

                # deleting this task, because we can't use it anymore
                task_list = self.delete_task(task_list, best_task['task_id'])

                # return if no more tasks available
                if self.is_empty(task_list):
                    return best_tasks_ids
                # also we can't add
                count_velocity -= int(best_task['story_points'])

                # choose the best task which we can get yet
                lasting_tasks = self.choose_best_with_condition(task_list, self.team_velocity - count_velocity)

                for task in lasting_tasks:
                    best_tasks_ids.append(task)

                return best_tasks_ids
            else:

                best_tasks_ids.append(best_task['task_id'])
                # delete this task, because w used it
                task_list = self.delete_task(task_list, best_task['task_id'])

        return best_tasks_ids

    @staticmethod
    def is_empty(task_list):
        if len(task_list) == 0:
            return True
        else:
            return False

    def choose_best_with_condition(self, task_list, points_left, other_ids=None):
        if other_ids is None:
            other_ids = []

        best_ratio = 0
        for task in task_list:
            if int(task['story_points']) <= points_left and float(task['ratio']) > best_ratio:
                best_ratio = task['ratio']
                best_task = task

        # if we used all points or didn't find any more matching tasks, we have nothing to do here
        if points_left == 0 or best_ratio == 0:
            return other_ids
        else:
            points_left -= int(best_task['story_points'])
            other_ids.append(best_task['task_id'])
            task_list = self.delete_task(task_list, int(best_task['task_id']))

            if task_list is None:
                return other_ids

            # call again recursively
            self.choose_best_with_condition(task_list, points_left, other_ids)

    @staticmethod
    def delete_task(task_list, task_id):

        for task in task_list:
            if task['task_id'] == task_id:
                task_list.remove(task)

                return task_list

    @staticmethod
    def print_chosen_tasks(chosen_tasks):
        print("Best tasks you can choose:")
        out_str = ', '.join(chosen_tasks)
        print(out_str, end='\n')
