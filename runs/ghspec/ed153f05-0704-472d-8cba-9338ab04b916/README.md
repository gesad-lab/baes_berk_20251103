# Run Summary

**Run ID**: ed153f05-0704-472d-8cba-9338ab04b916
**Framework**: ghspec
**Started**: 2025-10-31T18:27:39.087481Z
**Completed**: 2025-10-31T18:47:51.694124Z
**Duration**: 1212.61s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 201.34 |
| 2 | 2 | completed | 0/0 | 0 | 214.54 |
| 3 | 3 | completed | 0/0 | 0 | 158.17 |
| 4 | 4 | completed | 0/0 | 0 | 242.73 |
| 5 | 5 | completed | 0/0 | 0 | 184.23 |
| 6 | 6 | completed | 0/0 | 0 | 211.59 |

## Directory Structure

```
ed153f05-0704-472d-8cba-9338ab04b916/
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
