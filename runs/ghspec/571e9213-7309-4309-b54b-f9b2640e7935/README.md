# Run Summary

**Run ID**: 571e9213-7309-4309-b54b-f9b2640e7935
**Framework**: ghspec
**Started**: 2025-10-31T15:14:49.677705Z
**Completed**: 2025-10-31T15:34:00.055610Z
**Duration**: 1150.38s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 149.31 |
| 2 | 2 | completed | 0/0 | 0 | 289.26 |
| 3 | 3 | completed | 0/0 | 0 | 206.73 |
| 4 | 4 | completed | 0/0 | 0 | 190.49 |
| 5 | 5 | completed | 0/0 | 0 | 145.71 |
| 6 | 6 | completed | 0/0 | 0 | 168.87 |

## Directory Structure

```
571e9213-7309-4309-b54b-f9b2640e7935/
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
