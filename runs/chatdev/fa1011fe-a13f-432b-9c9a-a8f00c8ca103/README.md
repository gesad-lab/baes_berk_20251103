# Run Summary

**Run ID**: fa1011fe-a13f-432b-9c9a-a8f00c8ca103
**Framework**: chatdev
**Started**: 2025-10-31T15:43:25.215204Z
**Completed**: 2025-10-31T16:01:34.722208Z
**Duration**: 1089.51s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 253.78 |
| 2 | 2 | completed | 0/0 | 0 | 233.57 |
| 3 | 3 | completed | 0/0 | 0 | 600.02 |
| 4 | 4 | completed | 0/0 | 0 | 0.71 |
| 5 | 5 | completed | 0/0 | 0 | 0.71 |
| 6 | 6 | completed | 0/0 | 0 | 0.71 |

## Directory Structure

```
fa1011fe-a13f-432b-9c9a-a8f00c8ca103/
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
