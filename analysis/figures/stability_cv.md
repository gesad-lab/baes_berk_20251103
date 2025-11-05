# Visualization Documentation: stability_cv.svg

**Visualization Type**: Stability  
**Metric**: multi_metric_stability  
**Frameworks**: baes, chatdev, ghspec  
**Generated**: 2025-11-03T08:51:30.768598Z

---

## Rationale

This Stability visualization was generated to compare Multi Metric Stability performance across baes, chatdev, ghspec. The coefficient of variation plot measures consistency across runs to assess reliability.

**Interpretation Guidance**: Coefficient of Variation (CV = σ/μ) assesses measurement reproducibility. Decision thresholds: CV<0.3 (stable, acceptable reproducibility), CV 0.3-0.5 (moderately unstable, investigate sources), CV>0.5 (highly unstable, unreliable). Test selection: High CV indicates non-deterministic behavior—increase n_runs or use bootstrap methods that don't assume normality. Domain context: For LLM-based systems, CV<0.3 is achievable for token counts but challenging for execution time (network variability) or completeness (task complexity).

---

## Data

### Data: Stability Analysis (Coefficient of Variation)

#### CV Values by Framework and Metric

| Framework | API Calls (count) | Cached Tokens (count) | Execution Time (seconds) | Input Tokens (count) | Output Tokens (count) | Total Tokens (count) | Total Cost (USD) |
|-----------|-------|-------|-------|-------|-------|-------|-------|
| baes | 0.028 ✓ | 5.829 ✗ | 0.184 ✓ | 0.027 ✓ | 0.062 ✓ | 0.034 ✓ | 0.045 ✓ | 
| chatdev | 0.173 ✓ | 0.761 ✗ | 0.245 ✗ | 0.211 ✗ | 0.201 ✗ | 0.204 ✗ | 0.194 ✓ | 
| ghspec | 0.112 ✓ | 0.135 ✓ | 0.176 ✓ | 0.111 ✓ | 0.121 ✓ | 0.110 ✓ | 0.110 ✓ | 

*Note: ✓ = Stable (CV < 0.3), ✗ = Unstable (CV ≥ 0.3)*

#### Aggregation Methodology

| Property | Value |
|----------|-------|
| Stability Metric | Coefficient of Variation (CV = σ/μ) |
| Stability Threshold | CV < 0.3 |
| Interpretation | Lower CV = more consistent/reproducible |
| Statistical Basis | Ratio of standard deviation to mean |


---

## Analysis

### Analysis

This stability plot assesses the consistency of framework performance across 7 metrics using the Coefficient of Variation (CV). Lower CV values indicate more consistent, reproducible performance. **Stability Summary**: ghspec achieves stability (CV < 0.3) on 7/7 metrics (100.0%), while chatdev is stable on 2/7 metrics (28.6%). 

**Metric-Level Stability**: Across all frameworks, api_calls shows the best average stability (CV = 0.104), while cached_tokens is least stable (CV = 2.242). 

**Unstable Cases**: 6/21 framework-metric combinations (28.6%) show high variability (CV ≥ 0.3). This may indicate non-deterministic behavior, sensitivity to random initialization, or insufficient sampling (consider increasing n_runs for these cases). 

**Stability Methodology**: CV is calculated as σ/μ (standard deviation / mean) for each framework-metric combination across multiple independent runs. The threshold CV < 0.3 is a standard criterion from measurement science, where CV < 0.3 indicates acceptable stability for most experimental contexts. 

**Interpretation Guidance**: Frameworks with high stability (many ✓ indicators) are preferred for reproducible research, as they produce consistent results across runs. Unstable metrics (✗ indicators) require careful interpretation: (1) increase n_runs to reduce sampling uncertainty, (2) investigate sources of non-determinism (LLM temperature, random seeding), or (3) use statistical tests designed for high-variance data (bootstrapping, permutation tests).
