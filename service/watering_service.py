'''
    watering_service
'''


class watering_service():

    def __init__(self):
        pass

    def water_plants(self):
        if self.watering_required():
            if self.watering_allowed():
                self.activate_watering()
            else:
                self.water_when_next_allowed()
        else:
            self.schedule_next_soil_moisture_test()

    def watering_required(self) -> bool:
        return True

    def watering_allowed(self) -> bool:
        return True

    def activate_watering(self):
        pass

    def water_when_next_allowed(self):
        pass

    def schedule_next_soil_moisture_test(self):
        pass
