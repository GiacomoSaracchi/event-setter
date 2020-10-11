#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 11:16:47 2020

@author: giacomosaracchi
"""

from datetime import datetime
from threading import Timer
import calendar

class SetEvent:
    
    # Set default params
    today = datetime.today()
    date = f"{today.day}/{today.month}/{today.year}"
    
    # Initialize and call functions splitting date and time
    def __init__(self, event, time, date=date):
        self.event = event
        self.time = time
        self.date = date
        self.today = datetime.today()
        self.split_time()
        self.split_date()
        self.set_timer()
    
    # Split up time into hour, minute, second. Raise exceptions if not coherent
    def split_time(self):
        for char in self.time:
            if not char.isdigit():
                self.time = self.time.replace(char, " ")
        ls = [int(num) for num in self.time.split()]
        self.hour = ls[0]
        if self.hour > 23:
            raise ValueError("Up to 23 hours 59 minutes 59 seconds etc. in a day")
        self.minute = ls[1]
        if self.minute > 59:
            raise ValueError("Up to 59 minutes 59 seconds etc. in an hour")
        self.second = ls[2]
        if self.second > 59:
            raise ValueError("Up to 59 seconds 59 decisecods etc. in a minute")
    
    # Split up date into day, month, year. Raise exceptions if not coherent
    def split_date(self):
        for char in self.date:
            if not char.isdigit():
                self.date = self.date.replace(char, " ")
        ls = [int(num) for num in self.date.split()]
        self.year = ls[2]
        if self.year < self.today.year:
            raise ValueError("Can't set timer in the past")
        self.month = ls[1]
        if self.month > 12:
            raise ValueError("Up to 12 months in a year")
        self.day = ls[0]
        current_month_length = calendar.monthrange(self.today.year, self.today.month)[1]
        if self.day > current_month_length:
            raise ValueError(f"Up to {current_month_length} days in {calendar.month_name[self.month]}")
    
    # Set timer with event                 
    def set_timer(self):
        today = self.today
        set_time = today.replace(year=self.year, month=self.month, day=self.day, 
                                 hour=self.hour, minute=self.minute, 
                                 second=self.second)
        delta_t = set_time - today
        secs_to_event = delta_t.total_seconds() 
        self.timer = Timer(secs_to_event, self.event)
        self.timer.start()
    
    # Stop timer and cancel event
    def stop(self):
        self.timer.cancel()
