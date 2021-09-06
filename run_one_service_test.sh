echo '==============================='
echo 'Running unit Tests...'
echo '==============================='
docker exec -it valu_arte python3 -W ignore -m unittest discover --quiet -s tests/unit/service -p $1
