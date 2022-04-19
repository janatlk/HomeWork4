class Car:
    def __init__(self, title, model):
        self.t = title
        self.m = model

    def start_engine(self):
        print(f'{self.t} {self.m} engine is started!')

    def stop_engine(self):
        print(f'{self.t}  {self.m} engine is started')
