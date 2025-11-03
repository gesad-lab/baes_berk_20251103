# Run Summary

**Run ID**: 125bcb99-d16e-4c4f-a0df-ce6ee8397e2f
**Framework**: chatdev
**Started**: 2025-10-31T05:06:34.503204Z
**Completed**: 2025-10-31T05:12:06.008806Z
**Duration**: 331.51s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 328.01 |
| 2 | 2 | completed | 0/0 | 0 | 0.71 |
| 3 | 3 | completed | 0/0 | 0 | 0.69 |
| 4 | 4 | completed | 0/0 | 0 | 0.69 |
| 5 | 5 | completed | 0/0 | 0 | 0.69 |
| 6 | 6 | completed | 0/0 | 0 | 0.70 |

## Directory Structure

```
125bcb99-d16e-4c4f-a0df-ce6ee8397e2f/
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
