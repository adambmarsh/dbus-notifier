import os

import dbusnotify
from dotenv import dotenv_values


__version__ = '0.0.0'


class NotifySender(object):

    def __init__(self, title, messages=None):
        self._title = None
        self._messages = None
        self.title = title
        self.messages = messages

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, in_str=None):
        self._title = in_str or ""

    @property
    def messages(self):
        return self._messages

    @messages.setter
    def messages(self, in_dict=None):
        self._messages = in_dict or dict()

    def _post_notification(self, in_title="", in_description=""):
        ve_path = os.getenv("VIRTUAL_ENV")
        ve_config = dotenv_values(os.path.join(ve_path, ".env_dbus_notifier"))

        if ve_config:
            icon_file = os.path.join(ve_path, ve_config.get("DBUS_NOTIFIER_ICON", ''))
        else:
            config = dotenv_values(os.path.join(os.getcwd(), '.env_dbus_notifier'))
            icon_file = os.path.join(os.getcwd(), config.get("DBUS_NOTIFIER_ICON", ''))

        if not os.path.isfile(icon_file):
            icon_file = ""
        dbusnotify.write(
            in_description,
            title=in_title if in_title else self.title,
            icon=icon_file,  # On Windows .ico is required, on Linux - .png
        )

    def notify(self, message=None, select_key=None):
        title = self.title

        if select_key and self.messages:
            self._post_notification(title, self.messages.get(select_key, ""))
            return

        if not message:
            return

        self._post_notification(title, message)
