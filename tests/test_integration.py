import subprocess
import pytest

pytestmark = pytest.mark.integration

@pytest.mark.parametrize(
    'args',
    [
        pytest.param(('-d', 'yale.edu', '-b', 'baidu'), id="baidu"),
        pytest.param(('-d', 'yale.edu', '-b', 'certspotter'), id="certspotter"),
        pytest.param(('-d', 'hcl.com', '-b', 'crtsh'), id="crtsh"),
        pytest.param(('-d', 'yale.edu', '-b', 'duckduckgo'), id="duckduckgo"),
        pytest.param(('-d', 'yale.edu', '-b', 'hackertarget'), id="hackertarget"),
        pytest.param(('-d', 'yale.edu', '-b', 'otx'), id="otx"),
        pytest.param(('-d', 'yale.edu', '-b', 'rapiddns'), id="rapiddns"),
        pytest.param(('-d', 'yale.edu', '-b', 'threatminer'), id="threatminer"),
        pytest.param(('-d', 'yale.edu', '-b', 'urlscan'), id="urlscan"),
        pytest.param(('-d', 'yale.edu', '-b', 'yahoo'), id="yahoo"),
        pytest.param(('-d', 'yale.edu', '-c'), id="brute force"),
    ],
)
def test_theharvester(args: list[str]) -> None:
    cmd = ('theHarvester', *args)
    result = subprocess.run(cmd, text=True)

    assert result.returncode == 0, f'Command {" ".join(cmd)!r} failed with exit code {result.returncode}'
