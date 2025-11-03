# Run Summary

**Run ID**: 4503e38d-cd48-4abc-b926-94c39a29d962
**Framework**: chatdev
**Started**: 2025-10-29T01:37:53.001394Z
**Completed**: 2025-10-29T01:51:26.725665Z
**Duration**: 813.72s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 112.49 |
| 2 | 2 | completed | 0/0 | 0 | 113.52 |
| 3 | 3 | completed | 0/0 | 0 | 127.94 |
| 4 | 4 | completed | 0/0 | 0 | 144.60 |
| 5 | 5 | completed | 0/0 | 0 | 164.18 |
| 6 | 6 | completed | 0/0 | 0 | 150.99 |

## Directory Structure

```
4503e38d-cd48-4abc-b926-94c39a29d962/
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
