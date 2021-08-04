from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler, FileSystemEventHandler
from PySide2 import QtCore as qtc, QtWidgets as qtw
import os

CSV_FILE_DIR = "."

patterns = ["*.csv"]
ignore_patterns = None
ignore_directories = False
case_sensitive = True
go_recursively = True

class CSVWatcher(qtw.QWidget):
    signalFileChanged = qtc.Signal()
    def __ini__(self):
        print("initialized watcher")
        self.csvChangedEventHandler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
        self.csvChangedEventHandler.on_modified = self.on_modified
        self.observer = Observer()
        self.observer.schedule(self.csvChangedEventHandler, path=os.getcwd(), recursive=go_recursively)
        self.observer.start()

    def on_modified(self, event):
        ## signal changed to display handler
        self.signalFileChanged.emit()
        print("file changed")


class CSVModifiedHandler(FileSystemEventHandler, qtc.QThread):
    signalFileChanged = qtc.Signal()

    def __init__(self, filename, path):
        super(CSVModifiedHandler, self).__init__()
        self.filename = filename
        self.observer = Observer()
        self.observer.schedule(self, path, recursive=False)
        self.observer.start()

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(self.filename):
            self.signalFileChanged.emit()