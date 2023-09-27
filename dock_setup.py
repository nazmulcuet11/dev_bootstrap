# required packages
# 1. docklib
# 2. pyobjc

import os
from docklib import Dock

dock = Dock()

# move dock to the left side
dock.orientation = "left"

# remove all current items
dock.items["persistent-apps"] = []

# add new items
apps_to_add = [
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
    '/Applications/Sourcetree.app',
    '/Applications/Visual Studio Code.app',
    '/Applications/Xcode.app',
    '/Applications/Slack.app',
]
for app in apps_to_add:
    if os.path.exists(app):
        entry = dock.makeDockAppEntry(app)
        dock.items["persistent-apps"].append(entry)
    else:
        print("not found: " + app)

# save
dock.save()