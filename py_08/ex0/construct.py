import sys
import os


if sys.base_prefix == sys.prefix:
    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {sys.prefix}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix env\\Scripts\\activate # On Windows")
    print("Then run this program again.")
else:
    print("MATRIX STATUS: Welcome to the construct")
    print(f"Virtual Environment: {sys.prefix}")
    print()
    print(os.path.basename(sys.prefix))
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    