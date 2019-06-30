killall python
rm -rf result*.txt
rm -rf log-*.txt
python ../program.py config-A.txt result-A.txt >& log-A.txt &
python ../program.py config-B.txt result-B.txt >& log-B.txt &
