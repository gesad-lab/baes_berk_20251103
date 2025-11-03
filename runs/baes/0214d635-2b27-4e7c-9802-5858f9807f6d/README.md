# Run Summary

**Run ID**: 0214d635-2b27-4e7c-9802-5858f9807f6d
**Framework**: baes
**Started**: 2025-10-30T06:10:24.485498Z
**Completed**: 2025-10-30T06:13:14.271287Z
**Duration**: 169.79s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 26.82 |
| 2 | 2 | completed | 0/0 | 0 | 23.97 |
| 3 | 3 | completed | 0/0 | 0 | 33.98 |
| 4 | 4 | completed | 0/0 | 0 | 25.25 |
| 5 | 5 | completed | 0/0 | 0 | 29.68 |
| 6 | 6 | completed | 0/0 | 0 | 30.07 |

## Directory Structure

```
0214d635-2b27-4e7c-9802-5858f9807f6d/
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
