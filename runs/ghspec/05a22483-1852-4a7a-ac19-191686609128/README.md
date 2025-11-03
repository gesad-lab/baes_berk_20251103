# Run Summary

**Run ID**: 05a22483-1852-4a7a-ac19-191686609128
**Framework**: ghspec
**Started**: 2025-10-30T23:46:54.643907Z
**Completed**: 2025-10-31T00:06:28.677674Z
**Duration**: 1174.03s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 181.09 |
| 2 | 2 | completed | 0/0 | 0 | 143.34 |
| 3 | 3 | completed | 0/0 | 0 | 174.15 |
| 4 | 4 | completed | 0/0 | 0 | 262.12 |
| 5 | 5 | completed | 0/0 | 0 | 197.30 |
| 6 | 6 | completed | 0/0 | 0 | 216.02 |

## Directory Structure

```
05a22483-1852-4a7a-ac19-191686609128/
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
