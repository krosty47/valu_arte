echo '==============================='
echo 'Running integration Tests'
echo '==============================='
docker exec -it valu_arte python3 -W ignore -m unittest discover -v -s tests/integration -p 'test_*.py'
