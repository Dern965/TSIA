from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Circuito 1
qc1 = QuantumCircuit(3)
qc1.h(0)
qc1.h(1)
qc1.cx(0, 2)
qc1.z(1)
qc1.x(2)
qc1.rx(3.14159/4, 0)
qc1.measure_all()

# Circuito 2
qc2 = QuantumCircuit(4)
qc2.h(0)
qc2.h(1)
qc2.h(2)
qc2.cx(0, 3)
qc2.z(1)
qc2.rx(3.14159/3, 2)
qc2.x(3)
qc2.measure_all()

# Simulación
simulator = Aer.get_backend('qasm_simulator')
result1 = execute(qc1, simulator, shots=1024).result()
result2 = execute(qc2, simulator, shots=1024).result()

# Resultados
counts1 = result1.get_counts()
counts2 = result2.get_counts()

# Visualización
plot_histogram(counts1, title="Resultados del Circuito 1").show()
plot_histogram(counts2, title="Resultados del Circuito 2").show()
