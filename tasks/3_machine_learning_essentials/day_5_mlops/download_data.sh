filename="accepted_2007_to_2018Q4.csv.gz "
kaggle datasets download "wordsforthewise/lending-club" -f $filename --force
mv $filename $1
