^!r::{
    old_state := ClipboardAll()
    A_Clipboard := ""
    Send("^c")
    if !ClipWait(1) {
        ClipboardAll(old_state)
        return
    }

    data := A_Clipboard
    dir := HasCyrillic(data) ? "ru2en" : "en2ru"
    out := RunPyViaStdin(data, dir)

    if (out != "") {
        A_Clipboard := out
        Send("^v")
        Sleep 100
    }
    ClipboardAll(old_state)
}

HasCyrillic(data) {
    return RegExMatch(data, "[А-Яа-яЁё]")
}

RunPyViaStdin(data, dir) {
    sh := ComObject("WScript.Shell")
    pyScriptPath := A_ScriptDir "\hotkey-translate-layout.py"
    if !FileExist(pyScriptPath) {
        MsgBox "Файл hotkey-translate-layout.py не найден!`nПоложите его в папку: " A_ScriptDir
        return ""
    }
    cmd := 'pythonw -u "' pyScriptPath '" --dir ' dir
    exec := sh.Exec(cmd)
    exec.StdIn.Write(data)
    exec.StdIn.Close()
    return exec.StdOut.ReadAll()
}