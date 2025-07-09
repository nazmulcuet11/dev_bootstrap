#!/bin/bash

# Check for Homebrew and install if missing
if ! command -v brew &>/dev/null; then
  echo "Homebrew not found. Installing Homebrew..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Check for Ansible and install if missing
if ! command -v ansible-playbook &>/dev/null; then
  echo "Ansible not found. Installing Ansible via Homebrew..."
  brew install ansible
fi

# Run the main automation playbook
ansible-playbook --ask-become-pass master.yml