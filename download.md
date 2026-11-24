---
layout: default
title: DOWNLOAD
permalink: /download.html
---

<section class="title" markdown="1">

# PieTTY Releases

</section>

<section class="emph1" markdown="1">

### [PieTTY 0.4.16](https://github.com/hungte/pietty/releases/tag/0.4.16)

Release date: Nov 23 2026<br>x86 (32bit): [pietty-0.4.16-win32.zip](https://github.com/hungte/pietty/releases/download/0.4.16/pietty-0.4.16-win32.zip)<br>x64 (64bit): [pietty-0.4.16-win64.zip](https://github.com/hungte/pietty/releases/download/0.4.16/pietty-0.4.16-win64.zip)

</section>

<section class="plain" markdown="1">

<div class="row" markdown="1">

<div class="col" markdown="1">

Created by **priv**, PieTTY 0.4.16 fixes color rendering, paste, and mouse tracking in Codex CLI, both directly over SSH and inside tmux.

- Windows display scaling. Terminal text stays sharp at 150% scaling. When you move the window between displays with different scale settings, PieTTY redraws the text at the new display’s DPI.
- Big5 BBS artwork. Blocks and filled triangles now meet at cell edges, closing gaps in artwork such as the PTT welcome screen across font sizes and display scales. This is on by default. To use the font’s original shapes, uncheck Option → CJK Hacks → Draw seamless Big5 BBS art.
- Color. The faint “Ask Codex” placeholder is readable on the shaded input area. PieTTY renders 24-bit color and reports the session’s default foreground and background colors. This also fixes the Codex starfield in tmux with the default pane style.
- Mouse and keyboard. Codex can track pointer movement over the transcript. PieTTY sends SGR coordinates for clicks, drags, and wheel events, including on wide terminals. Hold Shift and drag to select text locally. In the standard and xterm keyboard profiles, Shift+Left opens a pending Codex question.
- Paste. When an application enables bracketed paste, PieTTY sends a multiline Windows clipboard paste as one block. Codex can distinguish pasted line breaks from presses of the Enter key.
- BBS and SSH. Big5 characters retain the color of each half when a BBS changes color between bytes. A trust icon marks PieTTY’s own SSH login prompts.
- Quick Connect and sessions. Quick Connect accepts a pasted 253-character hostname and can open portable profiles with names up to 2,047 bytes, including Big5 names. The dialog refreshes when you change its language. Portable INI export and connection startup are faster.
- Links and Windows integration. Clicking a wrapped URL opens the complete address. PieTTY rejects an overlong link or session name and reports failed SSH or Telnet URL-handler registration.

</div>

<div class="col" markdown="1">

由 priv 製作，PieTTY 0.4.16 修正了 Codex CLI 的色彩顯示、貼上與滑鼠追蹤問題。透過 SSH 直接執行 Codex，或在 tmux 中使用，都能受益。

- Windows 顯示縮放。 使用 150% 顯示縮放時，終端機文字仍然清晰。將視窗移到縮放比例不同的螢幕時，PieTTY 會依該螢幕的 DPI 重新繪製文字。
- Big5 BBS 圖案。 方塊字元與實心三角形現在會貼齊字格邊界，修正 PTT 歡迎畫面在部分字型、字級及顯示縮放比例下出現的縫隙。此功能預設啟用。若要使用字型原本的字形，請取消勾選 選項 → 亞洲語系修正 → 無縫繪製 Big5 BBS 圖案。
- 色彩顯示。 輸入區的背景色與淡色「Ask Codex」提示文字現在能清楚顯示。PieTTY 支援 24 位元色彩，也會回報目前工作階段的預設前景色與背景色。tmux 使用預設窗格樣式時，Codex 的星空畫面也能正確顯示。
- 滑鼠與鍵盤。 Codex 現在能追蹤滑鼠指標在對話紀錄上的移動。PieTTY 會以 SGR 格式回報點擊、拖曳與滾輪事件的座標，寬螢幕終端機也適用。按住 Shift 拖曳即可在本機選取文字。使用標準或 xterm 鍵盤設定時，可按 Shift+← 開啟 Codex 中待回答的問題。
- 貼上。 應用程式啟用括號貼上模式（bracketed paste）後，從 Windows 剪貼簿貼上的多行文字會以一個區塊送出。Codex 因此能區分貼上內容中的換行與手動按下 Enter。
- BBS 與 SSH。 若 BBS 在一個 Big5 字元的兩個位元組之間切換顏色，該字元的左右兩半會各自保留顏色。PieTTY 自己顯示的 SSH 登入提示會附上識別圖示。
- 快速連線與工作階段。 「快速連線」可完整貼上 253 個字元的主機名稱，也能開啟名稱長達 2,047 位元組的可攜式工作階段，包含 Big5 中文名稱。切換語言時，對話框會立即更新。匯出可攜式 INI 設定及啟動連線的速度也有所提升。
- 連結與 Windows 整合。 點擊折行的網址會開啟完整位址。PieTTY 會拒絕過長的連結或工作階段名稱，並在註冊 SSH 或 Telnet 網址處理程式失敗時顯示錯誤。

</div>

</div>

</section>

<section class="emph1" markdown="1">

### [PieTTY 0.4.15](https://github.com/hungte/pietty/releases/tag/0.4.15) (build 1)

Release date: Nov 22 2026<br>x86 (32bit): [pietty-0.4.15-build1-win32.zip](https://github.com/hungte/pietty/releases/download/0.4.15/pietty-0.4.15-build1-win32.zip)<br>x64 (64bit): [pietty-0.4.15-build1-win64.zip](https://github.com/hungte/pietty/releases/download/0.4.15/pietty-0.4.15-build1-win64.zip)

</section>

<section class="plain" markdown="1">

<div class="row" markdown="1">

<div class="col" markdown="1">

Created by **priv**, updates the multilingual Windows SSH client from the 0.4b14 code base. Extract the ZIP and run **pietty.exe**. For portable sessions, place your **pietty.ini** beside the executable. Windows 7 requires the secure DLL-loading update.

### Changes

- Modern SSH algorithms. Uses the PuTTY SSH engine at `29dd4b17`, 54 commits after PuTTY 0.85. SSH-2 is the default. Available algorithms include ChaCha20-Poly1305, AES-GCM, and hybrid ML-KEM and NTRU Prime key exchanges.
- Chinese dialogs on English Windows. Quick Connect, About, Save Session, and other affected dialogs and menus now use Unicode for their interface text.
- Security and portable sessions. Backported fixes for terminal escape sequences, character rendering, and excessive remote window-title updates. Restricted DLL loading at startup. Portable INI sessions now require a full host-key match and preserve saved cipher preferences.
- Smaller standalone builds. Both Windows builds include the SSH engine in `pietty.exe`. Link-time optimization and symbol stripping reduce executable size. The Windows Help command and bundled CHM manual were removed.

</div>

<div class="col" markdown="1">

由 priv 製作，PieTTY 0.4.15 (build 1) 延續 0.4b14 版的多語言 Windows SSH 用戶端。解壓縮後執行 `pietty.exe`。若使用可攜式工作階段，請將 `pietty.ini` 放在執行檔所在的資料夾。Windows 7 需安裝提供安全 DLL 載入功能的更新。

### 更新內容

- 更新 SSH 演算法。 採用 PuTTY 0.85 之後第 54 個提交（`29dd4b17`）的 SSH 引擎。預設使用 SSH-2，並支援 ChaCha20-Poly1305、AES-GCM，以及採用 ML-KEM 或 NTRU Prime 的混合式金鑰交換。
- 修正英文 Windows 上的中文介面。 快速連線（Quick Connect）、關於、儲存工作階段，以及其他受影響的對話方塊與選單，現在都以 Unicode 顯示介面文字。
- 安全性與可攜式工作階段。 修補終端機逸出序列與字元繪製的問題，限制遠端變更視窗標題的頻率，並在啟動時限制 DLL 載入。可攜式 INI 工作階段現在會比對完整的主機金鑰，並保留已儲存的加密演算法偏好。
- 縮小獨立執行檔。 兩種 Windows 版本的 `pietty.exe` 都內建 SSH 引擎。透過連結階段最佳化與移除符號來縮小執行檔。已移除 Windows 說明選單項目及隨附的 CHM 說明檔。

</div>

</div>

</section>

<section class="emph1" markdown="1">

### [PieTTY 0.4.00b14](https://github.com/hungte/pietty/releases/download/0.4.0b14/pietty0400b14.zip)

Release date: Nov 22 2010

MD5: f42ecd57e924fd3f39e808fa11f61154  pietty0400b14.zip

c5fd4b6546088b3061adb406a44272b2  pietty0400b14.exe

</section>

<section class="plain" markdown="1">

<div class="row" markdown="1">

<div class="col" markdown="1">

- The 0.4.00  is based on PuTTY 0.60, and bug fixes for PieTTY 0.3.x
- No SCP in 0.4 beta builds (use 0.3 below if you need SCP)
- (b1+) Fixed more BIG5 characters
- (b2+) Changed code page settings detection - so you will need to reconfigure the encoding for each session. Really sorry about that.
- (b3+) Fixed some messages, like taskbar menu on win7, fullscreen scrollbar (thank to priv)
- (b4+) NEW: You can toggle the prompt of '\*' in password now, by menu: "View / Prompt Password as \*"
- (b4+) Fixed: first time running on English Windows, the screen goes to whole black or strange symbols
- (b4+) Fixed: first run with PuTTY sessions, the connection would fail
- (b5+) NEW: EUC-JP now on menu!
- (b6+) NEW: "Reconnect" on Connection menu when your connection was dropped!
- (b6+) NEW: support magnet:? URN
- (b7+) Fixed: xterm line drawing characters in UTF8 mode
- (b8+) Fixed: Keyboard not respond after you got all rectangle words in PieTTY 0.3.27 then run 0.4 (due to encoding error)
- (b9+) NEW: Option » CJK Hacks » "Allow using proportional fonts" allows you to use fonts without monotypes.
- (b10+) NEW: Portable Mode (never write anything to registry). Please manually create a (empty) "PieTTY.ini" file with same filename to the pietty\*.exe and then it will use only the INI file.
- (b11+) Fix portable mode and add "export portable settings" in menu: Connection » Export for Portable
- (b12+) Change URL recognition pattern to RFC standard
- (b13+) Fix URL pattern: add '#'
- (b14+) Fix: deleting sessions should not create empty ini file, and added new option to control session auto delete

</div>

<div class="col" markdown="1">

- 0.4.00 是更新至 PuTTY 0.60 核心的修正版
- 暫不提供 scp/sftp 上傳檔案的能力，若有需求請改用 0.3
- (b1+) 修正了漢字轉換表格 (thanks to zcecil), 已能正常處理: 鬆 盃 尬 等字
- (b2+) 由於要修正之前對於字元集產生的種種問題，0.4 會使用跟 0.3 不同的字元集設定。 你可能要為部份連線記錄重新修改字元集(charset/encoding)的設定。
- (b3+) 修正部份訊息，如 win7 的工作列選單，全螢幕動軸（感謝 priv）
- (b4+) 此版起可以設定輸入密碼時是否要顯示 '\*' 號，從 menu 裡可以設定
- (b4+) 修正在非預設 CJK 的系統上，首次執行會畫面全黑或是一堆怪符號的問題
- (b4+) 修正在只用過 PuTTY 的系統上第一次執行時無法連線的問題
- (b5+) 選單裡現在可選用 EUC-JP 日文編碼了
- (b6+) 斷線後連線選單上可按「重新連線」了!
- (b6+) 支援 magnet:? 鏈結
- (b7+) 修正某些使用 terminal 畫線的程式在 UTF-8 mode 會變成 qqq 的問題
- (b8+) 修正用過 0.3.27 並遇到整個螢幕的方塊字後改用 0.4 會造成鍵盤無反應的問題 (原因為 encoding 字元集錯誤，選取一次 encoding 即可解決)
- (b9+) 開啟 選項 » 亞洲語系修正 » 「可選用非等寬字型」 後，可以選任何等寬或不等寬的字形。 這有助於選取一些 實際上是等寬但字型本身設定錯誤導致 PuTTY/PieTTY 無法選用的字型，如文泉驛等寬。
- (b10+) 內建可攜式設定的能力 (也可參考 [Jedi's PieTTY Portable](http://jedi.org/PieTTYPortable/)，將任意版本的 PieTTY/PuTTY 製成 Portable)。只要在 PieTTY\*.exe 同目錄下放一個與 exe 同名的 INI 空檔 (或叫 PieTTY.INI)， PieTTY 就不再會讀寫 Registry 的設定而是使用 INI 檔。
- (b11+) 修正可攜式設定的部份錯誤，新增「輸出設定」的機制 (選單上的連線 » 輸出可攜設定)
- (b12+) 調整 URL 字集為 RFC 標準
- (b13+) 修正 URL 字集: 應加入 #
- (b14+) 修正刪除舊連線設定時會產生空 INI 的問題，並加入選項以控制自動刪除舊連線的選項

</div>

</div>

</section>

<section class="emph1" markdown="1">

### [PieTTY 0.3.27](https://github.com/hungte/pietty/releases/download/0.3.27/pietty0327.exe)

Release date: Jun 14 2005

Final release of 0.3 series

MD5: 1533c60d6a9fda4715eaf88d89c05dc0

</section>

<section class="plain" markdown="1">

- <span class="red">若您不需要 SCP 功能，建議您改用 0.4 系列</span>
- URL 相關(跨行顯示與其它)修正
- 半透明顯示方式增為三種繪製方式以配合各種硬體
- 修正 Big5 日文片假名 A I 的轉碼錯誤
- Big5 下輸入日文時也會自動轉碼(等於全套的 unicode 補完)
- Big5 字碼表改用相容於 Unicode 補完2.40的 Big5-2003+中國海字集
- 內建簡易中文簡繁轉換，使用 autrijus 的表格。
- URL char selection on MB and UCS mode is synced
- Window Borderless mode and lots of related UI update
- Now  keeps last window position
- Association(Integration) with 'telnet://'
- New Multilingual Display Engines: Uniscribe and MLang ,
- 在 Windows 下 可以同時顯示非系統預設的語系，如在英文 Windows 上設英文字型 並同時顯示中文與韓文。
- Faded Window Drop shadow!!!
- 剪貼方式加強方便性，增加 MIRC 控制碼， BBS 與 IRC 互貼彩色不是夢！
- Fixed menu non-funcional in captionless mode
- 修正: - 跨行的網址在 hover 時只會有第一行顯示效果，可是按下去其實會自動跨行。
- Big5 日文片假名的 A I 顯示錯誤
- Big5 日文假名無法正確剪貼或輸入
- Big5 模式與 UTF8 模式對於超連結的判斷不同,

### Known Issues 已知問題：

- <span class="red">第一次使用 PieTTY 時，若直接選 PuTTY 舊設定會連線失敗。 請先隨便手動打入某些 IP 並建立連線後即可正常使用。 (fixed in 0.4)</span>
- Esc\[1;11m" 這樣的 ANSI 控制碼(關鍵在 m 後面直接加 ")在 Big5 mode 不開 Internal UCS 會導致 中文全部被拆開來變 ASCII 處理 (PuTTY 也會)，是否算 PuTTY 的 bug 或 feature 未確認。
- PieTTY 由於有不少圖形加速快取處理的部份， 若使用中變換系統色彩數目（常發生於使用遠端桌面）則很容易會出問題
- 在標題列用右鍵開啟右鍵選單(Context Menu)要開啟兩次才有作用， 第一次選任何功能都會無反應。
- 切換字元編碼 (Encoding/Charset) 後並不會即時對畫面產生影響， 請更新(refresh)已顯示內容或是重新多打幾個字試試。
- 漢字轉換的表格由於簡化字與正體字一對多的關係，之前使用 autrijus 的 perl 表格時似乎沒把優先順序問題處理好， 使用時請自行小心，以後的版本會再人工審閱。 目前已知轉換不良的字: 鬆 盃 (fixed in 0.4)
- 對於某些 codepage 的 Windows, 第一次執行會變成黑底黑字... 請先選 codepage 為 UTF8 或 System default etc. (fixed in 0.4)

</section>

<section class="emph1" markdown="1">

### PieTTY 0.3.25

Release date: Apr 06 2005

Download link is deprecated.

</section>

<section class="plain" markdown="1">

- Based on PuTTY 0.58 Release
- Imported latest PuTTY Unicode 4.0 width table
- Fixed cross-line href supporting

</section>

<section class="emph1" markdown="1">

### PieTTY 0.3.23

Release date: 03/25/2005

Download link is deprecated.

</section>

<section class="plain" markdown="1">

- Support Copy with AnsiSeq 剪貼ANSI控制碼
- Blur shadow effect
- Auto disable HREF in selection mode
- Important hacks now commited into official PuTTY.
- Imported latest PuTTY Unicode 4.0 width table
- (SpecialBuild) Compiled by Intel C++8.1 w/fully optimized
- Fixed SCP upload port bug
- Support AnsiSeq "in" DBCS 一字雙色(終於...)
- Dupe session codepage bug
- Moved some global options to sessions
- Fixed 0.3.20 Big5Kana code error: like '觀'

</section>

<section class="emph1" markdown="1">

### PieTTY 0.3.20

Release date: Mar 16 2005

Download link is deprecated.

</section>

<section class="plain" markdown="1">

- Performance Tuning: stable, smooth, and faster than ever!
- Href now with hover,cursor color option, and broken line support
- Fixed irssi bug when no term\_charset was assigned.
- Fixed SCP upload account bug
- <span class="red">**Fixed a GDI leak bug. Please upgrade!**</span>
- Fixed IME small font bug
- Block cursor is now green again
- Title will not be auto-saved if altered by term
- fixed ugly '\\' in utf8 mode
- customizable href visual effects
- fixed bug: crash when Reconf was called twice
- fixed bug: charset encoding selection display
- changed: size on title can be toggled
- fixed bug: title becomes empty when resizing
- fixed bug: classic putty mode still saved sessions
- changed: default title behaviour
- fixed bug: session with common names
- fixed bug: title always have ' - PieTTY'

</section>

<section class="emph1" markdown="1">

### PieTTY 0.3.11

Release date: Feb 27 2005

Download link is deprecated.

</section>

<section class="plain" markdown="1">

<div class="row" markdown="1">

<div class="col" markdown="1">

- Supports ssh://
- Increase host name length
- SCP drag-n-drop upload is back! (No rich GUI)
- Convert and display JPN Kana characters in Big5
- Titleless mode
- Allow switching to traditional PuTTY interface

</div>

<div class="col" markdown="1">

- 可處理 ssh://
- 提高輸入主機名稱處長度上限
- SCP 拖放
- 增加轉換與顯示 Big5 日文假名字元
- 無標題列模式
- 可選用傳統 PuTTY 界面等等

</div>

</div>

</section>

<section class="emph1" markdown="1">

### [PieTTY 0.3](https://github.com/hungte/pietty/releases/download/0.3/pietty03.exe)

Release date: Feb 22 2005

MD5: 3bed2a91213735d10d0a26a12cee2f46

</section>

<section class="plain" markdown="1">

<div class="row" markdown="1">

<div class="col" markdown="1">

First release of PieTTY, with fixes for Chinese and refactoring. No hyperlink support.

</div>

<div class="col" markdown="1">

PieTTY 的第一個版本，主要以中文修正與架構改變為主，但無超鏈結支援。

</div>

</div>

</section>

<section class="emph1" markdown="1">

## Legacy Non-PieTTY Builds

</section>

<section class="emph2" markdown="1">

## pputty 0.24 final (Mar 03 2005)

- [English Version](https://github.com/hungte/pietty/releases/download/OldReleases/pputty024.exe)
- [中文版](https://github.com/hungte/pietty/releases/download/OldReleases/cpputty024.exe)
- [Source](https://github.com/hungte/pietty/releases/download/OldReleases/pputty024_src.rar)

pputty 0.2.3 的源碼(Source) 於 2004 夏天就不再修改，這裡提供了我最後的版本。

注意: 由於 0.2.3 發佈後 PuTTY 有提出兩項 security patch, 所以 pputty 0.2.4版 就是 0.2.3 加上這兩項 patch。 由於整個計畫已改至 pietty ，所以這裡也不再提供新功能的追加。

這個版本的 code 寫得很不漂亮，我知道。 有些地方可能有問題，我也知道。 因為簡而言之 pputty 是一堆 Hack 急就章跟 try out 的集合... 那時對 PuTTY 的架構非常不懂所以一堆亂寫的東西，也所以才會開始 PieTTY project。

## pputty 0.2.3 (Jun 16 2004)

- [English Version](https://github.com/hungte/pietty/releases/download/OldReleases/pputty023.exe)

修正一些超鏈結的問題，讓一字雙色的字暫時不會破碎太嚴重等等

## pputty 0.1 (May 27 2004)

- [English Version](https://github.com/hungte/pietty/releases/download/OldReleases/pputty01.exe)
- [中文版](https://github.com/hungte/pietty/releases/download/OldReleases/cpputty01.exe)

使用 VS.NET2003(VC7) 編譯並加上所有 patch/hack 與 pputty UI (只改了一點點) 的版本。

## Jul 31 2003

### [lputty-20030731](https://github.com/hungte/pietty/releases/download/OldReleases/lputty-20030731.exe)

使用 VS.NET2003(VC7) 編譯並加上所有 patch/hack 但無 pputty UI。

### [lcputty-20030731 (Cygwin)](https://github.com/hungte/pietty/releases/download/OldReleases/lcputty-20030731.exe)

使用 Cygwin 編譯，有所有 patch/hack，無 pputty UI。

## [Putty 0.53b](https://github.com/hungte/pietty/releases/download/OldReleases/putty053b.exe)

使用官方 0.53b 的原始碼，Cygwin 編譯，只加上新注音 patch 及 CP950 Hack

## 中文透明 Putty

很早前我做的版本，有中文、透明化，原始碼弄不見了所以不再更新。

</section>
