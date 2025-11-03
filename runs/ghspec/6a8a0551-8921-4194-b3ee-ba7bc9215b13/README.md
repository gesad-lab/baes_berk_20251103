# Run Summary

**Run ID**: 6a8a0551-8921-4194-b3ee-ba7bc9215b13
**Framework**: ghspec
**Started**: 2025-10-31T02:35:45.036040Z
**Completed**: 2025-10-31T02:59:20.664506Z
**Duration**: 1415.63s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 416.10 |
| 2 | 2 | completed | 0/0 | 0 | 305.89 |
| 3 | 3 | completed | 0/0 | 0 | 172.13 |
| 4 | 4 | completed | 0/0 | 0 | 155.11 |
| 5 | 5 | completed | 0/0 | 0 | 182.68 |
| 6 | 6 | completed | 0/0 | 0 | 183.70 |

## Directory Structure

```
6a8a0551-8921-4194-b3ee-ba7bc9215b13/
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
