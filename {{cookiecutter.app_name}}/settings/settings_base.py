# -*- coding: utf-8 -*-
import os

# Installed apps
"""
All applications must be here for auto load urls e.t.c HINT: utils.application_utils
"""
INSTALLED_APPS = [
    'api',
]

### Databases
"""
Database connection info here
"""
#### End of databases block


#### Task block
TASKS_SETTING = {
    'delay': 600,
    'include': [
        'tasks.tasks'
    ]
}

#### End task block
