def check_libs() -> bool:
    from importlib.metadata import version, PackageNotFoundError

    print("Checking dependencies:")
    ok: bool = True

    for lib, desc in [
        ("pandas", "Data manipulation ready"),
        ("numpy", "Numerical computation ready"),
        ("matplotlib", "Visualization ready"),
        ("requests", "requests ready"),
    ]:
        try:
            print(f"[OK] {lib} ({version(lib)}) - {desc}")
        except PackageNotFoundError:
            print(f"[KO] {lib} - not found")
            ok = False

    return ok


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    import requests  # type: ignore
    import pandas as pd  # type: ignore
    import numpy as np  # type: ignore
    import matplotlib.pyplot as plt  # type: ignore
    print()
    if check_libs():
        print("Analyzing Matrix data...")
        try:
            url = "https://jsonplaceholder.typicode.com/users"
            response = requests.get(url)
            data = response.json()
            mani_data = pd.DataFrame(data)
            print("Processing 10 data points...")
            scores = np.random.randint(0, 100, len(mani_data))
            print("Generating visualization...")
            plt.bar(mani_data["name"], scores, color="tomato")
            plt.title("User Scores")
            plt.xlabel("Users")
            plt.ylabel("Score")
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            plt.savefig("ex1/matrix_analysis.png")
            print("Analysis complete! \nResults saved to: matrix_analysis.png")
        except Exception as e:
            print(e)


try:
    main()
except ModuleNotFoundError as e:
    missing_module = e.name if hasattr(e, "name") else str(e)

    print("LOADING STATUS: Missing dependencies detected!\n")

    print(f"[ERROR] Missing module: {missing_module}\n")

    print("Install dependencies using pip:")
    print("pip installs packages but does NOT manage "
          "dependency conflicts or environments.")
    print("   pip install -r requirements.txt\n")

    print("Install dependencies using Poetry:")
    print("Poetry manages dependencies, versions, and virtual environments.")
    print("   poetry install\n")
