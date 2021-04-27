from unittest.mock import patch

import Task2


@patch("Task2.get_text_from_network")
def test_count_dots(mock):
    mock.return_value = (
        '<meta http-equiv="Content-type" content="text/html; charset=utf-8" />\n  '
        '  <meta name="viewport" content="width=device-width'
    )
    assert Task2.count_dots_on_i("https://example.com/") == 5
