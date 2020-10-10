#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 11:16:47 2020

@author: giacomosaracchi
"""

from datetime import datetime, timedelta
from threading import Timer
import calendar

# event is function to execute. No () after name
# time is string made of separated hours, minutes
# day is int (up to the end of the month)

# 

class SetEvent:
    
    def __init__(self, event, time, day=datetime.today().day):
        self.event = event
        self.day = day
        self.time = time
        self.today = datetime.today()
        self.split_time()
        self.set_timer()
        
    def split_time(self):
        for char in self.time:
            if not char.isdigit():
                self.time = self.time.replace(char, " ")
        ls = [int(num) for num in self.time.split()]
        self.hour = ls[0]
        self.minute = ls[1]
        self.second = ls[2]
                    
    def set_timer(self):
        today = self.today
        set_time = today.replace(day=self.day, hour=self.hour, minute=self.minute,
                                 second=self.second) 
        set_time += timedelta(days=self.day - today.day)
        delta_t = set_time - today
        secs_to_event = delta_t.total_seconds() 
        self.timer = Timer(secs_to_event, self.event)
        self.timer.start()
    
    def stop_timer(self):
        self.timer.cancel()
        
    @property
    def day(self):
        return self._day
    
    @day.setter
    def day(self, value):
        today = datetime.today()
        current_month_length = calendar.monthrange(today.year, today.month)[1]
        if value > current_month_length:
            raise ValueError("Can't set for after the end of the month")
        self._day = value
        
        
        
        
        