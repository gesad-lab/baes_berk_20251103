# Visualization Documentation: qq_plot_total_cost_usd_baes.svg

**Visualization Type**: Qq Plot  
**Metric**: total_cost_usd  
**Frameworks**: baes  
**Generated**: 2025-11-03T11:46:48.558916Z

---

## Rationale

This Qq Plot visualization was generated to compare Total Cost (USD) performance across baes. The Q-Q plot assesses normality by comparing sample quantiles against theoretical normal distribution.

**Interpretation Guidance**: Q-Q plots assess normality assumption required for parametric tests. Decision tree: (1) Points follow diagonal line closely → data is normal → use t-test/ANOVA. (2) Systematic S-curve pattern → data is skewed → use Mann-Whitney U or transform data. (3) Points diverge at tails → heavy tails/outliers → use robust methods or trim outliers. (4) Shapiro-Wilk p<0.05 confirms non-normality → non-parametric tests mandatory. For sample sizes N>30, minor deviations acceptable due to Central Limit Theorem, but severe violations (p<0.01) still require robust alternatives.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| baes | 0.011 | 0.011 | [0.011, 0.011] | 0.000 | 0.010 | 0.013 | 0.011 | 0.012 | 0 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The qq plot reveals Total Cost (USD) patterns across frameworks. baes shows the lowest mean (0.011), while baes exhibits the highest (0.011), representing a 0.0% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 1/1 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

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

The Q–Q plot for Total Cost (USD) in the baes framework shows pronounced departures from normality. Points deviate systematically from the 45° reference line, forming stair‑step plateaus at roughly two levels of the sample quantiles, with a few extreme points in the upper tail. This pattern is consistent with discretization (limited measurement precision) and possible mixture/bimodality rather than a single Gaussian process. The upper tail contains clear high-cost outliers (≈0.0126), producing positive skew and heavier-than-normal tails. The embedded Shapiro–Wilk test reports p < 0.001 (α = 0.05), confirming a statistically significant violation of normality for N ≈ 100 observations. Programmatic diagnostics also indicated high skewness (|skew| > 1), implying that the mean is less reliable than the median for central tendency. No missing data are evident from the plot, but the clustering and repeated values suggest rounding or batching in cost computation (e.g., fixed billing increments), which can inflate ties and distort parametric inference. The strong S-shaped divergence and tail inflation argue against using t-based methods without transformation or robust alternatives. Confidence intervals for medians via bootstrap would better capture uncertainty under these conditions, and effect sizes should prioritize rank-based metrics (e.g., Hodges–Lehmann) rather than mean differences.

### Camera-Ready Paragraph

Figure: qq_plot_total_cost_usd_baes.svg presented a Q–Q plot of Total Cost (USD) for the baes framework and revealed strong deviations from normality. The sample quantiles formed horizontal plateaus and diverged markedly from the theoretical normal line, with pronounced inflation in the upper tail and several high-cost outliers. The Shapiro–Wilk test indicated a significant departure from a Gaussian distribution (p < 0.001, α = 0.05), consistent with positive skew and potential multimodality. These features suggested that the cost-generating mechanism might involve discretized billing increments or multiple operating regimes, leading to ties and heavy tails. As a consequence, parametric procedures that rely on normality and mean-based effect sizes were not appropriate. This supports the study’s methodological choice to use robust summaries (median, IQR) and non-parametric inference. Implications for the research questions are that comparisons of total cost across conditions should emphasize rank-based effect sizes (e.g., Hodges–Lehmann estimates with bootstrap 95% CIs) and Mann–Whitney/Kruskal–Wallis tests. The visualization therefore challenged any hypothesis of approximate normality for baes costs and motivates modeling strategies that accommodate skewed, heavy-tailed, or mixture distributions.

### Actionable Recommendations

Interpret the baes cost distribution using robust statistics: report medians, IQRs, and bootstrap 95% CIs; complement with rank-based effect sizes (Hodges–Lehmann, Cliff’s delta) and non-parametric tests (Mann–Whitney or Kruskal–Wallis) for group comparisons. Investigate the apparent discretization by checking rounding rules or billing granularity; if confirmed, model using integer/fixed-increment outcomes or a mixture model. Consider transformations (log, Box–Cox) only if they meaningfully stabilize variance and reduce skew; otherwise use quantile regression or robust regression (Huber/Tukey). Assess sensitivity via outlier-robust analyses (trimmed means, winsorization). Examine batch effects or regime shifts that could explain the bimodal pattern. For publication, pair the Q–Q plot with a histogram/density and a table of Shapiro–Wilk p-values, skewness, and robust estimates; explicitly state that parametric assumptions were violated and justify the chosen non-parametric/robust methods.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 46.3s
- Token Usage: 3,932 tokens (1,667 prompt + 2,265 completion)
- Estimated Cost: $0.0000 USD
