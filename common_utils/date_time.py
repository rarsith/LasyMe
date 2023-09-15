from datetime import datetime, timedelta
import calendar


class DateTime(object):
    def __init__(self):
        self.time_now = datetime.now()
        self.date_format = "%Y-%m-%d"
        self.time_format = "%H:%M"

    @property
    def curr_time(self):
        return self.time_now.strftime(self.time_format)

    @property
    def curr_date(self):
        return self.time_now.strftime(self.date_format)

    def today_to_end_day(self, end_day: str):
        today = self.time_now.date()
        end_day_to_datetime = datetime.strptime(end_day, self.date_format).date()
        days_left = end_day_to_datetime - today

        return days_left.days

    def start_to_end_day(self, start_day: str, end_day: str):
        start = datetime.strptime(start_day, self.date_format).date()
        end = datetime.strptime(end_day, self.date_format).date()
        interval_interval = end - start

        return interval_interval.days

    def get_time_elapsed(self, start_day: str, end_day: str, percentage=False, to_hours=False):
        start = datetime.strptime(start_day, self.date_format).date()
        total_time = self.start_to_end_day(start_day=start_day, end_day=end_day)
        time_left = self.today_to_end_day(end_day=end_day)
        today = self.time_now.date()
        today_hour = self.time_now.time()

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
    time_elapsed = date_time.get_time_elapsed(start_date_str, end_date_str)

    time_elapsed_percentage = date_time.get_time_elapsed(start_date_str, end_date_str, percentage=True)

    print("Days Left: ", left_days)
    print("Full Time Interval: ", full_interval)
    print("Time Elapsed: ", time_elapsed)
    print("Time Elapsed Percentage: ", time_elapsed_percentage)

    #
    # now = datetime.now().date()
    # print(now)
    #
    #
    # end_date = datetime.strptime(datetime_str, '%Y-%m-%d').date()
    # future = end_date - now
    # print(future)
