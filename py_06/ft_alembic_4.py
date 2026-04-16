import alchemy  # type: ignore

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
try:
    print(alchemy.create_earth())  # type: ignore
except AttributeError as e:
    print(e)
