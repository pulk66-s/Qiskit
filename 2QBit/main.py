import qiskit as q

def main():
    simulator = q.Aer.get_backend('qasm_simulator')
    circuit = q.QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.x(1)
    circuit.cx(0, 1)
    circuit.h(1)
    circuit.measure([0, 1], [0, 1])
    print(circuit.draw(output='text'))
    job = q.execute(circuit, simulator, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    print(counts)

if __name__ == "__main__":
    main()
