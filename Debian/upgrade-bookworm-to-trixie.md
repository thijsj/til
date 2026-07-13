# Upgrade Debian Bookworm to Trixie

1. Change apt sources. 
```grep -Rl 'bookworm' /etc/apt/* | xargs sed -i 's/bookworm/trixie/g'```

2. Use `apt update` to refresh the package lists.

3. Upgrade the system with `apt full-upgrade`.

## Insights
I tried using `aptitude dist-upgrade` but it finds too many conflicts and doesn't want to upgrade. Using `apt full-upgrade` worked fine.
