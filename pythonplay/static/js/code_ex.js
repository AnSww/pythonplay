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
output.value = " ";

async function main() {
    let pyodide = await loadPyodide({ indexURL: "https://cdn.jsdelivr.net/pyodide/v0.18.1/full/" });
    // Pyodide ready
    return pyodide;
};

let pyodideReadyPromise = main();

function addToOutput(s) {
    output.value += s + "\n";
}

async function evaluatePython() {
    let pyodide = await pyodideReadyPromise;
    try {
        console.log(editor.getValue())
        let output = pyodide.runPython(editor.getValue());
        addToOutput(output);
    } catch (err) {
        addToOutput(err);
    }
}