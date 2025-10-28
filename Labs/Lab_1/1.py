start = input("Enter the start time (HH:MM): ")
end = input("Enter the end time (HH:MM): ")

start_h, start_m = map(int, start.split(":"))
end_h, end_m = map(int, end.split(":"))
# с помощью map я проинтовываю часы и минуты, но предварительно разделяю их с помощью сплит

start_total = start_h * 60 + start_m
end_total = end_h * 60 + end_m

if end_total < start_total:
    end_total += 24 * 60
duration = end_total - start_total
hours = duration // 60
minutes = duration % 60
print(f"For how long your event has been continued: {hours} ч {minutes} мин")