# Run Summary

**Run ID**: 1be13722-80fb-40fb-90b3-7e076d4fb588
**Framework**: ghspec
**Started**: 2025-10-29T18:04:44.184265Z
**Completed**: 2025-10-29T18:26:03.814234Z
**Duration**: 1279.63s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 189.65 |
| 2 | 2 | completed | 0/0 | 0 | 172.57 |
| 3 | 3 | completed | 0/0 | 0 | 310.41 |
| 4 | 4 | completed | 0/0 | 0 | 232.81 |
| 5 | 5 | completed | 0/0 | 0 | 175.70 |
| 6 | 6 | completed | 0/0 | 0 | 198.48 |

## Directory Structure

```
1be13722-80fb-40fb-90b3-7e076d4fb588/
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
