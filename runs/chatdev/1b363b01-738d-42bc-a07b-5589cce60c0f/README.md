# Run Summary

**Run ID**: 1b363b01-738d-42bc-a07b-5589cce60c0f
**Framework**: chatdev
**Started**: 2025-10-28T21:43:55.965371Z
**Completed**: 2025-10-28T22:07:56.491398Z
**Duration**: 1440.53s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 196.03 |
| 2 | 2 | completed | 0/0 | 0 | 223.12 |
| 3 | 3 | completed | 0/0 | 0 | 228.89 |
| 4 | 4 | completed | 0/0 | 0 | 277.03 |
| 5 | 5 | completed | 0/0 | 0 | 255.38 |
| 6 | 6 | completed | 0/0 | 0 | 260.06 |

## Directory Structure

```
1b363b01-738d-42bc-a07b-5589cce60c0f/
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
