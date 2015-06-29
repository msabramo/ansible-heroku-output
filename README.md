# ansible-heroku-output

adapted from https://gist.github.com/cliffano/9868180

## Example

```
$ ansible-playbook foo.yml
...
PLAY [profilesvc] *************************************************************

GATHERING FACTS ***************************************************************
fatal: [host5] => SSH Error: data could not be sent to the remote host. Make sure this host can be reached over ssh
-----> ERROR: host5 was unreachable
       SSH Error: data could not be sent to the remote host. Make sure this host can be reached over ssh
ok: [host4]
ok: [host3]
ok: [host1]
ok: [host2]

TASK: [shell date] ************************************************************
changed: [host1]
-----> host1 [|] date [|] stdout
       Mon Jun 29 16:24:04 PDT 2015
changed: [host3]
-----> host3 [|] date [|] stdout
       Mon Jun 29 16:24:04 PDT 2015
changed: [host2]
-----> host2 [|] date [|] stdout
       Mon Jun 29 23:24:05 UTC 2015
changed: [host4]
-----> host4 [|] date [|] stdout
       Mon Jun 29 16:24:05 PDT 2015
```

## License

MIT
