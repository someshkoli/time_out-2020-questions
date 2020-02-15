test="_test"
py=".py"
zip=".zip"
python3 $1$test$py
python3 print_op.py
zip $1$zip ./input ./output -r
