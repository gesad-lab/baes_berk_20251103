# Run Summary

**Run ID**: eac8f63c-a67b-45fa-ad8a-79d46a6e8c85
**Framework**: ghspec
**Started**: 2025-10-31T11:15:16.982067Z
**Completed**: 2025-10-31T11:28:19.260436Z
**Duration**: 782.28s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 125.18 |
| 2 | 2 | completed | 0/0 | 0 | 112.58 |
| 3 | 3 | completed | 0/0 | 0 | 220.11 |
| 4 | 4 | completed | 0/0 | 0 | 118.15 |
| 5 | 5 | completed | 0/0 | 0 | 109.14 |
| 6 | 6 | completed | 0/0 | 0 | 97.11 |

## Directory Structure

```
eac8f63c-a67b-45fa-ad8a-79d46a6e8c85/
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
