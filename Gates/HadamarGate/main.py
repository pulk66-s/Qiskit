import qiskit as q
from qiskit_ibm_runtime import QiskitRuntimeService, Estimator, Options
from math import *

# service = QiskitRuntimeService(channel="ibm_quantum", token="a3b55c3a8a4a772be3c027be1026903b8eb9a401b3ae0a1dc5a0e4f58f961178b5bb1d644347081d68d7f77197d6d322d886691dc126310c1003f4771494195a")

# def state_0():
#     basic_circuit([1, 0])

# def state_1():
#     basic_circuit([0, 1])

# def state_sqrt2():
#     basic_circuit([1/sqrt(2), 1/sqrt(2)])

def reverse_cz():
    circuit = q.QuantumCircuit(2, 2)
    circuit.initialize([1, 0], 0)
    circuit.initialize([1, 0], 1)

    circuit.h(0)
    circuit.h(1)
    circuit.cnot(0, 1)
    # circuit.h(0)
    # circuit.h(1)
    circuit.measure([0, 1], [0, 1])

    # Execute the circuit
    backend = q.Aer.get_backend('qasm_simulator')
    job = q.execute(circuit, backend, shots=1000)
    result = job.result()

    # print the circuit
    print(circuit.draw())
    # Return the result
    counts = result.get_counts(circuit)
    print("\nTotal count for 00 and 11 are:", counts)
    return counts

def main():
    reverse_cz()

if __name__ == '__main__':
    main()
