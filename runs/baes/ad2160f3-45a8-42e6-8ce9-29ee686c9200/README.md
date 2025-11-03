# Run Summary

**Run ID**: ad2160f3-45a8-42e6-8ce9-29ee686c9200
**Framework**: baes
**Started**: 2025-10-30T16:36:56.261298Z
**Completed**: 2025-10-30T16:40:26.363383Z
**Duration**: 210.10s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 30.86 |
| 2 | 2 | completed | 0/0 | 0 | 26.78 |
| 3 | 3 | completed | 0/0 | 0 | 37.92 |
| 4 | 4 | completed | 0/0 | 0 | 33.90 |
| 5 | 5 | completed | 0/0 | 0 | 42.18 |
| 6 | 6 | completed | 0/0 | 0 | 38.45 |

## Directory Structure

```
ad2160f3-45a8-42e6-8ce9-29ee686c9200/
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
