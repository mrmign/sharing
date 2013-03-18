#!/bin/bash

#create the tables
mysql -uroot -proot share < database.sql

#import user data
mysql -uroot -proot share < user.sql

#import group data 
mysql -uroot -proot share < group.sql

#update group link count
mysql -uroot -proot share < linkCount.sql

#import links data
for i in {1..20}
do
    mysql -uroot -proot share < linkvalue$i.sql
    # echo "linkvalue"$i
done