import os

if __name__ == '__main__':
    command = "D:" \
        + " & cd Programming\DataStructAndAlgCourse\Labs\Lab4" \
        + " & coverage run -m unittest test_dfs.py" \
        + " & coverage report -m"

    os.system('start cmd /k "{0}"'.format(command))
