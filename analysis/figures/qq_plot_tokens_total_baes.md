# Visualization Documentation: qq_plot_tokens_total_baes.svg

**Visualization Type**: Qq Plot  
**Metric**: tokens_total  
**Frameworks**: baes  
**Generated**: 2025-11-03T11:42:32.125192Z

---

## Rationale

This Qq Plot visualization was generated to compare Total Tokens (count) performance across baes. The Q-Q plot assesses normality by comparing sample quantiles against theoretical normal distribution.

**Interpretation Guidance**: Q-Q plots assess normality assumption required for parametric tests. Decision tree: (1) Points follow diagonal line closely → data is normal → use t-test/ANOVA. (2) Systematic S-curve pattern → data is skewed → use Mann-Whitney U or transform data. (3) Points diverge at tails → heavy tails/outliers → use robust methods or trim outliers. (4) Shapiro-Wilk p<0.05 confirms non-normality → non-parametric tests mandatory. For sample sizes N>30, minor deviations acceptable due to Central Limit Theorem, but severe violations (p<0.01) still require robust alternatives.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| baes | 45122.300 | 44198.500 | [44190.000, 44213.500] | 1529.463 | 44120.000 | 50218.000 | 44177.500 | 47190.500 | 0 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The qq plot reveals Total Tokens (count) patterns across frameworks. baes shows the lowest mean (45122.300), while baes exhibits the highest (45122.300), representing a 0.0% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 1/1 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

*Shapiro-Wilk tests if data follows a bell curve (normal distribution). p>0.05 suggests normality; p<0.05 indicates non-normal data requiring robust statistical methods.* 

*Mann-Whitney U is a non-parametric test comparing groups without assuming normality. Ranks all values and tests if one group tends to have higher ranks. More robust than t-test for skewed data.*

**Skewness Detected**: 1 framework(s) exhibit high skewness (|skew| > 1.0), indicating median is more representative than mean. 

*Skewness measures distribution asymmetry. Positive skew: long right tail (mean>median). Negative skew: long left tail (mean<median). |skew|>1 indicates high skewness affecting mean reliability.*

**Statistical Methodology**: N=100 runs per framework, distributions characterized by median with bootstrap 95% CIs, IQR, and outlier detection (1.5×IQR criterion). 

*Bootstrapping estimates uncertainty by repeatedly resampling data with replacement. Creates thousands of simulated samples to calculate confidence intervals without assuming normal distributions.* 

*A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.*

---

## LLM-Enhanced Analysis

### Focused Insights

The Q–Q plot for Total Tokens (count) under the baes framework shows clear departures from normality. Instead of aligning with the 45° reference line, the points form an S-shaped pattern with two dense plateaus: one around ~44.1–44.3k tokens (negative theoretical quantiles) and another around ~47.0–47.3k (positive quantiles). This step-like structure indicates a mixture or bimodal distribution, suggesting two operating regimes rather than a single Gaussian process. The upper tail exhibits strong divergence, with two conspicuous outliers near ~50.1–50.2k tokens that lie far above the reference line, producing pronounced positive skew and heavy tails. The embedded Shapiro–Wilk test reports p < 0.001, providing strong evidence against normality at α = 0.05. Given N ≈ 100, such systematic deviations are unlikely to be sampling noise; CLT-based tolerance for mild deviations does not apply here. The programmatic summary flags high skewness (|skew| > 1), consistent with the visual impression that the mean overstates central tendency relative to the median. Data quality considerations include potential batching effects, context-window artifacts, or configuration changes across runs that could drive the bimodality. The discreteness of token counts may contribute to ties but does not explain the gap between clusters. For inference and comparisons, parametric tests assuming homoscedastic normality are inappropriate; non-parametric or robust methods (median/IQR, Mann–Whitney/Kruskal–Wallis, bootstrap CIs, trimmed means) are warranted, with explicit handling of upper-tail outliers.

### Camera-Ready Paragraph

Figure: qq_plot_tokens_total_baes.svg presented a Q–Q analysis of Total Tokens (count) for the baes framework. The sample quantiles did not follow the normal-theory reference line; instead, they exhibited an S-shaped deviation with two pronounced clusters around ~44.2k and ~47.1–47.3k tokens, and two extreme right-tail points near ~50.2k. The Shapiro–Wilk test indicated strong non-normality (p < 0.001), and the distribution showed positive skew and heavy tails, consistent with elevated skewness (|skew| > 1). These results refuted the hypothesis that token counts for baes were approximately normally distributed across runs. The pattern implies multiple operating regimes or configuration-induced shifts rather than random Gaussian fluctuations. Consequently, parametric procedures relying on normality (e.g., t-tests/ANOVA on means) would be model-misspecified, whereas robust or non-parametric approaches (median-based estimators, Mann–Whitney or Kruskal–Wallis, bootstrap confidence intervals) are more appropriate. This suggests that conclusions about relative token usage should emphasize distributional robustness and sensitivity to upper-tail observations, linking directly to the research question of how reliably token consumption can be compared across experimental conditions.

### Actionable Recommendations

In practice, treat baes token counts as non-normal and right-skewed. Report medians, IQRs, and bootstrap 95% CIs rather than means and standard errors. When comparing frameworks or conditions, use Mann–Whitney or Kruskal–Wallis, and complement with effect sizes robust to outliers (Hodges–Lehmann, Cliff’s delta). Perform sensitivity checks with 10–20% trimmed means or winsorization and confirm findings under Yeo–Johnson or log transforms. Investigate bimodality by stratifying runs by configuration, prompt length, or context-window usage; mixture modeling or change-point analysis may reveal regime shifts. Document and, if possible, control sources of the extreme upper-tail values. For publication, include the Q–Q plot alongside a density or violin plot, state Shapiro–Wilk p < 0.001, and justify the chosen robust methods and effect sizes.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 43.1s
- Token Usage: 4,152 tokens (1,663 prompt + 2,489 completion)
- Estimated Cost: $0.0000 USD
