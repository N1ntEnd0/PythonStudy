from Task3 import my_precious_logger


def test_output_to_stderr(capsys):
    my_precious_logger("error: file not found")
    captured = capsys.readouterr()
    assert captured.err == "error: file not found\n"
    assert captured.out == ""


def test_output_to_stdout(capsys):
    my_precious_logger("OK")
    captured = capsys.readouterr()
    assert captured.out == "OK\n"
    assert captured.err == ""
