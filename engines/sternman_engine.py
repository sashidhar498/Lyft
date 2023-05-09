from abc import ABC

class SternmanEngine(ABC):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        return True if self.warning_light_is_on else False