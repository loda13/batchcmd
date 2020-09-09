docker ps --format "table {{.Names}}\t{{.Command}}" --no-trunc|awk '{print $1,$5,$6}'|grep -v NAMES
free -g|grep Mem
