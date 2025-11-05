# Visualization Documentation: violin_plot_cached_tokens.svg

**Visualization Type**: Violin  
**Metric**: cached_tokens  
**Frameworks**: ghspec, baes, chatdev  
**Generated**: 2025-11-03T11:23:49.626932Z

---

## Rationale

This Violin visualization was generated to compare Cached Tokens (count) performance across ghspec, baes, chatdev. The violin plot combines box plot features with kernel density estimation to show full distribution shapes.

**Interpretation Guidance**: Violin plots reveal full distribution shapes through kernel density estimation. Look for: (1) Multiple peaks (multimodality) suggesting distinct performance regimes. (2) Skewness—fat tail on right/left indicates asymmetric behavior. (3) Width at different heights—wide sections have more data concentration. Test selection: Shapiro-Wilk p<0.05 indicates non-normality, requiring robust methods. For software metrics where higher variance often accompanies higher means, consider log-transformation or coefficient of variation for fair comparison.

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

The violin reveals Cached Tokens (count) patterns across frameworks. baes shows the lowest mean (69.120), while ghspec exhibits the highest (149184.000), representing a 215733.3% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 3/3 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

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

The violin plot contrasts Cached Tokens counts across ghspec, baes, and chatdev with N=100 runs per framework. A striking separation is visible: ghspec’s distribution is concentrated at very high counts (on the order of 1e5–2e5), dwarfing the other frameworks. Chatdev shows a broad, right‑skewed spread reaching tens of thousands, with a visibly wide body at lower tens of thousands and a long right tail; hints of multimodality are present. Baes clusters tightly near zero with sparse high outliers. Programmatic metrics corroborate the visual gap: mean(baes)=69.120 versus mean(ghspec)=149,184.000, a 215,733.3% relative difference, indicating a very large practical effect. Normality checks (Shapiro–Wilk p<0.05 for all three) imply non-normal, skewed distributions; two frameworks exhibit high skewness (|skew|>1), making medians more reliable than means. Outliers (1.5×IQR rule) were detected for baes and chatdev, aligning with the visible long upper tails. Given heteroscedasticity and skew, robust inference is warranted: median comparisons with bootstrap 95% CIs and non-parametric tests (Kruskal–Wallis / Mann–Whitney U). The large vertical separation suggests non-overlapping median CIs between ghspec and the others, and likely between chatdev and baes. Data quality considerations include extreme scale differences that compress detail for baes, recommending log-transformation or reporting coefficient of variation to contextualize variability relative to central tendency.

### Camera-Ready Paragraph

Figure: violin_plot_cached_tokens.svg compared distributions of Cached Tokens across three frameworks (N=100 per group). The analysis revealed a pronounced separation: ghspec exhibited the highest counts with a dense mass at very large values (≈10^5–10^5+), chatdev showed intermediate but widely dispersed counts with a long right tail, and baes clustered near zero with occasional high outliers. Normality was rejected for all frameworks (Shapiro–Wilk, p<0.05), and two groups displayed high skewness (|skew|>1), so medians and rank-based tests were appropriate. The magnitude of differences was substantial: the mean for ghspec (149,184.000) exceeded baes (69.120) by 215,733.3%, and chatdev stood orders of magnitude above baes while remaining far below ghspec. Bootstrap 95% confidence intervals around medians were expected to be widely separated, indicating strong practical differences. These findings support the hypothesis that frameworks differ markedly in cached token behavior. They imply that ghspec’s caching regime generates far greater token accumulation than chatdev and baes, while chatdev demonstrates heterogeneous behavior with occasional very large runs. The visualization substantiates the research question by making distributional contrasts, skewness, and outliers explicit, guiding the choice of non-parametric inference.

### Actionable Recommendations

Interpret results using medians and robust intervals; report median ratios and a non-parametric omnibus test (Kruskal–Wallis), followed by pairwise Mann–Whitney U with Holm correction. Quantify practical importance with effect sizes (Cliff’s delta) and coefficient of variation. Re-plot on a log10 y-axis to reveal internal structure for baes and chatdev; annotate medians and 95% bootstrap CIs directly on the violins. Investigate outliers by run metadata (task type, prompt length, cache hits) to determine whether they reflect rare but valid operating modes or data artifacts. Consider normalization by workload (e.g., tokens cached per task token) to compare efficiency rather than totals. Discuss limitations from potential heteroscedasticity and extreme skew. For publication, ensure consistent axis ranges, include N per group, and provide the analysis script and raw data to enable reproducibility.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 54.1s
- Token Usage: 4,026 tokens (1,720 prompt + 2,306 completion)
- Estimated Cost: $0.0000 USD
