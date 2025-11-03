# Run Summary

**Run ID**: 72c042f0-f3b3-4f7c-9b7c-52c70f2acf3d
**Framework**: baes
**Started**: 2025-10-31T04:21:23.181461Z
**Completed**: 2025-10-31T04:27:27.675294Z
**Duration**: 364.49s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 63.03 |
| 2 | 2 | completed | 0/0 | 0 | 59.68 |
| 3 | 3 | completed | 0/0 | 0 | 60.10 |
| 4 | 4 | completed | 0/0 | 0 | 63.37 |
| 5 | 5 | completed | 0/0 | 0 | 62.04 |
| 6 | 6 | completed | 0/0 | 0 | 56.27 |

## Directory Structure

```
72c042f0-f3b3-4f7c-9b7c-52c70f2acf3d/
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
