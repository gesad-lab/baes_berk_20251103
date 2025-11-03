# Run Summary

**Run ID**: f22f435a-b76f-458b-86f0-198fdc839907
**Framework**: chatdev
**Started**: 2025-10-30T00:08:39.520296Z
**Completed**: 2025-10-30T00:25:49.852679Z
**Duration**: 1030.33s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 172.35 |
| 2 | 2 | completed | 0/0 | 0 | 136.74 |
| 3 | 3 | completed | 0/0 | 0 | 219.67 |
| 4 | 4 | completed | 0/0 | 0 | 184.69 |
| 5 | 5 | completed | 0/0 | 0 | 166.70 |
| 6 | 6 | completed | 0/0 | 0 | 150.18 |

## Directory Structure

```
f22f435a-b76f-458b-86f0-198fdc839907/
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
