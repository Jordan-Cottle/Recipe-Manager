pushd recipe-manager
export PYTHONPATH="${PYTHONPATH};$(pwd)"
popd

pytest tests

