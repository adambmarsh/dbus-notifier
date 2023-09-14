import argparse
import sys

from dbus_notifier.notifysender import NotifySender


def main():
    parser = argparse.ArgumentParser(description="This program is a very simple test harness for NotifySender "
                                                 "which posts dbus notification messages.")
    parser.add_argument("-t", "--summary", help="A string containing the summary to use in notifications.",
                        type=str,
                        dest='title',
                        default='',
                        required=False)
    parser.add_argument("-n", "--messages", help="A dictionary containing notification codes and messages.",
                        type=str,
                        dest='notifications',
                        default=dict(),
                        required=False)

    args = parser.parse_args()

    if isinstance(args.notifications, str):
        args.notifications = dict(nf.split(":") for nf in args.notifications.strip().split(","))

    sender = NotifySender(args.title, args.notifications)

    # sender.notify(message="Post this")
    sender.notify(select_key=str(2))
    sender.notify(select_key=str(1))


if __name__ == '__main__':
    sys.exit(main())
