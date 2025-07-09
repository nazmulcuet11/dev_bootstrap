"""
Dock setup script for macOS.

This script configures the macOS dock with a predefined set of applications.
It moves the dock to the left side and adds commonly used applications.
"""

import os

from docklib import Dock

# Define applications to add to the dock
APPS_TO_ADD = [
    '/System/Applications/App Store.app',
    '/Applications/Safari.app',
    '/Applications/Google Chrome.app',
    '/Applications/Microsoft Outlook.app',
    '/Applications/Microsoft Teams.app',
    '/System/Applications/Notes.app',
    '/Applications/Notion.app',
    '/Applications/Proxyman.app',
    '/System/Applications/System Settings.app',
    '/System/Applications/Utilities/Terminal.app',
    '/Applications/Visual Studio Code.app',
    '/Applications/Xcode.app',
    '/Applications/Slack.app',
]


def main() -> None:
    """Configure the macOS dock with predefined applications."""
    dock = Dock()

    # Move dock to the left side
    dock.orientation = "left"

    # Remove all current items
    dock.items["persistent-apps"] = []

    # Add new items
    for app in APPS_TO_ADD:
        if os.path.exists(app):
            entry = dock.makeDockAppEntry(app)
            dock.items["persistent-apps"].append(entry)
        else:
            print(f"not found: {app}")

    # Save the dock configuration
    dock.save()


if __name__ == "__main__":
    main()
