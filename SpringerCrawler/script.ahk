
Esc::
clipboard = %current_line%
ExitApp
return

current_line := ""

f12::
global current_line
CoordMode, Mouse, Window
CoordMode, Pixel, Window
targetcolor := 0x4EADE3
Loop, read, C:\Users\tristan\source\repos\SpringerCrawler\SpringerCrawler\doi_raw2.txt
{
	; Place mouse and type next DOI
	MouseMove, 175, 1131
	current_line = %A_LoopReadLine%
	Send, %current_line%
	Sleep, 200
	Send, {Enter}
	; Retrieve color at this spot
	Sleep, 5000
	MouseMove, 159, 1064
	MouseClick, left
	Sleep, 400
	Send, {Enter}
}
Return

