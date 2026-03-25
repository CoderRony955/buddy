from PyQt6.QtCore import QThread, pyqtSignal
from ...db import action


class Start(QThread):
    data_feed_op = pyqtSignal(object)

    def __init__(self, data, url: str, db_name: str, collection_name: str):
        super().__init__()
        self.data = data
        self.url = url
        self.db_name = db_name
        self.collection_name = collection_name
        self.database = action.DB(self.url)

    def run(self):
        result = self.feed()
        self.data_feed_op.emit(result)

    def feed(self):
        try:
            # check cluster status
            cluster = self.database.ping()
            if isinstance(cluster, tuple):
                return cluster

            # feed data into specefic database's collection
            insert_data = self.database.insert_data(
                self.data, self.db_name, self.collection_name)
            if isinstance(insert_data, tuple):
                return insert_data

            return insert_data
        except Exception as e:
            return (e, False)
