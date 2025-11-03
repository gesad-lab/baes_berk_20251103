# Run Summary

**Run ID**: 47d18567-d148-48b2-82c9-d6b35cadcb8d
**Framework**: ghspec
**Started**: 2025-10-29T01:51:28.514606Z
**Completed**: 2025-10-29T02:01:50.072701Z
**Duration**: 621.56s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 88.54 |
| 2 | 2 | completed | 0/0 | 0 | 89.42 |
| 3 | 3 | completed | 0/0 | 0 | 78.29 |
| 4 | 4 | completed | 0/0 | 0 | 148.57 |
| 5 | 5 | completed | 0/0 | 0 | 109.00 |
| 6 | 6 | completed | 0/0 | 0 | 107.72 |

## Directory Structure

```
47d18567-d148-48b2-82c9-d6b35cadcb8d/
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
