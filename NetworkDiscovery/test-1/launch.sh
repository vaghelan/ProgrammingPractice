killall python
rm -rf result*.txt
rm -rf log-*.txt
python ../program.py config-A.txt result-A.txt >& log-A.txt &
#sleep 1
python ../program.py config-B.txt result-B.txt >& log-B.txt &
#sleep 1
python ../program.py config-C.txt result-C.txt >& log-C.txt &
#sleep 1
python ../program.py config-D.txt result-D.txt >& log-D.txt &
#sleep 1
python ../program.py config-E.txt result-E.txt >& log-E.txt &
