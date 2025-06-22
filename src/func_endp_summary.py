def calc_mean_press(week_hourly_measures: list) -> float:
    return sum(week_hourly_measures)/len(week_hourly_measures)

def calc_mean_exposition(week_daily_measures: list) -> float:
    return (sum(week_daily_measures)/3600)/len(week_daily_measures)

def summary_weather(week_codes: list) -> str:
    rain_codes=[51, 53, 55, 56, 57,61, 63, 65,66, 67, 80, 81, 82]
    snow_codes=[71, 73, 75, 77, 85, 86]
    thunderstorm_codes=[95, 96, 99]
    clear_codes=[0, 1, 2, 3, 45, 48]

    result={"rain":0,
            "snow":0,
            "thunderstorm":0,
            "clear":0}
    
    for code in week_codes:
        if code in rain_codes:
            result["rain"] += 1
        elif code in snow_codes:
            result["snow"] += 1
        elif code in thunderstorm_codes:
            result["thunderstorm"] += 1
        elif code in clear_codes:
            result["clear"] += 1

    max_category=max(result, key=result.get)

    return max_category