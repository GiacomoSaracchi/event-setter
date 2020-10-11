# event-setter

A single file containing the SetEvent class, which uses datetime, calendar and threading's Timer class to trigger a function at any given time. If the application used to run it crashes or is closed, the function will execute upon its reopening.

SetEvent parameters are:

  event: function to be run (default: None)
  
  time: time at which to run the function. String in the form "hour%minute%second" where % can be any separator (default: None)
  
  date: date at which to run the function. String in the form "day%month%year" where % can be any separator (default: today's date)
