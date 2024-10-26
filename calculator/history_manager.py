import pandas as pd

class HistoryManager:
    def __init__(self, filename='history.csv'):
        self.filename = filename
        try:
            self.history = pd.read_csv(filename)
        except FileNotFoundError:
            self.history = pd.DataFrame(columns=['operation', 'result'])

    def add_record(self, operation, result):
        new_record = {'operation': operation, 'result': result}
        self.history = self.history.append(new_record, ignore_index=True)
        self.history.to_csv(self.filename, index=False)

    def load_history(self):
        print(self.history)

    def clear_history(self):
        self.history = pd.DataFrame(columns=['operation', 'result'])
        self.history.to_csv(self.filename, index=False)
