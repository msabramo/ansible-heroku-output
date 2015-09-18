# adapted from https://gist.github.com/cliffano/9868180

import os

FIELDS = os.environ.get('ANSIBLE_HUMAN_LOG_FIELDS')
if FIELDS:
    FIELDS = FIELDS.split(',')
if not FIELDS:
    FIELDS = ['stdout', 'stderr']


def human_log(callback, host, res):
    if hasattr(res, 'startswith'):
        if callback == 'runner_on_unreachable':
            print('-----> ERROR: {host} was unreachable'.format(host=host))
        print(u"\n".join([
            u"       %s" % line for line in res.splitlines()]).encode("utf-8"))
    elif type(res) == type(dict()):
        for field in FIELDS:
            if field in res.keys():
                lines = res[field].splitlines()
                if not lines:
                    continue

                if 'cmd' in res.keys():
                    print(u'-----> {host} [|] {cmd} [|] {field}'.format(
                        host=host,
                        cmd=res['cmd'],
                        field=field).encode("utf-8"))
                elif 'invocation' in res.keys():
                    print('-----> {host} [|] {module_args} [|] {field}'.format(
                        host=host,
                        module_args=res['invocation']['module_args'],
                        field=field))
                else:
                    print('-----> {host} [|] {field}'.format(
                        host=host, field=field))

                print(u"\n".join([
                    u"       %s" % line for line in lines]).encode("utf-8"))


class CallbackModule(object):

    def on_any(self, *args, **kwargs):
        pass

    def runner_on_failed(self, host, res, ignore_errors=False):
        human_log('runner_on_failed', host, res)

    def runner_on_ok(self, host, res):
        human_log('runner_on_ok', host, res)

    def runner_on_error(self, host, msg):
        pass

    def runner_on_skipped(self, host, item=None):
        pass

    def runner_on_unreachable(self, host, res):
        human_log('runner_on_unreachable', host, res)

    def runner_on_no_hosts(self):
        pass

    def runner_on_async_poll(self, host, res, jid, clock):
        human_log('runner_on_async_poll', host, res)

    def runner_on_async_ok(self, host, res, jid):
        human_log('runner_on_async_ok', host, res)

    def runner_on_async_failed(self, host, res, jid):
        human_log('runner_on_async_failed', host, res)

    def playbook_on_start(self):
        pass

    def playbook_on_notify(self, host, handler):
        pass

    def playbook_on_no_hosts_matched(self):
        pass

    def playbook_on_no_hosts_remaining(self):
        pass

    def playbook_on_task_start(self, name, is_conditional):
        pass

    def playbook_on_vars_prompt(
            self, varname, private=True, prompt=None,
            encrypt=None, confirm=False, salt_size=None, salt=None,
            default=None):
        pass

    def playbook_on_setup(self):
        pass

    def playbook_on_import_for_host(self, host, imported_file):
        pass

    def playbook_on_not_import_for_host(self, host, missing_file):
        pass

    def playbook_on_play_start(self, pattern):
        pass

    def playbook_on_stats(self, stats):
        pass
