import importlib

from task_runner import run_task


def get_week(weeks: dict) -> str:
    valid_weeks = list(weeks.keys())
    week_range = f"{valid_weeks[0]} - {valid_weeks[-1]}"
    while True:
        week = input(f"Enter the week number ({week_range}, type 'end' to exit): ")
        if week.lower() == "end":
            return "end"
        if week in valid_weeks:
            return week
        print(f"Invalid week number. Valid weeks are: {week_range}")


def get_homework(week: str, weeks: dict) -> str:
    valid_homeworks = weeks[week]
    print("Available homeworks:")
    for i, homework in enumerate(valid_homeworks, start=1):
        print(f"{i}. {homework}")
    print(f"{len(valid_homeworks) + 1}. Webinar")

    homework_range = f"1 - {len(valid_homeworks)}"
    while True:
        homework = input(
            f"Enter the homework number ({homework_range}, type 'web' to choose webinar,"
            f"type 'back' to go back, type 'end' to exit): "
        )
        if homework.lower() in ["web", "end", "back"]:
            return homework.lower()
        if homework.isdigit() and 1 <= int(homework) <= len(valid_homeworks):
            return homework
        print(f"Invalid homework number. Valid homeworks are: {homework_range} or 'web'")


def get_tasks(week: str, homework: str) -> int:
    if homework == "web":
        module_name = f"week_{week.zfill(2)}.webinar.solutions"
    else:
        module_name = f"week_{week.zfill(2)}.homework_{homework.zfill(2)}.solutions"

    try:
        module = importlib.import_module(module_name)
        tasks = [func for func in dir(module) if func.startswith("task_")]
        task_count = len(tasks)
        print(f"There are {task_count} tasks available in this homework.")
        return task_count
    except ModuleNotFoundError:
        print(f"Module {module_name} not found.")
        return 0


def get_task_number(task_count: int) -> str:
    while True:
        task_number = input(
            f"Which task do you want to run? (1 - {task_count}, type 'back' to go back, type 'end' to exit): "
        )
        if task_number.lower() in ["end", "back"]:
            return task_number.lower()
        if task_number.isdigit() and 1 <= int(task_number) <= task_count:
            return task_number
        print(f"Invalid task number. Valid tasks are: 1 - {task_count}")


def main() -> None:
    weeks = {
        "1": ["Variables and Built-in Functions", "Boolean, None, and Strings"],
        "2": ["Conditions and Loops", "Functions"],
    }

    while True:
        week = get_week(weeks)
        if week == "end":
            break

        while True:
            homework = get_homework(week, weeks)
            if homework in ["end", "back"]:
                if homework == "end":
                    return
                break

            task_count = get_tasks(week, homework)
            if task_count == 0:
                continue

            while True:
                task_number = get_task_number(task_count)
                if task_number in ["end", "back"]:
                    if task_number == "end":
                        return
                    break

                run_task(week, homework, task_number)


if __name__ == "__main__":
    main()
