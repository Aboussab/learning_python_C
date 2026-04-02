
print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
filename = "ancient_fragment.txt"
print()
print(f"Accessing Storage Vault: {filename}\nConnection established...")

file = open("ancient_fragment.txt", "r")
try:
    file = open(filename)
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
    exit(0)

content = file.read()
print(content)
print()
print("Data recovery complete. Storage unit disconnected")
