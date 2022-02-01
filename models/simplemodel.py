from model import Model
from utils import mse


class SimpleModel(Model):
    def __init__(self, look_back):
        self.look_back = look_back

    # returns the average of the last days
    def predict_next(self, history):
        return sum(history[-self.look_back:]) / self.look_back


if __name__ == '__main__':
    SM = SimpleModel(10)
    evaluation = mse(SM, 50, 10)
    print(evaluation)
