import importlib


def run_task(week: str, homework: str, task_number: str) -> None:
    week = week.zfill(2)
    if homework == "web":
        homework = "webinar"
    else:
        homework = homework.zfill(2)

    try:
        if homework == "webinar":
            module_name = f"week_{week}.webinar.solutions"
        else:
            module_name = f"week_{week}.homework_{homework}.solutions"

        module = importlib.import_module(module_name)
        task_name = f"task_{task_number}"
        task = getattr(module, task_name, None)

        if task:
            task()
        else:
            print(f"Task {task_number} not found in {module_name}.")
    except ModuleNotFoundError:
        print(f"Module {module_name} not found.")
