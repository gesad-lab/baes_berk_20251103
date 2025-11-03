# Run Summary

**Run ID**: 60bef485-9942-4981-b6fe-8631607aada6
**Framework**: baes
**Started**: 2025-10-31T05:00:19.368973Z
**Completed**: 2025-10-31T05:06:29.716852Z
**Duration**: 370.35s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 60.42 |
| 2 | 2 | completed | 0/0 | 0 | 59.73 |
| 3 | 3 | completed | 0/0 | 0 | 60.69 |
| 4 | 4 | completed | 0/0 | 0 | 62.99 |
| 5 | 5 | completed | 0/0 | 0 | 63.29 |
| 6 | 6 | completed | 0/0 | 0 | 63.23 |

## Directory Structure

```
60bef485-9942-4981-b6fe-8631607aada6/
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
