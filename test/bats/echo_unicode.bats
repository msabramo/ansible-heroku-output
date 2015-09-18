#!/usr/bin/env bats

@test "Test playbook with Unicode" {
  run ansible-playbook -i localhost, --connection=local test/playbooks/echo_unicode.yml
  [ "$status" -eq 0 ]
  [[ "$output" = *"-----> localhost [|] echo \"测试\" [|] stdout"* ]]
  [[ "$output" = *"       测试"* ]]
}
