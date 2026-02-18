from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import matplotlib.pyplot as plt

# 1 qubit in superposition
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

# Use simulator
sim = Aer.get_backend('qasm_simulator')
compiled = transpile(qc, sim)
job = sim.run(compiled, shots=1024)
result = job.result()

counts = result.get_counts()
print("Counts:", counts)



plot_histogram(counts)
plt.show()
