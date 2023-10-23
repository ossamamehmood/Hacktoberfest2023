#!/bin/bash

HOST=127.0.0.1
PORT=3306

nc -z ${HOST} ${PORT}
if [ $? -eq 0 ]
then
    echo "Initiated the connection with the datbase"
else
    echo "pscale not connected !"
fi

usql 'mysql://root@127.0.0.1:3306/link-shortner'
