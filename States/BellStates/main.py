import qiskit as q

def main():
    simulator = q.Aer.get_backend('qasm_simulator')
    circuit = q.QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure([0, 1], [0, 1])
    job = q.execute(circuit, simulator, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    print("\nTotal count for 00 and 11 are:", counts)
    print(circuit.draw(output='text'))

if __name__ == "__main__":
    main()
