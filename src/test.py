from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

sim = AerSimulator()
compiled = transpile(qc, sim)

result = sim.run(compiled, shots=1000).result()
counts = result.get_counts()

print("Result:", counts)