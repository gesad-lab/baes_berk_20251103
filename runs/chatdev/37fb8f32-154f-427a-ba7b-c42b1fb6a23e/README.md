# Run Summary

**Run ID**: 37fb8f32-154f-427a-ba7b-c42b1fb6a23e
**Framework**: chatdev
**Started**: 2025-10-31T04:14:32.960800Z
**Completed**: 2025-10-31T04:20:04.598708Z
**Duration**: 331.64s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 328.15 |
| 2 | 2 | completed | 0/0 | 0 | 0.69 |
| 3 | 3 | completed | 0/0 | 0 | 0.69 |
| 4 | 4 | completed | 0/0 | 0 | 0.70 |
| 5 | 5 | completed | 0/0 | 0 | 0.69 |
| 6 | 6 | completed | 0/0 | 0 | 0.70 |

## Directory Structure

```
37fb8f32-154f-427a-ba7b-c42b1fb6a23e/
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
