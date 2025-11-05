# Visualization Documentation: rank_heatmap.svg

**Visualization Type**: Rank  
**Metric**: multi_metric_ranking  
**Frameworks**: chatdev, baes, ghspec  
**Generated**: 2025-11-03T08:51:30.457333Z

---

## Rationale

This Rank visualization was generated to compare Multi Metric Ranking performance across chatdev, baes, ghspec. The ranking visualization aggregates performance across metrics to identify overall leaders.

**Interpretation Guidance**: Rankings aggregate performance across metrics to identify overall leaders. Decision logic: (1) Rank by ascending mean for cost/time metrics (lower is better). (2) Use statistical tests (Kruskal-Wallis) to determine if differences are significant before ranking. (3) Assign tied ranks when p>0.05 (statistically indistinguishable). Practical thresholds: Average rank difference <0.5 is usually negligible. Consider that consistent rank-2 performer may be more valuable than inconsistent leader (rank-1 on some metrics, rank-3 on others) depending on use case requirements.

---

## Data

### Data: Framework Rankings

#### Ranking Matrix

| Framework | API Calls (count) | Cached Tokens (count) | Execution Time (seconds) | Input Tokens (count) | Output Tokens (count) | Total Tokens (count) | Total Cost (USD) | Avg Rank |
|-----------|-------|-------|-------|-------|-------|-------|-------|----------|
| chatdev | 1 | 2 | 3 | 2 | 2 | 2 | 2 | 2.00 |
| baes | 3 | 3 | 1 | 3 | 3 | 3 | 1 | 2.43 |
| ghspec | 2 | 1 | 2 | 1 | 1 | 1 | 3 | 1.57 |

*Note: Asterisk (*) indicates tied rank. Lower rank = better performance.*

####Aggregation Methodology

| Property | Value |
|----------|-------|
| Frameworks Compared | 3 |
| Metrics Evaluated | 7 |
| Ranking Method | Ascending order by mean value (lower is better) |
| Tie Handling | Frameworks with statistically identical values share rank |


---

## Analysis

### Analysis

This rank heatmap provides a comprehensive view of framework performance across 7 metrics, enabling identification of overall leaders and metric-specific strengths. **Overall Leader**: ghspec achieves the best average rank (1.57), while baes has the highest average rank (2.43). ghspec leads on 4/7 metrics (57.1% win rate). 

**Ranking Methodology**: Frameworks are ranked within each metric by ascending mean value (lower is better for cost/time metrics). Ties are assigned when frameworks have statistically equivalent values (p > 0.05 in pairwise tests). The heatmap uses color coding where green (rank 1) indicates best performance and red (rank 3) indicates worst. 

**Interpretation Guidance**: Use this visualization to identify: (1) overall winners (lowest average rank), (2) metric-specific strengths (rank 1 cells), and (3) consistency (low variance in ranks across metrics). Consider that a framework ranking 2nd on all metrics may be more valuable than one ranking 1st on some and last on others, depending on requirements.
