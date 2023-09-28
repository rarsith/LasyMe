from datetime import datetime, timedelta
import calendar


class DateTime(object):
    def __init__(self):
        self.date_format = "%Y-%m-%d"
        self.time_format = "%H:%M"
        self.date_and_time_format = '%Y-%m-%d %H:%M:%S:%f'

    @property
    def get_time_now(self):
        now = datetime.now()
        return now

    @property
    def date_and_time(self):
        now = datetime.now()
        return now.strftime(self.date_and_time_format)

    @property
    def curr_time(self):
        now = datetime.now()
        return now.strftime(self.time_format)

    @property
    def curr_date(self):
        now = datetime.now()
        return now.strftime(self.date_format)

    def has_weekend(self,  start_day, end_day, weekend=False) -> list:  # Takes raw date as start_day and end_date
        date_range = [start_day + timedelta(days=i) for i in range((end_day - start_day).days + 1)]
        weekdays = [date for date in date_range if date.weekday() < 5]
        if not weekend:
            return date_range
        return weekdays

    def today_to_end_day(self, end_day: str):
        now = datetime.now()
        today = now.date()
        end_day_to_datetime = datetime.strptime(end_day, self.date_format).date()
        days_left = end_day_to_datetime - today

        return days_left.days

    def start_to_end_day(self, start_day: str, end_day: str, exclude_weekend=False):

        start = datetime.strptime(start_day, self.date_format).date()
        end = datetime.strptime(end_day, self.date_format).date()

        days_full_range = self.has_weekend(start, end, weekend=exclude_weekend)

        if not exclude_weekend:
            interval_interval = end - start
            return interval_interval.days

        date_range = [start + timedelta(days=i) for i in range((end - start).days + 1)]
        weekdays = [date for date in date_range if date.weekday() < 5]

        days_excluding_weekends = len(weekdays)
        return days_excluding_weekends


    def get_time_elapsed(self, start_day: str, end_day: str, percentage=False, to_hours=False):
        now = datetime.now()
        start = datetime.strptime(start_day, self.date_format).date()
        total_time = self.start_to_end_day(start_day=start_day, end_day=end_day)
        time_left = self.today_to_end_day(end_day=end_day)
        today = now.date()
        today_hour = now.time()

        elapsed = today - start

        if not percentage:
            return elapsed.days

        else:
            if total_time !=0:
                to_percentage = ((total_time - time_left) / total_time)*100
                return to_percentage
            else:
                to_percentage = 100
                return to_percentage


if __name__ == "__main__":
    start_date_str = "2023-09-10"
    end_date_str = "2023-09-25"
    date_time = DateTime()

    left_days = date_time.today_to_end_day(end_date_str)
    print ("left_days", left_days)

    full_interval = date_time.start_to_end_day(start_date_str, end_date_str)
    full_interval_no_weekends = date_time.start_to_end_day(start_date_str, end_date_str, exclude_weekend=True)
    time_elapsed = date_time.get_time_elapsed(start_date_str, end_date_str)

    time_elapsed_percentage = date_time.get_time_elapsed(start_date_str, end_date_str, percentage=True)


    print("Days Left: ", left_days)
    print("Full Time Interval: ", full_interval)
    print("Time Elapsed: ", time_elapsed)
    print("Time Elapsed Workdays Only: ", full_interval_no_weekends)
    print("Time Elapsed Percentage: ", time_elapsed_percentage)

    #
    # now = datetime.now().date()
    # print(now)
    #
    #
    # end_date = datetime.strptime(datetime_str, '%Y-%m-%d').date()
    # future = end_date - now
    # print(future)
