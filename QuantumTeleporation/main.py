import qiskit as q

def main():
    simulator = q.Aer.get_backend('qasm_simulator')
    circuit = q.QuantumCircuit(3, 3)
    

if __name__ == "__main__":
    main()
