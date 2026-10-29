"""
Quantitative Volume Profile Engine
Author: Mehrdad Poorhassan (ORCID: 0009-0004-9269-3912)
"""

import numpy as np
import pandas as pd

class QuantitativeVolumeProfileEngine:
    def __init__(self, data: pd.DataFrame):
        self.data = data.copy()

    def calculate_volume_profile(self, bins: int = 50, value_area_pct: float = 0.70):
        price_min = self.data['low'].min()
        price_max = self.data['high'].max()
        price_bins = np.linspace(price_min, price_max, bins + 1)
        hist, bin_edges = np.histogram(self.data['close'], bins=price_bins, weights=self.data['volume'])
        poc_idx = np.argmax(hist)
        poc = (bin_edges[poc_idx] + bin_edges[poc_idx + 1]) / 2.0
        total_volume = np.sum(hist)
        target_volume = total_volume * value_area_pct
        sorted_indices = np.argsort(hist)[::-1]
        cumulative_volume = 0
        va_bins = []
        for idx in sorted_indices:
            cumulative_volume += hist[idx]
            va_bins.append(idx)
            if cumulative_volume >= target_volume:
                break
        va_edges = [bin_edges[i] for i in va_bins] + [bin_edges[i+1] for i in va_bins]
        return {'POC': poc, 'VAH': np.max(va_edges), 'VAL': np.min(va_edges)}

    def calculate_indicators(self):
        df = self.data
        tr = pd.concat([df['high'] - df['low'], np.abs(df['high'] - df['close'].shift()), np.abs(df['low'] - df['close'].shift())], axis=1).max(axis=1)
        df['ATR'] = tr.rolling(14).mean()
        delta = df['close'].diff()
        gain, loss = (delta.where(delta > 0, 0)).rolling(14).mean(), (-delta.where(delta < 0, 0)).rolling(14).mean()
        df['RSI'] = 100 - (100 / (1 + gain / loss))
        df['MACD'] = df['close'].ewm(span=12).mean() - df['close'].ewm(span=26).mean()
        return df
