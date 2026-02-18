from qiskit import QuantumCircuit, Aer, transpile
from qiskit.visualization import plot_histogram

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


try:
    plot_histogram(counts).show()
except:
    pass
