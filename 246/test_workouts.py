import pytest

from workouts import print_workout_days


@pytest.mark.parametrize("values, expected", [
    ('upper body #1', 'Mon\n'),
    ('lower body #1', 'Tue\n'),
    ('30 min cardio', 'Wed\n'),
    ('upper body #2', 'Thu\n'),
    ('lower body #2', 'Fri\n'),
    ('sun', 'No matching workout\n'),
    ('sat', 'No matching workout\n'),
    ('upper', 'Mon, Thu\n'),
    ('lower', 'Tue, Fri\n'),
])
def test_print_workout_days(capsys, values, expected):
    print_workout_days(values)
    captured = capsys.readouterr()
    assert captured.out == expected
