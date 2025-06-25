import sys
import types

bluetooth_stub = types.ModuleType("bluetooth")
bluetooth_stub.discover_devices = lambda lookup_names=True: []
sys.modules.setdefault('bluetooth', bluetooth_stub)

import run_conn_disc_tests as real
from run_conn_disc_tests_mock import mock_test_connect_disconnect


def test_mock_runs():
    """Ensure the mock connectivity test executes without error."""
    mock_test_connect_disconnect()


def test_real_runs(monkeypatch):
    """Run the real test with mocked bluetooth discovery."""
    monkeypatch.setattr(real.bluetooth, "discover_devices", lambda lookup_names=True: [("11:22:33:44:55:66", "Device")])
    real.test_connect_disconnect()
