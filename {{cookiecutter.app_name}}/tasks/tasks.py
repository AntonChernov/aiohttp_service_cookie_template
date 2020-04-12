# -*- coding: utf-8 -*-
"""
All tasks put here please! HINT: utils.task_utils
"""
from utils.task_utils import TaskDecorator
from log import _log as log


@TaskDecorator(10)
async def task_test(app, first_name='John', last_name='Doe'):
    log.debug(
        'Hi {0} {1} I am a async periodic task!'.format(
            first_name, last_name)
    )


