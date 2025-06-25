import sys
import types

# Provide a minimal bluetooth stub so the module can be imported without the
# real PyBluez dependency present during CI runs.
bluetooth_stub = types.ModuleType("bluetooth")
bluetooth_stub.discover_devices = lambda lookup_names=True: []
sys.modules.setdefault('bluetooth', bluetooth_stub)

import run_a2dp_tests as real
from run_a2dp_tests_mock import mock_test_a2dp_streaming


def test_mock_runs():
    """Ensure the mock streaming test executes without error."""
    mock_test_a2dp_streaming()


def test_real_runs(monkeypatch):
    """Run the real test with a mocked bluetooth discovery."""
    monkeypatch.setattr(real.bluetooth, "discover_devices", lambda lookup_names=True: [("00:11:22:33:44:55", "Device")])
    real.test_a2dp_streaming()
