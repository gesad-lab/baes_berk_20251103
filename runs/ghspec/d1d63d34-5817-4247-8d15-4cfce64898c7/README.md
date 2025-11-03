# Run Summary

**Run ID**: d1d63d34-5817-4247-8d15-4cfce64898c7
**Framework**: ghspec
**Started**: 2025-10-31T16:04:35.518795Z
**Completed**: 2025-10-31T16:26:11.805832Z
**Duration**: 1296.29s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 238.96 |
| 2 | 2 | completed | 0/0 | 0 | 180.34 |
| 3 | 3 | completed | 0/0 | 0 | 294.20 |
| 4 | 4 | completed | 0/0 | 0 | 247.04 |
| 5 | 5 | completed | 0/0 | 0 | 196.24 |
| 6 | 6 | completed | 0/0 | 0 | 139.50 |

## Directory Structure

```
d1d63d34-5817-4247-8d15-4cfce64898c7/
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
