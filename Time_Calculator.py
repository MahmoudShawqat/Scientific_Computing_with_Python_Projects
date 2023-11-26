def add_time(start_time, duration, start_day=None):
    # Days of the week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Convert start_time to 24-hour format
    start_time_parts = start_time.split(":")
    hours = int(start_time_parts[0])
    minutes = int(start_time_parts[1][:2])
    am_pm = start_time_parts[1][-2:]

    if am_pm == "PM" and hours != 12:
        hours += 12

    # Convert duration to minutes
    duration_parts = duration.split(":")
    duration_hours = int(duration_parts[0])
    duration_minutes = int(duration_parts[1])

    # Add duration to start_time
    total_minutes = hours * 60 + minutes + duration_hours * 60 + duration_minutes
    new_hours = total_minutes // 60 % 24
    new_minutes = total_minutes % 60

    # Determine AM or PM for the new time
    new_am_pm = "AM" if new_hours < 12 else "PM"

    # Convert new_hours to 12-hour format
    new_hours = new_hours % 12 if new_hours % 12 != 0 else 12

    # Format the result
    new_time = f"{new_hours:}:{new_minutes:02d} {new_am_pm}"

    # Determine the day of the week
    if start_day:
        start_day_index = days_of_week.index(start_day.capitalize())
        new_day_index = (start_day_index + total_minutes // (24 * 60)) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"

    # Add the number of days if more than one day has passed
    days_later = total_minutes // (24 * 60)
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time


print(add_time("2:59 AM", "24:00"))
# Returns: 6:10 PM

print(add_time("11:55 AM", "3:12"))
# Returns: 2:02 PM, Monday

print(add_time("9:15 PM", "5:30"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)