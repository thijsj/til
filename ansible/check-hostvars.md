# Check hostvars

Variables in Ansible are created in different files on different levels. They can be set on a host basis or on a group basis. Host can also be in multiple groups. If you get lost on what is the actual value of a variable, you check using the following command:

```bash
ansible -m debug -a "var=variable_name" host_name
```

or for hostvars:

```bash
ansible -m debug -a "var=hostvars['host_name'].get('variable_name')" <host_reference>
```
