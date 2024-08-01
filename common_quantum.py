import numpy as np
from qiskit import *

# //＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
def create_QuantumCircuit_by_Statevector(sv):
    length = len(sv)-1
    n_qubits = length.bit_length()
    qc = QuantumCircuit(n_qubits,n_qubits)
    qc.initialize(sv,range(n_qubits))
    qc.measure(range(n_qubits),range(n_qubits))
    return qc

def convert_probability2statevector(probabilities,address):
    width = len(probabilities[0])
    height = len(probabilities)
    n_qubits = width.bit_length() + height.bit_length()
    statevector = np.zeros(2**n_qubits)
    for y in range(height):
        for x in range(width):
            index = int(address[y][x],2)
            statevector[index] = probabilities[y][x]
    return statevector