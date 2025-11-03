# Run Summary

**Run ID**: 58ce6b58-4a03-4e23-9e94-18327d2ef4fa
**Framework**: chatdev
**Started**: 2025-10-28T19:59:28.328338Z
**Completed**: 2025-10-28T20:27:12.722588Z
**Duration**: 1664.39s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 265.30 |
| 2 | 2 | completed | 0/0 | 0 | 233.10 |
| 3 | 3 | completed | 0/0 | 0 | 246.98 |
| 4 | 4 | completed | 0/0 | 0 | 280.92 |
| 5 | 5 | completed | 0/0 | 0 | 314.56 |
| 6 | 6 | completed | 0/0 | 0 | 323.53 |

## Directory Structure

```
58ce6b58-4a03-4e23-9e94-18327d2ef4fa/
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
