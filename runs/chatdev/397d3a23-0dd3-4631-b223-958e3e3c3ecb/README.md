# Run Summary

**Run ID**: 397d3a23-0dd3-4631-b223-958e3e3c3ecb
**Framework**: chatdev
**Started**: 2025-10-29T08:00:01.327448Z
**Completed**: 2025-10-29T08:21:34.841196Z
**Duration**: 1293.51s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 215.24 |
| 2 | 2 | completed | 0/0 | 0 | 160.03 |
| 3 | 3 | completed | 0/0 | 0 | 237.83 |
| 4 | 4 | completed | 0/0 | 0 | 250.99 |
| 5 | 5 | completed | 0/0 | 0 | 208.10 |
| 6 | 6 | completed | 0/0 | 0 | 221.32 |

## Directory Structure

```
397d3a23-0dd3-4631-b223-958e3e3c3ecb/
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
