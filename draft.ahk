^!r::{
    old_state := ClipboardAll()
    A_Clipboard := ""
    Send("^c")
    if !ClipWait(1) {
        ClipboardAll(old_state)
        return
    }

    data := A_Clipboard
    out := RunPyViaStdin(data)

    A_Clipboard := out
    Send("^v")
    Sleep 100
    ClipboardAll(old_state)
}

RunPyViaStdin(data) {
    sh := ComObject("WScript.Shell")
    exec := sh.Exec('pythonw -u "D:\user\Projects\hotkey-translate-layout\hotkey-translate-layout.py"')
    exec.StdIn.Write(data)
    exec.StdIn.Close()
    return exec.StdOut.ReadAll()
}