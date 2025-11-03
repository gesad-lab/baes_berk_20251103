# Run Summary

**Run ID**: 8320a6f7-ae09-425e-b1a1-6781aec12eab
**Framework**: chatdev
**Started**: 2025-10-28T13:55:02.549657Z
**Completed**: 2025-10-28T14:17:18.351780Z
**Duration**: 1335.80s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 238.15 |
| 2 | 2 | completed | 0/0 | 0 | 256.94 |
| 3 | 3 | completed | 0/0 | 0 | 198.11 |
| 4 | 4 | completed | 0/0 | 0 | 205.23 |
| 5 | 5 | completed | 0/0 | 0 | 207.37 |
| 6 | 6 | completed | 0/0 | 0 | 230.00 |

## Directory Structure

```
8320a6f7-ae09-425e-b1a1-6781aec12eab/
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
