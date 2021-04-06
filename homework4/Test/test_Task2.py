from unittest.mock import patch

import Task2


@patch("Task2.count_dots_on_i")
def test_count_dots(mock):
    mock.return_value = 56
    assert Task2.count_dots_on_i("https://example.com/") == 56
