from client import NelsonSiegelYieldCurve

def run_example():
    print("=== GenPark Nelson-Siegel Yield Curve Example ===")
    ns = NelsonSiegelYieldCurve()
    print("Curve:", ns.benchmark_yield_curve())

if __name__ == "__main__":
    run_example()
