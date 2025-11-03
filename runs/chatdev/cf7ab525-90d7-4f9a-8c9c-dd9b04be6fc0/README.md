# Run Summary

**Run ID**: cf7ab525-90d7-4f9a-8c9c-dd9b04be6fc0
**Framework**: chatdev
**Started**: 2025-10-30T08:02:32.151830Z
**Completed**: 2025-10-30T08:22:40.860848Z
**Duration**: 1208.71s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 233.01 |
| 2 | 2 | completed | 0/0 | 0 | 240.90 |
| 3 | 3 | completed | 0/0 | 0 | 187.68 |
| 4 | 4 | completed | 0/0 | 0 | 157.91 |
| 5 | 5 | completed | 0/0 | 0 | 191.20 |
| 6 | 6 | completed | 0/0 | 0 | 198.00 |

## Directory Structure

```
cf7ab525-90d7-4f9a-8c9c-dd9b04be6fc0/
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
