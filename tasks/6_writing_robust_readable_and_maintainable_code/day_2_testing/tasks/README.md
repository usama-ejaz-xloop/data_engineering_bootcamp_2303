# Pythonpath

**Note**: Be sure to add `<project_path>/tasks/6_writing_robust_readable_and_maintainable_code/day_2_testing/tasks`
to `PYTHONPATH` env variable before trying to launch the tests.

```shell
export PYTHONPATH="${PYTHONPATH}:<project_path>/tasks/6_writing_robust_readable_and_maintainable_code/day_2_testing/tasks"
```

# Tox

To launch the tests using tox, use the following commands from the project root:

```shell
cd tasks/6_writing_robust_readable_and_maintainable_code/day_2_testing/tasks
pip install -r requirements.txt
tox
```

In case of any errors, be sure to check your tox.ini configuration file.
