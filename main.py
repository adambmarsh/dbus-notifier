"""
module: test harness for dbus-notifier
"""

import argparse
import sys
import time


from dbus_notifier.notifysender import NotifySender


def main():
    """
    main function
    :return: void
    """
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
                        default={},
                        required=False)

    args = parser.parse_args()

    if isinstance(args.notifications, str):
        args.notifications = dict(nf.split(":") for nf in args.notifications.strip().split(","))

    sender = NotifySender(args.title, args.notifications)

    # sender.notify(message="Post this")
    if not args.notifications:
        print("No notifications received")
        return

    for key in args.notifications.keys():
        time.sleep(0.5)
        sender.notify(select_key=str(key))


if __name__ == '__main__':
    sys.exit(main())
