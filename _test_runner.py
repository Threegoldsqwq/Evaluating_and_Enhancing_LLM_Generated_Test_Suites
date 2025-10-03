# _test_runner.py
import os, sys, types, json, unittest, pathlib, builtins, importlib.util

CANDIDATE_FILE = os.environ.get("CANDIDATE_FILE")
TEST_FILE = os.environ.get("TEST_FILE")
ENTRY_POINT = os.environ.get("ENTRY_POINT")

def die(msg, code=2):
    print(json.dumps({"error": msg}))
    sys.exit(code)

if not CANDIDATE_FILE or not TEST_FILE:
    die("missing env CANDIDATE_FILE/TEST_FILE")

# 1) Load canonical solution module as "candidate"
sol_path = pathlib.Path(CANDIDATE_FILE)
code = sol_path.read_text(encoding="utf-8")
candidate_mod = types.ModuleType("candidate")
exec(compile(code, str(sol_path), "exec"), candidate_mod.__dict__)
sys.modules["candidate"] = candidate_mod

# 2) Put symbol in builtins (safety net)
if ENTRY_POINT and hasattr(candidate_mod, ENTRY_POINT):
    setattr(builtins, ENTRY_POINT, getattr(candidate_mod, ENTRY_POINT))

# 3) Load the specific test file as a module so we can inject into its globals
test_path = pathlib.Path(TEST_FILE)
spec = importlib.util.spec_from_file_location("test_generated", str(test_path))
if spec is None or spec.loader is None:
    die(f"cannot load {TEST_FILE}")
test_mod = importlib.util.module_from_spec(spec)

# Inject the entry point into the test module globals BEFORE executing it
if ENTRY_POINT and hasattr(candidate_mod, ENTRY_POINT):
    test_mod.__dict__[ENTRY_POINT] = getattr(candidate_mod, ENTRY_POINT)

sys.modules["test_generated"] = test_mod
spec.loader.exec_module(test_mod)  # executes the test file

# 4) Build suite from that module and run
suite = unittest.defaultTestLoader.loadTestsFromModule(test_mod)
result = unittest.TextTestRunner(verbosity=0).run(suite)

out = {
    "testsRun": result.testsRun,
    "failures": len(result.failures),
    "errors": len(result.errors),
    "passed": result.testsRun - len(result.failures) - len(result.errors),
}
print(json.dumps(out))

if result.failures or result.errors:
    sys.exit(1)
