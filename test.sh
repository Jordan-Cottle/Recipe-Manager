pushd recipe-manager
export PYTHONPATH="${PYTHONPATH};$(pwd)"
popd

pytest --cov
passed=$?

if [[ $passed != 0 ]]; then
    echo "Tests failed to meet acceptance criteria!"
fi

exit $passed
