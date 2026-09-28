import math
from typing import List, Dict

class NelsonSiegelYieldCurve:
    @staticmethod
    def zero_rate(t: float, beta0: float, beta1: float, beta2: float, lambda_param: float) -> float:
        if t <= 0:
            return beta0 + beta1
        f1 = (1.0 - math.exp(-t / lambda_param)) / (t / lambda_param)
        f2 = f1 - math.exp(-t / lambda_param)
        return beta0 + beta1 * f1 + beta2 * f2

    @classmethod
    def generate_curve(cls, maturities: List[float], b0: float = 0.05, b1: float = -0.02, b2: float = 0.03, lam: float = 2.0) -> List[Dict[str, float]]:
        curve = []
        for t in maturities:
            rate = cls.zero_rate(t, b0, b1, b2, lam)
            curve.append({"maturity_years": t, "spot_yield_pct": round(rate * 100, 3)})
        return curve

    def benchmark_yield_curve(self) -> Dict[str, Any]:
        maturities = [0.5, 1.0, 2.0, 5.0, 10.0, 30.0]
        pts = self.generate_curve(maturities)
        return {"curve_points": pts, "parameters": {"beta0": 0.05, "beta1": -0.02, "beta2": 0.03, "lambda": 2.0}}
