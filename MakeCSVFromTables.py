# Scripted by Jakob / https://github.com/hothotcoffee

import ctypes

def Get():
    if ctypes.windll.user32.OpenClipboard(None):
        clipboard_handle = ctypes.windll.user32.GetClipboardData(1)
        if clipboard_handle:
            pointer_to_content = ctypes.windll.kernel32.GlobalLock(clipboard_handle)
            clipboard_data = ctypes.c_char_p(pointer_to_content).value
            ctypes.windll.kernel32.GlobalUnlock(clipboard_handle)
        else:
            return 'invalid handle'
        ctypes.windll.user32.CloseClipboard()
        return clipboard_data
    else:
        return 'ERROR'

text = Get().splitlines()

truncated_Table = ''

for i in text:
	if i == text[-1]:
		truncated_Table = truncated_Table + i
	else:
		truncated_Table = truncated_Table + i + ','

print(truncated_Table)

editor.appendText(truncated_Table)
