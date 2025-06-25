import sys
import types

bluetooth_stub = types.ModuleType("bluetooth")
bluetooth_stub.discover_devices = lambda lookup_names=True: []
sys.modules.setdefault('bluetooth', bluetooth_stub)

import run_hfp_tests as real
from run_hfp_tests_mock import mock_test_hfp


def test_mock_runs():
    """Ensure the mock HFP test executes without error."""
    mock_test_hfp()


def test_real_runs(monkeypatch):
    """Run the real HFP test with mocked bluetooth discovery."""
    monkeypatch.setattr(real.bluetooth, "discover_devices", lambda lookup_names=True: [("AA:BB:CC:DD:EE:FF", "Device")])
    real.test_hfp_connection()
