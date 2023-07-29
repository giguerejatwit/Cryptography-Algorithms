import numpy as np

from qiskit import *
from qiskit.visualization import *

# number of qubits
n = 4
# iterations
r = round((np.pi / 4) * np.sqrt(n))

# --------- Initialization ---------
grovers = QuantumCircuit(n + 1, n)

for i in range(n):
    grovers.h(i)

grovers.barrier()

# -------- Finalization ---------

  # Phase Inversion
p_inversion = QuantumCircuit(n + 1)
p_inversion.name = "PhaseInversion"
p_inversion.to_gate()

for i in range(n):
    if i == 1 or i == 2:
        p_inversion.x(i)

# p_inversion.barrier()

p_inversion.h(3)

# p_inversion.barrier()

p_inversion.ccx(0, 1, 4)

p_inversion.ccx(2, 4, 3)

p_inversion.ccx(0, 1, 4)

p_inversion.barrier()

p_inversion.h(3)

# p_inversion.barrier()
    
for i in range(n):
    if i == 1 or i == 2:
        p_inversion.x(i)

# p_inversion.barrier()

# p_inversion.to_gate()


# ------- inversion about the mean -------
m_inversion = QuantumCircuit(n + 1)
m_inversion.name = "MeanInversion"
m_inversion.to_gate()

for i in range(n):
    m_inversion.h(i)
    m_inversion.x(i)

# m_inversion.barrier()

m_inversion.h(3)

m_inversion.ccx(0, 1, 4)

m_inversion.ccx(2, 4, 3)

m_inversion.ccx(0, 1, 4)

m_inversion.h(3)

# m_inversion.barrier()

for i in range(n):
    m_inversion.x(i)
    m_inversion.h(i)

# m_inversion.barrier()

m_inversion.to_gate()

# add oracles
for i in range(r):
    grovers.compose(p_inversion, range(n))
    grovers.compose(m_inversion, range(n))

# --------- run simulation ---------
for i in range(n):
    grovers.measure(i, i)

quasm_sim = Aer.get_backend('qasm_simulator')
shots = 1024
qobj = assemble(grovers, quasm_sim)
result = quasm_sim.run(qobj).result()
answer = result.get_counts()
print(answer)
plot_histogram(answer)

m_inversion.draw(output='mpl', filename="MEAN_INVERSION.png")
grovers.draw(output='mpl', filename="Grovers.png")
