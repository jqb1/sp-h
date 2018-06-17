import csv


class TaskHandler:

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

    def choose_best_tasks(self, task_list, velocity_left, best_task_ids):

        best_task = None

        best_ratio = 0
        for task in task_list:

            if int(task['story_points']) <= velocity_left and float(task['ratio']) > best_ratio:
                best_ratio = int(task['ratio'])
                best_task = task

        # if we used all points or didn't find any more matching tasks, we have nothing to do here
        if velocity_left == 0 or best_ratio == 0:

            return best_task_ids

        else:
            velocity_left -= int(best_task['story_points'])
            best_task_ids.append(best_task['task_id'])

            task_list = self.delete_task(task_list, int(best_task['task_id']))

            if len(task_list) == 0:
                return best_task_ids

            # return ids when we end
            return self.choose_best_tasks(task_list, velocity_left, best_task_ids)

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
