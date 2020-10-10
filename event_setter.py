#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 11:16:47 2020

@author: giacomosaracchi
"""

from datetime import datetime
from threading import Timer
import calendar

# event is function to execute. No () after name
# time is string made of separated hours, minutes
# day is int (up to the end of the month)
# month is int (up to 12)

class SetEvent:
    
    today = datetime.today()
    
    def __init__(self, event, time, day=today.day, month=today.month):
        self.event = event
        self.time = time
        self.day = day
        self.month = month
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
        set_time = today.replace(month=self.month, day=self.day, hour=self.hour, 
                                 minute=self.minute, second=self.second)
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
            raise ValueError(f"Up to {current_month_length} days in {calendar.month_name[today.month]}")
        self._day = value
        
    @property
    def month(self):
        return self._month
    
    @month.setter
    def month(self, value):
        if value > 12:
            raise ValueError("Up to 12 months in a year")
        self._month = value
