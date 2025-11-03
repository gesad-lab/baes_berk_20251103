# Run Summary

**Run ID**: c8f72b41-44ec-4cd3-9d45-bf96b8d11fcc
**Framework**: chatdev
**Started**: 2025-10-28T14:43:53.705534Z
**Completed**: 2025-10-28T15:04:59.097509Z
**Duration**: 1265.39s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 195.95 |
| 2 | 2 | completed | 0/0 | 0 | 153.62 |
| 3 | 3 | completed | 0/0 | 0 | 161.66 |
| 4 | 4 | completed | 0/0 | 0 | 215.80 |
| 5 | 5 | completed | 0/0 | 0 | 265.89 |
| 6 | 6 | completed | 0/0 | 0 | 272.47 |

## Directory Structure

```
c8f72b41-44ec-4cd3-9d45-bf96b8d11fcc/
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
