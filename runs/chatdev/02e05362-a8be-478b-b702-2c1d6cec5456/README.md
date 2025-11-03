# Run Summary

**Run ID**: 02e05362-a8be-478b-b702-2c1d6cec5456
**Framework**: chatdev
**Started**: 2025-10-28T10:21:53.686830Z
**Completed**: 2025-10-28T10:56:09.541364Z
**Duration**: 2055.85s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 266.82 |
| 2 | 2 | completed | 0/0 | 0 | 258.96 |
| 3 | 3 | completed | 0/0 | 0 | 351.95 |
| 4 | 4 | completed | 0/0 | 0 | 339.21 |
| 5 | 5 | completed | 0/0 | 0 | 405.32 |
| 6 | 6 | completed | 0/0 | 0 | 433.59 |

## Directory Structure

```
02e05362-a8be-478b-b702-2c1d6cec5456/
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
