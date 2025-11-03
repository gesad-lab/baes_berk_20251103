# Run Summary

**Run ID**: 8771311d-ea1f-4f91-8bcd-04393ac9bf32
**Framework**: baes
**Started**: 2025-10-28T16:12:02.657558Z
**Completed**: 2025-10-28T16:16:42.740362Z
**Duration**: 280.08s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 56.11 |
| 2 | 2 | completed | 0/0 | 0 | 25.19 |
| 3 | 3 | completed | 0/0 | 0 | 56.18 |
| 4 | 4 | completed | 0/0 | 0 | 29.06 |
| 5 | 5 | completed | 0/0 | 0 | 45.66 |
| 6 | 6 | completed | 0/0 | 0 | 67.87 |

## Directory Structure

```
8771311d-ea1f-4f91-8bcd-04393ac9bf32/
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
