for i in {1..20}
do
    sed -i 's/created/updated/g' linkvalue$i.sql
    # echo "linkvalue"$i
done