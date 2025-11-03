# Run Summary

**Run ID**: a3c21fb7-5f61-4143-b00a-4bffec954ac2
**Framework**: baes
**Started**: 2025-10-29T19:53:26.809063Z
**Completed**: 2025-10-29T19:56:25.404287Z
**Duration**: 178.60s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 25.30 |
| 2 | 2 | completed | 0/0 | 0 | 38.23 |
| 3 | 3 | completed | 0/0 | 0 | 28.24 |
| 4 | 4 | completed | 0/0 | 0 | 21.67 |
| 5 | 5 | completed | 0/0 | 0 | 30.83 |
| 6 | 6 | completed | 0/0 | 0 | 34.32 |

## Directory Structure

```
a3c21fb7-5f61-4143-b00a-4bffec954ac2/
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
