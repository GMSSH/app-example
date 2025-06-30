#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

Install() {
    # do-something
    echo 'Successify'
}

Uninstall() {
     do-something
}

CleanData() {
     do-something
}

action=$1
clean_data=$2
if [ "$action" == 'install' ]; then
    Install
else
    Uninstall
    if [ "$clean_data" == 'true' ]; then
        CleanData
    fi
fi