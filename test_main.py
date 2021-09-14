import os

if __name__ == '__main__':
    command = "D:" \
        + " & cd Programming\DataStructAndAlgCourse\Labs\Lab2" \
        + " & coverage run -m unittest test_bst.py" \
        + " & coverage report -m"

    os.system('start cmd /k "{0}"'.format(command))
