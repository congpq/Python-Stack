#!/usr/bin/env bash
# Date 2017-05-19
# chkconfig: 2345 10 90
# description: Start and Stop redis

--在/etc/rc.d/init.d/目录下新建redis文件,将脚本内容拷贝进去
--chkconfig --add redis   #注册服务
--chkconfig --level 345 redis on  #指定服务在3、4、5级别运行

PATH=/app/redis/src:/sbin:/usr/bin:/bin
REDISPORT=6379
EXEC=/app/redis/src/redis-server
REDIS_CLI=/app/redis/src/redis-cli

PIDFILE=/var/run/redis.pid
CONF="/app/redis/redis.conf"
AUTH="1234"
case "$1" in
        start)
                if [ -f $PIDFILE ]
                then
                        echo "$PIDFILE exists, process is already running or crashed."
                else
                        echo "Starting Redis server..."
                        $EXEC $CONF
                fi
                if [ "$?"="0" ]
                then
                        echo "Redis is running..."
                fi
                ;;
        stop)
                if [ -f $PIDFILE ]
                then
                        PID=$(cat $PIDFILE)
                        echo "Stopping..." 
                       $REDIS_CLI -p $REDISPORT  SHUTDOWN
                        sleep 2
                       while [ -x $PIDFILE ]
                       do
                                echo "Waiting for Redis to shutdown..."
                               sleep 1
                        done
                        echo "Redis stopped"
				else
                        echo "$PIDFILE exists, process is not running."		
                fi
                ;;
        restart|force-reload)
                ${0} stop
                ${0} start
                ;;
        *)
               echo "Usage: /etc/init.d/redis {start|stop|restart|force-reload}" >&2
               exit 1
esac
