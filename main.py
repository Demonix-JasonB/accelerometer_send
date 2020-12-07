radio.set_group(1)
def on_forever():
    a_X = input.acceleration(Dimension.X)
    a_Y = input.acceleration(Dimension.Y)
    a_Z = input.acceleration(Dimension.Z)
    radio.send_value("Accel.x", a_X)
    radio.send_value("Accel.y", a_Y)
    radio.send_value("Accel.z", a_Z)
    led.toggle(0, 0)
basic.forever(on_forever)

