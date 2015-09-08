#!/usr/bin/env bats

@test "Test playbook with ASCII" {
  run ansible-playbook -i localhost, test/playbooks/echo_ascii.yml
}
