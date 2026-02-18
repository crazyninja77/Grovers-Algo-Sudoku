from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer
import matplotlib.pyplot as plt

# 1 qubit in superposition
# Create a Quantum Circuit with 1 quantum bit and 1 classical bit
qc = QuantumCircuit(1, 1)
# Apply Hadamard gate to qubit 0. This puts the qubit into a superposition state (|0> + |1>) / sqrt(2)
qc.h(0)
# Measure qubit 0 and store the result in classical bit 0. This collapses the superposition.
qc.measure(0, 0)

# Use simulator
# Get the Aer simulator backend
sim = Aer.get_backend('qasm_simulator')
# Transpile the circuit for the simulator
compiled = transpile(qc, sim)
# Run the compiled circuit on the simulator 1024 times (shots)
job = sim.run(compiled, shots=1024)
# Get the result from the job
result = job.result()

# Get the counts of the results (e.g., how many times '0' and '1' were measured)
counts = result.get_counts()
print("Counts:", counts)


# Plot the histogram of the counts
plot_histogram(counts)
plt.show()
