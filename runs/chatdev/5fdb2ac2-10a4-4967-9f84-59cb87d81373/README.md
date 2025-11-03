# Run Summary

**Run ID**: 5fdb2ac2-10a4-4967-9f84-59cb87d81373
**Framework**: chatdev
**Started**: 2025-10-28T19:16:21.960307Z
**Completed**: 2025-10-28T19:39:43.236986Z
**Duration**: 1401.28s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 172.01 |
| 2 | 2 | completed | 0/0 | 0 | 182.85 |
| 3 | 3 | completed | 0/0 | 0 | 241.53 |
| 4 | 4 | completed | 0/0 | 0 | 268.59 |
| 5 | 5 | completed | 0/0 | 0 | 262.89 |
| 6 | 6 | completed | 0/0 | 0 | 273.41 |

## Directory Structure

```
5fdb2ac2-10a4-4967-9f84-59cb87d81373/
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
