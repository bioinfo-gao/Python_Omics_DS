#!/bin/bash
grep "\bbash\b" /etc/passwd
RETVAL=$?
if [ $RETVAL -eq 0 ]
then
    USERS=`grep "\<bash$" /etc/passwd | wc -l`
    echo "There are $USERS with bash"
else
    echo "No such users"
fi

