# Run Summary

**Run ID**: 0da2a226-d594-4056-8a28-4710c3988192
**Framework**: ghspec
**Started**: 2025-10-31T08:54:12.746955Z
**Completed**: 2025-10-31T09:11:34.699093Z
**Duration**: 1041.95s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 168.90 |
| 2 | 2 | completed | 0/0 | 0 | 190.77 |
| 3 | 3 | completed | 0/0 | 0 | 152.01 |
| 4 | 4 | completed | 0/0 | 0 | 167.16 |
| 5 | 5 | completed | 0/0 | 0 | 199.72 |
| 6 | 6 | completed | 0/0 | 0 | 163.39 |

## Directory Structure

```
0da2a226-d594-4056-8a28-4710c3988192/
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
