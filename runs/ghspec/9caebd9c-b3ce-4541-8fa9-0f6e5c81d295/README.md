# Run Summary

**Run ID**: 9caebd9c-b3ce-4541-8fa9-0f6e5c81d295
**Framework**: ghspec
**Started**: 2025-10-29T12:20:13.558031Z
**Completed**: 2025-10-29T12:39:06.513712Z
**Duration**: 1132.96s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 161.14 |
| 2 | 2 | completed | 0/0 | 0 | 222.87 |
| 3 | 3 | completed | 0/0 | 0 | 215.74 |
| 4 | 4 | completed | 0/0 | 0 | 189.59 |
| 5 | 5 | completed | 0/0 | 0 | 176.19 |
| 6 | 6 | completed | 0/0 | 0 | 167.43 |

## Directory Structure

```
9caebd9c-b3ce-4541-8fa9-0f6e5c81d295/
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
