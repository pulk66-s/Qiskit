import qiskit as q
from math import *

def main():
    simulator = q.Aer.get_backend('qasm_simulator')
    circuit = q.QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.h(1)
    circuit.measure(0, 0)
    circuit.measure(1, 1)
    print(circuit.draw(output='text'))
    job = q.execute(circuit, simulator, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    print(counts)

if __name__ == '__main__':
    main()
