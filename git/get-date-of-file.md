# Get date of a file in Git

If you need the dates of a file in a Git repository, `git log` can help.

```bash
git log --follow --format=%ad --date=short -- path/to/your/file
```

## Explanation

- `--follow`: This option ensures that the history of the file is tracked even if it was renamed.
- `--format=%ad`: This specifies the format of the output, where `%ad` is the author date.
- `--date=short`: This formats the date in a short format (YYYY-MM-DD).
