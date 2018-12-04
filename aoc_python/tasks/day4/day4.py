from datetime import datetime, timedelta
import re, os

def get_log_guard(guard_id, data):
    data = map(lambda x: (datetime.strptime(re.search('\[(.*?)\]', x).group(), 
                        "[%Y-%m-%d %H:%M]"), x), 
                        data)
    data_sorted = sorted(data, key=lambda x:x[0])

    return [d for d in data_sorted if 'Guard #{}'.format(guard_id) in d[1]]

def compute_asleep_minutes(data):
    records = {}
    data = map(lambda x: (datetime.strptime(re.search('\[(.*?)\]', x).group(), 
                        "[%Y-%m-%d %H:%M]"), x), 
                        data)
    data_sorted = sorted(data, key=lambda x:x[0])
    fall_asleep = 0
    guard_id = None
    for d in data_sorted:
        dt = d[0]
        desc = d[1]
        if "begins shift" in desc:
            guard_id = re.search('Guard #\d*', desc).group()
        else:                  
            if 'falls asleep' in desc:
                fall_asleep = dt
            if 'wakes up' in desc:
                date = '{}-{}-{}'.format(dt.year, dt.month, dt.day)
                init_asleep_minute = [0 for _ in range(60)]
                for i in range((dt - fall_asleep).seconds / 60):
                    init_asleep_minute[fall_asleep.minute + i] = 1
                if not guard_id in records:
                    records[guard_id] = {date: init_asleep_minute}
                else:
                    if date in records[guard_id]:
                        record = records[guard_id][date]
                        for i in range((dt - fall_asleep).seconds / 60):
                            record[fall_asleep.minute + i] = 1
                        records[guard_id][date] = record
                    else:
                        records[guard_id][date] = init_asleep_minute
    return records

def get_minutes(guard_id, records):
    asleep_minutes = [m[1] for m in records[guard_id].items()]
    total_asleep = [sum(x) for x in zip(*asleep_minutes)]
    return total_asleep.index(max(total_asleep)), max(total_asleep), guard_id

def get_longuest_minute(records):
    max_minutes = 0
    minutes = 0
    guardid = None
    for guard_id in records.keys():
        asleep_minutes = [m[1] for m in records[guard_id].items()]
        total_asleep = [sum(x) for x in zip(*asleep_minutes)]
        if max(total_asleep) >  max_minutes:
            minutes = total_asleep.index(max(total_asleep))
            guardid = guard_id
    return int(filter(str.isdigit, guardid.replace('#',''))) * minutes


if __name__ == "__main__":
    inputs = []
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt'), 'rb') as f:
        for l in f.readlines():
            inputs.append(l.replace('\n', ''))

    records = compute_asleep_minutes(inputs)
    
    print get_longuest_minute(records)
