# Run Summary

**Run ID**: c5bb7fe4-4ad2-4476-b720-b357eb5a74ee
**Framework**: ghspec
**Started**: 2025-10-29T14:59:00.356589Z
**Completed**: 2025-10-29T15:22:02.956674Z
**Duration**: 1382.60s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 219.57 |
| 2 | 2 | completed | 0/0 | 0 | 315.87 |
| 3 | 3 | completed | 0/0 | 0 | 236.15 |
| 4 | 4 | completed | 0/0 | 0 | 209.16 |
| 5 | 5 | completed | 0/0 | 0 | 181.68 |
| 6 | 6 | completed | 0/0 | 0 | 220.16 |

## Directory Structure

```
c5bb7fe4-4ad2-4476-b720-b357eb5a74ee/
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
