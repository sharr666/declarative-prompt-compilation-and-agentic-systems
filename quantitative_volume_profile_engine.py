"""
Author: Mehrdad Poorhassan (Dr. Metal) — ORCID: 0009-0004-9269-3912
Rigorous Vectorized Volume Profile (Range-Distributed & Contiguous POC Expansion) & Wilder's RMA Engine
"""
from typing import Dict
import numpy as np
import pandas as pd

class QuantitativeVolumeProfileEngine:
    def __init__(self, num_bins: int = 50, value_area_pct: float = 0.70) -> None:
        self.num_bins = num_bins
        self.value_area_pct = value_area_pct

    def compute_volume_profile(self, df: pd.DataFrame) -> Dict[str, float]:
        low_min, high_max = float(df["low"].min()), float(df["high"].max())
        if high_max <= low_min:
            return {"POC": low_min, "VAH": high_max, "VAL": low_min, "va_volume_share": 1.0}
        bin_edges = np.linspace(low_min, high_max, self.num_bins + 1)
        bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
        bin_volumes = np.zeros(self.num_bins, dtype=np.float64)
        for l_val, h_val, v_val in zip(df["low"].to_numpy(float), df["high"].to_numpy(float), df["volume"].to_numpy(float)):
            mask = (bin_edges[1:] >= l_val) & (bin_edges[:-1] <= h_val)
            cnt = int(np.sum(mask))
            if cnt > 0:
                bin_volumes[mask] += v_val / cnt
        poc_idx = int(np.argmax(bin_volumes))
        total_vol = float(np.sum(bin_volumes))
        target_vol = total_vol * self.value_area_pct
        cum_vol = float(bin_volumes[poc_idx])
        left_idx = right_idx = poc_idx
        while cum_vol < target_vol and (left_idx > 0 or right_idx < self.num_bins - 1):
            lv = float(bin_volumes[left_idx - 1]) if left_idx > 0 else -1.0
            rv = float(bin_volumes[right_idx + 1]) if right_idx < self.num_bins - 1 else -1.0
            if rv >= lv:
                right_idx += 1
                cum_vol += rv
            else:
                left_idx -= 1
                cum_vol += lv
        return {
            "POC": round(float(bin_centers[poc_idx]), 4),
            "VAH": round(float(bin_edges[right_idx + 1]), 4),
            "VAL": round(float(bin_edges[left_idx]), 4),
            "va_volume_share": round(cum_vol / total_vol, 4) if total_vol > 0 else 0.0,
        }

    @staticmethod
    def compute_indicators(df: pd.DataFrame, atr_period: int = 14, rsi_period: int = 14) -> pd.DataFrame:
        out = df.copy()
        high, low, close = out["high"].astype(float), out["low"].astype(float), out["close"].astype(float)
        prev_close = close.shift(1)
        tr = pd.concat([(high - low), (high - prev_close).abs(), (low - prev_close).abs()], axis=1).max(axis=1)
        out["ATR"] = tr.ewm(alpha=1.0 / atr_period, adjust=False).mean()
        delta = close.diff().fillna(0.0)
        avg_gain = delta.clip(lower=0.0).ewm(alpha=1.0 / rsi_period, adjust=False).mean()
        avg_loss = (-delta).clip(lower=0.0).ewm(alpha=1.0 / rsi_period, adjust=False).mean()
        rs = np.where(avg_loss > 1e-12, avg_gain / np.maximum(avg_loss, 1e-12), np.inf)
        out["RSI"] = np.where((avg_gain <= 1e-12) & (avg_loss <= 1e-12), 50.0, np.where(avg_loss <= 1e-12, 100.0, 100.0 - (100.0 / (1.0 + rs))))
        out["MACD_Line"] = close.ewm(span=12, adjust=False).mean() - close.ewm(span=26, adjust=False).mean()
        out["MACD_Signal"] = out["MACD_Line"].ewm(span=9, adjust=False).mean()
        out["MACD_Hist"] = out["MACD_Line"] - out["MACD_Signal"]
        return out
