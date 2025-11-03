# Run Summary

**Run ID**: e290f58a-e8b6-4643-b605-d256980a159d
**Framework**: chatdev
**Started**: 2025-10-29T03:07:41.139655Z
**Completed**: 2025-10-29T03:17:41.432811Z
**Duration**: 600.29s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 102.81 |
| 2 | 2 | completed | 0/0 | 0 | 96.58 |
| 3 | 3 | completed | 0/0 | 0 | 86.10 |
| 4 | 4 | completed | 0/0 | 0 | 95.34 |
| 5 | 5 | completed | 0/0 | 0 | 113.64 |
| 6 | 6 | completed | 0/0 | 0 | 105.80 |

## Directory Structure

```
e290f58a-e8b6-4643-b605-d256980a159d/
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
