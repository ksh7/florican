import pytest


def test_notify(discord_notifier, mock_hikari_rest_app_client):
    text = "Lorem ipsum."

    discord_notifier.notify(text)

    mock_hikari_rest_app_client.fetch_channel.assert_called_with(
        discord_notifier._channel_id
    )
    mock_hikari_rest_app_client.create_message.assert_called_with(None, text)
