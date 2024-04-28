const output = document.getElementById("output");

const editor = CodeMirror.fromTextArea(document.getElementById("code"), {
    mode: {
        name: "python",
        version: 3,
        singleLineStringErrors: false
    },
    theme: "shadowfox",
    indentUnit: 4,
    matchBrackets: true
});

editor.setValue(`name = input("Введите ваше имя: ")
print("Привет,", name)`);


function addToOutput(s) {
    output.value += `${s}\n`;
}

const inputPromise = () => {
  let variable = " ";

  setTimeout(function() {
	output.oninput = function(){
    variable = output.value;
  }
  }, 1000000);


  return variable;
};

async function input(){
    let variable = await inputPromise();
    return variable;

}


async function main() {
    let pyodide = await loadPyodide({ indexURL: "https://cdn.jsdelivr.net/pyodide/v0.18.1/full/",
                                      stdin: input});
    // Pyodide ready
    return pyodide;
};

let pyodideReadyPromise = main();


async function evaluatePython() {
    output.value = "";
    let pyodide = await pyodideReadyPromise;
    setup_pyodide(startcode, pyodide);
    try {
        console.log(editor.getValue())
        let pycode = editor.getValue();
        pyodide.globals.code_to_run = pycode;

        let output = (pyodide.runPython('run_code(code_to_run)'))
        addToOutput(output);
    } catch (err) {
        addToOutput(err);
    }
}



let startcode = `
import sys, io, traceback
namespace = {}  # use separate namespace to hide run_code, modules, etc.
def run_code(code):
    """run specified code and return stdout and stderr"""
    out = io.StringIO()
    oldout = sys.stdout
    olderr = sys.stderr
    sys.stdout = sys.stderr = out
    try:
        # change next line to exec(code, {}) if you want to clear vars each time
        exec(code, {})
    except:
        traceback.print_exc()

    sys.stdout = oldout
    sys.stderr = olderr
    return out.getvalue()
`

function setup_pyodide(startcode, pyodide) {
	// setup pyodide environment to run code blocks as needed
	pyodide.runPython(startcode)
  }

