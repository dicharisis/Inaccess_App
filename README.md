The goal of this application is toreturn the matching
timestamps of a periodic task.

A periodic task is described by the following properties:
   # Period (every hour, every day, ...)
   # Invocation point (where inside the period should be invoked)
   # Timezone (days/months/years are timezone-depended)

The application should return all matching timestamps of a periodic task (ptlist) between 2 points in time
(t1, t2). t1, t2 and the entries of ptlist are in UTC with seconds accuracy, in the following form:
20060102T150405Z


The supported periods should be: 1h, 1d, 1mo, 1y. The invocation timestamp should be at the start of the
period (e.g. for 1h period a matching timestamp is considered the 20210729T010000Z). The application
should accept the following command-line arguments:
# --period
# --t1
# --t2
# --tz


On success, the application exit status is 0 and a list with all matching timestamps, in UTC, for the
requested period is printed on stdout. On failure, the application exit status is 10 and an appropriate
message is printed on stderr.
