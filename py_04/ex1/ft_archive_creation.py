import sys

print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
file = None
try:

    file = open("new_discovery.txt", "w")
    print(f"Initializing new storage unit: {file.name}")
    print("Storage unit created successfully...\n")

    print("Inscribing preservation data...")
    file.write(
        "[FRAGMENT 001] Digital preservation protocols established 2087\n")
    print("[FRAGMENT 001] Digital preservation protocols established 2087")

    file.write("[FRAGMENT 002] Knowledge must survive the entropy wars\n")
    print("[FRAGMENT 002] Knowledge must survive the entropy wars")

    file.write(
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n")
    print("[FRAGMENT 003] Every byte saved is a victory against oblivion")

    print("\nData inscription complete. Storage unit sealed")
    print(f"Archive {file.name} ready for long-term preservation.")
except Exception:
    print("errore, just happned.")
    sys.exit(1)
finally:
    if file is not None:
        file.close()
