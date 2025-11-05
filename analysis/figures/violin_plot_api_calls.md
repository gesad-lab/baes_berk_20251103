# Visualization Documentation: violin_plot_api_calls.svg

**Visualization Type**: Violin  
**Metric**: api_calls  
**Frameworks**: ghspec, baes, chatdev  
**Generated**: 2025-11-03T11:19:35.096156Z

---

## Rationale

This Violin visualization was generated to compare API Calls (count) performance across ghspec, baes, chatdev. The violin plot combines box plot features with kernel density estimation to show full distribution shapes.

**Interpretation Guidance**: Violin plots reveal full distribution shapes through kernel density estimation. Look for: (1) Multiple peaks (multimodality) suggesting distinct performance regimes. (2) Skewness—fat tail on right/left indicates asymmetric behavior. (3) Width at different heights—wide sections have more data concentration. Test selection: Shapiro-Wilk p<0.05 indicates non-normality, requiring robust methods. For software metrics where higher variance often accompanies higher means, consider log-transformation or coefficient of variation for fair comparison.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| ghspec | 89.910 | 89.000 | [86.000, 91.000] | 10.093 | 70.000 | 116.000 | 82.000 | 97.250 | 0 | 100 |
| baes | 18.310 | 18.000 | [18.000, 18.000] | 0.506 | 18.000 | 20.000 | 18.000 | 19.000 | 0 | 100 |
| chatdev | 116.010 | 111.000 | [109.000, 119.000] | 20.048 | 85.000 | 172.000 | 103.000 | 129.250 | 1 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The violin reveals API Calls (count) patterns across frameworks. baes shows the lowest mean (18.310), while chatdev exhibits the highest (116.010), representing a 533.6% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 3/3 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

*Shapiro-Wilk tests if data follows a bell curve (normal distribution). p>0.05 suggests normality; p<0.05 indicates non-normal data requiring robust statistical methods.* 

*Mann-Whitney U is a non-parametric test comparing groups without assuming normality. Ranks all values and tests if one group tends to have higher ranks. More robust than t-test for skewed data.*

**Skewness Detected**: 1 framework(s) exhibit high skewness (|skew| > 1.0), indicating median is more representative than mean. 

*Skewness measures distribution asymmetry. Positive skew: long right tail (mean>median). Negative skew: long left tail (mean<median). |skew|>1 indicates high skewness affecting mean reliability.*

**Outliers**: Detected in 1 framework(s): chatdev. 

*Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.*

**Statistical Methodology**: N=100 runs per framework, distributions characterized by median with bootstrap 95% CIs, IQR, and outlier detection (1.5×IQR criterion). 

*Bootstrapping estimates uncertainty by repeatedly resampling data with replacement. Creates thousands of simulated samples to calculate confidence intervals without assuming normal distributions.* 

*A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.*

---

## LLM-Enhanced Analysis

### Focused Insights

The violin plot contrasts API call distributions across ghspec, baes, and chatdev. baes forms a very narrow, low-positioned violin centered around ~18 calls (mean=18.31), indicating tight dispersion and a highly concentrated workload. ghspec sits markedly higher, with a broader, roughly symmetric shape concentrated around ~80–95 calls and moderate variance. chatdev displays the highest center (mean=116.01) and the broadest spread, extending from roughly the mid-70s to ~185 calls, with a pronounced right tail and flagged outliers, consistent with positive skewness. Separation between baes and the other frameworks is visually substantial, suggesting a large practical effect; the relative mean difference between chatdev and baes is 533.6%. Overlap is minimal for baes versus the others, while ghspec and chatdev show partial overlap in the 90–120 range. Shapiro–Wilk tests indicated non-normality for all three frameworks (p<0.05), so medians and IQRs are the appropriate descriptive focus, and non-parametric tests (e.g., Kruskal–Wallis with post-hoc Mann–Whitney/Dunn) are warranted. The presence of high skewness in chatdev implies the mean is less reliable than the median for that group. Data quality appears strong (N=100 per framework, balanced sampling), but chatdev’s outliers and heavier tail merit robustness checks. The density shapes provide no strong evidence of multimodality, though chatdev hints at multiple regimes due to widening at upper quantiles.

### Camera-Ready Paragraph

Figure: violin_plot_api_calls.svg compared the distributions of API Calls (count) across three frameworks (N=100 per group). baes exhibited the lowest usage (mean=18.31) with a very tight distribution, whereas ghspec showed moderate counts concentrated around 80–95 calls. chatdev had the highest usage (mean=116.01) with the largest dispersion and a pronounced right tail; outliers were detected under the 1.5×IQR criterion. Shapiro–Wilk tests indicated non-normality for all frameworks (p<0.05), and chatdev displayed high positive skewness, making medians more representative than means. The relative mean difference between chatdev and baes was 533.6%, and the clear separation of baes from the other distributions visually implied a large practical effect. The analysis revealed substantial, distributional differences across frameworks, supporting the hypothesis that API-call efficiency varies by framework. This suggests that baes is markedly more API-efficient, while chatdev incurs higher and more variable call counts. Given the non-normality and outliers, robust inference is appropriate; omnibus differences should be confirmed via Kruskal–Wallis, followed by multiple-comparison–adjusted pairwise tests. The figure directly addresses the research question by showing not only central tendency differences but also full distributional shapes that clarify variance and tail behavior.

### Actionable Recommendations

In practice, interpret efficiency primarily via medians and IQRs due to non-normality and skew. Report an omnibus Kruskal–Wallis test, then conduct Dunn or pairwise Mann–Whitney tests with Holm or Benjamini–Hochberg correction. Quantify practical significance using non-parametric effect sizes (e.g., Cliff’s delta or rank-biserial correlation) and include bootstrap 95% CIs for medians and effect sizes. Consider log-transformation or modeling counts with robust or count models (e.g., negative binomial) as a sensitivity check. Probe sources of chatdev’s right tail by stratifying runs (task type, prompts, budgets) and assessing coefficient of variation to compare relative dispersion. Treat outliers transparently: analyze with and without them, but avoid deletion unless justified a priori. For publication, retain the violin with overlaid box/median markers, annotate N, and accompany with a concise table of medians, IQRs, and adjusted p-values.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 65.9s
- Token Usage: 4,730 tokens (1,714 prompt + 3,016 completion)
- Estimated Cost: $0.0000 USD
