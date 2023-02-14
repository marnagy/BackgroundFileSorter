import sys
import time
import logging
import os
import threading
import time
from watchdog.observers import Observer
from watchdog.events import FileCreatedEvent

from main import sort_file

class CustomHandler(FileCreatedEvent):    
    def dispatch(self, event):
        #print(event)
        if event.event_type == 'created' and not event.is_directory:
            file_path: str = event.src_path
            file_name = file_path.split(os.pathsep)[-1]
            def move_after():
                print('Before sleep')
                time.sleep(60)
                print('After sleep')
                sort_file(file_name)
                print(f'File {file_name} moved.')
            threading.Thread(target=move_after).start()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    os.chdir(path)
    event_handler = CustomHandler()
    observer = Observer()
    observer.schedule(event_handler, path)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()