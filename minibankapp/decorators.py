# -*- coding: utf-8 -*-

from time import time
from functools import wraps
from .models import LogModel


class ActivityMonitoringClass:

    def __init__(self, show_data=True):
        self.show_data = show_data

    def __call__(self, original_function):

        @wraps(original_function)
        def wrapper(request, *args, **kwargs):
            user_log = str(request.user)
            data_log = f'{args}{kwargs}'
            if not self.show_data:
                data_log = 'Data restricted'
            start_time = time()
            action = original_function.__name__
            function = f'{request.__class__.__name__} - {request.get_full_path()}'
            result = original_function(request, *args, **kwargs)
            if result.status_code in [200, 201, 301, 302]:
                end_time = time()
                duration = round(end_time - start_time, 6)
                status_log = 'Success'
            else:
                duration = 0
                status_log = 'Failed'
            new_log = LogModel()
            new_log.action_log = action
            new_log.function_log = function
            new_log.duration_log = duration
            new_log.data_log = data_log[:250]
            new_log.user_log = user_log
            new_log.status_log = status_log
            new_log.save()
            return result    
        return wrapper
