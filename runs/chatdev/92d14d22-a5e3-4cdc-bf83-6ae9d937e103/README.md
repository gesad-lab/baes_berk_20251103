# Run Summary

**Run ID**: 92d14d22-a5e3-4cdc-bf83-6ae9d937e103
**Framework**: chatdev
**Started**: 2025-10-29T02:04:38.960959Z
**Completed**: 2025-10-29T02:19:02.575634Z
**Duration**: 863.61s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 200.71 |
| 2 | 2 | completed | 0/0 | 0 | 142.84 |
| 3 | 3 | completed | 0/0 | 0 | 133.06 |
| 4 | 4 | completed | 0/0 | 0 | 118.76 |
| 5 | 5 | completed | 0/0 | 0 | 131.42 |
| 6 | 6 | completed | 0/0 | 0 | 136.82 |

## Directory Structure

```
92d14d22-a5e3-4cdc-bf83-6ae9d937e103/
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
