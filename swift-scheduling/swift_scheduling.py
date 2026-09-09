from datetime import datetime, timedelta


def delivery_date(start, description):
    parsed_date = datetime.fromisoformat(start)
    new_dt = parsed_date.replace(hour=13, minute=0, second=0)
    match description:
        case "NOW":
            update_time = parsed_date + timedelta(hours=2)
        case "ASAP":
            if parsed_date >= new_dt:
                update_time = new_dt + timedelta(days=1)
            else:
                update_time = parsed_date.replace(hour=17, minute=0, second=0)
        case "EOW":
            if parsed_date.weekday() < 3:
                update_time = parsed_date + timedelta(days=4 - parsed_date.weekday())
                update_time = update_time.replace(hour=17, minute=0, second=0)
            else:
                update_time = parsed_date + timedelta(days=6 - parsed_date.weekday())
                update_time = update_time.replace(hour=20, minute=0, second=0)
        case description if description and description[0] in "123456789":
            if description[1] in "0123456789":
                new_month = int(description[0:2])
            else:
                new_month = int(description[0])
            update_time = parsed_date.replace(
                month=new_month, day=1, hour=8, minute=0, second=0
            )
            if parsed_date.month >= new_month:
                update_time = update_time.replace(year=update_time.year + 1)
            if update_time.weekday() >= 5:
                update_time = update_time + timedelta(days=7 - update_time.weekday())
        case description if description and description[0] == "Q":
            Last_Q_m = 3 * int(description[1])

            if Last_Q_m == 12:
                new_month = 1
                new_year = parsed_date.year + 1
            else:
                new_month = Last_Q_m + 1
                new_year = parsed_date.year

            update_time = parsed_date.replace(
                year=new_year, month=new_month, day=1, hour=8, minute=0, second=0
            ) - timedelta(days=1)

            if parsed_date.month > Last_Q_m:
                update_time = update_time.replace(year=update_time.year + 1)
            if update_time.weekday() >= 5:
                update_time = update_time - timedelta(days=update_time.weekday() - 4)

    return update_time.isoformat()
