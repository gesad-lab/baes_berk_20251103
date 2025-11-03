# Run Summary

**Run ID**: 73e7311d-d3de-4f1d-936a-b62320a0a272
**Framework**: chatdev
**Started**: 2025-10-30T16:40:31.413302Z
**Completed**: 2025-10-30T16:59:24.858033Z
**Duration**: 1133.44s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 169.51 |
| 2 | 2 | completed | 0/0 | 0 | 171.44 |
| 3 | 3 | completed | 0/0 | 0 | 171.11 |
| 4 | 4 | completed | 0/0 | 0 | 195.39 |
| 5 | 5 | completed | 0/0 | 0 | 212.30 |
| 6 | 6 | completed | 0/0 | 0 | 213.69 |

## Directory Structure

```
73e7311d-d3de-4f1d-936a-b62320a0a272/
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
