# Run Summary

**Run ID**: a9b902c1-41e4-4a90-8f67-cd76de6caf60
**Framework**: chatdev
**Started**: 2025-10-31T17:20:37.635729Z
**Completed**: 2025-10-31T17:39:13.462578Z
**Duration**: 1115.83s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 163.41 |
| 2 | 2 | completed | 0/0 | 0 | 134.88 |
| 3 | 3 | completed | 0/0 | 0 | 156.25 |
| 4 | 4 | completed | 0/0 | 0 | 162.04 |
| 5 | 5 | completed | 0/0 | 0 | 197.24 |
| 6 | 6 | completed | 0/0 | 0 | 302.00 |

## Directory Structure

```
a9b902c1-41e4-4a90-8f67-cd76de6caf60/
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
