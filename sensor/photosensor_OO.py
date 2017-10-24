from sensor.fake_analog_input_rbpi import FakeAnalogInput


class LightSensor(FakeAnalogInput):
    lightLevel = 0


photosensor = LightSensor(4)



