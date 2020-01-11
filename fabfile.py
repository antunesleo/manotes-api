from fabric import Connection

result = Connection(
   host='0.0.0.0',
   user='leonardo',
   connect_kwargs={'key_filename': '/home/antunesleo/.ssh/id_rsa'}
).run('ls -alt')
print(result)
