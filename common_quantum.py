import numpy as np
from qiskit import *

# //＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
def create_QuantumCircuit_by_Statevector(sv):
    n_qubits = len(sv).bit_length()
    qc = QuantumCircuit(n_qubits,n_qubits)
    qc.initialize(sv,range(n_qubits))
    qc.measure(range(n_qubits),range(n_qubits))
    return qc