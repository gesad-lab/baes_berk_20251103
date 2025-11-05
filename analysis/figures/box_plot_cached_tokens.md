# Visualization Documentation: box_plot_cached_tokens.svg

**Visualization Type**: Boxplot  
**Metric**: cached_tokens  
**Frameworks**: ghspec, baes, chatdev  
**Generated**: 2025-11-03T11:22:54.312735Z

---

## Rationale

This Boxplot visualization was generated to compare Cached Tokens (count) performance across ghspec, baes, chatdev. The box plot shows median, quartiles, and outliers to enable robust comparison of distributions.

**Interpretation Guidance**: Box plots use median (50th percentile) as the central measure, making them robust to outliers. When comparing groups: (1) Check for box overlap—minimal overlap suggests different distributions. (2) Examine outliers (points beyond whiskers)—these may indicate data quality issues or extreme cases worth investigating. (3) Compare IQR widths—larger IQR indicates higher variability. For statistical testing: If boxes show non-normal patterns (asymmetric, heavy outliers), prefer non-parametric tests (Mann-Whitney U, Kruskal-Wallis) over t-tests/ANOVA.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| ghspec | 149184.000 | 147008.000 | [140160.000, 154496.000] | 20169.201 | 113920.000 | 201600.000 | 133728.000 | 160992.000 | 0 | 100 |
| baes | 69.120 | 0.000 | [0.000, 0.000] | 402.895 | 0.000 | 2688.000 | 0.000 | 0.000 | 3 | 100 |
| chatdev | 10056.960 | 7872.000 | [6912.000, 8896.000] | 7654.752 | 0.000 | 39424.000 | 5184.000 | 12288.000 | 9 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The boxplot reveals Cached Tokens (count) patterns across frameworks. baes shows the lowest mean (69.120), while ghspec exhibits the highest (149184.000), representing a 215733.3% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 3/3 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

*Shapiro-Wilk tests if data follows a bell curve (normal distribution). p>0.05 suggests normality; p<0.05 indicates non-normal data requiring robust statistical methods.* 

*Mann-Whitney U is a non-parametric test comparing groups without assuming normality. Ranks all values and tests if one group tends to have higher ranks. More robust than t-test for skewed data.*

**Skewness Detected**: 2 framework(s) exhibit high skewness (|skew| > 1.0), indicating median is more representative than mean. 

*Skewness measures distribution asymmetry. Positive skew: long right tail (mean>median). Negative skew: long left tail (mean<median). |skew|>1 indicates high skewness affecting mean reliability.*

**Outliers**: Detected in 2 framework(s): baes, chatdev. 

*Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.*

**Statistical Methodology**: N=100 runs per framework, distributions characterized by median with bootstrap 95% CIs, IQR, and outlier detection (1.5×IQR criterion). 

*Bootstrapping estimates uncertainty by repeatedly resampling data with replacement. Creates thousands of simulated samples to calculate confidence intervals without assuming normal distributions.* 

*A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.*

---

## LLM-Enhanced Analysis

### Focused Insights

The boxplot contrasts Cached Tokens (count) across ghspec, baes, and chatdev. ghspec displayed the largest counts with a high median around 1.4–1.6×10^5 and a broad IQR, indicating substantial variability but consistently high caching. chatdev was an order of magnitude lower, with a median near 8–10×10^3 and a positively skewed distribution; several high-end outliers (≈25–40k) suggest occasional heavy caching events. baes clustered at (or very near) zero with negligible spread, punctuated by rare nonzero outliers, consistent with a zero-inflated or on/off caching regime. Boxes for ghspec and the other two frameworks showed minimal overlap, visually indicating distinct distributions; chatdev and baes overlapped only near the lower bound. Shapiro–Wilk normality tests rejected normality in all groups (p<0.05), and two frameworks showed high skewness, so median-based comparisons are preferred. The reported mean contrast underscored the effect magnitude: baes averaged 69.1 tokens while ghspec averaged 149,184 (a 215,733% relative difference). Bootstrapped 95% CIs for medians (per methodology) would emphasize uncertainty without normality assumptions; given the clear separation, inferential tests such as Kruskal–Wallis and pairwise Mann–Whitney U are appropriate. Data-quality considerations include zero inflation in baes, potential floor effects, and influential outliers in chatdev and baes that could reflect heterogeneous workloads or instrumentation artifacts.

### Camera-Ready Paragraph

Figure: box_plot_cached_tokens.svg compared the distribution of cached tokens across three frameworks. ghspec exhibited the largest counts, with a median near 1.5×10^5 and a wide interquartile range, whereas chatdev showed an order-of-magnitude lower median (~8–10×10^3) and a positively skewed distribution with several high-end outliers. baes clustered at zero with rare spikes. Shapiro–Wilk tests rejected normality in all groups (p<0.05), motivating non-parametric inference. The magnitude of the difference was large: the reported mean for ghspec exceeded that of baes by 215,733%, and the ghspec box overlapped minimally with the other frameworks. The analysis revealed clear separation among frameworks, supporting the hypothesis that framework choice materially affected cached-token usage. This suggests ghspec consistently maintained substantially more cached state, chatdev cached moderately with occasional heavy episodes, and baes effectively disabled or avoided caching. These findings address the research question by demonstrating distributional differences, with implications for memory footprint, reuse potential, and system cost. Non-parametric effect sizes (e.g., rank-biserial) would further quantify the visual gaps evident in the figure.

### Actionable Recommendations

In practice, interpret ghspec as a high-caching regime, chatdev as moderate with episodic spikes, and baes as near-zero caching. Use Kruskal–Wallis to test overall group differences, followed by Mann–Whitney U pairwise comparisons with Holm correction. Report medians, IQRs, and bootstrap 95% CIs, alongside rank-biserial (or Cliff’s delta) effect sizes to quantify separation. Diagnose zero inflation in baes (e.g., hurdle or zero-inflated models) and assess sensitivity by repeating analyses on log1p-transformed counts. Investigate outliers in chatdev and baes for workload or instrumentation causes. For publication, consider a log-scaled y-axis or broken axis to improve readability, annotate sample size (N=100 per framework), and add jittered points to convey density. Clearly state non-normality and justify non-parametric methods.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 55.2s
- Token Usage: 4,522 tokens (1,739 prompt + 2,783 completion)
- Estimated Cost: $0.0000 USD
