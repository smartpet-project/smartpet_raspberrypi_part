from . import *

def start_query_time():
    nowtime = strptime(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    plans = plan.get_all_plans()
    time_hour = nowtime.tm_hour
    time_min = nowtime.tm_min
    for plan_ in plans:
        plan_tm_hour = plan_["time"].split(":")[0]
        plan_tm_min = plan_["time"].split(":")[1]
        if time_hour == plan_tm_hour and time_min == (plan_tm_min - 5):
            transfer.send_detect_signal()
        elif time_hour == plan_tm_hour and time_min == plan_tm_min:
            if transfer.get_detect_result() == True:
                transfer.feed()