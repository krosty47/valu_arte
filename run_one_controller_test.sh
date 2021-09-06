clear
echo '==============================='
echo 'Running unit Tests...'
echo '==============================='
docker exec -it valu_arte python3 -W ignore -m unittest discover -v -s tests/unit/controller -p $1
