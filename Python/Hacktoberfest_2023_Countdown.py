import datetime

hacktoberfest_end_date = datetime.datetime(2023, 11, 1, 0, 0, 0)

def get_time_until_hacktoberfest():
    current_time = datetime.datetime.now()
    time_until_hacktoberfest = hacktoberfest_end_date - current_time
    return time_until_hacktoberfest

time_until_hacktoberfest = get_time_until_hacktoberfest()

print(f"Time until Hacktoberfest 2023 ends: {time_until_hacktoberfest.days} days, {time_until_hacktoberfest.seconds // 3600} hours, {(time_until_hacktoberfest.seconds // 60) % 60} minutes, {time_until_hacktoberfest.seconds % 60} seconds")
