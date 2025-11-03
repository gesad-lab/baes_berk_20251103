# Run Summary

**Run ID**: b88c3ef5-6288-44c7-9b10-656b54681dd7
**Framework**: chatdev
**Started**: 2025-10-29T19:16:35.948313Z
**Completed**: 2025-10-29T19:33:44.403879Z
**Duration**: 1028.46s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 174.04 |
| 2 | 2 | completed | 0/0 | 0 | 189.95 |
| 3 | 3 | completed | 0/0 | 0 | 146.12 |
| 4 | 4 | completed | 0/0 | 0 | 180.44 |
| 5 | 5 | completed | 0/0 | 0 | 160.70 |
| 6 | 6 | completed | 0/0 | 0 | 177.20 |

## Directory Structure

```
b88c3ef5-6288-44c7-9b10-656b54681dd7/
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
