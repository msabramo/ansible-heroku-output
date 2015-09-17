#!/usr/bin/env bats

@test "Test playbook with ASCII" {
  run ansible-playbook -i localhost, --connection=local test/playbooks/echo_ascii.yml
  [ "$status" -eq 0 ]
  [[ "$output" = *"-----> localhost [|] echo \"This is plain old ASCII\" [|] stdout"* ]]
  [[ "$output" = *"       This is plain old ASCII"* ]]
}
