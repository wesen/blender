# print this systems IP, use for logs
/sbin/ifconfig  | grep 'inet addr:'| grep -v '127.0.0.1' | cut -d: -f2 | head -n 1 | awk '{ print $1}'
