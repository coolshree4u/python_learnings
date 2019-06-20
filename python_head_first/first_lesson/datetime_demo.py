import datetime
import time
import html

print(datetime.datetime.today())

print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)

print(datetime.date.isoformat(datetime.date.today()))


print(time.strftime("%H:%M"))
print(time.strftime("%A %p"))



print(html.escape('This html fragment contains a <script>script</script>'))
print(html.unescape('This html fragment contains a &lt;script&gt;script&lt;/script&gt;'))

time_now = datetime.datetime.today()
right_this_minute = time_now.minute
print(time_now)
print(right_this_minute)