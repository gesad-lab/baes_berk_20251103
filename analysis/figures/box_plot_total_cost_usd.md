# Visualization Documentation: box_plot_total_cost_usd.svg

**Visualization Type**: Boxplot  
**Metric**: total_cost_usd  
**Frameworks**: ghspec, baes, chatdev  
**Generated**: 2025-11-03T11:43:56.914761Z

---

## Rationale

This Boxplot visualization was generated to compare Total Cost (USD) performance across ghspec, baes, chatdev. The box plot shows median, quartiles, and outliers to enable robust comparison of distributions.

**Interpretation Guidance**: Box plots use median (50th percentile) as the central measure, making them robust to outliers. When comparing groups: (1) Check for box overlap—minimal overlap suggests different distributions. (2) Examine outliers (points beyond whiskers)—these may indicate data quality issues or extreme cases worth investigating. (3) Compare IQR widths—larger IQR indicates higher variability. For statistical testing: If boxes show non-normal patterns (asymmetric, heavy outliers), prefer non-parametric tests (Mann-Whitney U, Kruskal-Wallis) over t-tests/ANOVA.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| ghspec | 0.065 | 0.064 | [0.062, 0.066] | 0.007 | 0.050 | 0.087 | 0.059 | 0.069 | 2 | 100 |
| baes | 0.011 | 0.011 | [0.011, 0.011] | 0.000 | 0.010 | 0.013 | 0.011 | 0.012 | 0 | 100 |
| chatdev | 0.053 | 0.050 | [0.048, 0.052] | 0.010 | 0.037 | 0.090 | 0.046 | 0.058 | 3 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The boxplot reveals Total Cost (USD) patterns across frameworks. baes shows the lowest mean (0.011), while ghspec exhibits the highest (0.065), representing a 487.5% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 3/3 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

*Shapiro-Wilk tests if data follows a bell curve (normal distribution). p>0.05 suggests normality; p<0.05 indicates non-normal data requiring robust statistical methods.* 

*Mann-Whitney U is a non-parametric test comparing groups without assuming normality. Ranks all values and tests if one group tends to have higher ranks. More robust than t-test for skewed data.*

**Skewness Detected**: 2 framework(s) exhibit high skewness (|skew| > 1.0), indicating median is more representative than mean. 

*Skewness measures distribution asymmetry. Positive skew: long right tail (mean>median). Negative skew: long left tail (mean<median). |skew|>1 indicates high skewness affecting mean reliability.*

**Outliers**: Detected in 2 framework(s): ghspec, chatdev. 

*Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.*

**Statistical Methodology**: N=100 runs per framework, distributions characterized by median with bootstrap 95% CIs, IQR, and outlier detection (1.5×IQR criterion). 

*Bootstrapping estimates uncertainty by repeatedly resampling data with replacement. Creates thousands of simulated samples to calculate confidence intervals without assuming normal distributions.* 

*A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.*

---

## LLM-Enhanced Analysis

### Focused Insights

The boxplot compares Total Cost (USD) across ghspec, baes, and chatdev and shows clear distributional separation. baes clusters tightly at the lowest cost, with a very narrow IQR around approximately one cent and short whiskers, indicating both low central tendency and high stability. In contrast, ghspec exhibits the highest central tendency with a broader IQR and a pronounced right tail; visible outliers approach nine cents. chatdev is intermediate, with a median below ghspec but a wider IQR than baes and right‑tail outliers similar in magnitude to ghspec. Minimal overlap of the boxes between baes and the other frameworks suggests practically meaningful differences in distributions. Programmatic diagnostics reported non-normality across all groups (Shapiro–Wilk p<0.05 for 3/3), and high skewness for two frameworks, reinforcing the choice of medians and non‑parametric tests for inference. The mean for baes (0.011) was far below ghspec (0.065), a 487.5% relative increase, and chatdev trailed ghspec but remained substantially higher than baes; these effect magnitudes are consistent with the visual gaps. Outliers were detected for ghspec and chatdev; while they increase variance, they appear consistent with heavy‑tailed cost behavior rather than artifacts. With N=100 per framework and bootstrap 95% CIs available, inference should rely on Kruskal–Wallis for overall differences and Mann–Whitney U for pairwise contrasts, complemented by effect sizes (e.g., Cliff’s delta) to quantify practical relevance.

### Camera-Ready Paragraph

Figure: box_plot_total_cost_usd.svg summarized the distribution of Total Cost (USD) across three frameworks. The analysis revealed that baes exhibited the lowest central tendency and the tightest dispersion, whereas ghspec showed the highest costs and greater variability; chatdev fell between these extremes. Outliers were observed for ghspec and chatdev. Normality was rejected for all groups by Shapiro–Wilk tests (p<0.05), and two frameworks displayed substantial positive skew, indicating that median-based comparisons were more appropriate than mean-based analyses. The mean difference between ghspec (0.065 USD) and baes (0.011 USD) represented a 487.5% relative increase, indicating a large practical effect. Given these distributional properties, non‑parametric procedures (Kruskal–Wallis for overall differences and Mann–Whitney U for pairwise contrasts) are warranted; bootstrap 95% confidence intervals around medians provide uncertainty quantification without normality assumptions. Collectively, the visualization supported the hypothesis that frameworks differed in cost and suggested that baes was consistently less expensive. This suggests that researchers prioritizing cost efficiency should preferentially consider baes, while recognizing that ghspec and chatdev incurred higher and more variable costs.

### Actionable Recommendations

In practice, treat baes as the cost-minimizing option, especially when budget stability is critical. Confirm visual impressions with a Kruskal–Wallis test followed by Dunn–Holm pairwise comparisons, and report effect sizes (Cliff’s delta or rank-biserial) alongside bootstrap 95% CIs for medians. Assess robustness by repeating analyses after winsorizing or trimming 1–5% tails and by conducting sensitivity checks excluding identified outliers. Verify that costs are normalized for task complexity and token usage; if quality outcomes matter, analyze cost-per-success or cost-per-quality-point to avoid misleading conclusions. For publication, report medians, IQRs, and CI bands in text, and consider adding violin plots to show density. Document seed control, prompt parity, and run-to-run variability (N=100) to strengthen replicability and interpretability.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 56.3s
- Token Usage: 4,209 tokens (1,744 prompt + 2,465 completion)
- Estimated Cost: $0.0000 USD
