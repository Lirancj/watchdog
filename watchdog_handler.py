import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            print(f"Directory event: {event.event_type}  Path: {event.src_path}")
        else:
            print(f"File event: {event.event_type}  Path: {event.src_path}")

def init_watchdog(directory_path):
    event_handler = Watcher()
    observer = Observer()
    observer.schedule(event_handler, directory_path, recursive=True)
    return observer

def main():
    directory_path = sys.argv[1]

    observer = init_watchdog(directory_path)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python watchdog_script.py <directory_path>")
        exit(1)
    
    main()
