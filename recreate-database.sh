echo -e "\n\tPrepared to replace example\n"
read -p "Continue? (yes/no): " REPLACE
if [ "$REPLACE" == "yes" ] || [ "$REPLACE" == "Yes" ] || [ "$REPLACE" == "YES" ]; then
echo -n "Deleting example .. "
curl -X DELETE http://localhost:5984/example
echo
echo -n "Creating example .. "
curl -X PUT http://localhost:5984/example
echo
./setup-app.sh
echo 'Populating Categories'
./populate_categories.sh example -v
echo
fi

