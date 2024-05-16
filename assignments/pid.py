import matplotlib.pyplot as plt
class PID_cruise:
    def __init__(self, kp, ki, kd, dt, tend):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.dt = dt
        self.tend = tend
        self.prev_error = 0
        self.integral = 0

    def change(self, throttle):
        error = self.tend - throttle
        self.integral = self.integral + error*dt
        derivative = (error - self.prev_error)/dt
        pid_out = self.kp * error + self.kd * derivative + self.ki * self.integral
        self.prev_error = error
        return pid_out

kp = 0.6
ki = 0.4
kd = 0.002
dt = 0.2
tend = 50
pid_model = PID_cruise(kp, ki, kd, dt, tend)
throttle = 0
y = []
x = []
num = 0.0
for i in range(50):
    x.append(num)
    num = num+0.1
for i in range(50):
    pid_model.ki = 0.4
    output = pid_model.change(throttle)
    throttle = throttle + output
    y.append(throttle)
    print("throttle:", throttle)
plt.figure(figsize=(10,6))
plt.plot(x,y)
plt.xlabel('time')
plt.ylabel('throttle in m/s^2')
plt.grid(True)
plt.show()




