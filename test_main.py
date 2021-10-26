import os

if __name__ == '__main__':
    command = "D:" \
        + " & cd Programming\DataStructAndAlgCourse\Labs\Lab5" \
        + " & coverage run -m unittest test_tarjan.py" \
        + " & coverage report -m"

    os.system('start cmd /k "{0}"'.format(command))
