class PID:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.prev_error = 0
        self.integral = 0

    def update(self, current_value):
        error = self.setpoint - current_value
        self.integral += error
        derivative = error - self.prev_error
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.prev_error = error
        return output

# Example usage
if __name__ == "__main__":
    pid = PID(1, 0.1, 0.01, 0)  # Example PID parameters and setpoint
    current_value = 0 # change later
    for _ in range(100):
        control_signal = pid.update(current_value)
        current_value += control_signal  # Simulating the system response
        print("Control signal:", control_signal, "Current value:", current_value)
