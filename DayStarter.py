import webbrowser
import os
import time

web_starter = [
    "https://www.finn.no/job/fulltime/search.html?industry=65&industry=8&location=1.20001.20061&occupation=0.23&published=1",
    "https://www.linkedin.com/feed/", "https://www.15min.lt/"]
editor = r"C:\Program Files\Sublime Text 3\sublime_text.exe"


def starter():
    """opens url from web_starter list"""
    for web in web_starter:
        webbrowser.open(web)


starter()

time.sleep(1800)  # after 30min open text editor

os.startfile(editor)
