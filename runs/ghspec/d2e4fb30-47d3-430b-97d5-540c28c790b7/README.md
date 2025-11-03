# Run Summary

**Run ID**: d2e4fb30-47d3-430b-97d5-540c28c790b7
**Framework**: ghspec
**Started**: 2025-10-30T14:02:47.439176Z
**Completed**: 2025-10-30T14:20:35.831213Z
**Duration**: 1068.39s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 164.19 |
| 2 | 2 | completed | 0/0 | 0 | 214.87 |
| 3 | 3 | completed | 0/0 | 0 | 247.23 |
| 4 | 4 | completed | 0/0 | 0 | 129.87 |
| 5 | 5 | completed | 0/0 | 0 | 130.79 |
| 6 | 6 | completed | 0/0 | 0 | 181.44 |

## Directory Structure

```
d2e4fb30-47d3-430b-97d5-540c28c790b7/
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
