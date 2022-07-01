#!/usr/bin/bash

set -e

# Create virtualenv
python3 -m venv venv
source venv/bin/activate

# Install florican
pip install .

# Configure florican
florican init

ls ~/.florican
grep "^## SSH config$" ~/.florican/config.yaml

cat > ~/.florican/config.yaml << EOF
---
ssh:
  username: foo

servers:
  localhost:
    - description: 'SSH Daemon'
      command: 'echo foo'
      expected: 'foo'
EOF

# Run florican
florican start

sleep 1

ls ~/.florican/florican.log
ps -p $(cat ~/.florican/florican.pid) | grep florican

# Get florican status
florican status | grep "^Daemon running: true$"
florican status | grep "description: SSH Daemon"

# Stop florican
florican stop

sleep 5

[ ! -f ~/.florican/florican.pid ]
florican status | grep "^Daemon running: false$"

# Cleanup
rm -rf ~/.florican
rm -rf venv
