import os
import re

cmd = 'adb shell pm dump com.xueqiu.android | findstr "versionName"'
st = os.popen(cmd)
print(st.read())