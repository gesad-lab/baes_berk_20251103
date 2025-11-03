# Run Summary

**Run ID**: d11f4a65-be07-4d1d-acd3-015420d33401
**Framework**: chatdev
**Started**: 2025-10-31T03:03:15.814199Z
**Completed**: 2025-10-31T03:21:07.442811Z
**Duration**: 1071.63s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 178.59 |
| 2 | 2 | completed | 0/0 | 0 | 142.19 |
| 3 | 3 | completed | 0/0 | 0 | 172.89 |
| 4 | 4 | completed | 0/0 | 0 | 174.89 |
| 5 | 5 | completed | 0/0 | 0 | 190.53 |
| 6 | 6 | completed | 0/0 | 0 | 212.53 |

## Directory Structure

```
d11f4a65-be07-4d1d-acd3-015420d33401/
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
