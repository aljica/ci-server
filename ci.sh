cd builds

echo "Cloning..."
git clone "https://${GITHUB_TOKEN}@github.com/${1}.git" $2
cd $2

echo "Checkout to commit"
git checkout $2

echo "Check syntax ..."
make lint

echo "Testing..."
make test