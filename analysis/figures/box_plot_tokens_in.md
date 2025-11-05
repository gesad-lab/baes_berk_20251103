# Visualization Documentation: box_plot_tokens_in.svg

**Visualization Type**: Boxplot  
**Metric**: tokens_in  
**Frameworks**: ghspec, baes, chatdev  
**Generated**: 2025-11-03T11:32:07.410626Z

---

## Rationale

This Boxplot visualization was generated to compare Input Tokens (count) performance across ghspec, baes, chatdev. The box plot shows median, quartiles, and outliers to enable robust comparison of distributions.

**Interpretation Guidance**: Box plots use median (50th percentile) as the central measure, making them robust to outliers. When comparing groups: (1) Check for box overlap—minimal overlap suggests different distributions. (2) Examine outliers (points beyond whiskers)—these may indicate data quality issues or extreme cases worth investigating. (3) Compare IQR widths—larger IQR indicates higher variability. For statistical testing: If boxes show non-normal patterns (asymmetric, heavy outliers), prefer non-parametric tests (Mann-Whitney U, Kruskal-Wallis) over t-tests/ANOVA.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| ghspec | 294720.580 | 288673.500 | [280733.500, 301019.000] | 32567.513 | 234785.000 | 394313.000 | 269970.750 | 315616.000 | 1 | 100 |
| baes | 35750.290 | 35167.000 | [35167.000, 35167.000] | 953.219 | 35167.000 | 38937.000 | 35167.000 | 37052.000 | 0 | 100 |
| chatdev | 154917.440 | 146999.500 | [141594.000, 153324.000] | 32749.365 | 102986.000 | 282095.000 | 135513.750 | 173201.750 | 3 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The boxplot reveals Input Tokens (count) patterns across frameworks. baes shows the lowest mean (35750.290), while ghspec exhibits the highest (294720.580), representing a 724.4% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 3/3 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

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

The boxplot contrasts Input Tokens across three frameworks and shows clear stratification. ghspec consumed the most tokens, with a high median near 2.9e5 and a broad IQR (roughly 2.7e5–3.1e5). chatdev was intermediate (median about 1.45e5; wider spread and a long right tail), while baes displayed the lowest usage (median around 3.6–3.8e4) with a very tight IQR. Whiskers and boxes exhibited minimal to no overlap between ghspec and the other groups, and only limited overlap between chatdev and baes, visually indicating large between-group effects. Programmatic diagnostics reported non-normality for all three distributions (Shapiro–Wilk p<0.05), high skewness for two frameworks, and outliers for ghspec and chatdev. The observed right-tail outliers (e.g., ghspec near 3.95e5; chatdev around 2.35–2.82e5) suggest occasional extreme runs or heterogeneous tasks. Means were therefore less reliable; nonetheless, the mean difference between ghspec and baes was pronounced (724.4% relative difference). Given the shape and separation, median-based inference and non-parametric tests are appropriate. A Kruskal–Wallis omnibus comparison, followed by pairwise Wilcoxon/Dunn tests with multiplicity control, would likely detect statistically significant differences, and the visual separation implies large effect sizes (stochastic superiority strongly favoring ghspec over the others). Bootstrapped 95% CIs for medians (as computed programmatically) are expected to show limited overlap, reinforcing the inference. Data appear complete but with heavy tails; reporting medians, IQRs, and outlier handling rules is crucial for reproducibility.

### Camera-Ready Paragraph

Figure: box_plot_tokens_in.svg compared Input Tokens (count) across ghspec, baes, and chatdev. The analysis revealed a clear ordering: ghspec exhibited the highest token consumption (median approximately 2.9×10^5 with a broad IQR), chatdev was intermediate (median roughly 1.45×10^5 with a pronounced right tail), and baes showed the lowest and most stable usage (median ≈3.6–3.8×10^4). Distributions were non-normal for all frameworks (Shapiro–Wilk p<0.05), and outliers were observed in ghspec and chatdev, indicating occasional extreme runs. The boxes and whiskers showed minimal overlap between groups, implying large between-group effects. Accordingly, non-parametric inference is warranted: a Kruskal–Wallis test, supplemented by pairwise Wilcoxon/Dunn procedures with Holm correction, is expected to yield statistically significant differences with large effect sizes, consistent with the 724% mean contrast between ghspec and baes. These results suggest that framework choice substantially affects input-token demand, with ghspec typically requiring an order of magnitude more tokens than baes and roughly double that of chatdev. This supports the hypothesis that architectural or prompting design differences drive distinct token budgets and informs cost–efficiency trade-offs in downstream applications.

### Actionable Recommendations

Interpret differences primarily via medians and IQRs, not means, given skewness and outliers. Conduct a Kruskal–Wallis omnibus test followed by pairwise Wilcoxon/Dunn comparisons with Holm correction; report effect sizes such as Cliff’s delta or rank-biserial correlation. Inspect outliers to distinguish data quality issues from legitimate extreme workloads; consider reporting results with and without outliers. Explore task-level stratification or mixed-effects/quantile models to control for workload heterogeneity. For robustness, assess sensitivity to log transformation and verify conclusions with bootstrap CIs for medians. In publication, annotate medians and sample sizes (N=100/group), add notches or CI bands, and overlay jittered points to convey density. Clarify token accounting rules and any preprocessing that could shift distributions.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 56.7s
- Token Usage: 4,962 tokens (1,740 prompt + 3,222 completion)
- Estimated Cost: $0.0000 USD
