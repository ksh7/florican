import pytest

from florican.notifiers import Encoding
from florican.gatekeeper import GateKeeper


def test_gatekeeper_load_config(gatekeeper):
    assert len(gatekeeper.checks) == 1
    assert len(gatekeeper._notifiers) == 1


def test_gatekeeper_notify_no_icon(gatekeeper, mock_notifier):
    message = "Lorem ipsum"
    gatekeeper.am_i_alive(message)

    mock_notifier.notify.assert_called_with(message)


def test_gatekeeper_notify_utf8(gatekeeper, mock_notifier):
    mock_notifier.ENCODING = Encoding.UTF8

    message = "Lorem ipsum"
    icon = "!"
    gatekeeper.am_i_alive(message, icon)

    mock_notifier.notify.assert_called_with(f"{icon} {message}")


def test_gatekeeper_notify_ascii(gatekeeper, mock_notifier):
    mock_notifier.ENCODING = Encoding.ASCII

    message = "Lorem ipsum"
    icon = "!"
    gatekeeper.am_i_alive(message, icon)

    mock_notifier.notify.assert_called_with(message)


@pytest.mark.parametrize("changed", (True, False))
@pytest.mark.parametrize("expected", (True, False))
def test_gatekeeper_tick_tick(mocker, gatekeeper, mock_notifier, changed, expected):
    check = mocker.Mock()
    check.run.return_value = (changed, expected, "foo", "bar")
    gatekeeper.checks = [check]

    gatekeeper.tick_tick()

    check.run.assert_called()

    if changed and expected:
        mock_notifier.notify.assert_called()
    elif changed and not expected:
        mock_notifier.notify.assert_called()
    elif not changed and expected:
        mock_notifier.notify.assert_not_called()
    elif not changed and not expected:
        mock_notifier.notify.assert_not_called()
