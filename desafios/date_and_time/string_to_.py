from datetime import datetime


def convert_string_with_hour_to_seconds(time: str) -> int:
    """Will receive a string with the format HH:MM:SS and will return the total of seconds

    Args:
        time (str): _description_

    Returns:
        int: _description_
    """
    time_obj = datetime.strptime(time, '%H:%M:%S')
    total_seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
    return total_seconds