import os

if __name__ == '__main__':
    command = "D:" \
        + " & cd Programming\DataStructAndAlgCourse\Labs\Lab1" \
        + " & coverage run -m unittest merge_sort_test.py" \
        + " & coverage report -m"

    os.system('start cmd /k "{0}"'.format(command))
