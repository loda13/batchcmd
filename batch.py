import paramiko

f = open('iplist')
l = open('sh')
cmd = l.read()

for i in f.read().splitlines():
    print(i)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=i, port=22, username='root', password='iflytek!ty')
    stdin, stdout, stderr = ssh.exec_command(cmd)
    result = stdout.read()
    if not result:
        result = stderr.read()
    ssh.close()
    print(result.decode())

f.close()
l.close()
