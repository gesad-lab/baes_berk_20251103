# Run Summary

**Run ID**: 7c79c25b-37bf-46a2-a3d2-3cc1f332e1a1
**Framework**: baes
**Started**: 2025-10-30T12:11:44.645732Z
**Completed**: 2025-10-30T12:15:42.721731Z
**Duration**: 238.08s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 35.17 |
| 2 | 2 | completed | 0/0 | 0 | 59.03 |
| 3 | 3 | completed | 0/0 | 0 | 31.35 |
| 4 | 4 | completed | 0/0 | 0 | 35.16 |
| 5 | 5 | completed | 0/0 | 0 | 36.85 |
| 6 | 6 | completed | 0/0 | 0 | 40.50 |

## Directory Structure

```
7c79c25b-37bf-46a2-a3d2-3cc1f332e1a1/
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
