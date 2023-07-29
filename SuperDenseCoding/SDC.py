import numpy as np

from qiskit import *
from qiskit.visualization import *
from qiskit.providers.ibmq import *

s = "01"
s = s[::-1]
n = 2

sdc_circuit = QuantumCircuit(n, n)


# set top qubit Hadarmard
sdc_circuit.h(0)
sdc_circuit.cx(0, 1)
 
# ---------- Oracle -------------  

sdc_circuit.barrier()

# 00 I
# 01 X
# 10 Z
# 11 Z-X

# sdc_circuit.z(0)
sdc_circuit.x(0)



sdc_circuit.barrier()

# ----------        -------------  

sdc_circuit.cx(0, 1)
sdc_circuit.h(0)

sdc_circuit.barrier()

for i in range(n):
    sdc_circuit.measure(i,i)

# end circuit

quasm_sim = Aer.get_backend('qasm_simulator')
shots = 1024
qobj = assemble(sdc_circuit, quasm_sim )
result = quasm_sim.run(qobj).result()
answer = result.get_counts()

print(answer)
plot_histogram(answer)



sdc_circuit.draw(output = 'mpl', filename = "SUPER_DENSE_CODING.png")

