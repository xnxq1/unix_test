import datetime
import pytz


def converter_time(unix: int) -> str:

    gmt = pytz.timezone('GMT')
    converted_time = datetime.datetime.fromtimestamp(unix, gmt)
    if converted_time.second != 0:
        converted_time = converted_time.strftime("%I:%M:%S %p")
    elif converted_time.minute != 0:
        converted_time = converted_time.strftime("%I:%M %p")
    else:
        converted_time = converted_time.strftime("%I %p")

    converted_time = converted_time.lstrip("0")
    return converted_time


def unix_time_converter(data: dict) -> str:
    result = ''
    indicate = 0
    count = 0
    for key, value in data.items():

        if indicate:
            result += converter_time(value[0]["value"])
            result += f'\n'

        result += f'{key.capitalize()}: '

        if len(value) == 0:
            result += 'Closed'
            result += f'\n'
        else:
            for i in range(indicate, len(value)):
                converted_time = converter_time(value[i]["value"])
                result += f'{converted_time}'
                count += 1

                if count % 2 == 1:
                    result += ' - '
                elif i != len(value) - 1:
                    result += ', '

            indicate = 0
            if value[-1]["type"] == "open":
                indicate = 1
            else:
                result += f'\n'
        count = 0

    return result


if __name__ == '__main__':
    data = {}
    print(unix_time_converter(data=data))
