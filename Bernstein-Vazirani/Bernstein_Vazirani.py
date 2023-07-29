import numpy as np

from qiskit import IBMQ, Aer
from qiskit import QuantumCircuit, assemble, transpile

from qiskit.providers.ibmq import least_busy

from qiskit.visualization import plot_histogram

#secret
s = "1101"

n = 4


# ----------- Oracle ----------
oracle = QuantumCircuit(n + 1)

oracle.barrier()

s = s[::-1]
for qubit in range(n):
        if(s[qubit] == '1'):
            oracle.cx(qubit, n)
        else:
            oracle.i(qubit)

oracle.barrier()

# ----------- BV Circut ----------
bv_circuit = QuantumCircuit(n + 1, n)

#flip the last bit 
bv_circuit.x(n)

# place Hadermarks
for qubit in range(n + 1):
        bv_circuit.h(qubit)

# bv_circuit.z(n)

# add oracle to circuit
bv_circuit.compose(oracle, inplace = True) 


for qubit in range(n):
        bv_circuit.h(qubit)

for i in range(n):
   bv_circuit.measure(i, i)

bv_circuit.draw(output='mpl', filename = "BV_Plot.png")

quasm_sim = Aer.get_backend('qasm_simulator')
shots = 1024
qobj = assemble(bv_circuit, quasm_sim )
result = quasm_sim.run(qobj).result()
answer = result.get_counts()

print(answer)
plot_histogram(answer)