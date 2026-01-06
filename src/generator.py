class Chat:
    def __init__(self, name: str, collection: str):
        self.name = name
        self.collection = collection
        self.messages = []
        self.metadata = None

class Assessment:
    def __init__(self, name: str, collection: str):
        self.name = name
        self.collection = collection
        self.questions = []
        self.metadata = None