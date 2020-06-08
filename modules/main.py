from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class Handler(FileSystemEventHandler):
	def on_modified(self, event):
		for filename in os.listdir(tracked_folder):
			src = tracked_folder + "\\" + filename
			destination = destination_folder + "\\" + filename
			os.rename(src, destination)

tracked_folder = "C:\\Users\\alex9\\Downloads"
destination_folder = "C:\\Users\\alex9\\Desktop"

event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, tracked_folder, recursive=True)
observer.start()

try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	observer.stop()

observer.join()