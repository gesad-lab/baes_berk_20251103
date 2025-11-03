# Run Summary

**Run ID**: 0a71f334-b4f4-4abe-b9eb-dea165dff38d
**Framework**: chatdev
**Started**: 2025-10-30T09:27:44.858691Z
**Completed**: 2025-10-30T09:45:26.368254Z
**Duration**: 1061.51s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 146.71 |
| 2 | 2 | completed | 0/0 | 0 | 161.49 |
| 3 | 3 | completed | 0/0 | 0 | 178.28 |
| 4 | 4 | completed | 0/0 | 0 | 191.97 |
| 5 | 5 | completed | 0/0 | 0 | 199.24 |
| 6 | 6 | completed | 0/0 | 0 | 183.82 |

## Directory Structure

```
0a71f334-b4f4-4abe-b9eb-dea165dff38d/
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
