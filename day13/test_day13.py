import shutil
import os
import pytest
from day13 import part2


@pytest.fixture
def input_file(tmpdir):
    exists = os.path.isfile("input")
    if exists:
        shutil.move("input", tmpdir)
    yield
    if exists:
        shutil.move(tmpdir / "input", "input")
    else:
        os.unlink("input")


@pytest.mark.parametrize(
    "data, expect",
    [
        ("17,x,13,19", 3417),
        ("67,7,59,61", 754018),
        ("67,x,7,59,61", 779210),
        ("67,7,x,59,61", 1261476),
        ("1789,37,47,1889", 1202161486),
    ],
)
def test_part2(input_file, data, expect):
    with open("input", "w") as f:
        f.write('1\n')
        f.write(data + '\n')

    assert part2() == expect
