# Run Summary

**Run ID**: 731e2bcf-0564-4a46-80bc-d3e0bf080047
**Framework**: ghspec
**Started**: 2025-10-29T05:16:35.351331Z
**Completed**: 2025-10-29T05:36:42.072947Z
**Duration**: 1206.72s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 170.39 |
| 2 | 2 | completed | 0/0 | 0 | 143.65 |
| 3 | 3 | completed | 0/0 | 0 | 148.67 |
| 4 | 4 | completed | 0/0 | 0 | 275.77 |
| 5 | 5 | completed | 0/0 | 0 | 264.72 |
| 6 | 6 | completed | 0/0 | 0 | 203.52 |

## Directory Structure

```
731e2bcf-0564-4a46-80bc-d3e0bf080047/
├── sprint_001/          # First sprint artifacts
│   ├── generated_artifacts/
│   ├── logs/
│   ├── metadata.json
│   └── validation.json
├── sprint_002/          # Second sprint artifacts
│   └── ...
├── final/               # Symlink to last successful sprint
└── metrics.json         # Run-level metrics (single source of truth)
```

## Accessing Results

### View final artifacts
```bash
cd final/generated_artifacts/managed_system/
```

### Compare sprints
```bash
diff -r sprint_001/generated_artifacts sprint_002/generated_artifacts
```

### View metrics (single source of truth)
```bash
cat metrics.json | jq
```

### Check specific sprint
```bash
cat sprint_001/metadata.json
```
