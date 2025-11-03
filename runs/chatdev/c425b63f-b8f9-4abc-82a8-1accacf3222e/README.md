# Run Summary

**Run ID**: c425b63f-b8f9-4abc-82a8-1accacf3222e
**Framework**: chatdev
**Started**: 2025-10-31T12:07:13.035256Z
**Completed**: 2025-10-31T12:23:55.193595Z
**Duration**: 1002.16s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 198.59 |
| 2 | 2 | completed | 0/0 | 0 | 138.92 |
| 3 | 3 | completed | 0/0 | 0 | 151.27 |
| 4 | 4 | completed | 0/0 | 0 | 146.09 |
| 5 | 5 | completed | 0/0 | 0 | 181.46 |
| 6 | 6 | completed | 0/0 | 0 | 185.83 |

## Directory Structure

```
c425b63f-b8f9-4abc-82a8-1accacf3222e/
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
