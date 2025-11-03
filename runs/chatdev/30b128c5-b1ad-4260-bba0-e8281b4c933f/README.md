# Run Summary

**Run ID**: 30b128c5-b1ad-4260-bba0-e8281b4c933f
**Framework**: chatdev
**Started**: 2025-10-30T03:58:45.621956Z
**Completed**: 2025-10-30T04:25:24.384177Z
**Duration**: 1598.76s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 274.26 |
| 2 | 2 | completed | 0/0 | 0 | 407.77 |
| 3 | 3 | completed | 0/0 | 0 | 175.57 |
| 4 | 4 | completed | 0/0 | 0 | 174.49 |
| 5 | 5 | completed | 0/0 | 0 | 203.15 |
| 6 | 6 | completed | 0/0 | 0 | 363.52 |

## Directory Structure

```
30b128c5-b1ad-4260-bba0-e8281b4c933f/
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
