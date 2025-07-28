import os
import subprocess
from pathlib import Path


def test_run_a2dp_mock():
    repo_root = Path(__file__).resolve().parents[1]
    results_dir = repo_root / "results"
    results_dir.mkdir(exist_ok=True)
    log_file = results_dir / "a2dp_test_results.txt"

    if log_file.exists():
        log_file.unlink()

    target_dir = Path("/usr/src/a2dp_test/results")
    target_dir.mkdir(parents=True, exist_ok=True)
    symlink_path = target_dir / "a2dp_test_results.txt"
    if symlink_path.exists() or symlink_path.is_symlink():
        symlink_path.unlink()
    symlink_path.symlink_to(log_file)

    try:
        subprocess.run([
            "python",
            str(repo_root / "a2dp_test" / "run_a2dp_tests_mock.py"),
        ], check=True)
    finally:
        if symlink_path.exists():
            symlink_path.unlink()
        try:
            target_dir.rmdir()
            target_dir.parent.rmdir()
        except OSError:
            pass

    assert log_file.exists(), "Result file was not created"
    content = log_file.read_text()
    assert "A2DP streaming with MockDevice1 successful" in content
