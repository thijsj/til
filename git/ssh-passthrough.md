# SSH passthrough to other vm

The idea for this quest was to have a VM containing my git repositories accessible via SSH from another VM. The git VM can only be accessed from our VPN which is fine in most cases. But I want git to be accessible for users outside of the VPN as well. The solution is to have a VM that is accessible from the outside and then have it forward SSH connections to the git VM.

## SSH Passthrough

At the accessible VM, I've created a `git` user with `/bin/sh` as the shell. The `.ssh/authorized_keys` file for this user contains the public keys of the users who should have access to the git VM. The command in the `authorized_keys` file looks like this:

```bash
command="ssh -T git@<git-vm-ip> $SSH_ORIGINAL_COMMAND" ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC...
```
