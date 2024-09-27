import pytest


@pytest.fixture
def temp_file(tmp_path):
    def _create_temp_file(content):
        temp_file = tmp_path / "temp_file.txt"
        temp_file.write_text(content)
        return temp_file

    return _create_temp_file
