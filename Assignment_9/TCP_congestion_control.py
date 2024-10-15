import matplotlib.pyplot as plt


class TCPCongestionControl:
    def __init__(self, algo, initial_cwnd=1, ssthresh=64):
        self.algo = algo
        self.cwnd = initial_cwnd  # Initial congestion window
        self.ssthresh = ssthresh  # Slow start threshold
        self.time_history = []  # Store time values
        self.cwnd_history = []  # Store cwnd values
        self.time = 0  # Current time

    def simulate(self, rounds):
        for i in range(rounds):
            self.time += 1
            self.time_history.append(self.time)
            self.cwnd_history.append(self.cwnd)

            if self.algo == 'Slow Start':
                self.cwnd *= 2  # Double cwnd in slow start
                if self.cwnd >= self.ssthresh:  # Transition to congestion avoidance
                    self.cwnd = self.ssthresh

            elif self.algo == 'TCP Reno':
                if self.cwnd < self.ssthresh:  # Slow Start phase
                    self.cwnd *= 2
                else:  # Congestion Avoidance phase
                    self.cwnd += 1

            elif self.algo == 'TCP Tahoe':
                if self.cwnd < self.ssthresh:  # Slow Start phase
                    self.cwnd *= 2
                else:  # Congestion Avoidance phase
                    self.cwnd += 1
                    # Simulating packet loss scenario to reset cwnd
                    if i == rounds // 2:  # Simulating packet loss at midpoint
                        self.ssthresh = self.cwnd // 2
                        self.cwnd = 1  # Resetting cwnd for Tahoe

            # Optional: Add a condition to simulate packet loss and adjustments
            # Here you can introduce random packet loss if needed

    def plot_cwnd(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.time_history, self.cwnd_history, marker='o', label=f'TCP {self.algo}')
        plt.title(f'TCP {self.algo} Congestion Window Over Time')
        plt.xlabel('Time')
        plt.ylabel('Congestion Window (cwnd)')
        plt.grid(True)
        plt.legend()
        plt.savefig('tcp_cwnd_simulation.png')  # Save the plot to a file
        plt.close()  # Close the plot to avoid display issues


if __name__ == "__main__":
    print("TCP Congestion Control Simulation")

    # User input for the algorithm and rounds
    algo = input("Select TCP Algorithm (Slow Start, TCP Reno, TCP Tahoe): ")
    rounds = int(input("Enter number of rounds for simulation: "))

    # Create an instance of the TCP congestion control
    tcp = TCPCongestionControl(algo)

    # Run the simulation
    tcp.simulate(rounds)

    # Plot the congestion window over time
    tcp.plot_cwnd()

    print(f"Simulation complete. The congestion window plot is saved as 'tcp_cwnd_simulation.png'.")
