import qiskit as q
from math import *

def state_0():
    basic_circuit([1, 0])

def state_1():
    basic_circuit([0, 1])

def state_sqrt2():
    basic_circuit([1/sqrt(2), 1/sqrt(2)])

def basic_circuit(qbit):
    simulator = q.Aer.get_backend('ibmq_5_yorktown')
    circuit = q.QuantumCircuit(1, 1)
    circuit.initialize(qbit, 0)
    circuit.h(0)
    circuit.measure(0, 0)
    print(circuit.draw(output='text'))
    job = q.execute(circuit, simulator, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    print(counts)

def main():
    state_0()
    state_1()
    state_sqrt2()

if __name__ == '__main__':
    main()
